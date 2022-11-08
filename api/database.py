import os
import sqlite3
from sqlite3 import Error


class DB:

    @classmethod
    def get_connection(cls):
        return sqlite3.connect("./api/db/rws.sqlite")

    @classmethod
    def select(cls, query, params=()):
        # print("DB Select classmethod")
        conn = cls.get_connection()
        cur = conn.cursor()
        cur.execute(query, params)
        rows = cur.fetchall()
        conn.close()
        return rows

    @classmethod
    def select_one(cls, query, params=()):
        # print("DB Select classmethod")
        conn = cls.get_connection()
        cur = conn.cursor()
        cur.execute(query, params)
        rows = cur.fetchone()
        conn.close()
        return rows
