import json
import pprint
from sqlite3 import Error
from api.models.lane_locations import LaneLocationModel


def fill_table():
    with open('../data/converted_data/refactored_ndw_data.json') as json_file:
        data = json.load(json_file)
        for p in data['events']:
            # pprint.pprint(p)
            # pprint.pprint(p["lanelocation"]["carriageway"])
            road_name = p['lanelocation']['km']
            km = p["lanelocation"]["km"]
            lane = p["lanelocation"]["lane"]
            carriage_way = p["lanelocation"]["carriageway"]
            uuid = p['measuring_point_id'].get("uuid")
            try:
                LaneLocationModel.insert_data(road_name, km, lane, carriage_way, uuid)
            except Error as e:
                print("Error while connecting to sqlite", e)


fill_table()
