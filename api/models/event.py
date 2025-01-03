from locale import Error

from operator import itemgetter, attrgetter

import pandas as pd

from api.db.database import DB


class EventModel:

    def __init__(self, id, road_name, avg_speed, flow_count, ts_event, uuid):
        self.id = id
        self.road_name = road_name
        self.avg_speed = avg_speed
        self.flow_count = flow_count
        self.ts_event = ts_event
        self.uuid = uuid

    @classmethod
    def find_all(cls):
        """returns all categories in the database

        Returns:
            list: all categories
        """
        rows = DB.select_all('SELECT * FROM Events')
        events = list()
        for row in rows:
            events.append(EventModel(row[0], row[1], row[2], row[3], row[4], row[5]))
        # print(rows)
        return sorted(events, key=attrgetter('ts_event'))

    @classmethod
    def find_event_by_id(cls, id_event):
        """returns one category by ID from the database

        Args:
            id_event ([int]): ID of the event

        Returns:
            dict: Event by ID
        """
        row = DB.select_one('SELECT * FROM Events WHERE id = ?', (id_event,))
        if row:
            event = EventModel(row[0], row[1], row[2], row[3], row[4], row[5])
        else:
            return None
        print(f"dit is een row regel 48 models/event: {row}")
        return row

    @classmethod
    def find_events_by_road_name(cls, road_name):
        """returns one category by ID from the database

        Args:
            road_name ([int]): ID of the event

        Returns:
            dict: Event by ID
        """

        rows = DB.select_all('SELECT * FROM Events WHERE road_name = ?', (road_name,))
        events = list()
        for row in rows:
            # print(f"dit is een row regel 63 models/event: {row}")
            events.append(EventModel(row[0], row[1], row[2], row[3], row[4], row[5]))

        # print(f"dit is een row regel 67 models/event: {row}")
        return sorted(events, key=attrgetter('ts_event'))

    @classmethod
    def insert_data(cls, event_list):
        """Adds events to the database

        Args:
            events ([string]): Name of events
            :param event_list: list of events
        """

        # the .format() method is used to format the string into a proper SQL statement using the given values as list.
        DB.create(
            'INSERT IGNORE INTO Events(road_name, avg_speed, flow_count, ts_event, uuid) VALUES{}'.format(
                ', '.join(map(str, event_list))))


def json(self):
    """Returns a JSON version of the current object

    Returns:
        dict: the object
    """
    return self.__dict__


# EventModel.find_all()
