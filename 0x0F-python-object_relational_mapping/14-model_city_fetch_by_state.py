#!/usr/bin/python3
"""
prints all City objects from the database hbtn_0e_14_usa
"""

from model_state import Base, State
from model_city import City
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
    for state_name, city_name, city_id in \
        session.query(State.name, City.name, City.id)\
            .filter(State.id == City.state_id).order_by(City.id.asc()):
        print(f'{state_name}: ({city_id}) {city_name}')
    session.close()
