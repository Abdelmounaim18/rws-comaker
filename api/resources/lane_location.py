import json

from api.data.data_endpoint_fetcher import DataEndpointFetcher
from api.models.lane_location import LaneLocationModel
import pprint
from timeit import default_timer as timer


class DBAddLaneLocations:
    @classmethod
    def add_all_lanelocations(cls):
        """
        Add all lanelocations to the database
        @return: Nothing
        """

        lane_location_list = []

        with open('./refactored_ndw_data.json') as json_file:
            combined_events = json.load(json_file)

        # appending all lanelocations to a list
        for event in combined_events['events']:
            try:
                road_name = event['lanelocation']['road']
                km = event['lanelocation']['km']
                lane = event['lanelocation']['lane']
                carriage_way = event['lanelocation']['carriageway']
                uuid = event['measuring_point_id'].get("uuid")
            except:
                continue

            lane_location_list.append((road_name, km, lane, carriage_way, uuid))

        LaneLocationModel.insert_data(lane_location_list)


# DBAddLaneLocations.add_all_lanelocations()
