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
        INSERT INTO target_markers (altitude, direction, distance, latitude, longitude, update_time, marker_type, is_active, ID)
        VALUES (%s::double precision, %s::double precision, %s::double precision, %s::double precision, %s::double precision, %s::integer, %s::target_type, %s::boolean, %s)
        """
        values = (data['_Alt'], data['_Direction'], data['_Distance'], data['_Lat'], data['_Lon'], data['_Timestamp'], data['_Type'], data['_isActive'], data['_ID'])
        cursor.execute(insert_query, values)
        
        # Commit the changes
        connection.commit()
        connection.close()
        cursor.close()