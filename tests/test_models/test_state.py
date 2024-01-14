#!/usr/bin/python3
''' test State class
    - test instantiation
    - test to_dict
'''

import unittest
from datetime import datetime
from models.base_model import BaseModel
from time import sleep
from models.state import State
from models.engine.file_storage import FileStorage
import models
import uuid



class TestState_instantiation(unittest.TestCase):

    def test_model_instantiation(self):
        self.assertEqual(State, type(State()))

    def test_att(self):
        instant = State()
        self.assertEqual(str, type(instant.name))
        self.assertEqual(str, type(instant.id))

    def test_created_at(self):
        self.assertEqual(datetime, type(State().created_at))


def test_id_equal(self):
    id1 = BaseModel()
    id2 = BaseModel()
    self.assertNotEqual(id1.id, id2.id)


class TestState_to_dict(unittest.TestCase):

    def test_check_type(self):
        instant = State()
        self.assertTrue(dict, type(instant.to_dict))

    def test_key_check(self):
        instant = State()
        self.assertIn("id", instant.to_dict())
        self.assertIn("created_at", instant.to_dict())
        self.assertIn("updated_at", instant.to_dict())
        self.assertIn("__class__", instant.to_dict())

    def test_date_time(self):
        instant = State()
        inst_dict = instant.to_dict()
        self.assertTrue(str, type(inst_dict["created_at"]))
        self.assertTrue(str, type(inst_dict["updated_at"]))

    def test_save(self):
        instant = State()
        sleep(0.05)
        first_updated_at = instant.updated_at
        instant.save()
        self.assertLess(first_updated_at, instant.updated_at)

if __name__ == '__main__':
    unittest.main()