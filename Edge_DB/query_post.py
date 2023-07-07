# written for Team Edge by Alex Owens (c) Octo Consulting LLC 2023
# Functions to put data into the database

import psycopg

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

# function to add a new shot
def post_shot_raw(preprocessed_audio_hash: str):
    with psycopg.connect(db_info) as connection, connection.cursor() as current:
        sql_code= f'''
        INSERT INTO shots (shot_time, preprocessed_audio_hash)
        VALUES (now(), '%s')
        RETURNING id;
        '''

        current.execute(sql_code, "UNIMPLEMENTED")
        connection.commit()

        return current.fetchone()[0] # fetchone returns a tuple