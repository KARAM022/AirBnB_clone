#!/usr/bin/python3
"""This module creates a Amenity class"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Class to manage amenity objects"""

    def __init__(self, name: str = ""):
        super().__init__()
        self.name = name
