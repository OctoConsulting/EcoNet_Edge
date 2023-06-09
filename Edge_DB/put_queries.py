# written for Team Edge by Sid Su (c) Octo Consulting LLC 2023
# Functions to put data into the database

import psycopg

db_info= "host= db \
    dbname=echonet \
    user= postgres \
    password= changemeoctobby"

# function to add a new shot
def put_shot_raw(shot_time: str, preprocessed_audio_hash: str):
    connection= psycopg.connect(db_info)
    current= connection.cursor()

    sql_code= f'''
    INSERT INTO shots (shot_time, preprocessed_audio_hash)
    VALUES (\'{shot_time}\', \'{preprocessed_audio_hash}\');
    '''

    print(sql_code)
    current.execute(sql_code)
    connection.commit()

    connection.close()
    current.close()

# function to add processing data to a shot row
# def put_shot_processed
def put_shot_processed(jason):
    connection= psycopg.connect(db_info)
    current= connection.cursor()

    sql_code= f'''
    INSERT INTO shots (shot_time, preprocessed_audio_hash)
    VALUES (\'{shot_time}\', \'{preprocessed_audio_hash}\');
    '''

    print(sql_code)
    current.execute(sql_code)
    connection.commit()

    connection.close()
    current.close()


'''
    shot_time timestamp
    process_time timestamp,
    event_id int,
    preprocessed_audio_hash VARCHAR(40), -- currently using SHA1HASH
    postprocessed_audio_hash VARCHAR(40),
    relative_coords spherical, -- theta, phi, r
    absolute_coords gps, -- lat, long
    gun_type gun, -- gun most likely
    gun_data jsonb -- json of gun data w/ confidence
);
'''