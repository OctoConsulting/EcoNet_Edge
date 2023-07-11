# written for Team Edge by Sid Su (c) Octo Consulting LLC 2023
# Functions to put data into the database

import psycopg
import datetime

db_info = "host= db \
    dbname=echonet \
    user= postgres \
    password= changemeoctobby"

# function to add a new shot


def put_shot_raw(shot_time: str, preprocessed_audio_hash: str):
    with psycopg.connect(db_info) as connection, connection.cursor() as current:
        sql_code = f'''
        INSERT INTO shots (shot_time, preprocessed_audio_hash)
        VALUES ('%s', '%s');
        '''
        current.execute(sql_code, shot_time, preprocessed_audio_hash)
        connection.commit()

# function to add detector model processed data into the relevant row.
# The primary key here is the hash of the preprocessed audio


def put_shot_detector_model(jason):
    connection = psycopg.connect(db_info)
    current = connection.cursor()

    sql_code = '''
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
        SET "_Alt" = COALESCE(%s::double precision, "_Alt"), "_Direction" = COALESCE(%s::double precision, "_Direction"), "_Distance" = COALESCE(%s::double precision, "_Distance"), "_Lat" = COALESCE(%s::double precision, "_Lat"), "_Lon" = COALESCE(%s::double precision, "_Lon"), "_Timestamp" = COALESCE(%s::integer, "_Timestamp"), "_Type" = COALESCE(%s::integer, "_Type"), "_isActive" = COALESCE(%s::boolean, "_isActive")
        WHERE "_ID" = %s
        """
        values = (
            data.get('_Alt'),
            data.get('_Direction'),
            data.get('_Distance'),
            data.get('_Lat'),
            data.get('_Lon'),
            data.get('_Timestamp'),
            data.get('_Type'),
            data.get('_isActive'),
            id
        )
        cursor.execute(update_query, values)

        # Commit the changes
        connection.commit()
        connection.close()
        cursor.close()


def put_shot(data, id):
    with psycopg.connect(db_info) as connection, connection.cursor() as cursor:
        # Example update query
        update_query = """
            UPDATE shots
            SET "shot_time" = COALESCE(%s::timestamp, "shot_time"), 
            "process_time" = COALESCE(%s::timestamp, "process_time"), 
            "event_id" = COALESCE(%s::integer, "event_id"), 
            "preprocessed_audio_hash" = COALESCE(%s, "preprocessed_audio_hash"), 
            "postprocessed_audio_hash" = COALESCE(%s, "postprocessed_audio_hash"), 
            "distance" = COALESCE(%s::double precision, "distance"), 
            "microphone_angle" = COALESCE(%s::double precision, "microphone_angle"), 
            "shooter_angle" = COALESCE(%s::double precision, "shooter_angle"), 
            "latitude" = COALESCE(%s::double precision, "latitude"), 
            "longitude" = COALESCE(%s::double precision, "longitude"), 
            "gun_type" = COALESCE(%s::gun, "gun_type")
            WHERE "id" = %s::integer
        """
        values = (
            data.get('shot_time'),
            data.get('process_time'),
            data.get('event_id'),
            data.get('preprocessed_audio_hash'),
            data.get('postprocessed_audio_hash'),
            data.get('distance'),
            data.get('microphone_angle'),
            data.get('shooter_angle'),
            data.get('latitude'),
            data.get('longitude'),
            data.get('gun_type'),
            id
        )
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
