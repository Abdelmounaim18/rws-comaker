import json
from typing import Union
from fastapi import FastAPI
from api.models.event import EventModel

app = FastAPI()

with open("data/converted_data/refactored_ndw_data.json") as json_file:
    json_data = json.load(json_file)

# print(EventModel.find_all())
test = EventModel.find_all()


@app.get("/")
def read_root():
    # return test
    return json_data["events"][0]


@app.get("/all-events")
def all_events():
    return test
