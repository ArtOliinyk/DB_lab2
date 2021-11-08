import psycopg2
from db_settings import *

conn = psycopg2.connect(database=DB_NAME, host=DB_HOST, user=DB_USER, password=DB_PASSWORD, port=DB_PORT)
cur = conn.cursor()


def __create_db():
    with open("create.sql", "r") as f:
        sql = f.read()
    cur.execute(sql)
    conn.commit()


def __populate_db():
    with open("populate.sql", "r") as f:
        sql = f.read()
    cur.execute(sql)
    conn.commit()


def seed():
    __create_db()
    __populate_db()


def __read_query():
    with open("query.sql", "r") as f:
        lines = f.readlines()
    return lines


def query_result(query_num: int):
    query = __read_query()[query_num - 1]
    cur.execute(query)
    rows = cur.fetchall()
    return rows
