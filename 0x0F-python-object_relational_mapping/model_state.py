#!/usr/bin/python3

"""
This module contains the class definition
of a State and an instance Base = declarative_base()
"""
import MySQLdb
from sqlalchemy import create_engine, Integer, String, Column
from sqlalchemy.orm import declarative_base
import sys

engine = create_engine(f'mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@localhost/{sys.argv[3]}', pool_pre_ping=True)
Base = declarative_base()

class State(Base):
    """This class links to MySQL table states"""

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)

