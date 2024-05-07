"""Functionality related to creating and modifying the database itself."""
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from enum import Enum
import os
from sqlalchemy.orm import Session


# import logging

DEFAULT_DB_STR = "plants.db"

class Base(DeclarativeBase):
    pass

def get_database_engine(db_name: str=DEFAULT_DB_STR) -> sqlalchemy.Engine:
    """Return database engine, creating db if none exists."""
    if os.path.exists(db_name):
        return create_engine("sqlite:///"+db_name, echo=True)
    # TODO: add logging here
    return create_database()

def create_database(db_name: str=DEFAULT_DB_STR) -> None:
    """Create sqlite database."""
    engine = create_engine("sqlite:///"+db_name, echo=True)
    Base.metadata.create_all(engine)
    return engine

def add_rows(ORMs, engine):
    with Session(engine) as session:
        session.add_all(ORMs)
        session.commit()
