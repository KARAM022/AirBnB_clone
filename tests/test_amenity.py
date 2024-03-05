#!/usr/bin/python3
import unittest
from models.amenity import Amenity

class TestModels(unittest.TestCase):
    """Tests cases for amenity class"""
    
    def test_amenity(self):
        """Test the initialization of default amenity attribute"""
        amenity = Amenity()
        self.assertEqual(amenity.name, "")
        self.assertEqual(str(amenity), "Amenity<>")
       
        """Test the initialization with specific values"""
        amenity = Amenity(name="ranim")
        self.assertEqual(amenity.name, "ranim")
       
if __name__ == "__main__":
    unittest.main()
