#!/usr/bin/python3
''' test  Review class
    - test instantiation
    - test to_dict
'''

import unittest
import models
import uuid
from datetime import datetime
from models.base_model import BaseModel
from time import sleep
from models.review import Review
from models.engine.file_storage import FileStorage


class TestReview_instantiation(unittest.TestCase):
    '''Unittest for User class'''

    def test_model_instantiation(self):
        self.assertEqual(Review, type(Review()))

    def test_att(self):
        instant = Review()
        self.assertEqual(str, type(instant.place_id))
        self.assertEqual(str, type(instant.user_id))
        self.assertEqual(str, type(instant.text))
        self.assertEqual(str, type(instant.id))

    def test_created_at(self):
        self.assertEqual(datetime, type(Review().created_at))

    def test_id_equal(self):
        id1 = Review()
        id2 = Review()
        self.assertNotEqual(id1.id, id2.id)


class TestReview_to_dict(unittest.TestCase):

    def test_check_type(self):
        instant = Review()
        self.assertTrue(dict, type(instant.to_dict))

    def test_key_check(self):
        instant = Review()
        self.assertIn("id", instant.to_dict())
        self.assertIn("created_at", instant.to_dict())
        self.assertIn("updated_at", instant.to_dict())
        self.assertIn("__class__", instant.to_dict())

    def test_date_time(self):
        instant = Review()
        inst_dict = instant.to_dict()
        self.assertTrue(str, type(inst_dict["created_at"]))
        self.assertTrue(str, type(inst_dict["updated_at"]))

    def test_save(self):
        instant = Review()
        sleep(0.05)
        first_updated_at = instant.updated_at
        instant.save()
        self.assertLess(first_updated_at, instant.updated_at)

if __name__ == '__main__':
    unittest.main()