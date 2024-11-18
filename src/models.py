import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Address(Base):
    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    def to_dict(self):
        return {}


class Character(Base):
    __tablename__ = 'character'

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    age = Column(Integer)
    faction = Column(String(200))


class Planet(Base):
    __tablename__ = 'planet'

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    population = Column(Integer)
    climate = Column(String(100))


class Starship(Base):
    __tablename__ = 'starship'

    id = Column(Integer, primary_key=True)
    model = Column(String(200))
    starship_class = Column(String(200))
    crew = Column(Integer)


class Vehicle(Base):
    __tablename__ = 'vehicle'

    id = Column(Integer, primary_key=True)
    model = Column(String(200))
    starship_class = Column(String(200))
    crew = Column(Integer)


class Favorite(Base):
    __tablename__ = 'favorite'

    id = Column(Integer, primary_key=True)
    
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    character_id = Column(Integer, ForeignKey('character.id'))
    character = relationship(Character)

    planet_id = Column(Integer, ForeignKey('planet.id'))
    planet = relationship(Planet)

    starship_id = Column(Integer, ForeignKey('starship.id'))
    starship = relationship(Starship)

    vehicle_id = Column(Integer, ForeignKey('vehicle_id'))
    vehicle = relationship(Vehicle)



## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
