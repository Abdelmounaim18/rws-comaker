import json
import pprint
from sqlite3 import Error
from api.models.events import EventModel


def fill_table():
    with open('../data/converted_data/refactored_ndw_data.json') as json_file:
        data = json.load(json_file)
        for p in data['events']:
            # pprint.pprint(p)
            # pprint.pprint(p["avgspeed"].get("kmph"))
            road_name = p['lanelocation']['road']
            avg_speed = p["avgspeed"].get("kmph")
            flow_count = p["flow"].get("count")
            ts_event = p['ts_event']
            uuid = p['measuring_point_id'].get("uuid")
            if avg_speed == 0:
                try:
                    EventModel.insert_data(road_name, "0", flow_count, ts_event, uuid)
                except Error as e:
                    print("Error while connecting to sqlite", e)
            if flow_count == 0:
                try:
                    EventModel.insert_data(road_name, avg_speed, "0", ts_event, uuid)
                except Error as e:
                    print("Error while connecting to sqlite", e)
            else:
                try:
                    EventModel.insert_data(road_name, avg_speed, flow_count, ts_event, uuid)
                except Error as e:
                    print("Error while connecting to sqlite", e)


fill_table()
