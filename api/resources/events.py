import json
from datetime import datetime

from mariadb import Error

from api.models.events import EventModel


def fill_table():
    with open('../data/converted_data/refactored_ndw_data.json') as json_file:
        data = json.load(json_file)
        for p in data['events']:
            print(p)
            road_name = p['lanelocation']['road']
            try:
                avg_speed = p["avgspeed"].get("kmph")
            except:
                avg_speed = None
            try:
                flow_count = p["flow"].get("count")
            except:
                flow_count = None
            ts_event = p['ts_event']
            uuid = p['measuring_point_id'].get("uuid")

            EventModel.insert_data(road_name, avg_speed, flow_count, ts_event, uuid)


fill_table()
