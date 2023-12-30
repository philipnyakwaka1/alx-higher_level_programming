#!/usr/bin/python3
"""
script that prints the first State object from the
database hbtn_0e_6_usa
"""

from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from urllib.parse import quote
import sys

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(quote(sys.argv[1]), quote(sys.argv[2]),
                                   quote(sys.argv[3])), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    query_object = session.query(State).first()
    if query_object is not None:
        print(f'{query_object.id}: {query_object.name}')
    else:
        print("Nothing")
    session.close()
