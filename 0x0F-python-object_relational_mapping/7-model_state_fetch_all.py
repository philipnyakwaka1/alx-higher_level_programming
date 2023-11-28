#!/usr/bin/python3
"""
This module  lists all State objects from the database hbtn_0e_6_usa
"""
from model_state import Base, State
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
import sys

engine = create_engine(f'mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@localhost/{sys.argv[3]}')
Session = sessionmaker(engine)
session = Session()

for state in session.query(State).from_statement(text("SELECT states.id, states.name\
    FROM states ORDER BY states.id ASC").columns(State.id, State.name)):
    print (f'{state.id}: {state.name}')
