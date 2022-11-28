import mariadb
import json
from api import db_connection


class DB:

    @classmethod
    def get_connection(cls):
        return mariadb.connect(**db_connection)

    @classmethod
    def select_all(cls, query, params=()):
        conn = cls.get_connection()
        cur = conn.cursor()
        cur.execute(query, params)
        rows = cur.fetchall()
        conn.close()
        return rows

    @classmethod
    def select_one(cls, query, params=()):
        conn = cls.get_connection()
        cur = conn.cursor()
        cur.execute(query, params)
        rows = cur.fetchone()
        conn.close()
        return rows

    @classmethod
    def create(cls, query, params=()):
        conn = cls.get_connection()
        cur = conn.cursor()
        cur.execute(query, params)
        conn.commit()
        conn.close()
