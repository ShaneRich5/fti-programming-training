import getpass
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship, backref, sessionmaker
import models

# Ask user for connection details
server = 'tmp-training.c21v9ghziray.us-west-1.rds.amazonaws.com'
database = 'training'
username = 'ftimaster'
password = getpass.getpass()

# Format connection string
connection_string_template = "mssql+pyodbc://{}:{}@{}:1433/{}?driver=SQL+Server+Native+Client+11.0"
connection_string = connection_string_template.format(username, password, server, database)

# create database engine from connection string
engine = create_engine(connection_string)

# configure session
Session = sessionmaker()
Session.configure(bind=engine)

# create session for interacting with database
session = Session()

# define the users to insert
users = [
    {"first_name": 'George', "last_name": 'Washington', "username": 'gwash'},
    {"first_name": 'Thomas', "last_name": 'Jefferson', "username": 'tjeff'}
]

# iterate new users
for user in users:
    # create user object from model
    user = models.User(first_name=user["first_name"], last_name=user["last_name"], username=user["username"])
    # create database record from object
    session.add(user)

# save changes to database
session.commit()

print('done inserting')