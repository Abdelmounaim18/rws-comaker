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
            count = DB.select_one('SELECT road_name, count(*) FROM Events WHERE road_name = ?', (row[1],))
            events.append(RoadModel(row[0], row[1], row[2], count[1]))
        return sorted(events, key=attrgetter('road_name'))

    @classmethod
    def insert_data(cls, road_list):
        """Adds road_list to the database

        Args:
            road_list ([string]): Name of road_list
            :param road_list
        """

        # the .format() method is used to format the string into a proper SQL statement using the given values as list.
        DB.create(
            'INSERT IGNORE INTO Roads(road_name, last_updated, event_count ) VALUES{}'.format(
                ', '.join(map(str, road_list))))

    def json(self):
        """Returns a JSON version of the current object

        Returns:
            dict: the object
        """
        return self.__dict__

