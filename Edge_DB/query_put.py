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
        SET "_Alt" = %s::double precision, "_Direction" = %s::double precision, "_Distance" = %s::double precision, "_Lat" = %s::double precision, "_Lon" = %s::double precision, "_Timestamp" = %s::integer, "_Type" = %s::integer, "_isActive" = %s::boolean
        WHERE "_ID" = %s
        """
        values = (
            data.get('_Alt', 0.0),
            data.get('_Direction', 0.0),
            data.get('_Distance', 0.0),
            data.get('_Lat', 0.0),
            data.get('_Lon', 0.0),
            data.get('_Timestamp', 0.0),
            data.get('_Type', 0),
            data.get('_isActive', True),
            id
        )
        values = (data.get('_Alt', 0.0), data['_Direction'], data['_Distance'], data['_Lat'], data['_Lon'], data['_Timestamp'], data['_Type'], data['_isActive'], id)
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