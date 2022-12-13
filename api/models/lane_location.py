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
        """returns all lanelocations in the database

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
    def find_carriageway_by_road_name(cls, road_name):
        """returns all lanelocations with specified road_name

        Args:
            road_name ([int]): ID of the event

        Returns:
            dict: Event by ID
        """
        rows = DB.select_all('SELECT * FROM LaneLocations WHERE road_name = ?', (road_name,))
        locations = list()
        for row in rows:
            locations.append(LaneLocationModel(row[0], row[1], row[2], row[3], row[4], row[5]))
        return locations

    @classmethod
    def find_lanelocation_by_lane(cls, road_name, lane):
        """returns all lanelocations with specified lane

        Args:
            road_name ([int]): ID of the event

        Returns:
            dict: Event by ID
        """
        rows = DB.select_all('SELECT * FROM LaneLocations WHERE road_name = ? AND lane = ?', (road_name, lane))
        locations = list()
        for row in rows:
            locations.append(LaneLocationModel(row[0], row[1], row[2], row[3], row[4], row[5]))
        return locations

    @classmethod
    def find_lanelocation_by_carriageway(cls, road_name, carriage_way):
        """returns all lanelocations with specified carriageway

        Args:
            road_name ([int]): ID of the event

        Returns:
            dict: Event by ID
            @param road_name:
            @param carriage_way:
        """
        rows = DB.select_all('SELECT * FROM LaneLocations WHERE road_name = ? AND carriage_way = ?', (road_name, carriage_way))
        locations = list()
        for row in rows:
            locations.append(LaneLocationModel(row[0], row[1], row[2], row[3], row[4], row[5]))
        return locations

    @classmethod
    def insert_data(cls, lane_location_list):
        """Adds lanelocations to the database

        Args:
            lanelocations ([string]): Name of lanelocations
            :param lane_location_list: list of lanelocations
        """
        # the .format() method is used to format the string into a proper SQL statement using the given values as list.
        DB.create(
            'INSERT IGNORE INTO LaneLocations(road_name, km, lane, carriage_way, uuid)  VALUES{}'.format(
                ', '.join(map(str, lane_location_list))))

    def json(self):
        """Returns a JSON version of the current object

        Returns:
            dict: the object
        """
        return self.__dict__
