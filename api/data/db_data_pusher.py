import json

from api.data.data_endpoint_fetcher import DataEndpointFetcher


class DBDataPusher:

    with open("../data/converted_data/ndw_data.json", "w") as json_file:
        json_file.write(json.dumps(DataEndpointFetcher.combine_matching_events(), indent=4))
    print("file exported")


    # def upload_to_db():
    #     for event in combined_events['events']:
    #         road_name = event['lanelocation']['road']
    #         try:
    #             avg_speed = event["avgspeed"].get("kmph")
    #         except:
    #             avg_speed = None
    #
    #         try:
    #             flow_count = event["flow"].get("count")
    #         except:
    #             flow_count = None
    #         ts_event = event['ts_event']
    #         uuid = event['measuring_point_id'].get("uuid")
    #
    #     EventModel.insert_data(road_name, avg_speed, flow_count, ts_event, uuid)
