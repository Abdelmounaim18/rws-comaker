import json
import xmltodict
import requests
import gzip
from iteration_utilities import unique_everseen
import os
import logging

logger = logging.getLogger(__name__)


class DataEndpointFetcher:
    compressed_data_end_point = (
        "https://opendata.ndw.nu/Ongevalideerde_snelheden_en_Intensiteiten.xml.gz"
    )

    url = compressed_data_end_point
    get_request = requests.get(url, allow_redirects=True)
    open("./raw_ndw_data.xml.gz", "wb").write(get_request.content)

    with gzip.open("./raw_ndw_data.xml.gz", "rb") as f:
        gzip_file_content = f.read()
        doc = xmltodict.parse(gzip_file_content)
        json_data = json.dumps(doc)
        converted_ndw_data = json.loads(json_data)
    print("downloaded and unzipped file")
    ndw_events = converted_ndw_data["SOAP:Envelope"]["SOAP:Body"]["ndw:NdwMrm"][
        "minute_speed_and_flow_events"
    ]["event"]

    os.remove("./raw_ndw_data.xml.gz")

    @classmethod
    def get_unique_measuring_point_ids(cls):
        measuring_point_ids = []
        for event in cls.ndw_events:
            measuring_point_ids.append(event["measuring_point_id"]["uuid"])
        unique_measuring_point_ids = list(unique_everseen(measuring_point_ids))
        return unique_measuring_point_ids

    @classmethod
    def get_events_with_same_measuring_point_id(cls, measuring_point_id):
        events_with_same_measuring_point_id = []
        for event in cls.ndw_events:
            if event["measuring_point_id"]["uuid"] == measuring_point_id:
                events_with_same_measuring_point_id.append(event)
        return events_with_same_measuring_point_id

    @classmethod
    def combine_matching_events(cls):
        matched_events = []
        combined_events = {"events": []}
        print("starting comparing ids")
        for measuring_point_id in cls.get_unique_measuring_point_ids():
            matched_events.append(cls.get_events_with_same_measuring_point_id(measuring_point_id))
        print("starting matching events")
        for i in range(len(matched_events)):
            try:
                merged_event = matched_events[i][0] | matched_events[i][1] | matched_events[i][2]
                combined_events["events"].append(merged_event)
            except:
                continue
        print("finished combining")
        # with open("../data/converted_data/refactored_ndw_data.json", "w") as json_file:
        #     json_file.write(json.dumps(combined_events, indent=4))

        return combined_events
