import unittest
from datetime import datetime
from models.base_model import BaseModel
from time import sleep


class TestBaseModel(unittest.TestCase):
    def test_id_equal(self):
        id1 = BaseModel()
        id2 = BaseModel()
        self.assertNotEqual(id1.id, id2.id)

    def test_model_instantiation(self):
        self.assertEqual(BaseModel, type(BaseModel()))


class TestBaseModel_to_dict(unittest.TestCase):
    def test_date_time(self):
        inst = BaseModel()
        inst_dict = inst.to_dict()
        self.assertTrue(str, type(inst_dict["created_at"]))
        self.assertTrue(str, type(inst_dict["updated_at"]))

    def test_check_type(self):
        inst = BaseModel
        self.assertTrue(dict, type(inst.to_dict))

    def test_key_check(self):
        inst = BaseModel()
        self.assertIn("id", inst.to_dict())
        self.assertIn("created_at", inst.to_dict())
        self.assertIn("updated_at", inst.to_dict())
        self.assertIn("__class__", inst.to_dict())


class TestBaseModel_save(unittest.TestCase):
    def test_save(self):
        inst = BaseModel()
        sleep(0.05)
        first_updated_at = inst.updated_at
        inst.save()
        self.assertLess(first_updated_at, inst.updated_at)


if __name__ == '__main__':
    unittest.main()
