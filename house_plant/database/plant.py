"""Functionality to create plant table."""
from house_plant.database.database import Base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from typing import Optional

from enum import Enum

class PetFriendly(Enum):
    """Enumeration of pet friendliness labels."""
    UNKNOWN = 1
    PET_SAFE = 2
    TOXIC = 3
    TUMMY_UPSET = 4
    OTHER = 5

class SoilTypes(Enum):
    """
    Enumeration of soil types.
        SANDY: Gritty or well-draining soil perfect for succulents.
        LOAMY: Holds plenty of moisture but also drains well so that sufficient air can reach the roots.
        CLAY: Common soil that absorbs water slowy and takes time to dry out. Likely compact and heavy.
    """
    UNKNOWN = 1
    SANDY = 2
    LOAMY = 3
    CLAY = 4
    OTHER = 5

class PlantORM(Base):
    """Column definitions for plant table."""
    __tablename__ = "plant_table"

    id: Mapped[int] = mapped_column(primary_key=True) #TODO: make automatic
    name: Mapped[str] = mapped_column()

    # TODO: add in once location table has been added
    # location_name: Mapped[str] = mapped_column(ForeignKey("location_table.name"))
    sublocation_name: Mapped[Optional[str]]

    scientific_type: Mapped[Optional[str]]
    common_type: Mapped[Optional[str]]

    # Not typed as optional because it will default to unknown
    # But not a required user input
    pet_friendly: Mapped[PetFriendly]
    soil: Mapped[SoilTypes]

    # int is number of days
    fertilizing_cadence:  Mapped[Optional[int]]
    repotting_cadence: Mapped[Optional[int]]

    light_info: Mapped[Optional[str]]
    dryness_info: Mapped[Optional[str]]
    fertilizing_info: Mapped[Optional[str]]
