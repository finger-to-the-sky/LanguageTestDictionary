from contextlib import nullcontext
import pytest
import tkinter as tk
from app.mode_functions.mode_window.listbox_worker.listbox_editor import ListBoxEditor
from app.tests.fixtures.test_mode_functions.listboxes_fixtures import test_editor


class TestListBoxEditor:

    @pytest.mark.parametrize(
        'master, is_red_test',
        [
            (tk.Tk(), False),
            (123, False),
            ('string', False),
            ({1, 2, 3}, False),
            ((1, 2, 3), False),
            ([], False),
            ([1, 2, 3], False),
            ({1: 2}, False),
            (None, False),
            (False, False),

            (tk.Tk(), 123),
            (tk.Tk(), 'string'),
            (tk.Tk(), {1, 2, 3}),
            (tk.Tk(), (1, 2, 3)),
            (tk.Tk(), []),
            (tk.Tk(), [1, 2, 3]),
            (tk.Tk(), {1: 2}),
            (tk.Tk(), None),

        ])
    def test_init_listbox_editor(self, master, is_red_test):
        with nullcontext():
            ListBoxEditor(master, is_red_test)

    def test_elements_init_listbox_editor(self, test_editor):
        with nullcontext():
            assert test_editor.edit_entry is None
            assert test_editor.confirm_button is None
            assert test_editor.delete_word_button is None
            assert test_editor.label_for_edit_win is None
            assert isinstance(test_editor.first_words_list_widget, tk.Listbox)
            assert isinstance(test_editor.second_words_list_widget, tk.Listbox)

    @pytest.mark.parametrize(
        "new_window, current_listbox, label_text",
        [
            (tk.Tk(), tk.Listbox(tk.Tk()), 'label'),
            (123, tk.Listbox(tk.Tk()), 'label'),
            ('string', tk.Listbox(tk.Tk()), 'label'),
            ({1, 2, 3}, tk.Listbox(tk.Tk()), 'label'),
            ((1, 2, 3), tk.Listbox(tk.Tk()), 'label'),
            ([], tk.Listbox(tk.Tk()), 'label'),
            ([1, 2, 3], tk.Listbox(tk.Tk()), 'label'),
            ({1: 2}, tk.Listbox(tk.Tk()), 'label'),
            (None, tk.Listbox(tk.Tk()), 'label'),
            (False, tk.Listbox(tk.Tk()), 'label'),

            (tk.Tk(), 123, 'label'),
            (tk.Tk(), 'string', 'label'),
            (tk.Tk(), {1, 2, 3}, 'label'),
            (tk.Tk(), (1, 2, 3), 'label'),
            (tk.Tk(), [], 'label'),
            (tk.Tk(), [1, 2, 3], 'label'),
            (tk.Tk(), {1: 2}, 'label'),
            (tk.Tk(), None, 'label'),
            (tk.Tk(), False, 'label'),
            (tk.Tk(), tk.Tk(), 'label'),

            (tk.Tk(), tk.Listbox(tk.Tk()), 123),
            (tk.Tk(), tk.Listbox(tk.Tk()), {1, 2, 3}),
            (tk.Tk(), tk.Listbox(tk.Tk()), (1, 2, 3)),
            (tk.Tk(), tk.Listbox(tk.Tk()), []),
            (tk.Tk(), tk.Listbox(tk.Tk()), [1, 2, 3]),
            (tk.Tk(), tk.Listbox(tk.Tk()), {1: 2}),
            (tk.Tk(), tk.Listbox(tk.Tk()), None),
            (tk.Tk(), tk.Listbox(tk.Tk()), False),
            (tk.Tk(), tk.Listbox(tk.Tk()), tk.Tk()),

        ]
    )
    def test_create_edit_window(self, test_editor, new_window, current_listbox, label_text):
        with nullcontext():
            test_editor.create_edit_window(new_window=new_window, current_listbox=current_listbox,
                                           label_text=label_text)
