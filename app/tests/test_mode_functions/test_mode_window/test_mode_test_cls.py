from contextlib import nullcontext
import pytest
import tkinter as tk
from app.mode_functions.mode_window.mode_test_classes.mode_test_cls import ModeTestWordsClass
from app.tests.configurations import INIT_TEST_MODE_CLASS
from app.tests.fixtures.test_mode_functions.mode_window_fixtures import mode_test_class


class TestModeTestClass:
    FIRST_LIST = ['hello', 'cat', 'egg', 'book']
    SECOND_LIST = ['здраствуйте', "кот", 'яйцо', 'книга']
    USER_LIST_WORDS = {'correct': ['cat', 'human'], 'incorrect': {'user_word': ['rivor'], 'incorrect_word': ['река'],
                                                                  'correct_answer': ['river']}}

    @pytest.mark.parametrize('root, title, size_window, first_list, second_list, is_red_test',
                             INIT_TEST_MODE_CLASS)
    def test_init_test_mode_class(self, root, title, size_window, first_list, second_list, is_red_test):
        with nullcontext():
            ModeTestWordsClass(root, title, size_window, first_list, second_list, is_red_test)

    def test_init_components(self, mode_test_class):
        with nullcontext():
            assert isinstance(mode_test_class.clear_btn, tk.Button)
            assert isinstance(mode_test_class.start_btn, tk.Button)

    @pytest.mark.parametrize(
        'check_word, user_text',
        [
            ('hello', 'здраствуйте'),
            (123, 'здраствуйте'),
            ('string', 'здраствуйте'),
            ({1, 2, 3}, 'здраствуйте'),
            ((1, 2, 3), 'здраствуйте'),
            ([], 'здраствуйте'),
            ([1, 2, 3], 'здраствуйте'),
            ({1: 2}, 'здраствуйте'),
            (None, 'здраствуйте'),
            (False, 'здраствуйте'),
            (tk.Tk(), 'здраствуйте'),
            ('hello', 123),
            ('hello', 'string'),
            ('hello', {1, 2, 3}),
            ('hello', (1, 2, 3)),
            ('hello', []),
            ('hello', [1, 2, 3]),
            ('hello', {1: 2}),
            ('hello', None),
            ('hello', False),
            ('hello', tk.Tk()),
        ]
    )
    def test_check_correct_answer(self, mode_test_class, check_word, user_text):
        with nullcontext():
            mode_test_class.first_list = self.FIRST_LIST
            mode_test_class.second_list = self.SECOND_LIST
            mode_test_class.check_correct_answer(check_word=check_word, user_text=user_text)

    @pytest.mark.parametrize(
        'column_name, current_list, selectmode',
        [
            ('Correct', ['first', 'second', 'third'], 'browse'),
            (123, ['first', 'second', 'third'], 'browse'),
            ('string', ['first', 'second', 'third'], 'browse'),
            ({1, 2, 3}, ['first', 'second', 'third'], 'browse'),
            ((1, 2, 3), ['first', 'second', 'third'], 'browse'),
            ([], ['first', 'second', 'third'], 'browse'),
            ([1, 2, 3], ['first', 'second', 'third'], 'browse'),
            ({1: 2}, ['first', 'second', 'third'], 'browse'),
            (None, ['first', 'second', 'third'], 'browse'),
            (False, ['first', 'second', 'third'], 'browse'),
            (tk.Tk(), ['first', 'second', 'third'], 'browse'),

            ('Correct', 123, 'browse'),
            ('Correct', 'string', 'browse'),
            ('Correct', {1, 2, 3}, 'browse'),
            ('Correct', (1, 2, 3), 'browse'),
            ('Correct', [], 'browse'),
            ('Correct', [1, 2, 3], 'browse'),
            ('Correct', {1: 2}, 'browse'),
            ('Correct', None, 'browse'),
            ('Correct', False, 'browse'),
            ('Correct', tk.Tk(), 'browse'),

            ('Correct', ['first', 'second', 'third'], 123),
            ('Correct', ['first', 'second', 'third'], 'string'),
            ('Correct', ['first', 'second', 'third'], {1, 2, 3}),
            ('Correct', ['first', 'second', 'third'], (1, 2, 3)),
            ('Correct', ['first', 'second', 'third'], []),
            ('Correct', ['first', 'second', 'third'], [1, 2, 3]),
            ('Correct', ['first', 'second', 'third'], {1: 2}),
            ('Correct', ['first', 'second', 'third'], None),
            ('Correct', ['first', 'second', 'third'], False),
            ('Correct', ['first', 'second', 'third'], tk.Tk()),
        ]
    )
    def test_create_table(self, mode_test_class, column_name, current_list, selectmode):
        with nullcontext():
            mode_test_class.create_table(column_name=column_name, current_list=current_list, selectmode=selectmode)

    def test_clear_user_answers_list(self, mode_test_class):
        with nullcontext():
            mode_test_class.USER_LIST_WORDS = self.USER_LIST_WORDS
            mode_test_class.clear_user_answers_list()
            assert mode_test_class.USER_LIST_WORDS['correct'] == []
            assert mode_test_class.USER_LIST_WORDS['incorrect']['user_word'] == []
            assert mode_test_class.USER_LIST_WORDS['incorrect']['incorrect_word'] == []
            assert mode_test_class.USER_LIST_WORDS['incorrect']['correct_answer'] == []
