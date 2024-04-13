from app.tk_functions import create_boolean_var, create_string_var, create_int_var
from contextlib import nullcontext
from app.tests.configurations import ROOT_KEYS_VAR
import pytest
import tkinter as tk


class TestVariableFunctions:

    @pytest.mark.parametrize(
        'args, kwargs, expectation', ROOT_KEYS_VAR + [

            ((), {'value': False}, nullcontext()),
            ((), {'value': 'Value'}, pytest.raises(AssertionError)),
            ((), {'value': 'True'}, nullcontext()),
            ((), {'value': 123}, nullcontext()),
            ((), {'value': [1, 2, 3]}, pytest.raises(AssertionError)),
            ((), {'value': {1, 2, 3}}, pytest.raises(AssertionError)),
            ((), {'value': {'value': False}}, pytest.raises(AssertionError)),
            ((), {'value': ('value', False)}, pytest.raises(AssertionError)),

            ((), {'name': 'bool'}, nullcontext()),
            ((), {'name': 123}, pytest.raises(AssertionError)),
            ((), {'name': {'bool', 123}}, pytest.raises(AssertionError)),
            ((), {'name': [1, 2, 3]}, pytest.raises(AssertionError)),
            ((), {'name': (1, 2, 3)}, pytest.raises(AssertionError)),
            ((), {'name': {1, 2, 3}}, pytest.raises(AssertionError)),
            ((), {'name': False}, pytest.raises(AssertionError)),
        ]
    )
    def test_create_boolean_var(self, args, kwargs, expectation):
        with expectation:
            boolean = create_boolean_var(*args, **kwargs)
            assert isinstance(boolean, tk.BooleanVar)

    @pytest.mark.parametrize(
        'args, kwargs, expectation', ROOT_KEYS_VAR + [

            ((), {'value': False}, nullcontext()),
            ((), {'value': 'Value'}, nullcontext()),
            ((), {'value': 'True'}, nullcontext()),
            ((), {'value': 123}, nullcontext()),
            ((), {'value': [1, 2, 3]}, nullcontext()),
            ((), {'value': {1, 2, 3}}, nullcontext()),
            ((), {'value': {'value': False}}, nullcontext()),
            ((), {'value': ('value', False)}, nullcontext()),

            ((), {'name': 'bool'}, nullcontext()),
            ((), {'name': 123}, pytest.raises(AssertionError)),
            ((), {'name': {'bool', 123}}, pytest.raises(AssertionError)),
            ((), {'name': [1, 2, 3]}, pytest.raises(AssertionError)),
            ((), {'name': (1, 2, 3)}, pytest.raises(AssertionError)),
            ((), {'name': {1, 2, 3}}, pytest.raises(AssertionError)),
            ((), {'name': False}, pytest.raises(AssertionError)),
        ]
    )
    def test_create_string_var(self, args, kwargs, expectation):
        with expectation:
            string_var = create_string_var(*args, **kwargs)
            assert isinstance(string_var, tk.StringVar)

    @pytest.mark.parametrize(
        'args, kwargs, expectation', ROOT_KEYS_VAR + [

            ((), {'value': False}, nullcontext()),
            ((), {'value': 'Value'}, nullcontext()),
            ((), {'value': 'True'}, nullcontext()),
            ((), {'value': 123}, nullcontext()),
            ((), {'value': [1, 2, 3]}, nullcontext()),
            ((), {'value': {1, 2, 3}}, nullcontext()),
            ((), {'value': {'value': False}}, nullcontext()),
            ((), {'value': ('value', False)}, nullcontext()),

            ((), {'name': 'bool'}, nullcontext()),
            ((), {'name': 123}, pytest.raises(AssertionError)),
            ((), {'name': {'bool', 123}}, pytest.raises(AssertionError)),
            ((), {'name': [1, 2, 3]}, pytest.raises(AssertionError)),
            ((), {'name': (1, 2, 3)}, pytest.raises(AssertionError)),
            ((), {'name': {1, 2, 3}}, pytest.raises(AssertionError)),
            ((), {'name': False}, pytest.raises(AssertionError)),
        ]
    )
    def test_create_int_var(self, args, kwargs, expectation):
        with expectation:
            int_var = create_int_var(*args, **kwargs)
            assert isinstance(int_var, tk.IntVar)
