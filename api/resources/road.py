import json
from datetime import datetime, timedelta
import pprint
import dateutil.parser
from api.data.data_endpoint_fetcher import DataEndpointFetcher
from api.db.database import DB
from api.models.event import EventModel
from api.models.road import RoadModel
from timeit import default_timer as timer


class DBAddRoads:
    @classmethod
    # Adding all roads to the database.
    def add_all_roads(cls):
        start = timer()
        # combined_events = DataEndpointFetcher.combine_matching_events()
        with open('./refactored_ndw_data.json') as json_file:
            combined_events = json.load(json_file)
        count = DB.select_all('SELECT road_name, count(*) FROM Events GROUP BY road_name')
        road_name = DB.select_all('SELECT road_name FROM Events GROUP BY road_name')
        print(road_name)
        count = dict(count)
        length_count = len(count)
        # count = count.values()
        # print(f" regel 23 count length: {length_count}")
        pprint.pprint(f" regel 24 count dict: {count}")
        # print(f" regel 25 {count.values()}")
        list_count = list(count.keys())
        pprint.pprint(f" regel 26 {list_count}")
        i = 0

        road_name = ""
        event_count = 0
        ts_event = ""
        # print(f"regel 32 road name: {i}")
        # print(f"regel 33 event count:  {count[i]}")
        # event_count = count[i]
        for event in combined_events['events']:
            for i in list_count:
                road_name = i
                ts_event = event['ts_event']
                event_count = count[i]

                last_updated = dateutil.parser.isoparse(ts_event).strftime('%Y-%m-%d %H:%M:%S')
                print(road_name, last_updated, event_count)
        # RoadModel.insert_data(road_name, last_updated, event_count)

        # elapsed_time = timer() - start  # in seconds
        # print(f"elapsed_time in de functie add_all_roads: {elapsed_time}")

    @classmethod
    def road_event_count(cls):
        # a: select road_name, count(*) from Events group by road_name
        count = DB.select_all(
            'SELECT COUNT(road_name), road_name FROM RWS_DB.Events GROUP BY road_name ORDER BY road_name')
        count = dict(count)
        count = count
        print(len(count))
        print(count)
        # print(count.values())
        return count

# DBAddRoads.road_event_count()

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
