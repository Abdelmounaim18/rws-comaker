import json
from typing import Union

from fastapi import FastAPI

from api.data.data_endpoint_fetcher import DataEndpointFetcher
from api.models.event import EventModel
from api.models.lane_location import LaneLocationModel
from api.models.road import RoadModel
from api.resources.event import EventById, EventByName, DBAddEvents
from api.resources.lane_location import DBAddLaneLocations
from api.resources.road import DBAddRoads

app = FastAPI()

#
# @app.get("/")
# def root():
#     return {"message": "not found"}


@app.get("/update")
def fetch_data():
    # DataEndpointFetcher.combine_matching_events()
    DBAddRoads.add_all_roads()
    DBAddEvents.add_all_events()
    DBAddLaneLocations.add_all_lanelocations()
    return {"message": "fetched new data"}


@app.get("/roads")
def all_roads():
    return RoadModel.find_all()


@app.get("/events")
def all_events():
    return EventModel.find_all()


@app.get("/lanelocations")
def all_events():
    return LaneLocationModel.find_all()


@app.get("/events/{id_event}")
def event_by_id(self=None, id_event: int = None):
    print(f"printed regel 36 van main : {EventModel.find_event_by_id(id_event)}")
    return EventModel.find_event_by_id(id_event)


@app.get("/events/road/{name_road}")
def events_by_road_name(self=None, name_road: str = None):
    return EventByName.get(self, name_road)
