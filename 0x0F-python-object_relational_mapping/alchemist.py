#!/usr/bin/python3
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer, Sequence
from sqlalchemy.orm import declarative_base, sessionmaker
from urllib.parse import quote
import sys
engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                       .format(quote(sys.argv[1]), quote(sys.argv[2]),
                               quote(sys.argv[3])), pool_pre_ping=True)
Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    firstname = Column(String(50))
    lastname = Column(String(50))
    age = Column(String(50))

    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def __repr__(self):
        return f'User({self.firstname}, {self.lastname}, {self.id}yrs)'


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
names = [{'firstname': 'Philip', 'lastname': 'Nyakwaka', 'age': 25},
         {'firstname': 'Fredrick', 'lastname': 'Oduor', 'age': 26},
         {'firstname': 'Josephine', 'lastname': 'Adongo', 'age': 28},
         {'firstname': 'Sally', 'lastname': 'Apiyo', 'age': 28}]
for user in names:
    existing_user = session.query(User).filter_by(firstname=user['firstname'],
                                                  lastname=user['lastname'], age=user['age']).first()
    if existing_user is None:
        new_user = User(user['firstname'], user['lastname'], user['age'])
        session.add(new_user)
        session.commit()

# qry = session.query(User).order_by(User.id)
# results = qry.all()
# print(results)
for user in session.query(User).order_by(User.id):
    print(f'{user.firstname}, {user.lastname}, {user.age}yrs')
# existing_user = session.query(User).filter_by(firstname='Philip',
    # lastname='Nyakwaka', age=25).first()
# session.delete(existing_user)
# session.commit()

session.close()
