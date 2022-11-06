import json
with open("./data/converted_data/refactored_ndw_data.json") as json_file:
    json_data = json.load(json_file)



print(json_data["events"][0])