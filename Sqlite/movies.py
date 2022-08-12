import sqlite3
from sqlite3 import Error

def connect_to_db():
    try:
        connection = sqlite3.connect("movies.db")
        print(sqlite3.version)
    except Error as e:
        print(e)
    return connection

connection = connect_to_db()

def create_table(connection, sql_query):
    try:
        cursor = connection.cursor()
        cursor.execute(sql_query)
    except Error as e:
        print(e)

create_table_query = """CREATE TABLE movies (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    name TEXT NOT NULL,
    director TEXT,
    year INTEGER
);
"""

create_table(connection, create_table_query)

def create_movie(connection, sql_query, data):
    cursor = connection.cursor()
    cursor.execute(sql_query, data)
    connection.commit()
    return cursor.lastrowid

movie_name = "Star Wars IV."
director = "George Lucas"
year = 1977

insert_movie_query = """INSERT INTO movies (name, director, year) 
VALUES (?, ?, ?);
"""

data = (movie_name, director, year)
data2 = ("Star Wars V.", "Irvin Kershner", 1980)

create_movie(connection, insert_movie_query, data)
create_movie(connection, insert_movie_query, data2)

def run_select_query(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)

    rows = cursor.fetchall()

    for row in rows:
        print(row)


select_query = """SELECT * FROM movies;"""

run_select_query(connection, select_query)