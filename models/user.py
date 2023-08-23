#!/usr/bin/python3
"""Defines  User class."""
from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """Representing a user for a MySQL database.
    Inherits from SQLAlchemy Base and links to the MySQL table users.
    Attributes:
        __tablename__ (str): name of the MySQL table to store users.
        email: (sqlalchemy String): user's email address.
        password (sqlalchemy String): user's password.
        first_name (sqlalchemy String):user's first name.
        last_name (sqlalchemy String): user's last name.
        places (sqlalchemy relationship): User-Place relationship.
        reviews (sqlalchemy relationship): User-Review relationship.
    """
    __tablename__ = "users"
    email = Column(String(125), nullable=False)
    password = Column(String(125), nullable=False)
    first_name = Column(String(125))
    last_name = Column(String(125))
    places = relationship("Place", backref="user", cascade="delete")
    reviews = relationship("Review", backref="user", cascade="delete")

