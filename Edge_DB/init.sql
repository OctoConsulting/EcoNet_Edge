-- make a new one :)
CREATE DATABASE echonet;

-- use echonet
\c echonet

-- then, delete the default database
DROP DATABASE postgres;

CREATE TYPE gun AS ENUM (
    'ar15',
    'ak47'
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
    distance double precision,
    angle double precision,
    azimuth double precision,
    latitude double precision,
    longitude double precision,
    gun_type gun -- gun most likely
);

CREATE TABLE shot_stats (
    id int primary key, -- match with the shots table
    distance_predict double precision,
    distance_predict_upper double precision,
    distance_predict_lower double precision,
    angle_predict double precision,
    angle_upper double precision,
    angle_lower double precision,
    azimuth_predict double precision,
    azimuth_upper double precision,
    azimuth_lower double precision,
    latitude_predict double precision,
    latitude_upper double precision,
    latitude_lower double precision,
    longitude_predict double precision,
    longitude_upper double precision,
    longitude_lower double precision,
    ar15_predict double precision,
    ar15_upper double precision,
    ar15_lower double precision,
    ak47_predict double precision,
    ak47_upper double precision,
    ak47_lower double precision,
    m4_predict double precision,
    m4_upper double precision,
    m4_lower double precision,
    glock17_predict double precision,
    glock17_upper double precision,
    glock17_lower double precision
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