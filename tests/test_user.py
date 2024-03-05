#!/usr/bin/python3
import unittest
from models.user import User

class TestModels(unittest.TestCase):
    """Tests cases for user class"""
    
    def test_user(self):
        """Test the initialization of default user attribute"""
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")
        self.assertEqual(str(user), "User<>, , >")
       
        """Test the initialization with specific values"""
        user = User(email="ranim@mail.com", password= "ranimeana", first_name= "jana", last_name="adroune")
        self.assertEqual(user.email, "ranim@mail.com")
        self.assertEqual(user.password, "ranimeana")
        self.assertEqual(user.first_name, "jana")
        self.assertEqual(user.last_name, "adroune")
       
if __name__ == "__main__":
    unittest.main()
