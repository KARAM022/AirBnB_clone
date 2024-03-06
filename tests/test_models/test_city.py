#!/usr/bin/python3
import unittest
from models.city import City

class TestModels(unittest.TestCase):
    """Tests cases for city class"""
    
    def test_city(self):
        """Test the initialization of default city attribute"""
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")
       
        """Test the initialization with specific values"""
        city = City(state_id="3", name= "Casa")
        self.assertEqual(city.state_id, "3")
        self.assertEqual(city.name, "Casa")
       

    def test_is_a_string(self):
        """Test if id is a string"""
        self.assertEqual(str, type(City().id))
       
if __name__ == "__main__":
    unittest.main()
