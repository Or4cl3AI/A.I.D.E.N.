```python
import sqlite3
from sqlite3 import Error

def create_connection():
    conn = None;
    try:
        conn = sqlite3.connect(':memory:') # creates a database in RAM
        return conn
    except Error as e:
        print(e)

    return conn

def close_connection(conn):
    conn.close()

def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def insert_data(conn, table, data):
    with conn:
        c = conn.cursor()
        c.execute(f"INSERT INTO {table} VALUES({data})")

def select_all_data(conn, table):
    with conn:
        c = conn.cursor()
        c.execute(f"SELECT * FROM {table}")
        rows = c.fetchall()

        for row in rows:
            print(row)

def update_data(conn, table, set_data, condition):
    with conn:
        c = conn.cursor()
        c.execute(f"UPDATE {table} SET {set_data} WHERE {condition}")

def delete_data(conn, table, condition):
    with conn:
        c = conn.cursor()
        c.execute(f"DELETE FROM {table} WHERE {condition}")
```