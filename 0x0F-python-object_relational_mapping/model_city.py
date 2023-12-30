#!/usr/bin/python3
"""
This module contains the class definition of a City
"""
from model_state import Base
from sqlalchemy import Integer, Column, String, Sequence, Foreignkey


class City(Base):
    """Contains class defination of city"""
    __tablename__ = 'cities'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, Foreignkey('states.id'), nullable=False)

    def __init__(self, name, state_id):
        """Initializes an instance of class cities"""
        self.name = name
        self.state_id = state_id
