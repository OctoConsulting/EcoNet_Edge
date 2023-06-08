# written for Team Edge by Sid Su (c) Octo Consulting LLC 2023
# Functions to query the database and "get" info

import psycopg

db_info= "host= 172.18.0.3 \
    dbname=echonet \
    user= postgres \
    password= changemeoctobby" # TODO: make not hardcoded

# helper function to make querying a whole table easier
def get_all_from(table: str) -> list[tuple]:
    connection= psycopg.connect(db_info)
    current= connection.cursor()

    current.execute(f"SELECT * FROM {table}")
    return_val= current.fetchall()

    connection.close()
    current.close()
    return return_val

# returns the entire shots table as a python array
def get_all_shots() -> list[tuple]:
    return get_all_from("shots")

# returns the entire events table as a python array
def get_all_events() -> list[tuple]:
    return get_all_from("events")

# helper function that gets all rows where value = column
def get_all_where(table: str, column: str, value: str) -> tuple:
    connection= psycopg.connect(db_info)
    current= connection.cursor()

    current.execute(f"SELECT * FROM {table} WHERE {column} = {value}")
    return_val= current.fetchall() # should only be one

    current.close()
    connection.close()
    return return_val

# helper function to get rows of a given table
def get_row(table: str, column: str, value: str) -> tuple:
    connection= psycopg.connect(db_info)
    current= connection.cursor()

    current.execute(f"SELECT * FROM {table} WHERE {column} = {value}")
    return_val= current.fetchone() # should only be one

    current.close()
    connection.close()
    return return_val

# returns the row of a shot given the id
def get_shot_by_id(id: int) -> tuple:
    return get_row("shots", "id", id)

# returns the row of a shot given the preprocessed audio hash
def get_shot_by_pre_hash(hash: str) -> tuple:
    return get_row("shots", "preprocessed_audio_hash", hash)

# returns the row of a shot given the postprocessed audio hash
def get_shot_by_pre_hash(hash: str) -> tuple:
    return get_row("shots", "postprocessed_audio_hash", hash)

# helper function that gets all rows where value = column
def get_all_where(table: str, column: str, value: str) -> tuple:
    connection= psycopg.connect(db_info)
    current= connection.cursor()

    current.execute(f"SELECT * FROM {table} WHERE {column} = {value}")
    return_val= current.fetchall() # should only be one

    current.close()
    connection.close()
    return return_val