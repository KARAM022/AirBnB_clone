#!/usr/bin/python3
import unittest
from datetime import datetime
from models.base_model import BaseModel
import uuid 

class TestModels(unittest.TestCase):
    """Tests cases for the BaseModel class"""
    
    def test_init_with_k(self):
        """Testing initialisation with keywards arguments"""
        dt = datetime.today()
        dt_iso = dt.isoformat()
        kwargs = {"id": "test_id", "created_at": dt_iso, "updated_at": dt_iso,
            "name": "Test", "__class__": "BaseModel"}
        model = BaseModel(**kwargs)
        self.assertEqual(model.id, "test_id")
        self.assertEqual(model.name, "Test")
        self.assertEqual(model.created_at, dt)
        self.assertEqual(model.updated_at, dt)
    
    def test_no_args_instan(self):
        self.assertEqual(BaseModel, type(BaseModel()))
       
    def test_init_without_k(self):
        """Testing initialisation without keywards arguments"""
        model = BaseModel()
        self.assertIsInstance(model.id, str)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)
    
        """Checking if id is a valid UUID"""
        try:
            uuid.UUID(model.id)
        except ValueError:
            self.fail("id is not a valid UUID")
            
    def test_string_repr(self):
        """Testing the string methode"""
        dt = datetime.today()
        dt_repr = repr(dt)
        model = BaseModel()
        model.id = "test_id"
        model.created_at = model.updated_at = dt
        modelstr = model.__str__()
        self.assertIn("[BaseModel] (test_id)", modelstr)
        self.assertIn("'id': 'test_id'", modelstr)
        self.assertIn("'created_at': " + dt_repr, modelstr)
        self.assertIn("'updated_at': " + dt_repr, modelstr)

    def test_to_dic(self):
        """Testing the to dic methode"""
        model = BaseModel()
        model.id = "test_id"
        model.created_at = datetime(2022, 1, 1, 0, 0, 0)
        model.updated_at = datetime(2022, 1, 1, 0, 0, 0)
        model_dict = model.to_dict()
        expected_dict = {'id': 'test_id', 'created_at': '2022-01-01T00:00:00', 
        'updated_at': '2022-01-01T00:00:00', '__class__': 'BaseModel'}
        self.assertEqual(model_dict, expected_dict)
    
    def save_update(self):
        """Testing if save methode update the update_at attribute"""
        model = BaseModel()
        model = BaseModel()
        old_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(old_updated_at, model.updated_at)

if __name__ == "__main__":
    unittest.main()
