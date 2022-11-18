import json
from datetime import datetime

import dateutil.parser

from data.data_endpoint_fetcher import DataEndpointFetcher
from flask_restful import Resource
from models.road import RoadModel


class Roads(Resource):

    def get(self):
        roads = RoadModel.find_all()
        if roads:
            return {'roads': [road.json() for road in roads]}, 200
        return {'message': 'No roads found'}, 404


class DBAddRoads(Resource):
    @classmethod
    def add_all_roads(cls):
        combined_events = DataEndpointFetcher.combine_matching_events()
        # with open('../data/converted_data/refactored_ndw_data.json') as json_file:
        #     combined_events = json.load(json_file)
        for event in combined_events['events']:
            try:
                road_name = event['lanelocation']['road']
                ts_event = event['ts_event']
                event_count = 0
            except:
                continue

            last_updated = dateutil.parser.isoparse(ts_event).strftime('%Y-%m-%d %H:%M:%S')
            RoadModel.insert_data(road_name, last_updated, event_count)


# DBAddRoads.add_all_roads()
