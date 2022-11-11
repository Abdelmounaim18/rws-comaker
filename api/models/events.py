import sqlite3

from operator import itemgetter, attrgetter

from api.database import DB


class EventModel:
    def __init__(self, id, road_name, avg_speed, ts_event, uuid):
        self.id = id
        self.road_name = road_name
        self.avg_speed = avg_speed
        self.ts_event = ts_event
        self.uuid = uuid

    # @classmethod
    # def find_all(cls):
    #     """returns all categories in the database
    #
    #     Returns:
    #         list: all categories
    #     """
    #
    #     conn = sqlite3.connect('../db/rws.db')
    #     cur = conn.cursor()
    #     rows = """SELECT * FROM Events"""
    #     cur.execute(rows)
    #     # print(cur.execute(rows))
    #     rows = DB.select('SELECT * FROM Events')
    #     events = list()
    #     for row in rows:
    #         events.append(EventModel(row[0], row[1], row[2], row[3], row[4]))
    #         conn.commit()
    #         cur.close()
    #     return sorted(events, key=attrgetter('road_name'))

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
        conn = sqlite3.connect('../db/rws.db')
        cur = conn.cursor()
        insert = """INSERT INTO Events(road_name, avg_speed, flow_count, ts_event, uuid)  VALUES(?, ?, ?, ?, ?)"""
        cur.execute(insert, (road_name, avg_speed, flow_count, ts_event, uuid))
        conn.commit()
        cur.close()

    def json(self):
        """Returns a JSON version of the current object

        Returns:
            dict: the object
        """
        return self.__dict__


# EventModel.find_all()
