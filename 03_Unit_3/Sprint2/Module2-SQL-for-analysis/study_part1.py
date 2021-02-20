import os
from dotenv import load_dotenv
import psycopg2
from psycopg2.extras import execute_values
import pandas
import sqlite3

conn = sqlite3.connect('study_part1.sqlite3')

cursor = conn.cursor()

sql = """
CREATE TABLE IF NOT EXISTS table_1 (
    student varchar,
    studied varchar,
    grade int,
    age int,
    sex varchar
);
"""
cursor.execute(sql)

insertion_query = f"INSERT INTO table_1 (student, studied, grade, age, sex) VALUES ('Lion-O', 'True', 85, 24, 'Male'), ('Cheetara', 'True', 95, 22, 'Female'), ('Mumm-Ra', 'False', 65, 153, 'Male'), ('Snarf', 'False', 70, 15, 'Male'), ('Panthro', 'True', 80, 30, 'Male');"

cursor.execute(insertion_query)

conn.commit()