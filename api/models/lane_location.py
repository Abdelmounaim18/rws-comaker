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
        print(rows)
        return locations

    @classmethod
    def insert_data(cls, road_name, km, lane, carriage_way, uuid):
        """Adds events to the database

        Args:
            events ([string]): Name of events
            :param road_name:
            :param km:
            :param lane:
            :param carriage_way:
            :param uuid:
        """
        db_values = (road_name, km, lane, carriage_way, uuid)
        DB.create(
            'INSERT INTO LaneLocations(road_name, km, lane, carriage_way, uuid)  VALUES(?, ?, ?, ?, ?)',
            db_values)

    def json(self):
        """Returns a JSON version of the current object

        Returns:
            dict: the object
        """
        return self.__dict__

# LaneLocationModel.find_all()
