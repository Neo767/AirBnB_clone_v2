#!/usr/bin/python3
<<<<<<< HEAD
'''
   Implementation of the User class which inherits from BaseModel
'''
import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
=======
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from models.place import Place
from models.review import Review
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv
>>>>>>> faa230737c93eaa318f40c81f1e809fb8a9751aa

storage_type = getenv("HBNB_TYPE_STORAGE")

<<<<<<< HEAD
class User(BaseModel, Base):
    '''
    Definition of the User class
    '''
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = "users"
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128))
        last_name = Column(String(128))
        places = relationship("Place", backref="user",
                cascade="delete")        
        reviews = relationship("Review", cascade="delete", backref="user")
=======

class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = 'users'
    if storage_type == 'db':
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship("Place", backref="user",
                              cascade="all, delete-orphan")
        reviews = relationship("Review", backref="user",
                               cascade="all, delete-orphan")
>>>>>>> faa230737c93eaa318f40c81f1e809fb8a9751aa
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""
