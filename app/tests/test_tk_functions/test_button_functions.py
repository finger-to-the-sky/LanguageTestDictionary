from contextlib import nullcontext
from tkinter import ttk
import tkinter as tk
import pytest
from app.tests.configuration import COLOR_GROUND_KEYS, FONT_KEYS, create_test_style
from app.tk_functions import create_ttk_button, create_button, create_int_var, create_radio_button
from app.tests.fixtures.test_root import test_root


class TestButtonFunctions:
    @pytest.mark.parametrize(
        'args, kwargs, expectation', COLOR_GROUND_KEYS + FONT_KEYS + [

            ((), {'image': 123}, pytest.raises(AssertionError)),
            ((), {'image': 'string'}, pytest.raises(AssertionError)),
            ((), {'image': {'key': 123}}, pytest.raises(AssertionError)),
            ((), {'image': [1, 2, 3]}, pytest.raises(AssertionError)),
            ((), {'image': (1, 2, 3)}, pytest.raises(AssertionError)),
            ((), {'image': {1, 2, 3}}, pytest.raises(AssertionError)),
            ((), {'image': False}, pytest.raises(AssertionError)),

            ((), {'height': '123213'}, nullcontext()),
            ((), {'height': 123}, nullcontext()),
            ((), {'height': 'string'}, pytest.raises(AssertionError)),
            ((), {'height': {'key': 123}}, pytest.raises(AssertionError)),
            ((), {'height': [1, 2, 3]}, pytest.raises(AssertionError)),
            ((), {'height': (1, 2, 3)}, pytest.raises(AssertionError)),
            ((), {'height': {1, 2, 3}}, pytest.raises(AssertionError)),
            ((), {'height': False}, nullcontext()),

            ((), {'width': '12333'}, nullcontext()),
            ((), {'width': 123}, nullcontext()),
            ((), {'width': 'string'}, pytest.raises(AssertionError)),
            ((), {'width': {'key': 123}}, pytest.raises(AssertionError)),
            ((), {'width': [1, 2, 3]}, pytest.raises(AssertionError)),
            ((), {'width': (1, 2, 3)}, pytest.raises(AssertionError)),
            ((), {'width': {1, 2, 3}}, pytest.raises(AssertionError)),
            ((), {'width': False}, nullcontext()),

            ((), {'anchor': tk.W}, nullcontext()),
            ((), {'anchor': tk.E}, nullcontext()),
            ((), {'anchor': tk.S}, nullcontext()),
            ((), {'anchor': tk.N}, nullcontext()),
            ((), {'anchor': 'se'}, nullcontext()),
            ((), {'anchor': 'sw'}, nullcontext()),
            ((), {'anchor': 'ne'}, nullcontext()),
            ((), {'anchor': 'nw'}, nullcontext()),
            ((), {'anchor': '12333'}, pytest.raises(AssertionError)),
            ((), {'anchor': 123}, pytest.raises(AssertionError)),
            ((), {'anchor': 'string'}, pytest.raises(AssertionError)),
            ((), {'anchor': {'key': 123}}, pytest.raises(AssertionError)),
            ((), {'anchor': [1, 2, 3]}, pytest.raises(AssertionError)),
            ((), {'anchor': (1, 2, 3)}, pytest.raises(AssertionError)),
            ((), {'anchor': {1, 2, 3}}, pytest.raises(AssertionError)),
            ((), {'anchor': False}, pytest.raises(AssertionError)),

            ((), {'padx': '12333'}, nullcontext()),
            ((), {'padx': 123}, nullcontext()),
            ((), {'padx': 'string'}, pytest.raises(AssertionError)),
            ((), {'padx': {'key': 123}}, pytest.raises(AssertionError)),
            ((), {'padx': [1, 2, 3]}, pytest.raises(AssertionError)),
            ((), {'padx': (1, 2, 3)}, pytest.raises(AssertionError)),
            ((), {'padx': {1, 2, 3}}, pytest.raises(AssertionError)),
            ((), {'padx': False}, nullcontext()),

            ((), {'pady': '12333'}, nullcontext()),
            ((), {'pady': 123}, nullcontext()),
            ((), {'pady': 'string'}, pytest.raises(AssertionError)),
            ((), {'pady': {'key': 123}}, pytest.raises(AssertionError)),
            ((), {'pady': [1, 2, 3]}, pytest.raises(AssertionError)),
            ((), {'pady': (1, 2, 3)}, pytest.raises(AssertionError)),
            ((), {'pady': {1, 2, 3}}, pytest.raises(AssertionError)),
            ((), {'pady': False}, nullcontext()),
        ]
    )
    def test_create_button(self, test_root, args, kwargs, expectation):
        with expectation:
            button = create_button(test_root, *args, **kwargs)
            assert isinstance(button, tk.Button)

    @pytest.mark.parametrize(
        'args, kwargs, expectation', [

            ((), {'background': 'blue'}, pytest.raises(AssertionError)),
            ((), {'background': 123}, pytest.raises(AssertionError)),
            ((), {'background': 'string'}, pytest.raises(AssertionError)),
            ((), {'background': {'key': 123}}, pytest.raises(AssertionError)),
            ((), {'background': [1, 2, 3]}, pytest.raises(AssertionError)),
            ((), {'background': (1, 2, 3)}, pytest.raises(AssertionError)),
            ((), {'background': {1, 2, 3}}, pytest.raises(AssertionError)),
            ((), {'background': False}, pytest.raises(AssertionError)),

            ((), {'font': 'blue'}, pytest.raises(AssertionError)),
            ((), {'font': 123}, pytest.raises(AssertionError)),
            ((), {'font': 'string'}, pytest.raises(AssertionError)),
            ((), {'font': {'key': 123}}, pytest.raises(AssertionError)),
            ((), {'font': [1, 2, 3]}, pytest.raises(AssertionError)),
            ((), {'font': (1, 2, 3)}, pytest.raises(AssertionError)),
            ((), {'font': ('Georgia', 12)}, pytest.raises(AssertionError)),
            ((), {'font': {1, 2, 3}}, pytest.raises(AssertionError)),
            ((), {'font': False}, pytest.raises(AssertionError)),

            ((), {'image': 123}, pytest.raises(AssertionError)),
            ((), {'image': 'string'}, pytest.raises(AssertionError)),
            ((), {'image': {'key': 123}}, pytest.raises(AssertionError)),
            ((), {'image': [1, 2, 3]}, pytest.raises(AssertionError)),
            ((), {'image': (1, 2, 3)}, pytest.raises(AssertionError)),
            ((), {'image': {1, 2, 3}}, pytest.raises(AssertionError)),
            ((), {'image': False}, pytest.raises(AssertionError)),

            ((), {'foreground': 'blue'}, pytest.raises(AssertionError)),
            ((), {'foreground': 123}, pytest.raises(AssertionError)),
            ((), {'foreground': 'string'}, pytest.raises(AssertionError)),
            ((), {'foreground': {'key': 123}}, pytest.raises(AssertionError)),
            ((), {'foreground': [1, 2, 3]}, pytest.raises(AssertionError)),
            ((), {'foreground': (1, 2, 3)}, pytest.raises(AssertionError)),
            ((), {'foreground': {1, 2, 3}}, pytest.raises(AssertionError)),
            ((), {'foreground': False}, pytest.raises(AssertionError)),

            ((), {'height': '123213'}, pytest.raises(AssertionError)),
            ((), {'height': 123}, pytest.raises(AssertionError)),
            ((), {'height': 'string'}, pytest.raises(AssertionError)),
            ((), {'height': {'key': 123}}, pytest.raises(AssertionError)),
            ((), {'height': [1, 2, 3]}, pytest.raises(AssertionError)),
            ((), {'height': (1, 2, 3)}, pytest.raises(AssertionError)),
            ((), {'height': {1, 2, 3}}, pytest.raises(AssertionError)),
            ((), {'height': False}, pytest.raises(AssertionError)),

            ((), {'width': '12333'}, nullcontext()),
            ((), {'width': 123}, nullcontext()),
            ((), {'width': 'string'}, nullcontext()),
            ((), {'width': {'key': 123}}, nullcontext()),
            ((), {'width': [1, 2, 3]}, nullcontext()),
            ((), {'width': (1, 2, 3)}, nullcontext()),
            ((), {'width': {1, 2, 3}}, nullcontext()),
            ((), {'width': False}, nullcontext()),

            ((), {'anchor': tk.W}, pytest.raises(AssertionError)),
            ((), {'anchor': tk.E}, pytest.raises(AssertionError)),
            ((), {'anchor': tk.S}, pytest.raises(AssertionError)),
            ((), {'anchor': tk.N}, pytest.raises(AssertionError)),
            ((), {'anchor': 'se'}, pytest.raises(AssertionError)),
            ((), {'anchor': 'sw'}, pytest.raises(AssertionError)),
            ((), {'anchor': 'ne'}, pytest.raises(AssertionError)),
            ((), {'anchor': 'nw'}, pytest.raises(AssertionError)),
            ((), {'anchor': '12333'}, pytest.raises(AssertionError)),
            ((), {'anchor': 123}, pytest.raises(AssertionError)),
            ((), {'anchor': 'string'}, pytest.raises(AssertionError)),
            ((), {'anchor': {'key': 123}}, pytest.raises(AssertionError)),
            ((), {'anchor': [1, 2, 3]}, pytest.raises(AssertionError)),
            ((), {'anchor': (1, 2, 3)}, pytest.raises(AssertionError)),
            ((), {'anchor': {1, 2, 3}}, pytest.raises(AssertionError)),
            ((), {'anchor': False}, pytest.raises(AssertionError)),

            ((), {'padx': '12333'}, pytest.raises(AssertionError)),
            ((), {'padx': 123}, pytest.raises(AssertionError)),
            ((), {'padx': 'string'}, pytest.raises(AssertionError)),
            ((), {'padx': {'key': 123}}, pytest.raises(AssertionError)),
            ((), {'padx': [1, 2, 3]}, pytest.raises(AssertionError)),
            ((), {'padx': (1, 2, 3)}, pytest.raises(AssertionError)),
            ((), {'padx': {1, 2, 3}}, pytest.raises(AssertionError)),
            ((), {'padx': False}, pytest.raises(AssertionError)),

            ((), {'pady': '12333'}, pytest.raises(AssertionError)),
            ((), {'pady': 123}, pytest.raises(AssertionError)),
            ((), {'pady': 'string'}, pytest.raises(AssertionError)),
            ((), {'pady': {'key': 123}}, pytest.raises(AssertionError)),
            ((), {'pady': [1, 2, 3]}, pytest.raises(AssertionError)),
            ((), {'pady': (1, 2, 3)}, pytest.raises(AssertionError)),
            ((), {'pady': {1, 2, 3}}, pytest.raises(AssertionError)),
            ((), {'pady': False}, pytest.raises(AssertionError)),
        ]
    )
    def test_create_ttk_button(self, test_root, args, kwargs, expectation):
        with expectation:
            button = create_ttk_button(test_root, *args, **kwargs)
            assert isinstance(button, ttk.Button)

    @pytest.mark.parametrize(
        'style, args, kwargs, expectation',
        [
            (create_test_style('testBtn.TButton'), (), {}, nullcontext()),
            ('12333', (), {}, pytest.raises(AttributeError)),
            (123, (), {}, pytest.raises(AttributeError)),
            ({'key': 123}, (), {}, pytest.raises(AttributeError)),
            ([1, 2, 3], (), {}, pytest.raises(AttributeError)),
            ((1, 2, 3), (), {}, pytest.raises(AttributeError)),
            ({1, 2, 3}, (), {}, pytest.raises(AttributeError)),
            (False, (), {}, pytest.raises(AttributeError)),
        ]
    )
    def test_create_ttk_button_style(self, test_root, style, args, kwargs, expectation):
        with expectation:
            button = create_ttk_button(test_root, style, *args, **kwargs),
            style = button[0].cget('style')
            assert style == 'testBtn.TButton'

    @pytest.mark.parametrize(
        'args, kwargs, expectation', COLOR_GROUND_KEYS + FONT_KEYS + [

            ((), {'image': 123}, pytest.raises(AssertionError)),
            ((), {'image': 'string'}, pytest.raises(AssertionError)),
            ((), {'image': {'key': 123}}, pytest.raises(AssertionError)),
            ((), {'image': [1, 2, 3]}, pytest.raises(AssertionError)),
            ((), {'image': (1, 2, 3)}, pytest.raises(AssertionError)),
            ((), {'image': {1, 2, 3}}, pytest.raises(AssertionError)),
            ((), {'image': False}, pytest.raises(AssertionError)),

            ((), {'height': '123213'}, nullcontext()),
            ((), {'height': 123}, nullcontext()),
            ((), {'height': 'string'}, pytest.raises(AssertionError)),
            ((), {'height': {'key': 123}}, pytest.raises(AssertionError)),
            ((), {'height': [1, 2, 3]}, pytest.raises(AssertionError)),
            ((), {'height': (1, 2, 3)}, pytest.raises(AssertionError)),
            ((), {'height': {1, 2, 3}}, pytest.raises(AssertionError)),
            ((), {'height': False}, nullcontext()),

            ((), {'width': '12333'}, nullcontext()),
            ((), {'width': 123}, nullcontext()),
            ((), {'width': 'string'}, pytest.raises(AssertionError)),
            ((), {'width': {'key': 123}}, pytest.raises(AssertionError)),
            ((), {'width': [1, 2, 3]}, pytest.raises(AssertionError)),
            ((), {'width': (1, 2, 3)}, pytest.raises(AssertionError)),
            ((), {'width': {1, 2, 3}}, pytest.raises(AssertionError)),
            ((), {'width': False}, nullcontext()),

            ((), {'anchor': tk.W}, nullcontext()),
            ((), {'anchor': tk.E}, nullcontext()),
            ((), {'anchor': tk.S}, nullcontext()),
            ((), {'anchor': tk.N}, nullcontext()),
            ((), {'anchor': 'se'}, nullcontext()),
            ((), {'anchor': 'sw'}, nullcontext()),
            ((), {'anchor': 'ne'}, nullcontext()),
            ((), {'anchor': 'nw'}, nullcontext()),
            ((), {'anchor': '12333'}, pytest.raises(AssertionError)),
            ((), {'anchor': 123}, pytest.raises(AssertionError)),
            ((), {'anchor': 'string'}, pytest.raises(AssertionError)),
            ((), {'anchor': {'key': 123}}, pytest.raises(AssertionError)),
            ((), {'anchor': [1, 2, 3]}, pytest.raises(AssertionError)),
            ((), {'anchor': (1, 2, 3)}, pytest.raises(AssertionError)),
            ((), {'anchor': {1, 2, 3}}, pytest.raises(AssertionError)),
            ((), {'anchor': False}, pytest.raises(AssertionError)),

            ((), {'padx': '12333'}, nullcontext()),
            ((), {'padx': 123}, nullcontext()),
            ((), {'padx': 'string'}, pytest.raises(AssertionError)),
            ((), {'padx': {'key': 123}}, pytest.raises(AssertionError)),
            ((), {'padx': [1, 2, 3]}, pytest.raises(AssertionError)),
            ((), {'padx': (1, 2, 3)}, pytest.raises(AssertionError)),
            ((), {'padx': {1, 2, 3}}, pytest.raises(AssertionError)),
            ((), {'padx': False}, nullcontext()),

            ((), {'pady': '12333'}, nullcontext()),
            ((), {'pady': 123}, nullcontext()),
            ((), {'pady': 'string'}, pytest.raises(AssertionError)),
            ((), {'pady': {'key': 123}}, pytest.raises(AssertionError)),
            ((), {'pady': [1, 2, 3]}, pytest.raises(AssertionError)),
            ((), {'pady': (1, 2, 3)}, pytest.raises(AssertionError)),
            ((), {'pady': {1, 2, 3}}, pytest.raises(AssertionError)),
            ((), {'pady': False}, nullcontext()),

            ((), {'value': False}, nullcontext()),
            ((), {'value': 'Value'}, nullcontext()),
            ((), {'value': 'True'}, nullcontext()),
            ((), {'value': 123}, nullcontext()),
            ((), {'value': [1, 2, 3]}, nullcontext()),
            ((), {'value': {1, 2, 3}}, nullcontext()),
            ((), {'value': {'value': False}}, nullcontext()),
            ((), {'value': ('value', False)}, nullcontext()),

            ((), {'variable': create_int_var()}, nullcontext()),
            ((), {'variable': False}, nullcontext()),
            ((), {'variable': 'Value'}, nullcontext()),
            ((), {'variable': 'True'}, nullcontext()),
            ((), {'variable': 123}, nullcontext()),
            ((), {'variable': [1, 2, 3]}, nullcontext()),
            ((), {'variable': {1, 2, 3}}, nullcontext()),
            ((), {'variable': {'value': False}}, nullcontext()),
            ((), {'variable': ('value', False)}, nullcontext()),
        ]
    )
    def test_create_radio_button(self, test_root, args, kwargs, expectation):
        with expectation:
            radio_btn = create_radio_button(test_root, *args, **kwargs)
            assert isinstance(radio_btn, tk.Radiobutton)
