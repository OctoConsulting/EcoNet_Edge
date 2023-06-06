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
    theta   double precision,
    phi     double precision
);

-- gps coordinates for drone manager
CREATE TYPE gps AS (
  latitude double precision,
  longitude double precision
);

CREATE TYPE gun AS ENUM (
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
    preprocessed_audio_hash VARCHAR(256),
    postprocessed_audio_hash VARCHAR(256)
);

CREATE TABLE events (
    id serial primary key,
    start_time timestamp,
    end_time timestamp,
    num_shots int,
    gun_type gun,
    coordinates spherical,
    dox gps,
    drone_video_hash VARCHAR(256)
);