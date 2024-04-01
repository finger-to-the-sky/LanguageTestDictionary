from contextlib import nullcontext
from tkinter import ttk
import tkinter as tk
import pytest


def create_test_root(title: str = None, geometry: str = None):
    root = tk.Tk()
    root.geometry(geometry)
    root.title(title)
    return root


def create_test_style(name: str, *args, **kwargs):
    style = ttk.Style()
    style.configure(style=name, *args, **kwargs)
    return name


ROOT_KEYS_VAR = [
    ((), {'master': create_test_root()}, nullcontext()),
    ((), {'master': tk.Frame(create_test_root())}, nullcontext()),
    ((), {'master': 'root'}, pytest.raises(AssertionError)),
    ((), {'master': 123}, pytest.raises(AssertionError)),
    ((), {'master': (1, 2, 3)}, pytest.raises(AssertionError)),
    ((), {'master': {'test': 123}}, pytest.raises(AssertionError)),
    ((), {'master': ['test', 123]}, pytest.raises(AssertionError)),
    ((), {'master': {'test', 123}}, pytest.raises(AssertionError)),
    ((), {'master': False}, pytest.raises(AssertionError)),
]
ROOT_KEYS = [
    (create_test_root(), (), {}, nullcontext()),
    (tk.Frame(create_test_root()), (), {}, nullcontext()),
    ('test', (), {}, pytest.raises(AssertionError)),
    (123, (), {}, pytest.raises(AssertionError)),
    ({'test': 123}, (), {}, pytest.raises(AssertionError)),
    ([1, 2, 3], (), {}, pytest.raises(AssertionError)),
    ({1, 2, 3}, (), {}, pytest.raises(AssertionError)),
    (('a', 'b', 'c'), (), {}, pytest.raises(AssertionError)),
    (False, (), {}, pytest.raises(AssertionError))
]
COLOR_GROUND_KEYS = [
    (create_test_root(), (), {'background': 'blue'}, nullcontext()),
    (create_test_root(), (), {'background': 123}, pytest.raises(AssertionError)),
    (create_test_root(), (), {'background': 'string'}, pytest.raises(AssertionError)),
    (create_test_root(), (), {'background': {'key': 123}}, pytest.raises(AssertionError)),
    (create_test_root(), (), {'background': [1, 2, 3]}, pytest.raises(AssertionError)),
    (create_test_root(), (), {'background': (1, 2, 3)}, pytest.raises(AssertionError)),
    (create_test_root(), (), {'background': {1, 2, 3}}, pytest.raises(AssertionError)),
    (create_test_root(), (), {'background': False}, pytest.raises(AssertionError)),

    (create_test_root(), (), {'foreground': 'blue'}, nullcontext()),
    (create_test_root(), (), {'foreground': 123}, pytest.raises(AssertionError)),
    (create_test_root(), (), {'foreground': 'string'}, pytest.raises(AssertionError)),
    (create_test_root(), (), {'foreground': {'key': 123}}, pytest.raises(AssertionError)),
    (create_test_root(), (), {'foreground': [1, 2, 3]}, pytest.raises(AssertionError)),
    (create_test_root(), (), {'foreground': (1, 2, 3)}, pytest.raises(AssertionError)),
    (create_test_root(), (), {'foreground': {1, 2, 3}}, pytest.raises(AssertionError)),
    (create_test_root(), (), {'foreground': False}, pytest.raises(AssertionError)),
]
FONT_KEYS = [
    (create_test_root(), (), {'font': 'blue'}, nullcontext()),
    (create_test_root(), (), {'font': 123}, nullcontext()),
    (create_test_root(), (), {'font': 'string'}, nullcontext()),
    (create_test_root(), (), {'font': {'key': 123}}, nullcontext()),
    (create_test_root(), (), {'font': [1, 2, 3]}, pytest.raises(AssertionError)),
    (create_test_root(), (), {'font': (1, 2, 3)}, pytest.raises(AssertionError)),
    (create_test_root(), (), {'font': ('Georgia', 12)}, nullcontext()),
    (create_test_root(), (), {'font': {1, 2, 3}}, nullcontext()),
    (create_test_root(), (), {'font': False}, nullcontext()),
]
