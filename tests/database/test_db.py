"""Test database creation and deletion."""

from house_plant.database.database import get_database_engine

def test_create_db():
    """Test create_database and get_database_engine."""
    get_database_engine(db_name = ":memory:")
