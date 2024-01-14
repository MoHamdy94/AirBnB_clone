#!/usr/bin/python3
''' test Place class
    - test instantiation
    - test to_dict
'''

import unittest
from datetime import datetime
from models.base_model import BaseModel
from time import sleep
from models.place import Place
from models.engine.file_storage import FileStorage



class TestPlace_instantiation(unittest.TestCase):
    '''Unittest for User class'''

    def test_model_instantiation(self):
        self.assertEqual(Place, type(Place()))

    def test_att(self):
        instant = Place()
        self.assertEqual(str, type(instant.name))
        self.assertEqual(str, type(instant.city_id))
        self.assertEqual(str, type(instant.user_id))
        self.assertEqual(str, type(instant.description))
        self.assertEqual(int, type(instant.number_rooms))
        self.assertEqual(int, type(instant.number_bathrooms))
        self.assertEqual(int, type(instant.number_bathrooms))
        self.assertEqual(int, type(instant.max_guest))
        self.assertEqual(int, type(instant.price_by_night))
        self.assertEqual(float, type(instant.latitude))
        self.assertEqual(float, type(instant.longitude))
        self.assertEqual(list, type(instant.amenity_ids))

    def test_created_at(self):
        self.assertEqual(datetime, type(Place().created_at))

    def test_id(self):
        id1 = Place()
        id2 = Place()
        self.assertNotEqual(id1.id, id2.id)


class TestPlace_to_dict(unittest.TestCase):

    def test_check_type(self):
        instant = Place()
        self.assertTrue(dict, type(instant.to_dict))

    def test_key_check(self):
        instant = Place()
        self.assertIn("id", instant.to_dict())
        self.assertIn("created_at", instant.to_dict())
        self.assertIn("updated_at", instant.to_dict())
        self.assertIn("__class__", instant.to_dict())

    def test_date_time(self):
        instant = Place()
        inst_dict = instant.to_dict()
        self.assertTrue(str, type(inst_dict["created_at"]))
        self.assertTrue(str, type(inst_dict["updated_at"]))

    def test_save(self):
        instant = Place()
        sleep(0.05)
        first_updated_at = instant.updated_at
        instant.save()
        self.assertLess(first_updated_at, instant.updated_at)

if __name__ == '__main__':
    unittest.main()