import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from flask import *
from flask_sqlalchemy import *

Base = declarative_base()

class user(Base):
    __tablename__ = 'user'
    userId = Column(Integer, primary_key=True)
    username = Column(String(20), nullable=False)
    password = Column(String(40), nullable=False)
    role =  Column(String(30), nullable=False)

class project(Base):
    __tablename__ = 'project'
    projectId = Column('projectId', Integer, primary_key = True)
    name = Column(String(100),unique=True)
    locality = Column(String(50))
    address = Column(String(200))
    date= Column(DateTime)
    phone_no = Column(String(50))
    no_student = Column(Integer)
    status = Column(String(100))

class version(Base):
    __tablename__ = 'version'
    version = Column(Integer, primary_key= True)
    pid = Column(Integer, ForeignKey('project.projectId'))
    date = Column(DateTime)

class template(Base):
    __tablename__ = 'template'
    qid = Column(Integer, primary_key=True)
    questions = Column(String(250))
    qtype = Column(String(250))


# Create an engine that stores data in the local directory's
# sqlalchemy_example.db file.
engine = create_engine('sqlite:///database.db')



# Create all tables in the engine. This is equivalent to "Create Table"
# statements in raw SQL.
Base.metadata.create_all(engine)

# RUn queries now

# Base.metadata.bind = engine
# DBSession = sessionmaker(bind=engine)
# session = DBSession()

# new_user = user()
# new_user.username = 'admin'
# new_user.password = 'pw'
# new_user.role = 'admin'
# session.add(new_user)
# session.commit()

# print(session.query(user).first().username)

app = Flask('__main__')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = ""

if __name__ == '__main__':
    app.run(debug=True)