from contextlib import nullcontext
from tkinter import ttk
import tkinter as tk
import pytest


@pytest.fixture
def test_root():
    root = tk.Tk()
    return root


def create_test_style(name: str, *args, **kwargs):
    style = ttk.Style()
    style.configure(style=name, *args, **kwargs)
    return name


ROOT_KEYS_VAR = [
    ((), {'master': tk.Tk()}, nullcontext()),
    ((), {'master': tk.Frame(tk.Tk())}, nullcontext()),
    ((), {'master': 'root'}, pytest.raises(AssertionError)),
    ((), {'master': 123}, pytest.raises(AssertionError)),
    ((), {'master': (1, 2, 3)}, pytest.raises(AssertionError)),
    ((), {'master': {'test': 123}}, pytest.raises(AssertionError)),
    ((), {'master': ['test', 123]}, pytest.raises(AssertionError)),
    ((), {'master': {'test', 123}}, pytest.raises(AssertionError)),
    ((), {'master': False}, pytest.raises(AssertionError)),
]
ROOT_KEYS = [
    (tk.Tk(), (), {}, nullcontext()),
    (tk.Frame(tk.Tk()), (), {}, nullcontext()),
    ('test', (), {}, pytest.raises(AssertionError)),
    (123, (), {}, pytest.raises(AssertionError)),
    ({'test': 123}, (), {}, pytest.raises(AssertionError)),
    ([1, 2, 3], (), {}, pytest.raises(AssertionError)),
    ({1, 2, 3}, (), {}, pytest.raises(AssertionError)),
    (('a', 'b', 'c'), (), {}, pytest.raises(AssertionError)),
    (False, (), {}, pytest.raises(AssertionError))
]
COLOR_GROUND_KEYS = [
    ((), {'background': 'blue'}, nullcontext()),
    ((), {'background': 123}, pytest.raises(AssertionError)),
    ((), {'background': 'string'}, pytest.raises(AssertionError)),
    ((), {'background': {'key': 123}}, pytest.raises(AssertionError)),
    ((), {'background': [1, 2, 3]}, pytest.raises(AssertionError)),
    ((), {'background': (1, 2, 3)}, pytest.raises(AssertionError)),
    ((), {'background': {1, 2, 3}}, pytest.raises(AssertionError)),
    ((), {'background': False}, pytest.raises(AssertionError)),

    ((), {'foreground': 'blue'}, nullcontext()),
    ((), {'foreground': 123}, pytest.raises(AssertionError)),
    ((), {'foreground': 'string'}, pytest.raises(AssertionError)),
    ((), {'foreground': {'key': 123}}, pytest.raises(AssertionError)),
    ((), {'foreground': [1, 2, 3]}, pytest.raises(AssertionError)),
    ((), {'foreground': (1, 2, 3)}, pytest.raises(AssertionError)),
    ((), {'foreground': {1, 2, 3}}, pytest.raises(AssertionError)),
    ((), {'foreground': False}, pytest.raises(AssertionError)),
]
FONT_KEYS = [
    ((), {'font': 'blue'}, nullcontext()),
    ((), {'font': 123}, nullcontext()),
    ((), {'font': 'string'}, nullcontext()),
    ((), {'font': {'key': 123}}, nullcontext()),
    ((), {'font': [1, 2, 3]}, pytest.raises(AssertionError)),
    ((), {'font': (1, 2, 3)}, pytest.raises(AssertionError)),
    ((), {'font': ('Georgia', 12)}, nullcontext()),
    ((), {'font': {1, 2, 3}}, nullcontext()),
    ((), {'font': False}, nullcontext()),
]
