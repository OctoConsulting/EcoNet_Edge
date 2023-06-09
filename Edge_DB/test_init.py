# written for Team Edge by Sid Su (c) Octo Consulting LLC 2023
# Initializes the database with test data

import psycopg
from psycopg.rows import dict_row
import json

db_info= "host= db \
    dbname=echonet \
    user= postgres \
    password= changemeoctobby" # TODO: make not hardcoded

with psycopg.connect(db_info) as connection, connection.cursor(row_factory= dict_row) as current:
  copy_sql= """
    copy shots(shot_time, process_time, event_id, preprocessed_audio_hash, postprocessed_audio_hash, distance, microphone_angle, shooter_angle, latitude, longitude, gun_type)
    from stdin with
    csv
    header
    delimiter as ','
  """

  from_csv= './test_shots.csv'
  with open(from_csv, 'r') as f:
    data= f.read()
    with current.copy(copy_sql) as copy:
      copy.write(data)

  copy_sql= """
    copy shot_stats(id, distance_predict, distance_upper, distance_lower, microphone_angle_predict, microphone_angle_upper, microphone_angle_lower, shooter_angle_predict, shooter_angle_upper, shooter_angle_lower, latitude_predict, latitude_upper, latitude_lower, longitude_predict, longitude_upper, longitude_lower, rifle_predict, rifle_upper, rifle_lower, pistol_predict, pistol_upper, pistol_lower)
    from stdin with
    csv
    header
    delimiter as ','
  """

  from_csv= './test_shot_stats.csv'
  with open(from_csv, 'r') as f:
    data= f.read()
    with current.copy(copy_sql) as copy:
      copy.write(data)
