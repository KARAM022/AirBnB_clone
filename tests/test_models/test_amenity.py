#!/usr/bin/python3
import unittest
from models.amenity import Amenity

class TestModels(unittest.TestCase):
    """Tests cases for amenity class"""
    
    def test_amenity(self):
        """Test the initialization of default amenity attribute"""
        amenity = Amenity()
        self.assertEqual(amenity.name, "")
       
        """Test the initialization with specific values"""
        amenity = Amenity(name="ranim")
        self.assertEqual(amenity.name, "ranim")

     def test_str(self):
         """Test if is a string"""
        self.assertEqual(str, type(Amenity().id))
       
if __name__ == "__main__":
    unittest.main()
