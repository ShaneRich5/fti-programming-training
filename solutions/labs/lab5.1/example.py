import getpass
from sqlalchemy import Column, String, Integer, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Ask user for connection details (same as last lab)

# Format connection string (similar to last lab, but with slight differences)
connection_string_template = "mssql+pyodbc://{}:{}@{}:1433/{}?driver=SQL+Server+Native+Client+11.0"
connection_string = connection_string_template.format(username, password, server, database)

# create database engine from connection string
engine = create_engine(connection_string)
Base = declarative_base()

# configure session
Session = sessionmaker()
Session.configure(bind=engine)

# create session for interacting with database
session = Session()


# define database models
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


# Insert data into the databsae
#
# 1) create a list of dictionaries for each of the three database tables defined in the database models above.
#
# 2) iterate each list and insert the records
# example:
# your_variable = ModelName(field_1_name=field_1_value, field_2_name=field_2_value)
# session.add(your_variable)
# session.commit()