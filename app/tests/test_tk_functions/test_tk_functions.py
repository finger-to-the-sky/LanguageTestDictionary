import tkinter as tk
import pytest
from app.config import PROJECT_DIR
from app.tk_functions import (create_image, create_label, create_ttk_combobox, create_entry,
                              create_listbox, create_frame, create_text_widget, create_ttk_treeview)
from tkinter import ttk
from contextlib import nullcontext
from app.tests.configurations import COLOR_GROUND_KEYS, FONT_KEYS
from app.tests.fixtures.test_root import test_root


class TestTkFunctions:
    CORRECT_IMAGE_PATH = f'{PROJECT_DIR}\\app\\other\\icons\\clear\\clear24.png'

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

            ((), {'textvariable': tk.StringVar()}, nullcontext()),
            ((), {'textvariable': 123}, nullcontext()),
            ((), {'textvariable': 'string'}, nullcontext()),
            ((), {'textvariable': {'key': 123}}, nullcontext()),
            ((), {'textvariable': [1, 2, 3]}, nullcontext()),
            ((), {'textvariable': (1, 2, 3)}, nullcontext()),
            ((), {'textvariable': {1, 2, 3}}, nullcontext()),
            ((), {'textvariable': False}, nullcontext()),
        ]
    )
    def test_create_label(self, test_root, args, kwargs, expectation):
        with expectation:
            label = create_label(test_root, *args, **kwargs)
            assert isinstance(label, tk.Label)

    @pytest.mark.parametrize(
        'args, kwargs, expectation', COLOR_GROUND_KEYS + FONT_KEYS + [

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
    def test_create_text_widget(self, test_root, args, kwargs, expectation):
        with expectation:
            text_widget = create_text_widget(test_root, *args, **kwargs)
            assert isinstance(text_widget, tk.Text)

    @pytest.mark.parametrize(
        'args, kwargs, expectation', COLOR_GROUND_KEYS + FONT_KEYS + [

            ((), {'selectbackground': 'blue'}, nullcontext()),
            ((), {'selectbackground': 123}, pytest.raises(AssertionError)),
            ((), {'selectbackground': 'string'}, pytest.raises(AssertionError)),
            ((), {'selectbackground': {'key': 123}}, pytest.raises(AssertionError)),
            ((), {'selectbackground': [1, 2, 3]}, pytest.raises(AssertionError)),
            ((), {'selectbackground': (1, 2, 3)}, pytest.raises(AssertionError)),
            ((), {'selectbackground': {1, 2, 3}}, pytest.raises(AssertionError)),
            ((), {'selectbackground': False}, pytest.raises(AssertionError)),

            ((), {'selectforeground': 'blue'}, nullcontext()),
            ((), {'selectforeground': 123}, pytest.raises(AssertionError)),
            ((), {'selectforeground': 'string'}, pytest.raises(AssertionError)),
            ((), {'selectforeground': [1, 2, 3]}, pytest.raises(AssertionError)),
            ((), {'selectforeground': (1, 2, 3)}, pytest.raises(AssertionError)),
            ((), {'selectforeground': {1, 2, 3}}, pytest.raises(AssertionError)),
            ((), {'selectforeground': False}, pytest.raises(AssertionError)),

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

            ((), {'selectmode': tk.SINGLE}, nullcontext()),
            ((), {'selectmode': tk.BROWSE}, nullcontext()),
            ((), {'selectmode': tk.MULTIPLE}, nullcontext()),
            ((), {'selectmode': tk.EXTENDED}, nullcontext()),
            ((), {'selectmode': 'single'}, nullcontext()),
            ((), {'selectmode': 'browse'}, nullcontext()),
            ((), {'selectmode': 'multiple'}, nullcontext()),
            ((), {'selectmode': 'extended'}, nullcontext()),
            ((), {'selectmode': 123}, nullcontext()),
            ((), {'selectmode': 'string'}, nullcontext()),
            ((), {'selectmode': {'key': 123}}, nullcontext()),
            ((), {'selectmode': [1, 2, 3]}, nullcontext()),
            ((), {'selectmode': (1, 2, 3)}, nullcontext()),
            ((), {'selectmode': {1, 2, 3}}, nullcontext()),
            ((), {'selectmode': False}, nullcontext()),
        ]
    )
    def test_create_listbox(self, test_root, args, kwargs, expectation):
        with expectation:
            listbox = create_listbox(test_root, *args, **kwargs)
            assert isinstance(listbox, tk.Listbox)

    @pytest.mark.parametrize(
        'args, kwargs, expectation', COLOR_GROUND_KEYS + FONT_KEYS + [
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
            ((), {'width': 'string'}, pytest.raises(AssertionError)),
            ((), {'width': {'key': 123}}, pytest.raises(AssertionError)),
            ((), {'width': [1, 2, 3]}, pytest.raises(AssertionError)),
            ((), {'width': (1, 2, 3)}, pytest.raises(AssertionError)),
            ((), {'width': {1, 2, 3}}, pytest.raises(AssertionError)),
            ((), {'width': False}, nullcontext()),
        ]
    )
    def test_create_entry(self, test_root, args, kwargs, expectation):
        with expectation:
            entry = create_entry(test_root, *args, **kwargs)
            assert isinstance(entry, tk.Entry)

    @pytest.mark.parametrize(
        'image_path, args, kwargs, expectation', [
            (CORRECT_IMAGE_PATH, (), {}, nullcontext()),
            (f'{PROJECT_DIR}\\app\\other\\icons\\clear\\unknown_image.png', (), {}, pytest.raises(AssertionError)),
            ([1, 2, 3], (), {}, pytest.raises(AssertionError)),
            ((1, 2, 3), (), {}, pytest.raises(AssertionError)),
            ({1, 2, 3}, (), {}, pytest.raises(AssertionError)),
            (123, (), {}, pytest.raises(AssertionError)),
            ('string', (), {}, pytest.raises(AssertionError)),
            ({'key': 123}, (), {}, pytest.raises(AssertionError)),
            (False, (), {}, pytest.raises(AssertionError)),

            (CORRECT_IMAGE_PATH, (), {'master': tk.Tk()}, nullcontext()),
            (CORRECT_IMAGE_PATH, (), {'master': tk.Frame(tk.Tk())}, nullcontext()),
            (CORRECT_IMAGE_PATH, (), {'master': 'root'}, pytest.raises(AssertionError)),
            (CORRECT_IMAGE_PATH, (), {'master': 123}, pytest.raises(AssertionError)),
            (CORRECT_IMAGE_PATH, (), {'master': (1, 2, 3)}, pytest.raises(AssertionError)),
            (CORRECT_IMAGE_PATH, (), {'master': {'test': 123}}, pytest.raises(AssertionError)),
            (CORRECT_IMAGE_PATH, (), {'master': ['test', 123]}, pytest.raises(AssertionError)),
            (CORRECT_IMAGE_PATH, (), {'master': {'test', 123}}, pytest.raises(AssertionError)),
            (CORRECT_IMAGE_PATH, (), {'master': False}, pytest.raises(AssertionError)),

            (CORRECT_IMAGE_PATH, (), {'height': '123213'}, nullcontext()),
            (CORRECT_IMAGE_PATH, (), {'height': 123}, nullcontext()),
            (CORRECT_IMAGE_PATH, (), {'height': 'string'}, pytest.raises(AssertionError)),
            (CORRECT_IMAGE_PATH, (), {'height': {'key': 123}}, pytest.raises(AssertionError)),
            (CORRECT_IMAGE_PATH, (), {'height': [1, 2, 3]}, pytest.raises(AssertionError)),
            (CORRECT_IMAGE_PATH, (), {'height': (1, 2, 3)}, pytest.raises(AssertionError)),
            (CORRECT_IMAGE_PATH, (), {'height': {1, 2, 3}}, pytest.raises(AssertionError)),
            (CORRECT_IMAGE_PATH, (), {'height': False}, nullcontext()),

            (CORRECT_IMAGE_PATH, (), {'width': '12333'}, nullcontext()),
            (CORRECT_IMAGE_PATH, (), {'width': 123}, nullcontext()),
            (CORRECT_IMAGE_PATH, (), {'width': 'string'}, pytest.raises(AssertionError)),
            (CORRECT_IMAGE_PATH, (), {'width': {'key': 123}}, pytest.raises(AssertionError)),
            (CORRECT_IMAGE_PATH, (), {'width': [1, 2, 3]}, pytest.raises(AssertionError)),
            (CORRECT_IMAGE_PATH, (), {'width': (1, 2, 3)}, pytest.raises(AssertionError)),
            (CORRECT_IMAGE_PATH, (), {'width': {1, 2, 3}}, pytest.raises(AssertionError)),
            (CORRECT_IMAGE_PATH, (), {'width': False}, nullcontext()),
        ]
    )
    def test_create_image(self, image_path, args, kwargs, expectation):
        with expectation:
            image = create_image(image_path, *args, **kwargs)
            assert isinstance(image, tk.PhotoImage)

    @pytest.mark.parametrize(
        'args, kwargs, expectation', [
            ((), {'background': 'blue'}, nullcontext()),
            ((), {'background': 123}, pytest.raises(AssertionError)),
            ((), {'background': 'string'}, pytest.raises(AssertionError)),
            ((), {'background': {'key': 123}}, pytest.raises(AssertionError)),
            ((), {'background': [1, 2, 3]}, pytest.raises(AssertionError)),
            ((), {'background': (1, 2, 3)}, pytest.raises(AssertionError)),
            ((), {'background': {1, 2, 3}}, pytest.raises(AssertionError)),
            ((), {'background': False}, pytest.raises(AssertionError)),

            ((), {'width': '12333'}, nullcontext()),
            ((), {'width': 123}, nullcontext()),
            ((), {'width': 'string'}, pytest.raises(AssertionError)),
            ((), {'width': {'key': 123}}, pytest.raises(AssertionError)),
            ((), {'width': [1, 2, 3]}, pytest.raises(AssertionError)),
            ((), {'width': (1, 2, 3)}, pytest.raises(AssertionError)),
            ((), {'width': {1, 2, 3}}, pytest.raises(AssertionError)),
            ((), {'width': False}, nullcontext()),
        ]
    )
    def test_create_frame(self, test_root, args, kwargs, expectation):
        with expectation:
            frame = create_frame(test_root, *args, **kwargs)
            assert isinstance(frame, tk.Frame)

    @pytest.mark.parametrize(
        'args, kwargs, expectation', FONT_KEYS + [
            ((), {'height': '123213'}, nullcontext()),
            ((), {'height': 123}, nullcontext()),
            ((), {'height': 'string'}, nullcontext()),
            ((), {'height': {'key': 123}}, nullcontext()),
            ((), {'height': [1, 2, 3]}, nullcontext()),
            ((), {'height': (1, 2, 3)}, nullcontext()),
            ((), {'height': {1, 2, 3}}, nullcontext()),
            ((), {'height': False}, nullcontext()),

            ((), {'width': '12333'}, nullcontext()),
            ((), {'width': 123}, nullcontext()),
            ((), {'width': 'string'}, pytest.raises(AssertionError)),
            ((), {'width': {'key': 123}}, pytest.raises(AssertionError)),
            ((), {'width': [1, 2, 3]}, pytest.raises(AssertionError)),
            ((), {'width': (1, 2, 3)}, pytest.raises(AssertionError)),
            ((), {'width': {1, 2, 3}}, pytest.raises(AssertionError)),
            ((), {'width': False}, nullcontext()),

            ((), {'values': '12333'}, nullcontext()),
            ((), {'values': 123}, nullcontext()),
            ((), {'values': 'string'}, nullcontext()),
            ((), {'values': {'key': 123}}, nullcontext()),
            ((), {'values': [1, 2, 3]}, nullcontext()),
            ((), {'values': (1, 2, 3)}, nullcontext()),
            ((), {'values': {1, 2, 3}}, nullcontext()),
            ((), {'values': False}, nullcontext()),
        ]
    )
    def test_create_ttk_combobox(self, test_root, args, kwargs, expectation):
        with expectation:
            combobox = create_ttk_combobox(test_root, *args, **kwargs)
            assert isinstance(combobox, ttk.Combobox)

    @pytest.mark.parametrize(
        'args, kwargs, expectation', [
            ((), {'columns': '12333'}, nullcontext()),
            ((), {'columns': 123}, nullcontext()),
            ((), {'columns': 'string'}, nullcontext()),
            ((), {'columns': {'key': 123}}, nullcontext()),
            ((), {'columns': [1, 2, 3]}, nullcontext()),
            ((), {'columns': (1, 2, 3)}, nullcontext()),
            ((), {'columns': {1, 2, 3}}, nullcontext()),
            ((), {'columns': False}, nullcontext()),

            ((), {'show': '12333'}, pytest.raises(AssertionError)),
            ((), {'show': 123}, pytest.raises(AssertionError)),
            ((), {'show': 'string'}, pytest.raises(AssertionError)),
            ((), {'show': {'key': 123}}, pytest.raises(AssertionError)),
            ((), {'show': [1, 2, 3]}, pytest.raises(AssertionError)),
            ((), {'show': (1, 2, 3)}, pytest.raises(AssertionError)),
            ((), {'show': {1, 2, 3}}, pytest.raises(AssertionError)),
            ((), {'show': False}, pytest.raises(AssertionError)),

            ((), {'selectmode': tk.BROWSE}, nullcontext()),
            ((), {'selectmode': tk.EXTENDED}, nullcontext()),
            ((), {'selectmode': 'browse'}, nullcontext()),
            ((), {'selectmode': 'extended'}, nullcontext()),
            ((), {'selectmode': tk.SINGLE}, pytest.raises(AssertionError)),
            ((), {'selectmode': tk.MULTIPLE}, pytest.raises(AssertionError)),
            ((), {'selectmode': 'single'}, pytest.raises(AssertionError)),
            ((), {'selectmode': 'multiple'}, pytest.raises(AssertionError)),
            ((), {'selectmode': 123}, pytest.raises(AssertionError)),
            ((), {'selectmode': 'string'}, pytest.raises(AssertionError)),
            ((), {'selectmode': {'key': 123}}, pytest.raises(AssertionError)),
            ((), {'selectmode': [1, 2, 3]}, pytest.raises(AssertionError)),
            ((), {'selectmode': (1, 2, 3)}, pytest.raises(AssertionError)),
            ((), {'selectmode': {1, 2, 3}}, pytest.raises(AssertionError)),
            ((), {'selectmode': False}, pytest.raises(AssertionError)),

            ((), {'height': '123213'}, nullcontext()),
            ((), {'height': 123}, nullcontext()),
            ((), {'height': 'string'}, pytest.raises(AssertionError)),
            ((), {'height': {'key': 123}}, pytest.raises(AssertionError)),
            ((), {'height': [1, 2, 3]}, pytest.raises(AssertionError)),
            ((), {'height': (1, 2, 3)}, pytest.raises(AssertionError)),
            ((), {'height': {1, 2, 3}}, pytest.raises(AssertionError)),
            ((), {'height': False}, nullcontext()),
        ]
    )
    def test_create_ttk_treeview(self, test_root, args, kwargs, expectation):
        with expectation:
            treeview = create_ttk_treeview(test_root, *args, **kwargs)
            assert isinstance(treeview, ttk.Treeview)
