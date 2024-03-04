#!/usr/bin/python3
"""This module creates a User class"""
from models.base_model import BaseModel


class City(BaseModel):
    """Class to manage city objects"""

    def __init__(self, state_id: str = "", name: str = ""):
        super().__init__()
        self.state_id = state_id
        self.name = name
