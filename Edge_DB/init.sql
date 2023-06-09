-- make a new one :)
CREATE DATABASE echonet;

-- use echonet
\c echonet

-- then, delete the default database
DROP DATABASE postgres;

-- spherical coordinates from acoustic model
-- azimuth is theta
-- angle is phi
-- measured in degrees
CREATE TYPE spherical AS (
    r       double precision,
    r_err   double precision,
    theta   double precision,
    theta_err double precision,
    phi     double precision,
    phi_err double precision
);

-- gps coordinates for drone manager
CREATE TYPE gps AS (
  latitude double precision,
  latitude_err double precision,
  longitude double precision,
  longitude_err double precision
);

CREATE TYPE gun_inference AS ENUM (
    'ak47',
    'm4',
    'glock17',
    'awp'
);

CREATE TABLE shots (
    id serial primary key,
    shot_time timestamp, -- timestamp allows day & time
    process_time timestamp,
    event_id int,
    preprocessed_audio_hash VARCHAR(40), -- currently using SHA1HASH
    postprocessed_audio_hash VARCHAR(40),
    relative_coords spherical, -- theta, phi, r
    absolute_coords gps, -- lat, long
    gun_type gun, -- gun most likely
    gun_data jsonb -- json of gun data w/ confidence
);

CREATE TABLE events (
    id serial primary key,
    start_time timestamp,
    end_time timestamp,
    num_shots int,
    drone_sent boolean,
    drone_id int,
    drone_video_hash VARCHAR(40)
);