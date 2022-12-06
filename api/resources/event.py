from tqdm import tqdm

from api.data.data_endpoint_fetcher import DataEndpointFetcher
from api.models.event import EventModel
import json
from timeit import default_timer as timer


class DBAddEvents:
    @classmethod
    def add_all_events(cls):
        # combined_events = DataEndpointFetcher.combine_matching_events()
        with open('../refactored_ndw_data.json') as json_file:
            combined_events = json.load(json_file)
        event_list = list()
        for event in tqdm(combined_events['events']):
            try:
                road_name = event['lanelocation']['road']

                avg_speed = event["avgspeed"].get("kmph")

                flow_count = event["flow"].get("count")

                ts_event = event['ts_event']

                uuid = event['measuring_point_id'].get("uuid")
            except:
                continue

            #
            event_list.append((road_name, avg_speed, flow_count, ts_event, uuid))
            # print(event_list[0])

            # print(event_list)
        # print(event_list)
        EventModel.insert_data(event_list)


DBAddEvents.add_all_events()


class EventByName:

    def get(self, road_name):
        """returns all events by road_name
        """
        events = EventModel.find_events_by_road_name(road_name)
        if events:
            return {'events': [event.json() for event in events]}, 200
        return {'message': 'Event not found'}, 404


class EventById:

    def get(self, id_event):
        """return event by ID

        Args:
            id_event ([int]): ID of the category

        Returns:
            dict: contains category by ID
        """
        event = EventModel.find_event_by_id(id_event)
        if event:
            print(f"printed regel 41 van resources/event {event}")
            return event.json(), 200
        return {'message': 'No event found'}, 404
