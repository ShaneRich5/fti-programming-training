from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, ForeignKey, create_engine
Base = declarative_base()


class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    abbreviation = Column(String)
    state_name = Column(String)


class Address(Base):
    __tablename__ = 'addresses'
    id = Column(Integer, primary_key=True)
    street_address = Column(String)
    street_address_2 = Column(String)
    city = Column(String)
    state_id = Column(Integer, ForeignKey(State.id))


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    primary_address_id = Column(Integer, ForeignKey(Address.id))