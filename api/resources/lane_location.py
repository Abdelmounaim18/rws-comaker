from api.data.data_endpoint_fetcher import DataEndpointFetcher
from api.models.lane_location import LaneLocationModel
import json
import pprint


class DBAddLaneLocations:
    @classmethod
    def add_all_lanelocations(cls):
        combined_events = DataEndpointFetcher.combine_matching_events()
        # data = open('../data/converted_data/refactored_ndw_data.json')
        # data = json.load(data)
        # # pprint.pprint(data)
        # for event in data['events']:
        #     pprint.pprint(event['measuring_point_id'].get("uuid"))
        for event in combined_events['events']:
            try:
                road_name = event['lanelocation']['road']

                km = event['lanelocation']['km']

                lane = event['lanelocation']['lane']

                carriage_way = event['lanelocation']['carriage_way']

                uuid = event['measuring_point_id'].get("uuid")
            except:
                continue

            LaneLocationModel.insert_data(road_name, km, lane, carriage_way, uuid)


DBAddLaneLocations.add_all_lanelocations()
