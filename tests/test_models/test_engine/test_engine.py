#!/usr/bin/python3
import os
import models
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review

class TestModels(unittest.TestCase):
    """Tests cases for File storage file"""
    
    def test_storage_initializes(self):
        """Testing initialisation"""
        self.assertEqual(type(models.storage), FileStorage)
     
    def test_FileStorage_instan_with_no_args(self):
        """Testing instantiation without arguments"""
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_FileStorage_instan_with_arg(self):
        """Testing instantiation with arguments"""
        with self.assertRaises(TypeError):
            FileStorage(None)
    
class TestFileStorage_method(unittest.TestCase):
    """Unittests for testing methods of the FileStorage class."""
    
    def test_all(self):
        self.assertEqual(dict, type(models.storage.all()))
    
    def test_all_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.all(None)
            
    def test_new(self):
        model = BaseModel()
        user = User()
        state = State()
        place = Place()
        city = City()
        amenity = Amenity()
        review = Review()
        models.storage.new(model)
        models.storage.new(user)
        models.storage.new(state)
        models.storage.new(place)
        models.storage.new(city)
        models.storage.new(amenity)
        models.storage.new(review)
        self.assertIn("BaseModel." + model.id, models.storage.all().keys())
        self.assertIn(model, models.storage.all().values())
        self.assertIn("User." + user.id, models.storage.all().keys())
        self.assertIn(user, models.storage.all().values())
        self.assertIn("State." + state.id, models.storage.all().keys())
        self.assertIn(state, models.storage.all().values())
        self.assertIn("Place." + place.id, models.storage.all().keys())
        self.assertIn(place, models.storage.all().values())
        self.assertIn("City." + city.id, models.storage.all().keys())
        self.assertIn(city, models.storage.all().values())
        self.assertIn("Amenity." + amenity.id, models.storage.all().keys())
        self.assertIn(amenity, models.storage.all().values())
        self.assertIn("Review." + review.id, models.storage.all().keys())
        self.assertIn(review, models.storage.all().values())
        
    def test_save(self):
        model = BaseModel()
        user = User()
        state = State()
        place = Place()
        city = City()
        amenity = Amenity()
        review = Review()
        models.storage.new(model)
        models.storage.new(user)
        models.storage.new(state)
        models.storage.new(place)
        models.storage.new(city)
        models.storage.new(amenity)
        models.storage.new(review)
        models.storage.save()
        save_text = ""
        with open("file.json", "r") as f:
            save_text = f.read()
            self.assertIn("BaseModel." + model.id, save_text)
            self.assertIn("User." + user.id, save_text)
            self.assertIn("State." + state.id, save_text)
            self.assertIn("Place." + place.id, save_text)
            self.assertIn("City." + city.id, save_text)
            self.assertIn("Amenity." + amenity.id, save_text)
            self.assertIn("Review." + review.id, save_text)
    
    def test_reload(self):
        model = BaseModel()
        user = User()
        state = State()
        place = Place()
        city = City()
        amenity = Amenity()
        review = Review()
        models.storage.new(model)
        models.storage.new(user)
        models.storage.new(state)
        models.storage.new(place)
        models.storage.new(city)
        models.storage.new(amenity)
        models.storage.new(review)
        models.storage.save()
        models.storage.reload()
        obj = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + model.id, obj)
        self.assertIn("User." + user.id, obj)
        self.assertIn("State." + state.id, obj)
        self.assertIn("Place." + place.id, obj)
        self.assertIn("City." + city.id, obj)
        self.assertIn("Amenity." + amenity.id, obj)
        self.assertIn("Review." + review.id, obj)
    
    @classmethod
    def setUpClass(cls):
        """Set up the test class."""
        try:
            os.rename("file.json", "tempo")
        except IOError:
            pass

    @classmethod
    def tearDownClass(cls):
        """Tear down the test class."""
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tempo", "file.json")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}
    
    
if __name__ == "__main__":
    unittest.main()
