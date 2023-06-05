CREATE DATABASE echonet;

CREATE USER listener PASSWORD 'changemeoctobby';

CREATE TABLE shots (
    id serial primary key,
    shot_time time,
    process_time time
);

-- spherical coordinates from acoustic model
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
CREATE TABLE events (
    id serial primary key,
    start_time time,
    end_time time,
    num_shots int,
    coordinates spherical
);