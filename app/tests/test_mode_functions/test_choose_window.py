from contextlib import nullcontext

import pytest
import tkinter as tk
from tkinter import ttk
from app.mode_functions.choose_window import WindowChooseClass


@pytest.fixture
def choose_class():
    return WindowChooseClass(tk.Tk())


class TestChooseWindow:
    TEXT_BUTTON = 'Test'
    STYLE_BUTTON = 'ChooseButton.TButton'

    @pytest.mark.parametrize(
        'root', [tk.Tk(), 123, 'string', {1, 2, 3}, (1, 2, 3), [], [1, 2, 3], {1: 2}, None, False, ]
    )
    def test_init_choose_class(self, root):
        with nullcontext():
            WindowChooseClass(root)

    def test_elements_choose_class(self, choose_class):
        assert isinstance(choose_class.root, tk.Tk)
        if isinstance(choose_class.root, tk.Toplevel):
            assert True
        assert isinstance(choose_class.window, tk.Toplevel)
        assert isinstance(choose_class.label_font, dict)
        assert isinstance(choose_class.label, tk.Label)

    @pytest.mark.parametrize(
        'text_button, style_button',
        [
            (TEXT_BUTTON, STYLE_BUTTON),
            (123, STYLE_BUTTON),
            ('string', STYLE_BUTTON),
            ({1, 2, 3}, STYLE_BUTTON),
            ((1, 2, 3), STYLE_BUTTON),
            ([], STYLE_BUTTON),
            ([1, 2, 3], STYLE_BUTTON),
            ({1: 2}, STYLE_BUTTON),
            (None, STYLE_BUTTON),
            (False, STYLE_BUTTON),
            (tk.Tk(), STYLE_BUTTON),

            (TEXT_BUTTON, 123),
            (TEXT_BUTTON, 'string'),
            (TEXT_BUTTON, {1, 2, 3}),
            (TEXT_BUTTON, (1, 2, 3)),
            (TEXT_BUTTON, []),
            (TEXT_BUTTON, [1, 2, 3]),
            (TEXT_BUTTON, {1: 2}),
            (TEXT_BUTTON, None),
            (TEXT_BUTTON, False),
            (TEXT_BUTTON, tk.Tk()),
        ]
    )
    def test_create_mode_button(self, choose_class, text_button, style_button):
        with nullcontext():
            btn = choose_class.create_choose_button(text_button=text_button, style_button=style_button)
            assert isinstance(btn, ttk.Button)
