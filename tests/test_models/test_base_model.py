import unittest
from datetime import datetime
from models.base_model import BaseModel
from time import sleep
import models
import uuid


class TestBaseModel(unittest.TestCase):
    def test_id_equal(self):
        id1 = BaseModel()
        id2 = BaseModel()
        self.assertNotEqual(id1.id, id2.id)
    
    def test_model_instantiation(self):
        self.assertEqual(BaseModel, type(BaseModel()))



class TestBaseModel_to_dict(unittest.TestCase):
    def test_date_time(self):
        instant = BaseModel()
        inst_dict = instant.to_dict()
        self.assertTrue(str, type(inst_dict["created_at"]))
        self.assertTrue(str, type(inst_dict["updated_at"]))

    def test_check_type(self):
        instant = BaseModel
        self.assertTrue(dict, type(instant.to_dict))

    def test_key_check(self):
        instant = BaseModel()
        self.assertIn("id", instant.to_dict())
        self.assertIn("created_at", instant.to_dict())
        self.assertIn("updated_at", instant.to_dict())
        self.assertIn("__class__", instant.to_dict())



class TestBaseModel_save(unittest.TestCase):
    def test_save(self):
        instant = BaseModel()
        sleep(0.05)
        first_updated_at = instant.updated_at
        instant.save()
        self.assertLess(first_updated_at, instant.updated_at)


if __name__ == '__main__':
    unittest.main()