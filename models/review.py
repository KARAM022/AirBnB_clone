#!/usr/bin/python3
"""This module creates a Review class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Class to manage review objects"""
    def __init__(self, place_id: str = "", user_id: str = "",text: str = ""):
        super().__init__()
        self.place_id = place_id
        self.user_id = user_id
        self.text = text
