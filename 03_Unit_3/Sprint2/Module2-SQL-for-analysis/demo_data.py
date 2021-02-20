### Part 1 - Making and populating a Database
import sqlite3

# Open a connection to a new (blank) database file `demo_data.sqlite3`
conn = sqlite3.connect('demo_data.sqlite3')

# Make a cursor, and execute an appropriate `CREATE TABLE` statement to accept 
# the above data (name the table `demo`)
cursor = conn.cursor()

sql = """
CREATE TABLE IF NOT EXISTS demo (
    s TEXT NOT NULL,
    x INT NOT NULL,
    y INT NOT NULL
)
"""
cursor.execute(sql)

# Write and execute appropriate `INSERT INTO` statements to add the data (as
# shown above) to the database
insertion_query = f"INSERT INTO demo (s, x, y) VALUES ('g',3, 9), ('v', 5, 7), ('f', 8, 7);"

cursor.execute(insertion_query)

test = cursor.execute('SELECT * FROM demo').fetchall()
print(test)
# [('g', 3, 9), ('v', 5, 7), ('f', 8, 7)]

conn.commit()

# Count how many rows you have - it should be 3!
rows = cursor.execute("SELECT COUNT(*) FROM demo").fetchall()
print(rows[0][0])
# 3

# How many rows are there where both `x` and `y` are at least 5?
rows_five = cursor.execute("SELECT COUNT(*) FROM demo WHERE x > 4 AND y > 4").fetchall()
print(rows_five[0][0])
# 2

# How many unique values of `y` are there (hint - `COUNT()` can accept a keyword 
# `DISTINCT`)?
unique_vals = cursor.execute("SELECT COUNT(DISTINCT y) FROM demo").fetchall()
print(unique_vals[0][0])
# 2

conn.close()

