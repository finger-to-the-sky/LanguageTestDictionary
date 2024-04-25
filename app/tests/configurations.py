from contextlib import nullcontext
from tkinter import ttk
import tkinter as tk
import pytest


def create_test_style(name: str, *args, **kwargs):
    style = ttk.Style()
    style.configure(style=name, *args, **kwargs)
    return name


ROOT_KEYS_VAR = [
    ((), {'master': tk.Tk()}, nullcontext()),
    ((), {'master': tk.Toplevel(tk.Tk())}, nullcontext()),
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
    (tk.Toplevel(tk.Tk()), (), {}, nullcontext()),
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


INIT_TEST_MODE_CLASS = [
            (tk.Tk(), 'TestTitle', '800x600', [1, 2, 3], [1, 2, 3], False),
            (123, 'TestTitle', '800x600', [1, 2, 3], [1, 2, 3], False),
            ('string', 'TestTitle', '800x600', [1, 2, 3], [1, 2, 3], False),
            ({1, 2, 3}, 'TestTitle', '800x600', [1, 2, 3], [1, 2, 3], False),
            ((1, 2, 3), 'TestTitle', '800x600', [1, 2, 3], [1, 2, 3], False),
            ([], 'TestTitle', '800x600', [1, 2, 3], [1, 2, 3], False),
            ([1, 2, 3], 'TestTitle', '800x600', [1, 2, 3], [1, 2, 3], False),
            ({1: 2}, 'TestTitle', '800x600', [1, 2, 3], [1, 2, 3], False),
            (None, 'TestTitle', '800x600', [1, 2, 3], [1, 2, 3], False),
            (False, 'TestTitle', '800x600', [1, 2, 3], [1, 2, 3], False),
            (tk.Tk(), 'TestTitle', '800x600', [1, 2, 3], [1, 2, 3], False),

            (tk.Tk(), 123, '800x600', [1, 2, 3], [1, 2, 3], False),
            (tk.Tk(), 'string', '800x600', [1, 2, 3], [1, 2, 3], False),
            (tk.Tk(), {1, 2, 3}, '800x600', [1, 2, 3], [1, 2, 3], False),
            (tk.Tk(), (1, 2, 3), '800x600', [1, 2, 3], [1, 2, 3], False),
            (tk.Tk(), [], '800x600', [1, 2, 3], [1, 2, 3], False),
            (tk.Tk(), [1, 2, 3], '800x600', [1, 2, 3], [1, 2, 3], False),
            (tk.Tk(), {1: 2}, '800x600', [1, 2, 3], [1, 2, 3], False),
            (tk.Tk(), None, '800x600', [1, 2, 3], [1, 2, 3], False),
            (tk.Tk(), False, '800x600', [1, 2, 3], [1, 2, 3], False),
            (tk.Tk(), tk.Tk(), '800x600', [1, 2, 3], [1, 2, 3], False),

            (tk.Tk(), 'TestTitle', 123, [1, 2, 3], [1, 2, 3], False),
            (tk.Tk(), 'TestTitle', 'string', [1, 2, 3], [1, 2, 3], False),
            (tk.Tk(), 'TestTitle', {1, 2, 3}, [1, 2, 3], [1, 2, 3], False),
            (tk.Tk(), 'TestTitle', (1, 2, 3), [1, 2, 3], [1, 2, 3], False),
            (tk.Tk(), 'TestTitle', [], [1, 2, 3], [1, 2, 3], False),
            (tk.Tk(), 'TestTitle', [1, 2, 3], [1, 2, 3], [1, 2, 3], False),
            (tk.Tk(), 'TestTitle', {1: 2}, [1, 2, 3], [1, 2, 3], False),
            (tk.Tk(), 'TestTitle', None, [1, 2, 3], [1, 2, 3], False),
            (tk.Tk(), 'TestTitle', False, [1, 2, 3], [1, 2, 3], False),
            (tk.Tk(), 'TestTitle', tk.Tk(), [1, 2, 3], [1, 2, 3], False),

            (tk.Tk(), 'TestTitle', '800x600', 123, [1, 2, 3], False),
            (tk.Tk(), 'TestTitle', '800x600', 'string', [1, 2, 3], False),
            (tk.Tk(), 'TestTitle', '800x600', {1, 2, 3}, [1, 2, 3], False),
            (tk.Tk(), 'TestTitle', '800x600', (1, 2, 3), [1, 2, 3], False),
            (tk.Tk(), 'TestTitle', '800x600', [], [1, 2, 3], False),
            (tk.Tk(), 'TestTitle', '800x600', [1, 2, 3], [1, 2, 3], False),
            (tk.Tk(), 'TestTitle', '800x600', {1: 2}, [1, 2, 3], False),
            (tk.Tk(), 'TestTitle', '800x600', None, [1, 2, 3], False),
            (tk.Tk(), 'TestTitle', '800x600', False, [1, 2, 3], False),
            (tk.Tk(), 'TestTitle', '800x600', tk.Tk(), [1, 2, 3], False),

            (tk.Tk(), 'TestTitle', '800x600', [1, 2, 3], 123, False),
            (tk.Tk(), 'TestTitle', '800x600', [1, 2, 3], 'string', False),
            (tk.Tk(), 'TestTitle', '800x600', [1, 2, 3], {1, 2, 3}, False),
            (tk.Tk(), 'TestTitle', '800x600', [1, 2, 3], (1, 2, 3), False),
            (tk.Tk(), 'TestTitle', '800x600', [1, 2, 3], [], False),
            (tk.Tk(), 'TestTitle', '800x600', [1, 2, 3], [1, 2, 3], False),
            (tk.Tk(), 'TestTitle', '800x600', [1, 2, 3], {1: 2}, False),
            (tk.Tk(), 'TestTitle', '800x600', [1, 2, 3], None, False),
            (tk.Tk(), 'TestTitle', '800x600', [1, 2, 3], False, False),
            (tk.Tk(), 'TestTitle', '800x600', [1, 2, 3], tk.Tk(), False),

            (tk.Tk(), 'TestTitle', '800x600', [1, 2, 3], [1, 2, 3], 123),
            (tk.Tk(), 'TestTitle', '800x600', [1, 2, 3], [1, 2, 3], 'string'),
            (tk.Tk(), 'TestTitle', '800x600', [1, 2, 3], [1, 2, 3], {1, 2, 3}),
            (tk.Tk(), 'TestTitle', '800x600', [1, 2, 3], [1, 2, 3], (1, 2, 3)),
            (tk.Tk(), 'TestTitle', '800x600', [1, 2, 3], [1, 2, 3], []),
            (tk.Tk(), 'TestTitle', '800x600', [1, 2, 3], [1, 2, 3], [1, 2, 3]),
            (tk.Tk(), 'TestTitle', '800x600', [1, 2, 3], [1, 2, 3], {1: 2}),
            (tk.Tk(), 'TestTitle', '800x600', [1, 2, 3], [1, 2, 3], None),
            (tk.Tk(), 'TestTitle', '800x600', [1, 2, 3], [1, 2, 3], False),
            (tk.Tk(), 'TestTitle', '800x600', [1, 2, 3], [1, 2, 3], tk.Tk()),

        ]