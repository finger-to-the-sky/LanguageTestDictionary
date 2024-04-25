import pytest
import tkinter as tk

from app.mode_functions.mode_window.mode_test_classes.mode_test_cls import ModeTestWordsClass
from app.mode_functions.mode_window.mode_test_classes.mode_test_words_init import ModeTestWordsInit


@pytest.fixture
def mode_test_class():
    return ModeTestWordsClass(tk.Tk(), 'TestTitle', '800x600', [1], [1])


@pytest.fixture
def mode_test_words_class():
    return ModeTestWordsInit(tk.Tk(), title='TestTitle', size_window='1024x800', first_list=[], second_list=[])
