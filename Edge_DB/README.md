# Usage

## Installation of the Dev Environment

NOTE: this is unnecessary if running through the AWS VM on 44.something.something.something.weezer

run Docker Desktop

navigate to this directory,

run the following. Note that if running from the Octo Network, it will probably
fail a few times. This is because some of the urls it tries to install from are
blocked on the Octo Network (Canadians or something). Just keep rerunning it and
it will eventually work though.

In Powershell
```Powershell
powershell.exe .\build.ps1
```

or In Bash
```Bash
./bulid.sh
```

Afterwards it will put you inside the development container.

In order to push changes to the environment, exit the container by running

```Bash
exit
```

and run

```Powershell
powershell.exe .\build.ps1
```

again

## Summary of Dev Files

DockerfileDatabase

creates and sets the password for the database. in the future it will install
something to write long-term backups to the docker volume (which will then be
backed up to the cloud)

dev_env_setup/Dockerfile

creates the dev environment as a Debian 11 instance and installs several
development tools. Also runs the Flask and Waitress message broker service.
Edit this file to add dependencies from pip or apt.

build.ps1 and build.sh

builds database and the flask message broker service. Flask runs on port 80, the
database runs on port 5432.

init.sql

run by the database container at build time. Initializes tables and data types

test_init.py and tessdata/test_shots.csv and tessdata/test_shot_stats.csv

run by the build scripts after starting containers. test_init.py runs SQL code
to add test data to the database. can be easily modified to add to more tables

app.py
run by the Flask the message broker service for what get, post, put, etc. requests are made available. Contains several skeleton functions right now.

## Usage
```Bash
curl http://localhost:5000/db/get_all_shots
```

or in Python
```Python
import requests
requests.get('http://localhost:5000/db/get_all_shots')
```

or in JavaScript
```JavaScript
fetch('http://localhost:5000/db/get_all_shots', {
    method: "GET"
})
```

## API Documentation

```Bash
curl http://44.204.71.132//db/get_all_shots
```

Returns the whole shots table as a JSON.

The layout of the shots table
* id - Counts up from 1 for each shot. Lets us go between tables so we can get the infos and all that :)
* shot_time - the time of the shot. Currently in an SQL-native format. Should be easy to convert to anything. On the Python side it's really easy, but idk how it looks from the JS side, so if there's a problem, just let me know
* process_time - when did the shot finish being processed? Same format as shot_time. Relevant, because if this column is filled, the processing or the shot is completely done, and no new info is coming in.
* distance - distance from the microphone in meters. Detected by the acoustic model
* microphone angle (azimuth) - Angle in degrees from the microphone to the shooter. Renamed for more clarity
* shooter_angle (angle) - Angle in degrees from the shooter to the microphone. Renamed for more clarity.
* latitude - GPS latitude -90 to 90 degrees
* longitude - GPS longitude -90 to 90 degrees
* gun_type - an enum accepting "rifle" and "pistol"

```Bash
curl http://44.204.71.132/db/get_all_shot_stats
```

Returns the whole shot stats table as a JSON

* id - key corresponding to an entry in the shots table. Does not increment on its own, rather relies on entries in the shots table

the following have x_predict, x_upper and x_lower representing a confidence interval

* distance
* microphone_angle
* shooter_angle
* latitude
* longitude
* rifle
* pistol

```Bash
curl http://44.204.71.132/db/get_all_events
```

Returns the whole events or "shooter" table as a JSON. It's so we don't send all the drones for the same shooter, so if 3 shots come within like 10 seconds in the same area, we only send 1 drone

* COLUMNS WIP, NOT SURE WHAT WE WILL NEED YET

```Bash
curl http://44.204.71.132/db/get_drone1_status
curl http://44.204.71.132/db/get_drone2_status
curl http://44.204.71.132/db/get_drone3_status
```

Returns the status of each drone.

* drone_latitude - Location of the drone -90 to 90
* drone_longitude - Location of the drone -180 to 180
* drone_status 0 means rest, 1 means flight, etc. Will probably change to an ENUM later
* video_status 0 means not connected, 1 means connected, etc. Will probably change to an ENUM later
* drone_battery - 0 to 100, change of the drone
* followed_event - integer corresponding to an id in the Event table. Which event is the drone going to? 0 means not following an event, -1 means error

# SQL Stuff for development
You can ignore this stuff, it's mostly for me :)
# a lil crashcourse on sql :)

If you're like me, then you learned SQL for a class freshman year of college, then proceeded to forget everything about SQL.

Let's jog our memory a bit :)

Build and start the PostgreSQL container with

```Powershell
# needs Docker installed :)
powershell.exe .\on_windows.ps1
```

Create a database
```SQL
/* commands should be uppercase, while names should be lowercase */
-- also comments are nice :)
CREATE DATABASE test_db
```

Create a table: (info about [data types](https://www.postgresql.org/docs/current/datatype.html))
```SQL
CREATE TABLE test_table (
    id serial primary key,
    cost money,
    process_time time
);
```

Basic select statement
```SQL
SELECT * FROM shots
```

Importing data
```SQL
COPY test_table (process_time, cost)
FROM '/mnt/store/test_data.csv'
DELIMITER ','
CSV HEADER;
```

Making 
for later...

https://towardsdatascience.com/sending-data-from-a-flask-app-to-postgresql-database-889304964bf2