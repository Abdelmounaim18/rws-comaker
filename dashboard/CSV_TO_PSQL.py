import psycopg2
import psycopg2.extras

import pandas as pd

# Connect to an existing database
conn = psycopg2.connect("dbname=rws user=postgres password=altun")

cur = conn.cursor()

conn.autocommit = True

csv_file = pd.read_csv("./xml-to-csv-converter.csv")
csv_file.reset_index(drop=True, inplace=True)
csv_file.head()


# print(csv_file)


def create_staging_table(cursor):
    cursor.execute("""
    DROP TABLE IF EXISTS staging_ndw_data CASCADE;
    CREATE UNLOGGED TABLE staging_ndw_data(
    ts_event                    TEXT,
    ts_state                    TEXT,
    measuring_point_id_uuid     TEXT,
    lanelocation_road           TEXT,
    lanelocation_carriageway    TEXT,
    lanelocation_lane           TEXT,
    lanelocation_km             TEXT,
    avgspeed_kmph               TEXT,
    flow_count                  TEXT,
    avgspeed_unknown            TEXT,
    flow_uknown                 TEXT,
    avgspeed_no_traffic         TEXT
    );""")


#
#
with conn.cursor() as cursor:
    create_staging_table(cursor)


def send_csv_to_psql(connection, csv, table_):
    sql = "COPY %s FROM STDIN WITH CSV HEADER DELIMITER AS ','"
    file = open(csv, "r")
    table = table_
    with connection.cursor() as cur:
        cur.execute("truncate " + table + ";")  # avoid duplicates
        cur.copy_expert(sql=sql % table, file=file)
        connection.commit()
        print("Data copied to " + table + " table")
    return connection.commit()


send_csv_to_psql(conn, "./xml-to-csv-converter.csv", "staging_ndw_data")
