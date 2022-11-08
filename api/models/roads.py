import sqlite3
import os
from sqlite3 import Error


class RoadModel:
    def __init__(self, id, road_name, last_updated, event_count):
        self.id = id
        self.road_name = road_name
        self.last_updated = last_updated
        self.event_count = event_count


def insert_data(road_name, last_updated, event_count):
    """Adds new category to the database

    Args:
        category ([string]): Name of new category
        :param event_count:
        :param last_updated:
        :param road_name:
    """
    conn = sqlite3.connect('../db/rws.sqlite')
    cur = conn.cursor()
    data = """INSERT INTO Roads(road_name, last_updated, event_count) VALUES(?, ?, ?)"""
    cur.execute(data, (road_name, last_updated, event_count))
    conn.commit()
    cur.close()


# def json(self):
#     return self.__dict__

insert_data("A1", "2021-01-01 00:00:00", 0)
