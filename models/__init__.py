#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from models.engine.file_storage import FileStorage
from os import environ


if environ["HBNB_TYPE_STORAGE"] == "db":
    from models.engine.db_storage import DBStorage

    storage = DBStorage()
    storage.reload()

else:  # file storage selected
    from models.engine.file_storage import FileStorage

    storage = FileStorage()
    storage.reload()
