import json
from typing import Union

from fastapi import FastAPI

from resources.road import Roads

app = FastAPI()


@app.get("/roads")
def all_roads(self=None):
    return Roads.get(self)
