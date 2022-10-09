#!/usr/bin/python3
"""
Defines a City model.
Inherits from SQLAlchemy Base and links to the MySQL table states.
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, ForeignKey

Base = declarative_base()


class City(Base):
    """Represents a city for a MySQL database.

    __tablename__ (str): The name of the MySQL table to store States.
    id (sqlalchemy.Integer): The city's id.
    name (sqlalchemy.String): The city's name.
    state_id(sqlalchemy.Integer): The state id of the city
    """

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
