from app.tk_functions import create_boolean_var, create_string_var, create_int_var
from contextlib import nullcontext
from app.tests.configuration import ROOT_KEYS_VAR, create_test_root
import pytest
import tkinter as tk


class TestVariableFunctions:

    @pytest.mark.parametrize(
        'args, kwargs, expectation', ROOT_KEYS_VAR + [

            ((), {'master': create_test_root(), 'value': False}, nullcontext()),
            ((), {'master': create_test_root(), 'value': 'Value'}, pytest.raises(AssertionError)),
            ((), {'master': create_test_root(), 'value': 'True'}, nullcontext()),
            ((), {'master': create_test_root(), 'value': 123}, nullcontext()),
            ((), {'master': create_test_root(), 'value': [1, 2, 3]}, pytest.raises(AssertionError)),
            ((), {'master': create_test_root(), 'value': {1, 2, 3}}, pytest.raises(AssertionError)),
            ((), {'master': create_test_root(), 'value': {'value': False}}, pytest.raises(AssertionError)),
            ((), {'master': create_test_root(), 'value': ('value', False)}, pytest.raises(AssertionError)),

            ((), {'master': create_test_root(), 'name': 'bool'}, nullcontext()),
            ((), {'master': create_test_root(), 'name': 123}, pytest.raises(AssertionError)),
            ((), {'master': create_test_root(), 'name': {'bool', 123}}, pytest.raises(AssertionError)),
            ((), {'master': create_test_root(), 'name': [1, 2, 3]}, pytest.raises(AssertionError)),
            ((), {'master': create_test_root(), 'name': (1, 2, 3)}, pytest.raises(AssertionError)),
            ((), {'master': create_test_root(), 'name': {1, 2, 3}}, pytest.raises(AssertionError)),
            ((), {'master': create_test_root(), 'name': False}, pytest.raises(AssertionError)),
        ]
    )
    def test_create_boolean_var(self, args, kwargs, expectation):
        with expectation:
            boolean = create_boolean_var(*args, **kwargs)
            assert isinstance(boolean, tk.BooleanVar)

    @pytest.mark.parametrize(
        'args, kwargs, expectation', ROOT_KEYS_VAR + [

            ((), {'master': create_test_root(), 'value': False}, nullcontext()),
            ((), {'master': create_test_root(), 'value': 'Value'}, nullcontext()),
            ((), {'master': create_test_root(), 'value': 'True'}, nullcontext()),
            ((), {'master': create_test_root(), 'value': 123}, nullcontext()),
            ((), {'master': create_test_root(), 'value': [1, 2, 3]}, nullcontext()),
            ((), {'master': create_test_root(), 'value': {1, 2, 3}}, nullcontext()),
            ((), {'master': create_test_root(), 'value': {'value': False}}, nullcontext()),
            ((), {'master': create_test_root(), 'value': ('value', False)}, nullcontext()),

            ((), {'master': create_test_root(), 'name': 'bool'}, nullcontext()),
            ((), {'master': create_test_root(), 'name': 123}, pytest.raises(AssertionError)),
            ((), {'master': create_test_root(), 'name': {'bool', 123}}, pytest.raises(AssertionError)),
            ((), {'master': create_test_root(), 'name': [1, 2, 3]}, pytest.raises(AssertionError)),
            ((), {'master': create_test_root(), 'name': (1, 2, 3)}, pytest.raises(AssertionError)),
            ((), {'master': create_test_root(), 'name': {1, 2, 3}}, pytest.raises(AssertionError)),
            ((), {'master': create_test_root(), 'name': False}, pytest.raises(AssertionError)),
        ]
    )
    def test_create_string_var(self, args, kwargs, expectation):
        with expectation:
            string_var = create_string_var(*args, **kwargs)
            assert isinstance(string_var, tk.StringVar)

    @pytest.mark.parametrize(
        'args, kwargs, expectation', ROOT_KEYS_VAR + [

            ((), {'master': create_test_root(), 'value': False}, nullcontext()),
            ((), {'master': create_test_root(), 'value': 'Value'}, nullcontext()),
            ((), {'master': create_test_root(), 'value': 'True'}, nullcontext()),
            ((), {'master': create_test_root(), 'value': 123}, nullcontext()),
            ((), {'master': create_test_root(), 'value': [1, 2, 3]}, nullcontext()),
            ((), {'master': create_test_root(), 'value': {1, 2, 3}}, nullcontext()),
            ((), {'master': create_test_root(), 'value': {'value': False}}, nullcontext()),
            ((), {'master': create_test_root(), 'value': ('value', False)}, nullcontext()),

            ((), {'master': create_test_root(), 'name': 'bool'}, nullcontext()),
            ((), {'master': create_test_root(), 'name': 123}, pytest.raises(AssertionError)),
            ((), {'master': create_test_root(), 'name': {'bool', 123}}, pytest.raises(AssertionError)),
            ((), {'master': create_test_root(), 'name': [1, 2, 3]}, pytest.raises(AssertionError)),
            ((), {'master': create_test_root(), 'name': (1, 2, 3)}, pytest.raises(AssertionError)),
            ((), {'master': create_test_root(), 'name': {1, 2, 3}}, pytest.raises(AssertionError)),
            ((), {'master': create_test_root(), 'name': False}, pytest.raises(AssertionError)),
        ]
    )
    def test_create_int_var(self, args, kwargs, expectation):
        with expectation:
            int_var = create_int_var(*args, **kwargs)
            assert isinstance(int_var, tk.IntVar)
