#!/usr/bin/python3
import unittest
from models.review import Review

class TestModels(unittest.TestCase):
    """Tests cases for review class"""
    
    def test_review(self):
        """Test the initialization of default review attribute"""
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")
       
        """Test the initialization with specific values"""
        review = Review(place_id="123", user_id= "234", text= "I love this place")
        self.assertEqual(review.place_id, "123")
        self.assertEqual(review.user_id, "234")
        self.assertEqual(review.text, "I love this place")
    
    def test_is_a_string(self):
        """Test if id is a string"""
        self.assertEqual(str, type(Review().id))
       
if __name__ == "__main__":
    unittest.main()
