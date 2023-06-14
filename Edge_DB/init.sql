-- make a new one :)
CREATE DATABASE echonet;

-- use echonet
\c echonet

-- then, delete the default database
DROP DATABASE postgres;

CREATE TYPE gun AS ENUM (
    'rifle',
    'pistol'
);

-- EdgeDevice Status DB
CREATE TABLE edge_device_status (
    bat_percent double precision,
    cpu_load double precision,
    cpu_temp double precision,
    hdd_available double precision
);

CREATE TABLE shots (
    id serial primary key,
    shot_time timestamp, -- timestamp allows day & time
    process_time timestamp,
    event_id integer,
    preprocessed_audio_hash VARCHAR(40), -- currently using SHA1HASH
    postprocessed_audio_hash VARCHAR(40),
    distance double precision,
    microphone_angle double precision,
    shooter_angle double precision,
    latitude double precision,
    longitude double precision,
    gun_type gun -- gun most likely
);

CREATE TABLE shot_stats (
    id integer primary key, -- match with the shots table
    distance_predict double precision,
    distance_upper double precision,
    distance_lower double precision,
    microphone_angle_predict double precision,
    microphone_angle_upper double precision,
    microphone_angle_lower double precision,
    shooter_angle_predict double precision,
    shooter_angle_upper double precision,
    shooter_angle_lower double precision,
    latitude_predict double precision,
    latitude_upper double precision,
    latitude_lower double precision,
    longitude_predict double precision,
    longitude_upper double precision,
    longitude_lower double precision,
    rifle_predict double precision,
    rifle_upper double precision,
    rifle_lower double precision,
    pistol_predict double precision,
    pistol_upper double precision,
    pistol_lower double precision
);

CREATE TABLE events (
    id serial primary key,
    start_time timestamp,
    end_time timestamp,
    num_shots integer,
    drone_sent boolean,
    drone_id integer,
    drone_video_hash VARCHAR(40)
);

CREATE TABLE drone_status_template (
    drone_latitude double precision,
    drone_longitude double precision,
    drone_status integer,
    video_status integer,
    drone_battery double precision,
    followed_event integer
);

CREATE TABLE drone_1_status AS (SELECT * FROM drone_status_template);
CREATE TABLE drone_2_status AS (SELECT * FROM drone_status_template);
CREATE TABLE drone_3_status AS (SELECT * FROM drone_status_template);