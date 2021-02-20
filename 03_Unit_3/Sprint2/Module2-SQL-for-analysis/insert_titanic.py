import psycopg2
from psycopg2.extras import execute_values
import pandas

DB_NAME = 'zninzmrd'
DB_USER = 'zninzmrd'
DB_PASS = 'iOj0vECcKLDZ50DdidwUHsdkVzGj62KX'
DB_HOST = 'lallah.db.elephantsql.com'

# Connect to ElephantSQL - hosted PostgreSQL DB
conn = psycopg2.connect(dbname=DB_NAME,
                        user=DB_USER,
                        password=DB_PASS,
                        host=DB_HOST)

cursor = conn.cursor()

cursor.execute("SELECT * from test_table;")

results = cursor.fetchall()
# print(results)

#### Connect to SQLite DB for TITANIC Data ####

import sqlite3

sl_conn = sqlite3.connect('titanic.sqlite3')
sl_cursor = sl_conn.cursor()
passengers = sl_cursor.execute('SELECT * FROM titanic;').fetchall()
# print(passengers)

query = '''
CREATE TABLE IF NOT EXISTS passengers (
    id SERIAL PRIMARY KEY,
    survived bool,
    pclass int,
    name varchar,
    sex varchar,
    age int,
    sib_spouse_count int,
    parent_child_count int,
    fare float8
);
'''

cursor.execute(query)

CSV_FILEPATH = "titanic.csv"

for passenger in passengers:
    insert_passenger = """
        INSERT INTO passengers
        (Survived, Pclass, Name, Sex, Age, Siblings_Spouses_Aboard,
        Parents_Children_Aboard, Fare)
        VALUES """ + str(passenger[1:]) + ";"
    cursor.execute(passengers)

cursor.execute('SELECT * from passengers;')
cursor.fetchall()
conn.commit() # actually update the database