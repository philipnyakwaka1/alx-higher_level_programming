#!/usr/bin/python3
"""
This module contains the class definition State and Base class
"""
from sqlalchemy import create_engine, Integer, String, Column
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class State(Base):
    """This class links to MySQL table states"""

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
