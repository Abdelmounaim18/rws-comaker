from fastapi import FastAPI
import logging
import subprocess
from api.models.event import EventModel
from api.models.lane_location import LaneLocationModel
from api.models.road import RoadModel
from api.resources.event import EventByName

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/update")
def fetch_data():
    from api.data.data_endpoint_fetcher import DataEndpointFetcher
    from api.resources.road import DBAddRoads
    from api.resources.event import DBAddEvents
    from api.resources.lane_location import DBAddLaneLocations

    DataEndpointFetcher.combine_matching_events()
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


@app.get("/lanelocations/{road_name}")
def carriageway_by_road_name(road_name: str):
    return LaneLocationModel.find_carriageway_by_road_name(road_name)


@app.get("/lanelocations/{road_name}/lane/{lane}")
def lanelocation_by_lane(road_name: str, lane: int):
    return LaneLocationModel.find_lanelocation_by_lane(road_name, lane)


@app.get("/lanelocations/{road_name}/carriageway/{carriageway}")
def lanelocation_by_carriageway(road_name: str, carriageway: str):
    return LaneLocationModel.find_lanelocation_by_carriageway(road_name, carriageway)


@app.get("/events/{id_event}")
def event_by_id(self=None, id_event: int = None):
    print(f"printed regel 36 van main : {EventModel.find_event_by_id(id_event)}")
    return EventModel.find_event_by_id(id_event)


@app.get("/events/road/{name_road}")
def events_by_road_name(self=None, name_road: str = None):
    return EventByName.get(self, name_road)



##### ENDPOINT FOR LOGGING #####
# @app.get("/logs1")
# def logs():
#     result = subprocess.run(["python", "-m", "uvicorn", "api.main:app", "--reload"], capture_output=True)
#     return result.stdout.decode()
#
# @app.get("/logs")
# def logs():
#     p = subprocess.Popen(["python", "-m", "uvicorn", "api.main:app", "--reload"], stdout=subprocess.PIPE, universal_newlines=True)
#     for line in p.stdout:
#         yield line