import pytest
from tinydb import TinyDB
from app.config import updated_path


@pytest.fixture
def test_db():
    return TinyDB(f'{updated_path}/app/other/db/test_db.json')
