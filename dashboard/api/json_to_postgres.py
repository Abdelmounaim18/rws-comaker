import psycopg2
import psycopg2.extras
import psycopg2.extensions
import pandas as pd
import json

conn = psycopg2.connect("dbname=rws user=postgres password=altun")

cur = conn.cursor()

conn.autocommit = True

converted_ndw_data_json = pd.read_json("../data/converted_data/refactored_ndw_data_1.json")  # read json file
df = converted_ndw_data_json  # create dataframe
df = df.to_json()


# df['events'] = list(map(lambda x: json.dumps(x), df['events']))  # add a new column with the same value as the row
# df['events'] = json.dumps(df['events'], indent=4)
# df['events'] = json.dumps(df['events'])

# print(df)

def insert_data(df, table, cur):
    if len(df) > 0:
        # df_columns = list(df)
        # # create (col1,col2,...)
        # columns = ",".join(df_columns)

        # create VALUES('%s', '%s",...) one '%s' per column
        values = "VALUES({})".format(",".join(["%s"]))

        # create INSERT INTO table (columns) VALUES('%s',...)
        insert_stmt = "INSERT INTO {} ({}) {}".format(table, columns, values)
        cur.execute("truncate " + table + ";")  # avoid duplicates
        psycopg2.extras.execute_batch(cur, insert_stmt, df)
    conn.commit()


insert_data(df, 'ndw_data', cur)

# def create_staging_table_events(cursor):
#     cursor.execute("""
#     DROP TABLE IF EXISTS events CASCADE;
#     CREATE UNLOGGED TABLE events(
#     ts_event                    TEXT,
#     ts_state                    TEXT,
#     measuring_point_id          TEXT,
#     uuid                        TEXT
#     );""")
#
#
# def create_staging_table_lanelocation(cursor):
#     cursor.execute("""
#     DROP TABLE IF EXISTS lanelocation CASCADE;
#     CREATE UNLOGGED TABLE lanelocation(
#     road                        TEXT,
#     carroageway                 TEXT,
#     lane                        TEXT,
#     km                          TEXT
#     );""")
#
#
# def create_staging_table_roads(cursor):
#     cursor.execute("""
#     DROP TABLE IF EXISTS lanelocation CASCADE;
#     CREATE UNLOGGED TABLE lanelocation(
#     road                        TEXT,
#     carroageway                 TEXT,
#     lane                        TEXT,
#     km                          TEXT
#     );""")
#
#
# with conn.cursor() as cursor:
#     create_staging_table_lanelocation(cursor)
#     create_staging_table_events(cursor)
