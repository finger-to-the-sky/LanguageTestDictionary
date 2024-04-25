from contextlib import nullcontext

import pytest
import tkinter as tk
from app.fonts import FontManager
from app.mode_functions.mode_window.listbox_worker.listbox_editor import ListBoxEditor
from app.mode_functions.mode_window.mode_test_classes.mode_test_words_init import ModeTestWordsInit
from app.tests.configurations import INIT_TEST_MODE_CLASS
from app.tests.fixtures.test_mode_functions.mode_window_fixtures import mode_test_words_class


class TestInit:
    @pytest.mark.parametrize(
        'root, title, size_window, first_list, second_list, is_red_test',
        INIT_TEST_MODE_CLASS
    )
    def test_init_mode_words_class_init(self, root, title, size_window, first_list, second_list, is_red_test):
        with nullcontext():
            ModeTestWordsInit(root, title, size_window, first_list, second_list, is_red_test)

    def test_valid_components_from_init(self, mode_test_words_class):
        assert isinstance(mode_test_words_class.first_list, list)
        assert isinstance(mode_test_words_class.second_list, list)
        assert isinstance(mode_test_words_class.font, FontManager)
        assert isinstance(mode_test_words_class.window_mode, type(None))
        assert isinstance(mode_test_words_class.text_worker, type(None))
        assert isinstance(mode_test_words_class.is_visible_results, tk.BooleanVar)
        assert isinstance(mode_test_words_class.button_clicked, tk.BooleanVar)
        assert isinstance(mode_test_words_class.error, type(None))
        assert isinstance(mode_test_words_class.error_text, tk.StringVar)
        assert isinstance(mode_test_words_class.main_win_error, tk.BooleanVar)
        assert isinstance(mode_test_words_class.window, tk.Toplevel)
        assert isinstance(mode_test_words_class.frame, tk.Frame)
        assert isinstance(mode_test_words_class.words_worker, ListBoxEditor)


class TestModeTestWordsInit:
    TestCase = [
        ('TestText', tk.Tk(), nullcontext()),
        (123, tk.Tk(), nullcontext()),
        (tk.Tk(), tk.Tk(), nullcontext()),
        ({1, 2, 3}, tk.Tk(), nullcontext()),
        ((1, 2, 3), tk.Tk(), nullcontext()),
        ([], tk.Tk(), nullcontext()),
        ([1, 2, 3], tk.Tk(), nullcontext()),
        ({1: 2}, tk.Tk(), nullcontext()),
        (None, tk.Tk(), nullcontext()),
        (False, tk.Tk(), nullcontext()),

        ('TestText', 123, pytest.raises(AssertionError)),
        ('TestText', 'string', pytest.raises(AssertionError)),
        ('TestText', {1, 2, 3}, pytest.raises(AssertionError)),
        ('TestText', (1, 2, 3), pytest.raises(AssertionError)),
        ('TestText', [], pytest.raises(AssertionError)),
        ('TestText', [1, 2, 3], pytest.raises(AssertionError)),
        ('TestText', {1: 2}, pytest.raises(AssertionError)),
        ('TestText', None, nullcontext()),
        ('TestText', False, pytest.raises(AssertionError)),

    ]

    @pytest.mark.parametrize(
        'text, window, expectation',
        TestCase
    )
    def test_set_error(self, mode_test_words_class, text, window, expectation):
        with expectation:
            assert isinstance(mode_test_words_class.set_error(text, window=window), tk.Label)

    @pytest.mark.parametrize(
        'label_text, window, expectation',
        TestCase
    )
    def test_set_header(self, mode_test_words_class, label_text, window, expectation):
        with expectation:
            assert isinstance(mode_test_words_class.set_header(window=window, label_text=label_text), tk.Label)

    def test_create_window_mode(self, mode_test_words_class):
        with nullcontext():
            mode_test_words_class.create_window_mode()
            assert isinstance(mode_test_words_class.window_mode, tk.Toplevel)
