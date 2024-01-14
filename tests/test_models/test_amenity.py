import unittest
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):

    # Initialization Tests

    def test_initialization_default_name(self):
        amenity = Amenity()
        self.assertEqual(amenity.name, "")  # Empty string by default

    def test_initialization_with_name(self):
        amenity = Amenity(name="Gym")
        self.assertEqual(amenity.name, "Gym")

    def test_initialization_invalid_name(self):
        with self.assertRaises(ValueError):
            Amenity(name=123)  # Number is not a valid name

    # Attribute Access Tests

    def test_name_getter(self):
        amenity = Amenity(name="Pool")
        self.assertEqual(amenity.name, "Pool")

    def test_name_setter(self):
        amenity = Amenity()
        amenity.name = "Sauna"
        self.assertEqual(amenity.name, "Sauna")

    # Edge Case Tests

    def test_long_name(self):
        long_name = "A" * 100  # Excessively long name
        amenity = Amenity(name=long_name)
        self.assertEqual(amenity.name, long_name)

    def test_case_sensitivity(self):
        amenity1 = Amenity(name="Gym")
        amenity2 = Amenity(name="gym")
        self.assertNotEqual(amenity1, amenity2)  # Case-sensitive comparison

    def test_none_value(self):
        with self.assertRaises(TypeError):
            Amenity(name=None)


if __name__ == '__main__':
    unittest.main()
