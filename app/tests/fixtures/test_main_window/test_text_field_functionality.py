import pytest
from app.translator.text_field_functionality import TextWorker, TextFieldFunctionality


@pytest.fixture
def test_text_worker():
    return TextWorker(src='English', dest='Russian')


@pytest.fixture
def test_text_field_functionality():
    return TextFieldFunctionality()
