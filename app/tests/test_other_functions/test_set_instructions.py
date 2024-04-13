from contextlib import nullcontext
from app.other.instruction.instructions import set_instruction_field
import pytest
import tkinter as tk

INSTRUCTION_TEXT = 'This is instruction text'


@pytest.mark.parametrize(
    'window, text, args, kwargs',
    [
        (tk.Tk(), INSTRUCTION_TEXT, (), {'side': tk.BOTTOM, 'pady': 30}),
        (123, INSTRUCTION_TEXT, (), {'side': tk.BOTTOM, 'pady': 30}),
        ('string', INSTRUCTION_TEXT, (), {'side': tk.BOTTOM, 'pady': 30}),
        ({1, 2, 3}, INSTRUCTION_TEXT, (), {'side': tk.BOTTOM, 'pady': 30}),
        ((1, 2, 3), INSTRUCTION_TEXT, (), {'side': tk.BOTTOM, 'pady': 30}),
        ([], INSTRUCTION_TEXT, (), {'side': tk.BOTTOM, 'pady': 30}),
        ([1, 2, 3], INSTRUCTION_TEXT, (), {'side': tk.BOTTOM, 'pady': 30}),
        ({1: 2}, INSTRUCTION_TEXT, (), {'side': tk.BOTTOM, 'pady': 30}),
        (None, INSTRUCTION_TEXT, (), {'side': tk.BOTTOM, 'pady': 30}),
        (False, INSTRUCTION_TEXT, (), {'side': tk.BOTTOM, 'pady': 30}),

        (tk.Tk(), 123, (), {'side': tk.BOTTOM, 'pady': 30}),
        (tk.Tk(), 'string', (), {'side': tk.BOTTOM, 'pady': 30}),
        (tk.Tk(), {1, 2, 3}, (), {'side': tk.BOTTOM, 'pady': 30}),
        (tk.Tk(), (1, 2, 3), (), {'side': tk.BOTTOM, 'pady': 30}),
        (tk.Tk(), [], (), {'side': tk.BOTTOM, 'pady': 30}),
        (tk.Tk(), [1, 2, 3], (), {'side': tk.BOTTOM, 'pady': 30}),
        (tk.Tk(), {1: 2}, (), {'side': tk.BOTTOM, 'pady': 30}),
        (tk.Tk(), None, (), {'side': tk.BOTTOM, 'pady': 30}),
        (tk.Tk(), False, (), {'side': tk.BOTTOM, 'pady': 30}),
        (tk.Tk(), tk.Tk(), (), {'side': tk.BOTTOM, 'pady': 30}),

        (tk.Tk(), INSTRUCTION_TEXT, (), {'123': 123}),
        (tk.Tk(), INSTRUCTION_TEXT, (), {'side': 123}),
        (tk.Tk(), INSTRUCTION_TEXT, (), {'pady': 'string'}),
        (tk.Tk(), INSTRUCTION_TEXT, (), {'padx': {1, 2, 3}}),
        (tk.Tk(), INSTRUCTION_TEXT, (), {'anchor': (1, 2, 3)}),
        (tk.Tk(), INSTRUCTION_TEXT, (), {'padx': []}),
        (tk.Tk(), INSTRUCTION_TEXT, (), {'padx': [1, 2, 3]}),
        (tk.Tk(), INSTRUCTION_TEXT, (), {'padx': {1: 2}}),
        (tk.Tk(), INSTRUCTION_TEXT, (), {'padx': None}),
        (tk.Tk(), INSTRUCTION_TEXT, (), {'padx': False}),

    ]
)
def test_set_instruction(window, text, args, kwargs):
    with nullcontext():
        set_instruction_field(window, text, *args, **kwargs)
