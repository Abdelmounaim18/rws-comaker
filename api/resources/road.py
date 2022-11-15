import json
from datetime import datetime, timedelta
import pprint
import dateutil.parser
from api.data.data_endpoint_fetcher import DataEndpointFetcher
from api.models.road import RoadModel


class DBAddRoads:
    @classmethod
    def add_all_roads(cls):
        combined_events = DataEndpointFetcher.combine_matching_events()
        print(combined_events)
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
            print(road_name, last_updated, event_count)
            RoadModel.insert_data(road_name, last_updated, event_count)


DBAddRoads.add_all_roads()

# check if ts_event has a newer date than the previous one
# if so, update last_updated from ts_event
# if not, do nothing
#     @classmethod
#     def update_last_updated(cls):
#         ndw_data = open('../data/converted_data/refactored_ndw_data.json')
#         ndw_data = json.load(ndw_data)
#
#         first_date = ndw_data['events'][0]['ts_event']
#
#         for event in ndw_data['events']:
#             try:
#                 road_name = event['lanelocation']['road']
#                 ts_event = event['ts_event']
#                 if ts_event > first_date:
#                     last_updated = dateutil.parser.isoparse(ts_event).strftime('%Y-%m-%d %H:%M:%S')
#                 else:
#                     last_updated = dateutil.parser.isoparse(first_date).strftime('%Y-%m-%d %H:%M:%S')
#             except:
#                 continue
#
#             print(road_name, last_updated)
#             RoadModel.insert_data(road_name, last_updated)
#
#         old_ts_event = ndw_data['events'][0]['ts_event']
#         old_ts_event = dateutil.parser.isoparse(old_ts_event).strftime('%Y-%m-%d %H:%M:%S')
#
#         new_ts_event = ndw_data['events'][1]['ts_event']
#         new_ts_event = dateutil.parser.isoparse(new_ts_event).strftime('%Y-%m-%d %H:%M:%S')
#         if new_ts_event > old_ts_event:
#             print(f'{new_ts_event} is newer')
#         print(f'old_ts_event: {old_ts_event}, new_ts_event: {new_ts_event}')
#         pass
#
#
# DBAddRoads.update_last_updated()
