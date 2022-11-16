import json

from api.data.data_endpoint_fetcher import DataEndpointFetcher
from api.models.event import EventModel


class DBAddEvents:
    @classmethod
    def add_all_events(cls):
        combined_events = DataEndpointFetcher.combine_matching_events()
        for event in combined_events['events']:
            try:
                road_name = event['lanelocation']['road']

                avg_speed = event["avgspeed"].get("kmph")

                flow_count = event["flow"].get("count")

                ts_event = event['ts_event']
                uuid = event['measuring_point_id'].get("uuid")
            except:
                continue

            EventModel.insert_data(road_name, avg_speed, flow_count, ts_event, uuid)


DBAddEvents.add_all_events()
