import pytest
import tkinter as tk
from app.tests.configuration import ROOT_KEYS
from app.tk_functions import (create_label, create_ttk_combobox, create_entry, create_top_level,
                              create_listbox, create_frame, create_text_widget, create_ttk_treeview, create_button,
                              create_ttk_button, create_radio_button, create_boolean_var,
                              create_string_var, create_int_var)
from tkinter import ttk


@pytest.mark.parametrize(
    'root, args, kwargs, expectation', ROOT_KEYS
)
def test_root_functions(root, args, kwargs, expectation):
    with expectation:
        button = create_button(root, *args, **kwargs)
        ttk_button = create_ttk_button(root, *args, **kwargs)
        radio_button = create_radio_button(root, *args, **kwargs)
        boolean_var = create_boolean_var(root, *args, **kwargs)
        string_var = create_string_var(root, *args, **kwargs)
        int_var = create_int_var(root, *args, **kwargs)
        label = create_label(root, *args, **kwargs)
        ttk_combobox = create_ttk_combobox(root, *args, **kwargs)
        entry = create_entry(root, *args, **kwargs)
        top_level = create_top_level(root, *args, **kwargs)
        listbox = create_listbox(root, *args, **kwargs)
        frame = create_frame(root, *args, **kwargs)
        text_widget = create_text_widget(root, *args, **kwargs)
        ttk_treeview = create_ttk_treeview(root, *args, **kwargs)
        assert isinstance(button, tk.Button)
        assert isinstance(ttk_button, ttk.Button)
        assert isinstance(radio_button, tk.Radiobutton)
        assert isinstance(boolean_var, tk.BooleanVar)
        assert isinstance(string_var, tk.StringVar)
        assert isinstance(int_var, tk.IntVar)
        assert isinstance(label, tk.Label)
        assert isinstance(ttk_combobox, ttk.Combobox)
        assert isinstance(entry, tk.Entry)
        assert isinstance(top_level, tk.Toplevel)
        assert isinstance(listbox, tk.Listbox)
        assert isinstance(frame, tk.Frame)
        assert isinstance(text_widget, tk.Text)
        assert isinstance(ttk_treeview, ttk.Treeview)
