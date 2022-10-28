from prodict import Prodict
import json
import xmltodict
import requests
import gzip
# from urllib import request
import pandas as pd
import os

compressed_data_end_point = (
    "https://opendata.ndw.nu/Ongevalideerde_snelheden_en_Intensiteiten.xml.gz"
)


def download_file_from_url():
    url = compressed_data_end_point
    r = requests.get(url, allow_redirects=True)
    open("./raw_ndw_data.xml.gz", "wb").write(r.content)
    decompress_gzip_file()


def decompress_gzip_file():
    with gzip.open("./raw_ndw_data.xml.gz", "rb") as f:
        file_content = f.read()
        xml_content = xmltodict.parse(file_content)
        json_content = json.dumps(xml_content)
        with open("./converted_data/converted_ndw_data.json", "w") as json_file:
            json_file.write(json_content)
        delete_gzip_file()


def delete_gzip_file():
    import os

    os.remove("./raw_ndw_data.xml.gz")


download_file_from_url()


with open("./converted_data/converted_ndw_data.json", "rb") as f:
    data = Prodict.from_dict(json.load(f))
    events = data["SOAP:Envelope"]["SOAP:Body"]["ndw:NdwMrm"][
        "minute_speed_and_flow_events"
    ]["event"]

event_dict = {}
event_dict["roads"] = {}

for event in events:
    try:
        road_name = event["lanelocation"]["road"]
        event_dict["roads"][road_name] = {}
    except:
        next
    try:
        event_dict["roads"][road_name]["last_event_update"] = event["ts_event"]
        event_dict["roads"][road_name]["measuring_point_id"] = event["measuring_point_id"]["uuid"]
        event_dict["roads"][road_name]["average_speed"] = event["avgspeed"]["kmph"]
    except:
        next
    try:
        event_dict["roads"][road_name]["vehicle_count"] = event["flow"]["count"]
    except:
        next

with open("./converted_data/clean_ndw_data.json", "w") as json_file:
    json_file.write(json.dumps(event_dict, indent=4))

test_dict = {}

for event in events:
    test_dict.update(event)

   

with open("./converted_data/test_ndw_data.json", "w") as json_file:
    json_file.write(json.dumps(test_dict, indent=4))
