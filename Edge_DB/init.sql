CREATE DATABASE echonet;

CREATE TABLE shots (
    id SERIAL PRIMARY KEY,
    shot_time time,
    process_time time
);
/*
CREATE TABLE mytable (
  id INT NOT NULL AUTO_INCREMENT,
  name VARCHAR(50) NOT NULL,
  PRIMARY KEY (id)
  ) */