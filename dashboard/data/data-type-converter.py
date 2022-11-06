from prodict import Prodict
import json
import xmltodict
import requests
import gzip
from iteration_utilities import unique_everseen
import os

compressed_data_end_point = (
    "https://opendata.ndw.nu/Ongevalideerde_snelheden_en_Intensiteiten.xml.gz"
)


def download_file_from_url():
    url = compressed_data_end_point
    r = requests.get(url, allow_redirects=True)
    open("./raw_ndw_data.xml.gz", "wb").write(r.content)


def decompress_gzip_file():
    with gzip.open("./raw_ndw_data.xml.gz", "rb") as f:
        gzip_file_content = f.read()
        with open("./converted_data/converted_ndw_data.xml", "wb") as xml_file:
            xml_file.write(gzip_file_content)
    delete_gzip_file()


def delete_gzip_file():
    os.remove("./raw_ndw_data.xml.gz")


download_file_from_url()
decompress_gzip_file()


# converts xml to json
def convert_xml_to_json():
    with open("./converted_data/converted_ndw_data.xml") as fd:
        doc = xmltodict.parse(fd.read())
        json_data = json.dumps(doc)
        with open("./converted_data/converted_ndw_data.json", "w") as json_file:
            json_file.write(json_data)


convert_xml_to_json()

# open json file and convert to dict
with open("./converted_data/converted_ndw_data.json") as json_file:
    json_data = json.load(json_file)
    events = json_data["SOAP:Envelope"]["SOAP:Body"]["ndw:NdwMrm"][
        "minute_speed_and_flow_events"
    ]["event"]


def get_unique_measuring_point_ids():
    measuring_point_ids = []
    for event in events:
        measuring_point_ids.append(event["measuring_point_id"]["uuid"])
    unique_measuring_point_ids = list(unique_everseen(measuring_point_ids))
    return unique_measuring_point_ids


# get all events with the same measuring_point_id
def get_events_with_same_measuring_point_id(measuring_point_id):
    events_with_same_measuring_point_id = []
    for event in events:
        if event["measuring_point_id"]["uuid"] == measuring_point_id:
            events_with_same_measuring_point_id.append(event)
    return events_with_same_measuring_point_id


matched_events = []
combined_events = {}
combined_events["events"] = []

for measuring_point_id in get_unique_measuring_point_ids():
    matched_events.append(get_events_with_same_measuring_point_id(measuring_point_id))

for i in range(len(matched_events)):
    try:
        merged_event = matched_events[i][0] | matched_events[i][1] | matched_events[i][2]
        combined_events["events"].append(merged_event)
    except:
        pass

with open("./converted_data/refactored_ndw_data.json", "w") as json_file:
    json_file.write(json.dumps(combined_events, indent=4))
