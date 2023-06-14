# written for Team Edge by Sid Su (c) Octo Consulting LLC 2023
# Functions to query the database and "get" info

import psycopg
from psycopg.rows import dict_row
import json

db_info= "host= db \
    dbname=echonet \
    user= postgres \
    password= changemeoctobby" # TODO: make not hardcoded

def get_all_shots() -> dict:
    with psycopg.connect(db_info) as connection, connection.cursor(row_factory= dict_row) as current:
        current.execute("SELECT * FROM shots")
        return current.fetchall()

def get_all_shot_stats() -> dict:
    with psycopg.connect(db_info) as connection, connection.cursor(row_factory= dict_row) as current:
        current.execute("SELECT * FROM shot_stats")
        return current.fetchall()
    
def get_all_events() -> dict:
    with psycopg.connect(db_info) as connection, connection.cursor(row_factory= dict_row) as current:
        current.execute("SELECT * FROM events")
        return current.fetchall()

# helper function that gets all rows where value == column
def get_all_where(table: str, column: str, operator: str, value:str) -> dict:
    with psycopg.connect(db_info) as connection, connection.cursor(row_factory= dict_row) as current:
        current.execute(f"SELECT * FROM %s WHERE %s %s %s", table, column, operator, value)
        return current.fetchall()

# helper function that gets all rows where value == column
def get_row(table: str, column: str, value:str) -> dict:
    with psycopg.connect(db_info) as connection, connection.cursor(row_factory= dict_row) as current:
        current.execute(f"SELECT * FROM %s WHERE %s = %s", table, column, value)
        return current.fetchone() # should only be one