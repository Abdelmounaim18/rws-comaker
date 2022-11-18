import json
from typing import Union

from fastapi import FastAPI

from data.data_endpoint_fetcher import DataEndpointFetcher
from resources.road import Roads, DBAddRoads

app = FastAPI()


@app.get("/roads")
def all_roads(self=None):
    return Roads.get(self)


@app.get("/fetch/ndw-data")
def fetch_data():
    DBAddRoads.add_all_roads()
    return {'msg': 'running fetch ndw data'}, 200
