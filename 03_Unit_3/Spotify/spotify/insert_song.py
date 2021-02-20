import os
from dotenv import load_dotenv
import psycopg2
from psycopg2.extras import execute_values
import pandas

# Set up .env variables to connect to postgres later

load_dotenv()

DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')
DB_HOST = os.getenv('DB_HOST')

# Instantiate spotify data

CSV_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "spotify", "song.csv")

connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
print(type(connection)) #> <class 'psycopg2.extensions.connection'>

cursor = connection.cursor()
print(type(cursor)) #> <class 'psycopg2.extensions.cursor'>


sql = """
DROP TABLE IF EXISTS songs;
CREATE TABLE IF NOT EXISTS songs (
    acousticness float8,
    artists varchar,
    danceability float8,
    duration_ms float8,
    energy float8,
    explicit float8,
    id varchar,
    instrumentalness float8,
    key int4,
    liveness float8,
    loudness float8,
    mode int4,
    name varchar,
    popularity int4,
    release_date varchar,
    speechiness float8,
    tempo float8,
    valence float8,
    year int4
);
"""

cursor.execute(sql)

# READ SONG DATA FROM THE CSV FILE
df = pandas.read_csv(CSV_FILEPATH)
print(df.columns.tolist())

df = df.astype("object") # converts numpy dtypes to native python dtypes (avoids psycopg2.ProgrammingError: can't adapt type 'numpy.int64')

# how to convert dataframe to a list of tuples?
list_of_tuples = list(df.to_records(index=False))

insertion_query = f"""INSERT INTO songs
        (acousticness, artists, danceability, duration_ms, energy, explicit, id, instrumentalness, key, liveness, loudness, mode, name, popularity, release_date, speechiness, tempo, valence, year) VALUES %s"""
execute_values(cursor, insertion_query, list_of_tuples) # third param: data as a list of tuples!

# CLEAN UP

connection.commit() # actually save the records / run the transaction to insert rows

cursor.close()
connection.close()