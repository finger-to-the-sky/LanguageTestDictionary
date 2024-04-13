from contextlib import nullcontext
from app.other.custom_print import colored_print
import pytest
import tkinter as tk


@pytest.mark.parametrize(
    'message, color, style, expectation',
    [
        ('This is test error', 'red', 'bright', nullcontext()),
        (123, 'red', 'bright', nullcontext()),
        ({1, 2, 3}, 'red', 'bright', nullcontext()),
        ((1, 2, 3), 'red', 'bright', nullcontext()),
        ([], 'red', 'bright', nullcontext()),
        ([1, 2, 3], 'red', 'bright', nullcontext()),
        ({1: 2}, 'red', 'bright', nullcontext()),
        (None, 'red', 'bright', nullcontext()),
        (False, 'red', 'bright', nullcontext()),
        (tk.Tk(), 'red', 'bright', nullcontext()),

        ('This is test error', 123, 'bright', nullcontext()),
        ('This is test error', 'string', 'bright', nullcontext()),
        ('This is test error', {1, 2, 3}, 'bright', pytest.raises(AssertionError)),
        ('This is test error', (1, 2, 3), 'bright', nullcontext()),
        ('This is test error', [], 'bright', pytest.raises(AssertionError)),
        ('This is test error', [1, 2, 3], 'bright', pytest.raises(AssertionError)),
        ('This is test error', {1: 2}, 'bright', pytest.raises(AssertionError)),
        ('This is test error', None, 'bright', nullcontext()),
        ('This is test error', False, 'bright', nullcontext()),
        ('This is test error', tk.Tk(), 'bright', nullcontext()),

        ('This is test error', 'red', 123, nullcontext()),
        ('This is test error', 'red', 'string', nullcontext()),
        ('This is test error', 'red', {1, 2, 3}, pytest.raises(AssertionError)),
        ('This is test error', 'red', (1, 2, 3), nullcontext()),
        ('This is test error', 'red', [], pytest.raises(AssertionError)),
        ('This is test error', 'red', [1, 2, 3], pytest.raises(AssertionError)),
        ('This is test error', 'red', {1: 2}, pytest.raises(AssertionError)),
        ('This is test error', 'red', None, nullcontext()),
        ('This is test error', 'red', False, nullcontext()),
        ('This is test error', 'red', tk.Tk(), nullcontext()),
    ]
)
def test_colored_print(message, color, style, expectation):
    with expectation:
        assert colored_print(message=message, style=style, color=color) is True
