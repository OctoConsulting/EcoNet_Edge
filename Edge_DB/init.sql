-- make a new one :)
CREATE DATABASE echonet;

-- use echonet
\c echonet

-- then, delete the default database
DROP DATABASE postgres;

CREATE TYPE err_range AS (
    lower_bound double precision,
    upper_bound double precision
);

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
    preprocessed_audio_hash VARCHAR(40), -- currently using SHA1HASH
    postprocessed_audio_hash VARCHAR(40),
    relative_coords spherical, -- theta, phi, r
    absolute_coords gps, -- lat, long
    gun_type gun, -- gun most likely
);

CREATE TABLE shot_stats (
    id serial primary key,
    r_err err_range,
    theta_err err_range,
    phi_err err_range
    latitude_err err_range,
    longitude_err err_range,
    ak74_confidence double precision,
    glock17_confidence double precision,
    awp_confidence double precision,
    ak74_err err_range,
    glock17_err err_range,
    awp_err err_range
)

CREATE TABLE events (
    id serial primary key,
    start_time timestamp,
    end_time timestamp,
    num_shots int,
    drone_sent boolean,
    drone_id int,
    drone_video_hash VARCHAR(40)
);