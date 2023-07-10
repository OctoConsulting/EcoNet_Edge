# written for Team Edge by Alex Owens (c) Octo Consulting LLC 2023
# Functions to put data into the database

import psycopg
import datetime
db_info= "host= db \
    dbname=echonet \
    user= postgres \
    password= changemeoctobby" # TODO: make not hardcoded

def post_marker(data):
    with psycopg.connect(db_info) as connection, connection.cursor() as cursor:
        # Example update query
        insert_query = """
        INSERT INTO target_markers ("_Alt", "_Direction", "_Distance", "_Lat", "_Lon", "_Timestamp", "_Type", "_isActive", "_ID")
        VALUES (%s::double precision, %s::double precision, %s::double precision, %s::double precision, %s::double precision, %s::integer, %s::integer, %s::boolean, %s)
        """
        values = (
            data.get('_Alt', 0.0),
            data.get('_Direction', 0.0),
            data.get('_Distance', 0.0),
            data.get('_Lat', 0.0),
            data.get('_Lon', 0.0),
            data.get('_Timestamp', 0),
            data.get('_Type', 0),
            data.get('_isActive', True),
            data.get('_ID')
        )
        cursor.execute(insert_query, values)
        
        # Commit the changes
        connection.commit()
        connection.close()
        cursor.close()

def post_shot(data):
    with psycopg.connect(db_info) as connection, connection.cursor() as cursor:
        # Example update query
        insert_query = """
        INSERT INTO shots ("shot_time", "process_time", "event_id", "preprocessed_audio_hash", "postprocessed_audio_hash", "distance", "microphone_angle", "shooter_angle", "latitude", "longitude", "gun_type")
        VALUES (%s::timestamp, %s::timestamp, %s::integer, %s, %s, %s::double precision, %s::double precision, %s::double precision, %s::double precision, %s::double precision, %s::gun)
        RETURNING "id"
        """
        values = (
            data.get('shot_time', datetime.datetime.now()),
            data.get('process_time', datetime.datetime.now()),
            data.get('event_id', -1),
            data.get('preprocessed_audio_hash', "x"),
            data.get('postprocessed_audio_hash', "x"),
            data.get('distance', 0.0),
            data.get('microphone_angle', 0.0),
            data.get('shooter_angle', 0.0),
            data.get('latitude', 0.0),
            data.get('longitude', 0.0),
            data.get('gun_type', 'pistol')
        )
        cursor.execute(insert_query, values)
        id = cursor.fetchone()[0]
        # Commit the changes
        connection.commit()
        connection.close()
        cursor.close()
        return id

# function to add a new shot
def post_shot_raw(preprocessed_audio_hash: str):
    with psycopg.connect(db_info) as connection, connection.cursor() as current:
        sql_code= f'''
        INSERT INTO shots (shot_time, preprocessed_audio_hash)
        VALUES (now(), (%s))
        RETURNING id;
        '''

        current.execute(sql_code, (preprocessed_audio_hash,))
        connection.commit()

        return current.fetchone()[0] # fetchone returns a tuple
    
# function to add a new shot
def post_target_marker(info: dict):
    info_tup= (info['latitude'], info['longitude'], info['altitude'])
    with psycopg.connect(db_info) as connection, connection.cursor() as current:
        sql_code= f'''
        INSERT INTO shots (_Lat, _Lon, _Alt, _Timestamp, _Type, _isActive)
        VALUES ((%s), (%s), (%s), now(), 1, true)
        RETURNING id;
        '''

        current.execute(sql_code, info_tup)
        connection.commit()

        return current.fetchone()[0] # fetchone returns a tuple