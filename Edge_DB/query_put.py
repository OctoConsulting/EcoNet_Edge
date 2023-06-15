# written for Team Edge by Sid Su (c) Octo Consulting LLC 2023
# Functions to put data into the database

import psycopg

db_info= "host= db \
    dbname=echonet \
    user= postgres \
    password= changemeoctobby"

# function to add a new shot
def put_shot_raw(shot_time: str, preprocessed_audio_hash: str):
    with psycopg.connect(db_info) as connection, connection.cursor() as current:
        sql_code= f'''
        INSERT INTO shots (shot_time, preprocessed_audio_hash)
        VALUES ('%s', '%s');
        '''
        current.execute(sql_code, shot_time, preprocessed_audio_hash)
        connection.commit()

# function to add detector model processed data into the relevant row.
# The primary key here is the hash of the preprocessed audio

def put_shot_detector_model(jason):
    connection= psycopg.connect(db_info)
    current= connection.cursor()

    sql_code= '''
        INSERT INTO shots (shot_time, preprocessed_audio_hash)
        VALUES (\'{shot_time}\', \'{preprocessed_audio_hash}\');
    '''

    print(sql_code)
    current.execute(sql_code)
    connection.commit()

    connection.close()
    current.close()

    print("UNIMPLEMENTED")
'''

def put_shot_acoustic_model():
    print("UNIMPLEMENTED")

def put_shot_drone_mission():
    print("UNIMPLEMENTED")
    '''