import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.db.database import database, create_tables

@pytest.fixture(scope="module")
def client():
    client = TestClient(app)
    yield client

@pytest.fixture(autouse=True)
async def setup_and_teardown():
    await database.connect()
    await create_tables()
    yield
    await database.disconnect()
