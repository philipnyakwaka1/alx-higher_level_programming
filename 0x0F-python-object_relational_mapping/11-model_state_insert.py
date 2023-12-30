#!/usr/bin/python3
"""
script that lists all State objects that contain
the letter a from the database hbtn_0e_6_usa
"""

from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from urllib.parse import quote
import sys

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(quote(sys.argv[1]), quote(sys.argv[2]),
                                   quote(sys.argv[3])), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    existing_state = session.query(State).filter_by(
        name=quote('Louisiana')).all()
    if len(existing_state) == 0:
        new_state = State(name='Louisiana')
        session.add(new_state)
        session.commit()
    session.close()
