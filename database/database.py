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

class User(Base):
    __tablename__ = 'user'
    userId = Column(Integer, primary_key=True)
    username = Column(String(20), nullable=False)
    password = Column(String(40), nullable=False)
    role =  Column(String(30), nullable=False)

class Project(Base):
    __tablename__ = 'project'
    projectid = Column('projectid', Integer, primary_key = True)
    name = Column(String(100),unique=True)
    locality = Column(String(50))
    address = Column(String(200))
    date= Column(DateTime)
    phone_no = Column(String(50))
    no_student = Column(Integer)
    status = Column(String(100))

class Version(Base):
    __tablename__ = 'version'
    version = Column(Integer, primary_key= True)
    projectid = Column(Integer, ForeignKey('project.projectid'))
    date = Column(DateTime)

class Template(Base):
    __tablename__ = 'template'
    qid = Column(Integer, primary_key=True)
    question = Column(String(250))
    qtype = Column(String(250))

class Assessment(Base):
    __tablename__ = 'assessment'
    aid = Column(Integer, primary_key=True)
    projectid = Column(Integer, ForeignKey('project.projectid'))
    qid = Column(Integer, ForeignKey('template.qid'))
    questions = Column(String(250))

class Activity(Base):
    __tablename__ = 'activity'
    aid = Column(Integer, primary_key=True)
    projectid = Column(Integer, ForeignKey('project.projectid'))
    name = Column(String(50), nullable=False)
    description = Column(String(250), nullable=False)
    startDate = Column(DateTime)
    duration = Column(Integer, primary_key=True)
    progress= Column(String, nullable=False)
    version = Column(Integer, ForeignKey('version.version'))

# Create an engine that stores data in the local directory's
# sqlalchemy_example.db file.
engine = create_engine('sqlite:///database.db')



# Create all tables in the engine. This is equivalent to "Create Table"
# statements in raw SQL.
Base.metadata.create_all(engine)



# Insert sample data
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

new_user = User()
new_user.username = 'admin'
new_user.password = 'pw'
new_user.role = 'admin'

session.add(new_user)
session.commit()


new_user = User()
new_user.username = 'fw'
new_user.password = 'pw'
new_user.role = 'field_worker'

session.add(new_user)
session.commit()

template = Template()
template.question = "Number of students"
template.qtype = "string"

session.add(template)
session.commit()


# Read from tables
# print(session.query(user).first().username)

app = Flask('__main__')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = ""

if __name__ == '__main__':
    app.run(debug=True)