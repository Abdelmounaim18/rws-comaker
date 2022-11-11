import json
from sqlite3 import Error
from api.models.roads import RoadModel


def fill_table():
    with open('../data/converted_data/refactored_ndw_data.json') as json_file:
        data = json.load(json_file)
        for p in data['events']:
            # print(p['ts_event'])
            road_name = p['lanelocation']['road']
            last_updated = p['ts_event']
            event_count = 0
            try:
                RoadModel.insert_data(road_name, last_updated, event_count)
            except Error as e:
                print("Error while connecting to sqlite", e)


fill_table()
