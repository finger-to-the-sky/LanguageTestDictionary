from app.config import PROJECT_DIR
from app.tk_functions import (create_image, create_label, create_ttk_combobox, create_entry, create_top_level,
                              create_listbox, create_frame, create_text_widget, create_ttk_treeview)
from tkinter import ttk
import tkinter as tk
import pytest
from contextlib import nullcontext
from app.tests.configuration import ROOT_KEYS, COLOR_GROUND_KEYS, FONT_KEYS, create_test_root


class TestTkFunctions:
    CORRECT_IMAGE_PATH = f'{PROJECT_DIR}\\app\\other\\icons\\clear\\clear24.png'

    @pytest.mark.parametrize(
        'root, args, kwargs, expectation',
        ROOT_KEYS
    )
    def test_create_top_level(self, root, args, kwargs, expectation):
        with expectation:
            toplevel = create_top_level(root)
            assert isinstance(toplevel, tk.Toplevel)

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

            (create_test_root(), (), {'textvariable': tk.StringVar()}, nullcontext()),
            (create_test_root(), (), {'textvariable': 123}, nullcontext()),
            (create_test_root(), (), {'textvariable': 'string'}, nullcontext()),
            (create_test_root(), (), {'textvariable': {'key': 123}}, nullcontext()),
            (create_test_root(), (), {'textvariable': [1, 2, 3]}, nullcontext()),
            (create_test_root(), (), {'textvariable': (1, 2, 3)}, nullcontext()),
            (create_test_root(), (), {'textvariable': {1, 2, 3}}, nullcontext()),
            (create_test_root(), (), {'textvariable': False}, nullcontext()),
        ]
    )
    def test_create_label(self, root, args, kwargs, expectation):
        with expectation:
            label = create_label(root, *args, **kwargs)
            assert isinstance(label, tk.Label)

    @pytest.mark.parametrize(
        'root, args, kwargs, expectation', ROOT_KEYS + COLOR_GROUND_KEYS + FONT_KEYS + [

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
    def test_create_text_widget(self, root, args, kwargs, expectation):
        with expectation:
            text_widget = create_text_widget(root, *args, **kwargs)
            assert isinstance(text_widget, tk.Text)

    @pytest.mark.parametrize(
        'root, args, kwargs, expectation', ROOT_KEYS + COLOR_GROUND_KEYS + FONT_KEYS + [

            (create_test_root(), (), {'selectbackground': 'blue'}, nullcontext()),
            (create_test_root(), (), {'selectbackground': 123}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'selectbackground': 'string'}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'selectbackground': {'key': 123}}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'selectbackground': [1, 2, 3]}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'selectbackground': (1, 2, 3)}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'selectbackground': {1, 2, 3}}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'selectbackground': False}, pytest.raises(AssertionError)),

            (create_test_root(), (), {'selectforeground': 'blue'}, nullcontext()),
            (create_test_root(), (), {'selectforeground': 123}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'selectforeground': 'string'}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'selectforeground': {'key': 123}}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'selectforeground': [1, 2, 3]}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'selectforeground': (1, 2, 3)}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'selectforeground': {1, 2, 3}}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'selectforeground': False}, pytest.raises(AssertionError)),

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

            (create_test_root(), (), {'selectmode': tk.SINGLE}, nullcontext()),
            (create_test_root(), (), {'selectmode': tk.BROWSE}, nullcontext()),
            (create_test_root(), (), {'selectmode': tk.MULTIPLE}, nullcontext()),
            (create_test_root(), (), {'selectmode': tk.EXTENDED}, nullcontext()),
            (create_test_root(), (), {'selectmode': 'single'}, nullcontext()),
            (create_test_root(), (), {'selectmode': 'browse'}, nullcontext()),
            (create_test_root(), (), {'selectmode': 'multiple'}, nullcontext()),
            (create_test_root(), (), {'selectmode': 'extended'}, nullcontext()),
            (create_test_root(), (), {'selectmode': 123}, nullcontext()),
            (create_test_root(), (), {'selectmode': 'string'}, nullcontext()),
            (create_test_root(), (), {'selectmode': {'key': 123}}, nullcontext()),
            (create_test_root(), (), {'selectmode': [1, 2, 3]}, nullcontext()),
            (create_test_root(), (), {'selectmode': (1, 2, 3)}, nullcontext()),
            (create_test_root(), (), {'selectmode': {1, 2, 3}}, nullcontext()),
            (create_test_root(), (), {'selectmode': False}, nullcontext()),
        ]
    )
    def test_create_listbox(self, root, args, kwargs, expectation):
        with expectation:
            listbox = create_listbox(root, *args, **kwargs)
            assert isinstance(listbox, tk.Listbox)

    @pytest.mark.parametrize(
        'root, args, kwargs, expectation', ROOT_KEYS + COLOR_GROUND_KEYS + FONT_KEYS + [
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
            (create_test_root(), (), {'width': 'string'}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'width': {'key': 123}}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'width': [1, 2, 3]}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'width': (1, 2, 3)}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'width': {1, 2, 3}}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'width': False}, nullcontext()),
        ]
    )
    def test_create_entry(self, root, args, kwargs, expectation):
        with expectation:
            entry = create_entry(root, *args, **kwargs)
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

            (CORRECT_IMAGE_PATH, (), {'master': create_test_root()}, nullcontext()),
            (CORRECT_IMAGE_PATH, (), {'master': tk.Frame(create_test_root())}, nullcontext()),
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
        'root, args, kwargs, expectation', ROOT_KEYS + [
            (create_test_root(), (), {'background': 'blue'}, nullcontext()),
            (create_test_root(), (), {'background': 123}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'background': 'string'}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'background': {'key': 123}}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'background': [1, 2, 3]}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'background': (1, 2, 3)}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'background': {1, 2, 3}}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'background': False}, pytest.raises(AssertionError)),

            (create_test_root(), (), {'width': '12333'}, nullcontext()),
            (create_test_root(), (), {'width': 123}, nullcontext()),
            (create_test_root(), (), {'width': 'string'}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'width': {'key': 123}}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'width': [1, 2, 3]}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'width': (1, 2, 3)}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'width': {1, 2, 3}}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'width': False}, nullcontext()),
        ]
    )
    def test_create_frame(self, root, args, kwargs, expectation):
        with expectation:
            frame = create_frame(root, *args, **kwargs)
            assert isinstance(frame, tk.Frame)

    @pytest.mark.parametrize(
        'root, args, kwargs, expectation', ROOT_KEYS + FONT_KEYS + [
            (create_test_root(), (), {'height': '123213'}, nullcontext()),
            (create_test_root(), (), {'height': 123}, nullcontext()),
            (create_test_root(), (), {'height': 'string'}, nullcontext()),
            (create_test_root(), (), {'height': {'key': 123}}, nullcontext()),
            (create_test_root(), (), {'height': [1, 2, 3]}, nullcontext()),
            (create_test_root(), (), {'height': (1, 2, 3)}, nullcontext()),
            (create_test_root(), (), {'height': {1, 2, 3}}, nullcontext()),
            (create_test_root(), (), {'height': False}, nullcontext()),

            (create_test_root(), (), {'width': '12333'}, nullcontext()),
            (create_test_root(), (), {'width': 123}, nullcontext()),
            (create_test_root(), (), {'width': 'string'}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'width': {'key': 123}}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'width': [1, 2, 3]}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'width': (1, 2, 3)}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'width': {1, 2, 3}}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'width': False}, nullcontext()),

            (create_test_root(), (), {'values': '12333'}, nullcontext()),
            (create_test_root(), (), {'values': 123}, nullcontext()),
            (create_test_root(), (), {'values': 'string'}, nullcontext()),
            (create_test_root(), (), {'values': {'key': 123}}, nullcontext()),
            (create_test_root(), (), {'values': [1, 2, 3]}, nullcontext()),
            (create_test_root(), (), {'values': (1, 2, 3)}, nullcontext()),
            (create_test_root(), (), {'values': {1, 2, 3}}, nullcontext()),
            (create_test_root(), (), {'values': False}, nullcontext()),
        ]
    )
    def test_create_ttk_combobox(self, root, args, kwargs, expectation):
        with expectation:
            combobox = create_ttk_combobox(root, *args, **kwargs)
            assert isinstance(combobox, ttk.Combobox)

    @pytest.mark.parametrize(
        'root, args, kwargs, expectation', ROOT_KEYS + [
            (create_test_root(), (), {'columns': '12333'}, nullcontext()),
            (create_test_root(), (), {'columns': 123}, nullcontext()),
            (create_test_root(), (), {'columns': 'string'}, nullcontext()),
            (create_test_root(), (), {'columns': {'key': 123}}, nullcontext()),
            (create_test_root(), (), {'columns': [1, 2, 3]}, nullcontext()),
            (create_test_root(), (), {'columns': (1, 2, 3)}, nullcontext()),
            (create_test_root(), (), {'columns': {1, 2, 3}}, nullcontext()),
            (create_test_root(), (), {'columns': False}, nullcontext()),

            (create_test_root(), (), {'show': '12333'}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'show': 123}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'show': 'string'}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'show': {'key': 123}}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'show': [1, 2, 3]}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'show': (1, 2, 3)}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'show': {1, 2, 3}}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'show': False}, pytest.raises(AssertionError)),

            (create_test_root(), (), {'selectmode': tk.BROWSE}, nullcontext()),
            (create_test_root(), (), {'selectmode': tk.EXTENDED}, nullcontext()),
            (create_test_root(), (), {'selectmode': 'browse'}, nullcontext()),
            (create_test_root(), (), {'selectmode': 'extended'}, nullcontext()),
            (create_test_root(), (), {'selectmode': tk.SINGLE}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'selectmode': tk.MULTIPLE}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'selectmode': 'single'}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'selectmode': 'multiple'}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'selectmode': 123}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'selectmode': 'string'}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'selectmode': {'key': 123}}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'selectmode': [1, 2, 3]}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'selectmode': (1, 2, 3)}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'selectmode': {1, 2, 3}}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'selectmode': False}, pytest.raises(AssertionError)),

            (create_test_root(), (), {'height': '123213'}, nullcontext()),
            (create_test_root(), (), {'height': 123}, nullcontext()),
            (create_test_root(), (), {'height': 'string'}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'height': {'key': 123}}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'height': [1, 2, 3]}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'height': (1, 2, 3)}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'height': {1, 2, 3}}, pytest.raises(AssertionError)),
            (create_test_root(), (), {'height': False}, nullcontext()),
        ]
    )
    def test_create_ttk_treeview(self, root, args, kwargs, expectation):
        with expectation:
            treeview = create_ttk_treeview(root, *args, **kwargs)
            assert isinstance(treeview, ttk.Treeview)
