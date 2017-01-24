from sqlalchemy import create_engine
#from .database import session
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from logic_circuit import app

engine = create_engine(app.config["DATABASE_URI"])
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

import datetime

from sqlalchemy import Column, Integer, String, Text, DateTime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from flask.ext.login import UserMixin

class User(Base, UserMixin):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(128))
    email = Column(String(128), unique=True)
    password = Column(String(128))
    entries = relationship("Entry", backref="author")

class Logic_Circuit(Base):
    __tablename__ = "entries"

    id = Column(Integer, primary_key=True)
    Equation = Column(String(1024))
    Output = Column(Text)
    datetime = Column(DateTime, default=datetime.datetime.now)
    author_id = Column(Integer, ForeignKey('users.id'))