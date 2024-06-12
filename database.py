import sqlite3

def get_db_connection():
    conn = sqlite3.connect('ice_cream_parlor.db')
    conn.row_factory = sqlite3.Row
    return conn
