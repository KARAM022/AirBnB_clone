#!/usr/bin/python3
"""This module creates a User class"""
from models.base_model import BaseModel


class State(BaseModel):
    """Class to manage state objects"""
    
    def __init__(self, name: str = ""):
        super().__init__()
        self.name = name
