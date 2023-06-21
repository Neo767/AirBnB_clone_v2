#!/usr/bin/python3
<<<<<<< HEAD
'''
    Implementation of the State class    
'''
=======
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
from os import getenv
import models
>>>>>>> faa230737c93eaa318f40c81f1e809fb8a9751aa

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
import os
import models
from models.city import City

<<<<<<< HEAD

class State(BaseModel, Base):
    '''
    Implementation for the State.
    '''
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state",
                              cascade="delete")
    else:
        name = ""

        @property
        def cities(self):
            city_dict = models.storage.all(City)
            state_query = self.id
            city_list = []
            for k, v in city_dict.items():
                if v.state_id == self.id:
                    city_list.append(v)
            return city_list
=======
storage_type = getenv("HBNB_TYPE_STORAGE")


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    if storage_type == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state",
                              cascade="all, delete-orphan")
    else:
        name = ""

    if storage_type != 'db':
        @property
        def cities(self):
            """
            get list of City instances with state_id
            equals to the current State.id
            """
            list_cities = []
            all_cities = models.storage.all(City)
            for key, city_obj in all_cities.items():
                if city_obj.state_id == self.id:
                    list_cities.append(city_obj)
            return list_cities
>>>>>>> faa230737c93eaa318f40c81f1e809fb8a9751aa
