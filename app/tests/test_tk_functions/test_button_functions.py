from contextlib import nullcontext
from tkinter import ttk
import tkinter as tk
import pytest

from app.tests.configuration import ROOT_KEYS, COLOR_GROUND_KEYS, FONT_KEYS, create_test_root, create_test_style
from app.tk_functions import create_ttk_button, create_button, create_int_var, create_radio_button


class TestButtonFunctions:
    @pytest.mark.parametrize(
        'root, args, kwargs, expectation', ROOT_KEYS + COLOR_GROUND_KEYS + FONT_KEYS + [

            (create_test_root(), (), {'image': 123}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'image': 'string'}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'image': {'key': 123}}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'image': [1, 2, 3]}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'image': (1, 2, 3)}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'image': {1, 2, 3}}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'image': False}, pytest.raises(AssertionError)),

            (create_test_root(), (), {'height': '123213'}, nullcontext()),
            (create_test_root(), (), {'height': 123}, nullcontext()),
            (create_test_root(), (), {'height': 'string'}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'height': {'key': 123}}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'height': [1, 2, 3]}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'height': (1, 2, 3)}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'height': {1, 2, 3}}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'height': False}, nullcontext()),

            (create_test_root(), (), {'width': '12333'}, nullcontext()),
            (create_test_root(), (), {'width': 123}, nullcontext()),
            (create_test_root(), (), {'width': 'string'}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'width': {'key': 123}}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'width': [1, 2, 3]}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'width': (1, 2, 3)}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'width': {1, 2, 3}}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'width': False}, nullcontext()),

            (create_test_root(), (), {'anchor': tk.W}, nullcontext()),
            (create_test_root(), (), {'anchor': tk.E}, nullcontext()),
            (create_test_root(), (), {'anchor': tk.S}, nullcontext()),
            (create_test_root(), (), {'anchor': tk.N}, nullcontext()),
            (create_test_root(), (), {'anchor': 'se'}, nullcontext()),
            (create_test_root(), (), {'anchor': 'sw'}, nullcontext()),
            (create_test_root(), (), {'anchor': 'ne'}, nullcontext()),
            (create_test_root(), (), {'anchor': 'nw'}, nullcontext()),
            (create_test_root(), (), {'anchor': '12333'}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'anchor': 123}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'anchor': 'string'}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'anchor': {'key': 123}}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'anchor': [1, 2, 3]}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'anchor': (1, 2, 3)}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'anchor': {1, 2, 3}}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'anchor': False}, pytest.raises(AssertionError)),

            (create_test_root(), (), {'padx': '12333'}, nullcontext()),
            (create_test_root(), (), {'padx': 123}, nullcontext()),
            (create_test_root(), (), {'padx': 'string'}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'padx': {'key': 123}}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'padx': [1, 2, 3]}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'padx': (1, 2, 3)}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'padx': {1, 2, 3}}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'padx': False}, nullcontext()),

            (create_test_root(), (), {'pady': '12333'}, nullcontext()),
            (create_test_root(), (), {'pady': 123}, nullcontext()),
            (create_test_root(), (), {'pady': 'string'}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'pady': {'key': 123}}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'pady': [1, 2, 3]}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'pady': (1, 2, 3)}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'pady': {1, 2, 3}}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'pady': False}, nullcontext()),
        ]
    )
    def test_create_button(self, root, args, kwargs, expectation):
        with expectation:
            button = create_button(root, *args, **kwargs)
            assert isinstance(button, tk.Button)

    @pytest.mark.parametrize(
        'root, args, kwargs, expectation', ROOT_KEYS + [

            (create_test_root(), (), {'background': 'blue'}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'background': 123}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'background': 'string'}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'background': {'key': 123}}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'background': [1, 2, 3]}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'background': (1, 2, 3)}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'background': {1, 2, 3}}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'background': False}, pytest.raises(AssertionError)),

            (create_test_root(), (), {'font': 'blue'}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'font': 123}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'font': 'string'}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'font': {'key': 123}}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'font': [1, 2, 3]}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'font': (1, 2, 3)}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'font': ('Georgia', 12)}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'font': {1, 2, 3}}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'font': False}, pytest.raises(AssertionError)),

            (create_test_root(), (), {'image': 123}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'image': 'string'}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'image': {'key': 123}}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'image': [1, 2, 3]}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'image': (1, 2, 3)}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'image': {1, 2, 3}}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'image': False}, pytest.raises(AssertionError)),

            (create_test_root(), (), {'foreground': 'blue'}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'foreground': 123}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'foreground': 'string'}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'foreground': {'key': 123}}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'foreground': [1, 2, 3]}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'foreground': (1, 2, 3)}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'foreground': {1, 2, 3}}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'foreground': False}, pytest.raises(AssertionError)),

            (create_test_root(), (), {'height': '123213'}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'height': 123}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'height': 'string'}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'height': {'key': 123}}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'height': [1, 2, 3]}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'height': (1, 2, 3)}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'height': {1, 2, 3}}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'height': False}, pytest.raises(AssertionError)),

            (create_test_root(), (), {'width': '12333'}, nullcontext()),
            (create_test_root(), (), {'width': 123}, nullcontext()),
            (create_test_root(), (), {'width': 'string'}, nullcontext()),
            (create_test_root(), (), {'width': {'key': 123}}, nullcontext()),
            (create_test_root(), (), {'width': [1, 2, 3]}, nullcontext()),
            (create_test_root(), (), {'width': (1, 2, 3)}, nullcontext()),
            (create_test_root(), (), {'width': {1, 2, 3}}, nullcontext()),
            (create_test_root(), (), {'width': False}, nullcontext()),

            (create_test_root(), (), {'anchor': tk.W}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'anchor': tk.E}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'anchor': tk.S}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'anchor': tk.N}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'anchor': 'se'}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'anchor': 'sw'}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'anchor': 'ne'}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'anchor': 'nw'}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'anchor': '12333'}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'anchor': 123}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'anchor': 'string'}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'anchor': {'key': 123}}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'anchor': [1, 2, 3]}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'anchor': (1, 2, 3)}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'anchor': {1, 2, 3}}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'anchor': False}, pytest.raises(AssertionError)),

            (create_test_root(), (), {'padx': '12333'}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'padx': 123}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'padx': 'string'}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'padx': {'key': 123}}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'padx': [1, 2, 3]}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'padx': (1, 2, 3)}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'padx': {1, 2, 3}}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'padx': False}, pytest.raises(AssertionError)),

            (create_test_root(), (), {'pady': '12333'}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'pady': 123}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'pady': 'string'}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'pady': {'key': 123}}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'pady': [1, 2, 3]}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'pady': (1, 2, 3)}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'pady': {1, 2, 3}}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'pady': False}, pytest.raises(AssertionError)),
        ]
    )
    def test_create_ttk_button(self, root, args, kwargs, expectation):
        with expectation:
            button = create_ttk_button(root, *args, **kwargs)
            assert isinstance(button, ttk.Button)

    @pytest.mark.parametrize(
        'root, style, args, kwargs, expectation',
        [
            (create_test_root(), create_test_style('testBtn.TButton'), (), {}, nullcontext()),
            (create_test_root(), '12333', (), {}, pytest.raises(AttributeError)),
            (create_test_root(), 123, (), {}, pytest.raises(AttributeError)),
            (create_test_root(), {'key': 123}, (), {}, pytest.raises(AttributeError)),
            (create_test_root(), [1, 2, 3], (), {}, pytest.raises(AttributeError)),
            (create_test_root(), (1, 2, 3), (), {}, pytest.raises(AttributeError)),
            (create_test_root(), {1, 2, 3}, (), {}, pytest.raises(AttributeError)),
            (create_test_root(), False, (), {}, pytest.raises(AttributeError)),
        ]
    )
    def test_create_ttk_button_style(self, root, style, args, kwargs, expectation):
        with expectation:
            button = create_ttk_button(root, style, *args, **kwargs),
            style = button[0].cget('style')
            assert style == 'testBtn.TButton'

    @pytest.mark.parametrize(
        'root, args, kwargs, expectation', ROOT_KEYS + COLOR_GROUND_KEYS + FONT_KEYS + [

            (create_test_root(), (), {'image': 123}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'image': 'string'}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'image': {'key': 123}}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'image': [1, 2, 3]}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'image': (1, 2, 3)}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'image': {1, 2, 3}}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'image': False}, pytest.raises(AssertionError)),

            (create_test_root(), (), {'height': '123213'}, nullcontext()),
            (create_test_root(), (), {'height': 123}, nullcontext()),
            (create_test_root(), (), {'height': 'string'}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'height': {'key': 123}}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'height': [1, 2, 3]}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'height': (1, 2, 3)}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'height': {1, 2, 3}}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'height': False}, nullcontext()),

            (create_test_root(), (), {'width': '12333'}, nullcontext()),
            (create_test_root(), (), {'width': 123}, nullcontext()),
            (create_test_root(), (), {'width': 'string'}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'width': {'key': 123}}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'width': [1, 2, 3]}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'width': (1, 2, 3)}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'width': {1, 2, 3}}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'width': False}, nullcontext()),

            (create_test_root(), (), {'anchor': tk.W}, nullcontext()),
            (create_test_root(), (), {'anchor': tk.E}, nullcontext()),
            (create_test_root(), (), {'anchor': tk.S}, nullcontext()),
            (create_test_root(), (), {'anchor': tk.N}, nullcontext()),
            (create_test_root(), (), {'anchor': 'se'}, nullcontext()),
            (create_test_root(), (), {'anchor': 'sw'}, nullcontext()),
            (create_test_root(), (), {'anchor': 'ne'}, nullcontext()),
            (create_test_root(), (), {'anchor': 'nw'}, nullcontext()),
            (create_test_root(), (), {'anchor': '12333'}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'anchor': 123}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'anchor': 'string'}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'anchor': {'key': 123}}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'anchor': [1, 2, 3]}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'anchor': (1, 2, 3)}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'anchor': {1, 2, 3}}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'anchor': False}, pytest.raises(AssertionError)),

            (create_test_root(), (), {'padx': '12333'}, nullcontext()),
            (create_test_root(), (), {'padx': 123}, nullcontext()),
            (create_test_root(), (), {'padx': 'string'}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'padx': {'key': 123}}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'padx': [1, 2, 3]}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'padx': (1, 2, 3)}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'padx': {1, 2, 3}}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'padx': False}, nullcontext()),

            (create_test_root(), (), {'pady': '12333'}, nullcontext()),
            (create_test_root(), (), {'pady': 123}, nullcontext()),
            (create_test_root(), (), {'pady': 'string'}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'pady': {'key': 123}}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'pady': [1, 2, 3]}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'pady': (1, 2, 3)}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'pady': {1, 2, 3}}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'pady': False}, nullcontext()),

            (create_test_root(), (), {'value': False}, nullcontext()),
            (create_test_root(), (), {'value': 'Value'}, nullcontext()),
            (create_test_root(), (), {'value': 'True'}, nullcontext()),
            (create_test_root(), (), {'value': 123}, nullcontext()),
            (create_test_root(), (), {'value': [1, 2, 3]}, nullcontext()),
            (create_test_root(), (), {'value': {1, 2, 3}}, nullcontext()),
            (create_test_root(), (), {'value': {'value': False}}, nullcontext()),
            (create_test_root(), (), {'value': ('value', False)}, nullcontext()),

            (create_test_root(), (), {'variable': create_int_var()}, nullcontext()),
            (create_test_root(), (), {'variable': False}, nullcontext()),
            (create_test_root(), (), {'variable': 'Value'}, nullcontext()),
            (create_test_root(), (), {'variable': 'True'}, nullcontext()),
            (create_test_root(), (), {'variable': 123}, nullcontext()),
            (create_test_root(), (), {'variable': [1, 2, 3]}, nullcontext()),
            (create_test_root(), (), {'variable': {1, 2, 3}}, nullcontext()),
            (create_test_root(), (), {'variable': {'value': False}}, nullcontext()),
            (create_test_root(), (), {'variable': ('value', False)}, nullcontext()),
        ]
    )
    def test_create_radio_button(self, root, args, kwargs, expectation):
        with expectation:
            radio_btn = create_radio_button(root, *args, **kwargs)
            assert isinstance(radio_btn, tk.Radiobutton)
