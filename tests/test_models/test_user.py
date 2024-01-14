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


class TestUser_instantiation(unittest.TestCase):
    def test_model_instantiation(self):
        self.assertEqual(User, type(User()))

    def test_att(self):
        inst = User()
        self.assertEqual(str, type(inst.email))
        self.assertEqual(str, type(inst.password))
        self.assertEqual(str, type(inst.first_name))
        self.assertEqual(str, type(inst.last_name))
        self.assertEqual(str, type(inst.id))

    def test_created_at(self):
        self.assertEqual(datetime, type(User().created_at))

    def test_id_equal(self):
        id1 = BaseModel()
        id2 = BaseModel()
        self.assertNotEqual(id1.id, id2.id)


class TestBaseModel_to_dict(unittest.TestCase):

    def test_check_type(self):
        inst = User()
        self.assertTrue(dict, type(inst.to_dict))

    def test_key_check(self):
        inst = User()
        self.assertIn("id", inst.to_dict())
        self.assertIn("created_at", inst.to_dict())
        self.assertIn("updated_at", inst.to_dict())
        self.assertIn("__class__", inst.to_dict())

    def test_date_time(self):
        inst = User()
        inst_dict = inst.to_dict()
        self.assertTrue(str, type(inst_dict["created_at"]))
        self.assertTrue(str, type(inst_dict["updated_at"]))

    def test_save(self):
        inst = User()
        sleep(0.05)
        first_updated_at = inst.updated_at
        inst.save()
        self.assertLess(first_updated_at, inst.updated_at)



if __name__ == '__main__':
    unittest.main()