#!/usr/bin/python3
import unittest
from models.state import State

class TestModels(unittest.TestCase):
    """Tests cases for state class"""
    
    def test_state(self):
        """Test the initialization of default state attribute"""
        state = State()
        self.assertEqual(state.name, "")
        self.assertEqual(str(state), "State<>")
       
        """Test the initialization with specific values"""
        state = State(name="Mohammedia")
        self.assertEqual(state.name, "Mohammedia")
       
if __name__ == "__main__":
    unittest.main()
