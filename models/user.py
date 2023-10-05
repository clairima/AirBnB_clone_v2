#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
<<<<<<< HEAD
    places = relationship(
                        "Place",
                        backref="user",
                        cascade="all, delete-orphan"
    )
    reviews = relationship(
                        "Review",
                        backref="user",
                        cascade="all, delete-orphan"
    )
=======
    places = relationship("Place", cascade="all, delete", backref="user")
    reviews = relationship("Review", cascade="all, delete", backref="user")
>>>>>>> 0fe80b577b6fafde27865818d45f58fe74c945c6
