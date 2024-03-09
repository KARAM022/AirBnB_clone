#!/usr/bin/python3
import unittest
from models.place import Place


class TestModels(unittest.TestCase):
    """Tests cases for place class"""
    def test_place(self):
        """Test the initialization of default place attribute"""
        place = Place()
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])

        """Test the initialization with specific values"""
        place = Place(city_id="3",
                      user_id="234",
                      name="warm sweet",
                      description="warm sweet for lovers",
                      number_rooms=10,
                      number_bathrooms=1,
                      max_guest=2,
                      price_by_night=1000,
                      latitude=50.7749,
                      longitude=120.94,
                      amenity_ids=["1", "2", "3"])
        self.assertEqual(place.city_id, "3")
        self.assertEqual(place.user_id, "234")
        self.assertEqual(place.name, "warm sweet")
        self.assertEqual(place.description, "warm sweet for lovers")
        self.assertEqual(place.number_rooms, 10)
        self.assertEqual(place.number_bathrooms, 1)
        self.assertEqual(place.max_guest, 2)
        self.assertEqual(place.price_by_night, 1000)
        self.assertEqual(place.latitude, 50.7749)
        self.assertEqual(place.longitude, 120.94)

        self.assertEqual(place.amenity_ids, ["1", "2", "3"])

    def test_is_a_string(self):
        """Test if id is a string"""
        self.assertEqual(str, type(Place().id))


if __name__ == "__main__":
    unittest.main()
