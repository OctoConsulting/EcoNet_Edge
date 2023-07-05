# written for Team Edge by Alex Owens (c) Octo Consulting LLC 2023
# Functions to delete data from the database

import psycopg

db_info= "host= db \
    dbname=echonet \
    user= postgres \
    password= changemeoctobby"

def delete_marker(id):
    with psycopg.connect(db_info) as connection, connection.cursor() as cursor:
        delete_query = """
        DELETE FROM target_markers
        WHERE id = %s;
        """
        values = (id,)  # Replace id with the actual ID value you want to delete
        cursor.execute(delete_query, values)

        # Commit the changes
        connection.commit()