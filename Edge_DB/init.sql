-- make a new one :)
CREATE DATABASE echonet;

-- use echonet
\c echonet

-- then, delete the default database
DROP DATABASE postgres;

CREATE TYPE err_range AS (
    prediction double precision,
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
    'ar15'
    'm4',
    'glock17'
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
    gun_type gun -- gun most likely
);

CREATE TABLE shot_stats (
    id serial primary key,
    r_err err_range,
    theta_err err_range,
    phi_err err_range,
    latitude_err err_range,
    longitude_err err_range,
    ak74_err err_range,
    glock17_err err_range,
    awp_err err_range
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

CREATE TABLE drone_1_status (
    drone_loc gps,
    drone_status int,
    video_status int,
    assigned_event int
)