import psycopg

# helper function to make querying a whole table easier
def get_all_from(table: str):
    connection= psycopg.connect("host= 172.18.0.2 \
                                dbname= echonet \
                                user= postgres \
                                password= changemeoctobby") # TODO: make not hardcoded
    current= connection.cursor()

    current.execute(f"SELECT * FROM {table}")
    ret= current.fetchall()

    current.close()
    connection.close()

    return ret

# returns the entire shots table as a python array
def get_all_shots():
    return get_all_from("shots")

# returns the entire events table as a python array
def get_all_events():
    return get_all_from("events")

# helper function to get rows of a given table
def get_row(table: str, id: int):
    connection= psycopg.connect("host= 172.18.0.3 \
                                dbname= echonet \
                                user= postgres \
                                password= changemeoctobby") # TODO: make not hardcoded
    current= connection.cursor()

    current.execute(f"SELECT * FROM {table} where id == {id}")
    ret= current.fetchone() # should only be one

    current.close()
    connection.close()

    return ret

# returns the row of a shot given the id
def get_shot(id: int):
    get_row("shots", 1)

def put_shot(shot_time: str, audio_file):
    print("UNIMPLEMENTED")
