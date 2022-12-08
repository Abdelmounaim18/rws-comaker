import pprint
from operator import attrgetter

from mariadb import IntegrityError, Error
from api.db.database import DB


class LaneLocationModel:

    def __init__(self, id, road_name, km, lane, carriage_way, uuid):
        self.id = id
        self.road_name = road_name
        self.km = km
        self.lane = lane
        self.carriage_way = carriage_way
        self.uuid = uuid

    @classmethod
    def find_all(cls):
        """returns all categories in the database

        Returns:
            list: all categories
        """
        rows = DB.select_all('SELECT * FROM LaneLocations')
        locations = list()
        for row in rows:
            locations.append(LaneLocationModel(row[0], row[1], row[2], row[3], row[4], row[5]))
        # print(rows)
        return sorted(locations, key=attrgetter('road_name'))

    @classmethod
    def insert_data(cls, lane_location_list):
        """Adds lanelocations to the database

        Args:
            lanelocations ([string]): Name of lanelocations
            :param lane_location_list: list of lanelocations
        """
        # the .format() method is used to format the string into a proper SQL statement using the given values as list.
        DB.create(
            'INSERT INTO LaneLocations(road_name, km, lane, carriage_way, uuid)  VALUES{}'.format(
                ', '.join(map(str, lane_location_list))))

    def json(self):
        """Returns a JSON version of the current object

        Returns:
            dict: the object
        """
        return self.__dict__
