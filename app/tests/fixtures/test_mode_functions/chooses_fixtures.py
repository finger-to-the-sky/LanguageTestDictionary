import pytest
import tkinter as tk
from app.mode_functions.choose_window import WindowChooseClass


@pytest.fixture
def choose_class():
    return WindowChooseClass(tk.Tk())