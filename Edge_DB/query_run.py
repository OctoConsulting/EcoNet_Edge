# written for EchoNet by Sid Su (c) Octo Consulting LLC 2023
# Functions that connect to the database

import psycopg

db_info= "host= db \
    dbname=echonet \
    user= postgres \
    password= changemeoctobby"

# runs inputted sql_code string arg in the database
#def get_sql_run(sql_code: str) -> :
    