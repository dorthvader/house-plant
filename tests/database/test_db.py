"""Test database creation and deletion."""

import sqlalchemy

def test_create_db(temp_engine):
    """Test create_database and get_database_engine."""
    assert isinstance(temp_engine, sqlalchemy.Engine)
