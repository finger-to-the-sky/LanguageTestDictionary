from contextlib import nullcontext
from app.other.get_path import get_path_project
import tkinter as tk

import pytest


@pytest.mark.parametrize(
    'file', ['README.md', 123, './', {1, 2, 3}, (1, 2, 3), [], [1, 2, 3], {1: 2}, None, False, tk.Tk()]
)
def test_get_path_project(file):
    with nullcontext():
        get_path_project(file=file)
