#!/usr/bin/python3

import MySQLdb
from sqlalchemy import create_engine, Integer, Column, String
from sqlalchemy.orm import declarative_base, sessionmaker
from urllib.parse import quote

passwd = quote("Ominaphi@123")
engine = create_engine(
    f'mysql+mysqldb://nygma:{passwd}@localhost:3306/alchemist', echo=True)
Base = declarative_base()

# creating tables


class City(Base):
    __tablename__ = 'city'
    id = Column(Integer, primary_key=True, autoincrement=True)
    state_id = Column(Integer)
    name = Column(String(50))

    def __repr__(self):
        return f'{self.__class__.__name__}(id={self.id}, state_id={self.state_id}, name={self.name})'


Base.metadata.create_all(engine)

# creating a session for editing table

Session = sessionmaker(bind=engine)
session = Session()
Dallas = City(state_id=1, name='Dallas')
session.add(Dallas)
session.commit()
results = session.query(City).filter_by(name='Dallas').first()
print(results.name)
