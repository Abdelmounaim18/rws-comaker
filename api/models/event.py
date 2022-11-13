from mariadb import IntegrityError, Error

from api.db import database
from operator import itemgetter, attrgetter

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
        print(rows)
        return sorted(events, key=attrgetter('ts_event'))

    @classmethod
    def insert_data(cls, road_name, avg_speed, flow_count, ts_event, uuid):
        """Adds events to the database

        Args:
            events ([string]): Name of events
            :param road_name:
            :param avg_speed:
            :param flow_count:
            :param ts_event:
            :param uuid:
        """
        db_values = (road_name, avg_speed, flow_count, ts_event, uuid)
        try:
            DB.create(
                'INSERT INTO Events(road_name, avg_speed, flow_count, ts_event, uuid)  VALUES(?, ?, ?, ?, ?)',
                db_values)
        except Error:
            print(Error)

    def json(self):
        """Returns a JSON version of the current object

        Returns:
            dict: the object
        """
        return self.__dict__


EventModel.find_all()
