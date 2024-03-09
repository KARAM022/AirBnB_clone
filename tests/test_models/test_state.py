#!/usr/bin/python3
import unittest
from models.state import State


class TestModels(unittest.TestCase):
    """Tests cases for state class"""
    def test_state(self):
        """Test the initialization of default state attribute"""
        state = State()
        self.assertEqual(state.name, "")

        """Test the initialization with specific values"""
        state = State(name="Mohammedia")
        self.assertEqual(state.name, "Mohammedia")

    def test_is_a_string(self):
        """Test if id is a string"""
        self.assertEqual(str, type(State().id))


if __name__ == "__main__":
    unittest.main()
