# written for Team Edge by Sid Su (c) Octo Consulting LLC 2023
# Functions to query the database and "get" info

import psycopg
from psycopg.rows import dict_row
import json

db_info= "host= db \
    dbname=echonet \
    user= postgres \
    password= changemeoctobby" # TODO: make not hardcoded

# helper function to make querying a whole table easier
def get_all_from(table: str) -> dict:
    try:
        connection= psycopg.connect(db_info)
        current= connection.cursor(row_factory= dict_row)

        current.execute(f"SELECT * FROM {table}")
        return(current.fetchall())
    
    except Exception as e:
        print(f"There was an error accessing the database: {e}")

    finally: # runs, even after return :)
        if connection:
            connection.close()
        if current:
            current.close()

# helper function that gets all rows where value == column
def get_all_where(table: str, column: str, operator: str, value:str) -> dict:
    try:
        connection= psycopg.connect(db_info)
        current= connection.cursor(row_factory= dict_row)

        current.execute(f"SELECT * FROM {table} WHERE {column} {operator} {value}")
        return(current.fetchall())
    
    except Exception as e:
        print(f"There was an error accessing the database: {e}")

    finally:
        if connection:
            connection.close()
        if current:
            current.close()

# helper function that gets all rows where value == column
def get_row(table: str, column: str, value:str) -> dict:
    try:
        connection= psycopg.connect(db_info)
        current= connection.cursor(row_factory= dict_row)

        current.execute(f"SELECT * FROM {table} WHERE {column} = {value}")
        return_val= current.fetchone() # should only be one
    
    except Exception as e:
        print(f"There was an error accessing the database: {e}")

    finally:
        if connection:
            connection.close()
        if current:
            current.close()

    current= connection.cursor()