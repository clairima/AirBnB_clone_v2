#!/usr/bin/python3
""" Place Module for HBNB project """
from sqlalchemy import Column, String, ForeignKey, Integer, Float
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from models.amenity import Amenity
from sqlalchemy import Table
from os import getenv
from models.review import Review


place_amenity = Table("place_amenity", Base.metadata,
                      Column("place_id", String(60),
                             ForeignKey("places.id"),
                             primary_key=True, nullable=False),
                      Column("amenity_id", String(60),
                             ForeignKey("amenities.id"),
                             primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, default=0)
    number_bathrooms = Column(Integer, default=0)
    max_guest = Column(Integer, default=0)
    price_by_night = Column(Integer, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    reviews = relationship("Review", cascade="all, delete", backref="place")
    amenity_ids = []
    amenities = relationship(
        'Amenity',
        secondary=place_amenity,
        back_populates='place_amenities',
        viewonly=False
    )

    if getenv("HBNB_TYPE_STORAGE", None) != "db":
        @property
        def reviews(self):
            """Get linked review list"""
            from models import storage
            reviews = []
            for review in list(storage.all(Review).values()):
                if review.place_id == self.id:
                    reviews.append(review)
            return reviews
