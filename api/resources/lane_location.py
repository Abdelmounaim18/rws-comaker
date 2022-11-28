from api.data.data_endpoint_fetcher import DataEndpointFetcher
from api.models.lane_location import LaneLocationModel
import pprint
from timeit import default_timer as timer

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
            road_name = event['lanelocation']['road']
            # pprint.pprint(road_name)

            km = event['lanelocation']['km']
            # pprint.pprint(km)

            lane = event['lanelocation']['lane']
            # pprint.pprint(lane)

            carriage_way = event['lanelocation']['carriageway']
            # pprint.pprint(carriage_way)

            uuid = event['measuring_point_id'].get("uuid")
            # pprint.pprint(uuid)

            LaneLocationModel.insert_data(road_name, km, lane, carriage_way, uuid)


begin = timer()
DBAddLaneLocations.add_all_lanelocations()
eind = timer() - begin
print(f"tijd buiten de functie regel 30: {eind}")