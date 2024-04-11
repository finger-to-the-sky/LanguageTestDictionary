import pytest
from LanguageTestDictionary import MainWindow


@pytest.fixture
def main_window():
    main = MainWindow()
    return main
