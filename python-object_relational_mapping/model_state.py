#!/usr/bin/python3
"""
Defines State class
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class State(Base):
    """
    Defines State class
    """

    id = Column(
        Integer,
        primary_key=True,
        nullable=False,
        autoincrement=True
    )

    name = Column(String(128), nullable=False)
