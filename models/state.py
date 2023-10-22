#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
import shlex
import models
from models.city import City

class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship(
        "City",
        back_populates="state",
        cascade="all, delete-orphan"
    )

    @property
    def cities(self):
        ver = models.storage.all()
        list1 = []
        result = []
        for key in ver:
            city = key.replace('.', ' ')
            city = shlex.split(city)
            if (city[0] == 'City'):
                list1.append(ver[key])
        for element in list1:
            if (element.state_id == self.id):
                result.append(element)
        return (result)
