import psycopg

# helper function to make querying a whole table easier
def get_all_from(table: str):
    connection= psycopg.connect("host= 172.18.0.3 \
                                dbname= echonet \
                                user= postgres \
                                password= changemeoctobby") # TODO: make not hardcoded
    current= connection.cursor()

    current.execute(f"SELECT * FROM {table}")
    ret= current.fetchall()

    current.close()
    connection.close()

    return ret

def get_all_shots():
    return get_all_from("shots")

def get_all_events():
    return get_all_from("events")