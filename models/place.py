#!/usr/bin/python3
"""This module creates a Place class"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Class to manage place objects"""
    def __init__(self, city_id: str = "", user_id: str = "",
                 name: str = "", description: str = "",
                 number_rooms: int = 0, number_bathrooms: int = 0,
                 max_guest: int = 0, price_by_night: int = 0,
                 latitude: float = 0.0, longitude: float = 0.0,
                 amenity_ids: list = []):

        super().__init__()
        self.city_id = city_id
        self.user_id = user_id
        self.name = name
        self.description = description
        self.number_rooms = number_rooms
        self.number_bathrooms = number_bathrooms
        self.max_guest = max_guest
        self.price_by_night = price_by_night
        self.latitude = latitude
        self.longitude = longitude
        self.amenity_ids = amenity_ids
