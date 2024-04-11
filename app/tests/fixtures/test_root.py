import pytest
import tkinter as tk


@pytest.fixture
def test_root():
    root = tk.Tk()
    return root
