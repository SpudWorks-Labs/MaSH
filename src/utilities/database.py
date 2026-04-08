import sqlite3


database = 'database.db'


def init_database():
    with sqlite3.connect(database) as connection:
        cursor = connection.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS projects (
                name TEXT NOT NULL UNIQUE,
                path TEXT NOT NULL,
                repo TEXT
            );
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS models (
                name TEXT NOT NULL UNIQUE,
                desc TEXT NOT NULL,
                model TEXT
            );
        ''')


def update_database(table, payload):
    with sqlite3.connect(database) as connection:
        cursor = connection.cursor()
        placeholders = ", ".join(["?"] * len(payload))
        template = f"({placeholders})"
        cmd = f"INSERT INTO {table} VALUES {template}"
        cursor.execute(cmd, payload)


def read_database(table):
    with sqlite3.connect(database) as connection:
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM {table}")

        return cursor.fetchall()


def remove_database(table, name):
    with sqlite3.connect(database) as connection:
        cursor = connection.cursor()
        cursor.execute(f"DELETE FROM {table} WHERE name == '{name}'")

