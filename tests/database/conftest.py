from sqlalchemy import create_engine
from sqlalchemy.orm import Session
import pytest

from house_plant.database.database import Base

@pytest.fixture(scope="session")
def temp_engine():
    """Create temp sqlite database for testing."""
    engine = create_engine("sqlite:///:memory:", echo=True)
    Base.metadata.create_all(engine)
    yield engine
    with Session(engine) as session:
        session.close()
