import json
from typing import Union

from fastapi import FastAPI

from api.models.event import EventModel
from api.models.lane_location import LaneLocationModel
from api.models.road import RoadModel
from api.resources.event import EventById

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/roads")
async def all_roads():
    return RoadModel.find_all()


@app.get("/events")
async def all_events():
    return EventModel.find_all()


@app.get("/lanelocations")
async def all_events():
    return LaneLocationModel.find_all()


@app.get("/events/{id_event}")
async def event_by_id(id_event: int):
    print(f"printed regel 36 van main : {EventModel.find_event_by_id(id_event)}")
    return EventModel.find_event_by_id(id_event)
    # return {'message': 'resource not found'}, 404
