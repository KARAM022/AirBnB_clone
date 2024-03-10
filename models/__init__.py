#!/usr/bin/python3
"""link BaseModel to FileStorage by using the variable storage"""
from models.engine.file_storage import FileStorage
from  models.user import User

storage = FileStorage()
storage.reload()
