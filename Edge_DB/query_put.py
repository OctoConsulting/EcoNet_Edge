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

def put_marker(data, id):
    with psycopg.connect(db_info) as connection, connection.cursor() as cursor:
        # Example update query
        update_query = """
        UPDATE target_markers
        SET altitude = %s::double precision, direction = %s::double precision, distance = %s::double precision, latitude = %s::double precision, longitude = %s::double precision, update_time = %s::integer, marker_type = %s::target_type, is_active = %s::boolean,
        WHERE id = %s
        """
        values = (data['_Alt'], data['_Direction'], data['_Distance'], data['_Lat'], data['_Lon'], data['_Timestamp'], data['_Type'], data['_isActive'], id)
        cursor.execute(update_query, values)
        
        # Commit the changes
        connection.commit()
        connection.close()
        cursor.close()
'''

def put_shot_acoustic_model():
    print("UNIMPLEMENTED")

def put_shot_drone_mission():
    print("UNIMPLEMENTED")
    '''