#!/usr/bin/python3
''' test City class
    - test instantiation
    - test to_dict
'''

import unittest
from datetime import datetime
from models.base_model import BaseModel
from time import sleep
from models.city import City
from models.engine.file_storage import FileStorage



class TestCity_instantiation(unittest.TestCase):

    def test_model_instantiation(self):
        self.assertEqual(City, type(City()))

    def test_id_equal(self):
        id1 = City()
        id2 = City()
        self.assertNotEqual(id1.id, id2.id)

    def test_att(self):
        instant = City()
        self.assertEqual(str, type(instant.name))
        self.assertEqual(str, type(instant.state_id))

    def test_created_at(self):
        self.assertEqual(datetime, type(City().created_at))



class TestCity_to_dict(unittest.TestCase):

    def test_check_type(self):
        instant = City()
        self.assertTrue(dict, type(instant.to_dict))

    def test_key_check(self):
        instant = City()
        self.assertIn("id", instant.to_dict())
        self.assertIn("created_at", instant.to_dict())
        self.assertIn("updated_at", instant.to_dict())
        self.assertIn("__class__", instant.to_dict())

    def test_date_time(self):
        instant = City()
        inst_dict = instant.to_dict()
        self.assertTrue(str, type(inst_dict["created_at"]))
        self.assertTrue(str, type(inst_dict["updated_at"]))

    def test_save(self):
        instant = City()
        sleep(0.05)
        first_updated_at = instant.updated_at
        instant.save()
        self.assertLess(first_updated_at, instant.updated_at)


if __name__ == '__main__':
    unittest.main()
