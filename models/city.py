#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Table, Column, Integer, Numeric, String
from sqlalchemy.ext.declarative import declarative_base


class City(BaseModel, Base):
    """The city class, contains state ID and name"""

    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), Foreign_key("states.id"), nullable=False)
