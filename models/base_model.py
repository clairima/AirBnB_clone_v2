#!/usr/bin/python3
"""
This module defines a base class for all models in our hbnb clone
"""
from sqlalchemy import Column, String, DateTime
import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""
    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime,
                        default=datetime.utcnow,
                        nullable=False)
    updated_at = Column(DateTime,
                        default=datetime.utcnow,
                        nullable=False)

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        dictionary = self.__dict__.copy()
        dictionary.pop('_sa_instance_state', None)
        return '[{}] ({}) {}'.format(cls, self.id, dictionary)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.utcnow()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = self.__dict__.copy()
        dictionary.pop('_sa_instance_state', None)
        dictionary['__class__'] = self.__class__.__name__
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary

    def delete(self):
        """Deletes the current instance from the storage (models.storage)"""
        from models import storage
        storage.delete(self)
