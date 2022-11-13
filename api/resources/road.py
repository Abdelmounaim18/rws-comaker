import json
from datetime import datetime

import dateutil.parser

from api.data.data_endpoint_fetcher import DataEndpointFetcher
from api.models.road import RoadModel


class DBAddRoads:
    @classmethod
    def add_all_roads(cls):
        # combined_events = DataEndpointFetcher.combine_matching_events()
        with open('../data/converted_data/refactored_ndw_data.json') as json_file:
            combined_events = json.load(json_file)
        for event in combined_events['events']:
            try:
                road_name = event['lanelocation']['road']
                ts_event = event['ts_event']
                event_count = 0
            except:
                continue

            last_updated = dateutil.parser.isoparse(ts_event).strftime('%Y-%m-%d %H:%M:%S')
            print(road_name, last_updated, event_count)
            RoadModel.insert_data(road_name, last_updated, event_count)


DBAddRoads.add_all_roads()


