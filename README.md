
# EchoNet Edge

Official Repo for EchoNet Edge.

## Model for microserivce 

#### { 5 word max description }

```http
  GET /api/items 
```
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | **Required**. {description here} |

Return format
file {
    hello
},
body {
    thing:
}

## Contents

| Functionality |     Desciption                                                      |
| ----------------- | ------------------------------------------------------------------ |
| [Main Program](#Main) |  |
| [API](#API) |  |
| [Drone Protocal](#Drone-Protocol) |  |
| [Drone Managment](#Drone-Management) |  |
| [Shot Detection](#Shot-Detection) |  |
| [Preprossessing](#Preprossessing) |  |
| [Model](#Model) |  |
| [Database](#Database) |  |


## Installation

Install my-project with npm

```bash
  npm install my-project
  cd my-project
```
    
## Run Locally

Clone the project

```bash
  git clone https://link-to-project
```

Go to the project directory

```bash
  cd my-project
```

Install dependencies

```bash
  npm install
```

Start the server

```bash
  npm run start
```


## Main

## API
This is a centralized API that manages communication with other EchoNet microservices.
## API Reference

#### Get list of detection endpoints 

```http
  GET /api/detections
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | **Required**. Your API key |

#### Get list of drone endpoints 

```http
  GET /api/drone/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of item to fetch |

#### Get list of toto endpoints 

```http
  GET /api/toto/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of item to fetch |

#### Get list of surge endpoints 

```http
  GET /api/surge/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of item to fetch |


## Run Locally

Clone the project

```bash
  git clone https://link-to-project
```

Go to the project directory

```bash
  cd Edge_API
```

```making a vitual enviroment
  python -m venv .venv
  .venv/bin/activate
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Start the server

```bash
  flask run
```

## Drone Protocol
Setting up a dev environment:

Prereq: Docker

Navigate to Edge_Parrot/dev_env_setup

run:
```Bash
chmod +x setup.sh
./setup.sh
```
if you need Sphinx, run ./postinst.sh inside the container

## Drone Management 
## Shot Detection
## Preprossessing
## Model

This is for model dummy

```http
  GET /api/getLocation 
```
| Parameter           | Type          | Description                                       |
| :------------------ | :------------ | :-----------------------------------------------  |
| `ProccessedData`    | `byte array ` | **Required**. return an spherical coordinates     |

Return format
body {
  "theta": theta,
  "phi": phi,
  "r": r
}

step to set up single docker container and test in git bash:
```bash
* cd Edge_Model
* docker build -t model .
* docker run -p 9000:5000 model
* curl -X POST localhost:9000/model

```

step to setup all docker compose and test in git bash:
```bash
* docker-compose build
* docker compose up
* curl -X POST localhost:8004/model
```

## Database
The database is setup as a PostgreSQL database, with two tables, one for shots and one for "events.

The shots table has:
* id
* shot_time
* process_time
* event_id
* preprocessed_audio_hash
* postprocessed_audio_hash

The events table has:
* id
* start_time
* end_time
* num_shots
* gun_type
* spherical coordinates (θ, φ, r)
* gps coordinates (lat, long)
* drone_video_hash
