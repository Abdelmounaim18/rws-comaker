import json
import xmltodict
import requests
import gzip
from iteration_utilities import unique_everseen
import os
import logging
from timeit import default_timer as timer
from tqdm import tqdm

logger = logging.getLogger(__name__)


class DataEndpointFetcher:
    @classmethod
    def fetch_data(cls):
        begin = timer()
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
        eind = timer() - begin
        print(f"Download & unzip tijd regel 35: {eind}")

    @classmethod
    def get_unique_measuring_point_ids(cls):
        start = timer()
        measuring_point_ids = []
        for event in cls.ndw_events:
            measuring_point_ids.append(event["measuring_point_id"]["uuid"])
        unique_measuring_point_ids = list(unique_everseen(measuring_point_ids))
        end = timer() - start
        print(f"get unique measuring point id tijd regel 45: {end}")
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
        start = timer()
        matched_events = []
        combined_events = {"events": []}
        print("starting comparing ids")
        for measuring_point_id in tqdm(cls.get_unique_measuring_point_ids()):
            matched_events.append(cls.get_events_with_same_measuring_point_id(measuring_point_id))
        end = timer() - start
        print(f"\neinde van comparing ids tijd regel 68: {end}")
        print("starting matching events")
        begin = timer()
        for i in tqdm(range(len(matched_events))):
            try:
                merged_event = matched_events[i][0] | matched_events[i][1] | matched_events[i][2]
                combined_events["events"].append(merged_event)
            except:
                continue
        print("finished combining")
        with open("../refactored_ndw_data.json", "w") as json_file:
            json_file.write(json.dumps(combined_events, indent=4))
        eind = timer() - begin
        print(f"einde van combining events tijd regel 81: {eind}")

        return combined_events

# DataEndpointFetcher.fetch_data()
# DataEndpointFetcher.combine_matching_events()
