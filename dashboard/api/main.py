import json
from typing import Union
from fastapi import FastAPI

app = FastAPI()

with open("../data/converted_data/refactored_ndw_data.json") as json_file:
    json_data = json.load(json_file)

print(json_data["events"][0])


@app.get("/")
def read_root():
    return json_data["events"][0]


@app.get("/all-events")
def all_events():
    return json_data["events"]
