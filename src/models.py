import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User (Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    # date_subs = Column(DateTime, nullable=False)


class Personajes (Base): 
    __tablename__ = "personajes"
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    birthday_year = Column(Integer, nullable=False)
    Gender = Column(String(6), nullable=False)
    Height = Column(Integer, nullable=False)
    Skin_color = Column(String(200), nullable=False)
    Eye_color = Column(String(200), nullable=False)


class Planetas (Base):
    __tablename__ = "planetas"
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    diameter = Column(Integer, nullable=False)
    rotation_period = Column(Integer, nullable=False)
    orbital_period = Column(Integer, nullable=False)


class Vehiculos (Base):
    __tablename__ = "vehiculos"
    id = Column(Integer, primary_key=True)
    model = Column(String(250), nullable=False)
    vehicle_class = Column(String(250), nullable=False)
    manufacturer = Column(String(250), nullable=False)
    length = Column(Integer, nullable=False)


class Personajes_Fav (Base):
    __tablename__ = "personajes_fav"
    id = Column(Integer, primary_key=True)
    user_id  = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    character_id = Column(Integer, ForeignKey('personajes.id'))
    character = relationship(Personajes)

class Planetas_Fav (Base):
    __tablename__ = "planetas_fav"
    id = Column(Integer, primary_key=True)
    user_id  = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    planet_id = Column(Integer, ForeignKey('planetas.id'))
    planet = relationship(Planetas)

class Vehiculos_Fav (Base):
    __tablename__ = "vehiculos_fav"
    id = Column(Integer, primary_key=True)
    user_id  = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    vehicle_id = Column(Integer, ForeignKey('vehiculos.id'))
    vehicle = relationship(Vehiculos)

    def to_dict(self):
        return {}
## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
