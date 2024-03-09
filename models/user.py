#!/usr/bin/python3
"""This module used for creating a User class"""
from models.base_model import BaseModel


class User(BaseModel):
    """Class to manage user objects"""
    def __init__(self, email: str = "", password: str = "",
                 first_name: str = "", last_name: str = ""):
        super().__init__()
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
