import json
import sqlite3
import os
from sqlite3 import Error


class LaneLocationModel:
    def __init__(self, id, road_name, km, lane, carriage_way, uuid):
        self.id = id
        self.road_name = road_name
        self.avg_speed = lane
        self.ts_event = carriage_way
        self.uuid = uuid

    @classmethod
    def insert_data(cls, road_name, km, lane, carriage_way, uuid):
        """Adds new category to the database

        Args:
            category ([string]): Name of new category
            :param road_name:
            :param km:
            :param lane:
            :param carriage_way:
            :param uuid:
        """
        conn = sqlite3.connect('../db/rws.sqlite')
        cur = conn.cursor()
        insert = """INSERT INTO LaneLocations(road_name, km, lane, carriage_way, uuid)  VALUES(?, ?, ?, ?, ?)"""
        cur.execute(insert, (road_name, km, lane, carriage_way, uuid))
        conn.commit()
        cur.close()

    def json(self):
        """Returns a JSON version of the current object

        Returns:
            dict: the object
        """
        return self.__dict__
