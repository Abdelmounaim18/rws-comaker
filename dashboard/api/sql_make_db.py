import sqlite3
import json
import os


class ndwDataModel:

    def __init__(self, id, name):
        """ndwDataModel constructor

        Args:
            id (int): database id
            name (string): display name
        """
        self.id = id
        self.name = name

    def json(self):
        """returns json object of the model

        Returns:
            dict: json object of the model
        """
        return self.__dict__
