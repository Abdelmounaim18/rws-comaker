import json
import pprint
import dateutil.parser
from tqdm import tqdm

from api.db.database import DB
from api.models.event import EventModel
from api.models.road import RoadModel
from timeit import default_timer as timer


class DBAddRoads:
    @classmethod
    def add_all_roads(cls):
        """
        Add all roads to the database

        @return: Nothing
        """
        road_list = []

        with open('./refactored_ndw_data.json') as json_file:
            combined_events = json.load(json_file)
        # querying event count for each road
        count = DB.select_all(
            'SELECT road_name, count(*) FROM Events GROUP BY road_name')
        count = dict(count)  # converting to dict for easier access

        # querying the latest event for each road
        latest_event = DB.select_all(
            'SELECT road_name, max(ts_event) FROM Events GROUP BY road_name')
        # making a dictionary to easily access and extract the latest event for each road
        latest_event = dict(latest_event)
        # extracting the latest event for each road
        latest_date = list(latest_event.values())
        # extracting the road names from the dictionary
        road_names_count_list = list(count.keys())
        # appending all roads to a list
        for i in road_names_count_list:
            road_name = i
            event_count = count[i]
            last_updated = latest_date[road_names_count_list.index(i)]
            last_updated = dateutil.parser.isoparse(last_updated).strftime('%Y-%m-%d %H:%M:%S')

            road_list.append((road_name, last_updated, event_count))

        RoadModel.insert_data(road_list)


# DBAddRoads.add_all_roads()
# DBAddRoads.road_event_count()
