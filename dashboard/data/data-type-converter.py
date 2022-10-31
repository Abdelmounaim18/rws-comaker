from prodict import Prodict
import json
import xmltodict
import requests
import gzip
# from urllib import request
from iteration_utilities import unique_everseen
import pandas as pd
import os


compressed_data_end_point = (
    "https://opendata.ndw.nu/Ongevalideerde_snelheden_en_Intensiteiten.xml.gz"
)


# def download_file_from_url():
#     url = compressed_data_end_point
#     r = requests.get(url, allow_redirects=True)
#     open("./raw_ndw_data.xml.gz", "wb").write(r.content)



# def decompress_gzip_file():
#     with gzip.open("./raw_ndw_data.xml.gz", "rb") as f:
#         file_content = f.read()
#         xml_content = xmltodict.parse(file_content)
#         json_content = json.dumps(xml_content)
#         with open("./converted_data/converted_ndw_data.json", "w") as json_file:
#             json_file.write(json_content)
        
#         delete_gzip_file()


# def delete_gzip_file():
#     import os
#     os.remove("./raw_ndw_data.xml.gz")

# decompress_gzip_file()
# download_file_from_url()



with open("./converted_data/converted_ndw_data.json", "rb") as f:
    data = Prodict.from_dict(json.load(f))
    events = data["SOAP:Envelope"]["SOAP:Body"]["ndw:NdwMrm"][
        "minute_speed_and_flow_events"
    ]["event"]

event_dict = {}
# event_dict["measurements"] = []


for event in events:
    try:
        road = event["lanelocation"]["road"]
        event_dict[road] = []
        measuring_point_id = event["measuring_point_id"]["uuid"]

        try:
            if not avgspeed = event["avgspeed"]["kmph"]
        except:
            pass
        try:
            flow_count = event["flow"]["count"]
        except:
            pass

      

        # event_dict[road][event["measuring_point_id"]["uuid"]] = {"speed": event["avgspeed"]["kmph"], "flow": event["flow"]["count"]}
    except:
        next
    
    event_dict[road].append({
            "id": measuring_point_id,
            "avgspeed": avgspeed,
            "flow_count": flow_count
            })
    
    # print(measuring_point_id)

    # if measuring_point_id in event_dict[road]:
    #     print(measuring_point_id)
    #     event_dict[road][measuring_point_id]["speed"].append(avgspeed)
    #     event_dict[road][measuring_point_id]["flow"].append(flow_count)

    

print(event_dict)
# event_dict = list(unique_everseen(event_dict))





# x = 0
# while x < len(event_dict):

#     try:
#             if any(event["measuring_point_id"]["uuid"] in key for key in event_dict[x]):
#                 print("yes")
#                 event_dict[x]["road"] = event["lanelocation"]["road"]
#                 # event_dict[x]["e9af9383-2d7f-4963-88c9-38aa1d9c33cc"] = {"speed": 10, "flow": 10}
#     except:
#             next

#     print(event_dict[x])
#     for event in events:
#         # if event["measuring_point_id"]["uuid"] == event_dict[x]:
#         #     event_dict[x]["road"] = event["lanelocation"]["road"]
#         try:
#             if any(event["measuring_point_id"]["uuid"] in key for key in event_dict[x]):
#                 print("yes")
#                 event_dict[x]["road"] = event["lanelocation"]["road"]
#                 # event_dict[x]["e9af9383-2d7f-4963-88c9-38aa1d9c33cc"] = {"speed": 10, "flow": 10}
#         except:
#             next
    
#     x+=1


with open("./converted_data/clean_ndw_data.json", "w") as json_file:
    json_file.write(json.dumps(event_dict, indent=4))
