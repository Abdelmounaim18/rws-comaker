from operator import attrgetter
from api.db.database import DB


class RoadModel:
    def __init__(self, id, road_name, last_updated, event_count):
        self.id = id
        self.road_name = road_name
        self.last_updated = last_updated
        self.event_count = event_count

    @classmethod
    def find_all(cls):
        """returns all categories in the database

        Returns:
            list: all categories
        """
        rows = DB.select_all('SELECT * FROM Roads')
        events = list()
        for row in rows:
            events.append(RoadModel(row[0], row[1], row[2], row[3]))
        return sorted(events, key=attrgetter('road_name'))

    @classmethod
    def insert_data(cls, road_name, last_updated, event_count):
        """Adds events to the database

        Args:
            events ([string]): Name of events
            :param event_count:
            :param last_updated:
            :param road_name:
        """

        db_values = (road_name, last_updated, event_count)

        try:
            DB.create(
                'INSERT INTO Roads(road_name, last_updated, event_count ) VALUES(?, ?, ?) ON DUPLICATE KEY UPDATE '
                'road_name = road_name',
                db_values)
        except:
            pass

    def json(self):
        """Returns a JSON version of the current object

        Returns:
            dict: the object
        """
        return self.__dict__

    @classmethod
    def update_event_count(cls, road_name, event_count):
        pass
