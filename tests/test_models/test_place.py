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
        inst = Place()
        self.assertEqual(str, type(inst.name))
        self.assertEqual(str, type(inst.city_id))
        self.assertEqual(str, type(inst.user_id))
        self.assertEqual(str, type(inst.description))
        self.assertEqual(int, type(inst.number_rooms))
        self.assertEqual(int, type(inst.number_bathrooms))
        self.assertEqual(int, type(inst.number_bathrooms))
        self.assertEqual(int, type(inst.max_guest))
        self.assertEqual(int, type(inst.price_by_night))
        self.assertEqual(float, type(inst.latitude))
        self.assertEqual(float, type(inst.longitude))
        self.assertEqual(list, type(inst.amenity_ids))

    def test_created_at(self):
        self.assertEqual(datetime, type(Place().created_at))

    def test_id(self):
        id1 = Place()
        id2 = Place()
        self.assertNotEqual(id1.id, id2.id)


class TestPlace_to_dict(unittest.TestCase):

    def test_check_type(self):
        inst = Place()
        self.assertTrue(dict, type(inst.to_dict))

    def test_key_check(self):
        inst = Place()
        self.assertIn("id", inst.to_dict())
        self.assertIn("created_at", inst.to_dict())
        self.assertIn("updated_at", inst.to_dict())
        self.assertIn("__class__", inst.to_dict())

    def test_date_time(self):
        inst = Place()
        inst_dict = inst.to_dict()
        self.assertTrue(str, type(inst_dict["created_at"]))
        self.assertTrue(str, type(inst_dict["updated_at"]))

    def test_save(self):
        inst = Place()
        sleep(0.05)
        first_updated_at = inst.updated_at
        inst.save()
        self.assertLess(first_updated_at, inst.updated_at)


if __name__ == '__main__':
    unittest.main()
