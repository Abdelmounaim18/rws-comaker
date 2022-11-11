import json
import sqlite3
import os
from sqlite3 import Error


class RoadModel:
    def __init__(self, id, road_name, last_updated, event_count):
        self.id = id
        self.road_name = road_name
        self.last_updated = last_updated
        self.event_count = event_count

    @classmethod
    def insert_data(cls, road_name, last_updated, event_count):
        """Adds new category to the database

        Args:
            category ([string]): Name of new category
            :param event_count:
            :param last_updated:
            :param road_name:
        """
        conn = sqlite3.connect('../db/rws.sqlite')
        cur = conn.cursor()
        insert = """INSERT INTO Roads(road_name, last_updated, event_count) VALUES(?, ?, ?)"""
        cur.execute(insert, (road_name, last_updated, event_count))
        conn.commit()
        cur.close()

    def json(self):
        """Returns a JSON version of the current object

        Returns:
            dict: the object
        """
        return self.__dict__
