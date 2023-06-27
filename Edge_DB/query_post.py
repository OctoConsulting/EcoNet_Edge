import psycopg

db_info= "host= db \
    dbname=echonet \
    user= postgres \
    password= changemeoctobby" # TODO: make not hardcoded

def post_marker(data):
    with psycopg.connect(db_info) as connection, connection.cursor() as cursor:
        # Example update query
        insert_query = """
        INSERT target_markers
        SET altitude = %s::double precision, direction = %s::double precision, distance = %s::double precision, latitude = %s::double precision, longitude = %s::double precision, update_time = %s::integer, marker_type = %s::target_type, is_active = %s::boolean, ID = %s,
        """
        values = (data['_Alt'], data['_Direction'], data['_Distance'], data['_Lat'], data['_Lon'], data['_Timestamp'], data['_Type'], data['_isActive'], data['_ID'])
        cursor.execute(insert_query, values)
        
        # Commit the changes
        connection.commit()
        connection.close()
        cursor.close()