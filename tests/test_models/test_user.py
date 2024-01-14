#!/usr/bin/python3
''' test User class
    - test instantiation
    - test filStorage
'''

import unittest
from datetime import datetime
from models.base_model import BaseModel
from time import sleep
from models.user import User
from models.engine.file_storage import FileStorage
import models
import uuid


class TestUser_instantiation(unittest.TestCase):

    def test_model_instantiation(self):
        self.assertEqual(User, type(User()))

    def test_att(self):
        instant = User()
        self.assertEqual(str, type(instant.email))
        self.assertEqual(str, type(instant.password))
        self.assertEqual(str, type(instant.first_name))
        self.assertEqual(str, type(instant.last_name))
        self.assertEqual(str, type(instant.id))

    def test_created_at(self):
        self.assertEqual(datetime, type(User().created_at))

    def test_id_equal(self):
        id1 = BaseModel()
        id2 = BaseModel()
        self.assertNotEqual(id1.id, id2.id)


class TestBaseModel_to_dict(unittest.TestCase):

    def test_check_type(self):
        instant = User()
        self.assertTrue(dict, type(instant.to_dict))

    def test_key_check(self):
        instant = User()
        self.assertIn("id", instant.to_dict())
        self.assertIn("created_at", instant.to_dict())
        self.assertIn("updated_at", instant.to_dict())
        self.assertIn("__class__", instant.to_dict())

    def test_date_time(self):
        instant = User()
        inst_dict = instant.to_dict()
        self.assertTrue(str, type(inst_dict["created_at"]))
        self.assertTrue(str, type(inst_dict["updated_at"]))

    def test_save(self):
        instant = User()
        sleep(0.05)
        first_updated_at = instant.updated_at
        instant.save()
        self.assertLess(first_updated_at, instant.updated_at)



if __name__ == '__main__':
    unittest.main()