import sqlite3

def get_connection():
    connection = sqlite3.connect('concerts.db')
    connection.row_factory = sqlite3.Row  # Enables dict-like access to rows
    return connection

def get_cursor(connection):
    return connection.cursor()
