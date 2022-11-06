# import psycopg2
# import psycopg2.extras
# import psycopg2.extensions
# import pandas as pd
# import json
#
# conn = psycopg2.connect("dbname=rws user=postgres password=altun")
#
# cur = conn.cursor()
#
# conn.autocommit = True
#
#
# def create_staging_table_events(cursor):
#     cursor.execute("""
#     DROP TABLE IF EXISTS events CASCADE;
#     CREATE UNLOGGED TABLE events(
#     ts_event                    TEXT,
#     ts_state                    TEXT,
#     measuring_point_id          TEXT,
#     uuid                        TEXT
#     );""")


# def create_staging_table_lanelocation(cursor):
#     cursor.execute("""
#     DROP TABLE IF EXISTS lanelocation CASCADE;
#     CREATE UNLOGGED TABLE lanelocation(
#     road                        TEXT,
#     carroageway                 TEXT,
#     lane                        TEXT,
#     km                          TEXT
#     );""")


# def create_staging_table_roads(cursor):
#     cursor.execute("""
#     DROP TABLE IF EXISTS lanelocation CASCADE;
#     CREATE UNLOGGED TABLE lanelocation(
#     road                        TEXT,
#     carroageway                 TEXT,
#     lane                        TEXT,
#     km                          TEXT
#     );""")


# with conn.cursor() as cursor:
#     create_staging_table_lanelocation(cursor)
#     create_staging_table_events(cursor)
