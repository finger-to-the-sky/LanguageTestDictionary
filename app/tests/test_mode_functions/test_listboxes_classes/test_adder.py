from contextlib import nullcontext

import pytest
import tkinter as tk
from app.mode_functions.mode_window.listbox_worker.adder import ListBoxAdderClass
from app.tests.fixtures.test_mode_functions.listboxes_fixtures import test_listbox_adder


class TestListboxAdder:
    TEST_ENTRY = tk.Entry(tk.Tk())
    TEST_ENTRY.insert(0, 'v')

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
    def test_init_listbox_adder(self, master, is_red_test):
        with nullcontext():
            ListBoxAdderClass(master=master, is_red_test=is_red_test)

    def test_init_elements_listbox_adder(self, test_listbox_adder):
        with nullcontext():
            assert isinstance(test_listbox_adder.window_is_active, tk.BooleanVar)
            assert isinstance(test_listbox_adder.first_label, tk.Label)
            assert isinstance(test_listbox_adder.second_label, tk.Label)
            assert isinstance(test_listbox_adder.first_words_list_widget, tk.Listbox)
            assert isinstance(test_listbox_adder.second_words_list_widget, tk.Listbox)
            assert isinstance(test_listbox_adder.frame, tk.Frame)
            assert isinstance(test_listbox_adder.add_word_btn, tk.Button)

    def test_check_len_list(self, test_listbox_adder):
        with nullcontext():
            test_listbox_adder.SECOND_LANGUAGE_LIST = [i for i in range(200)]

            assert test_listbox_adder.check_len_list() == (False, 'Вы не можете добавить больше 100 слов!')
            test_listbox_adder.SECOND_LANGUAGE_LIST = [i for i in range(25)]
            test_listbox_adder.is_red_test = True
            assert test_listbox_adder.check_len_list() == (True,)

    @pytest.mark.parametrize(
        'text, window, error_status, expectation',
        [
            ('Error', tk.Tk(), tk.BooleanVar(value=False), nullcontext()),
            ({1, 2, 3}, tk.Tk(), tk.BooleanVar(value=False), nullcontext()),
            ((1, 2, 3), tk.Tk(), tk.BooleanVar(value=False), nullcontext()),
            ([], tk.Tk(), tk.BooleanVar(value=False), nullcontext()),
            ([1, 2, 3], tk.Tk(), tk.BooleanVar(value=False), nullcontext()),
            ({1: 2}, tk.Tk(), tk.BooleanVar(value=False), nullcontext()),
            (None, tk.Tk(), tk.BooleanVar(value=False), nullcontext()),
            (False, tk.Tk(), tk.BooleanVar(value=False), nullcontext()),
            (tk.Tk(), tk.Tk(), tk.BooleanVar(value=False), nullcontext()),

            ('Error', 123, tk.BooleanVar(value=False), pytest.raises(AssertionError)),
            ('Error', 'string', tk.BooleanVar(value=False), pytest.raises(AssertionError)),
            ('Error', {1, 2, 3}, tk.BooleanVar(value=False), pytest.raises(AssertionError)),
            ('Error', (1, 2, 3), tk.BooleanVar(value=False), pytest.raises(AssertionError)),
            ('Error', [], tk.BooleanVar(value=False), pytest.raises(AssertionError)),
            ('Error', [1, 2, 3], tk.BooleanVar(value=False), pytest.raises(AssertionError)),
            ('Error', {1: 2}, tk.BooleanVar(value=False), pytest.raises(AssertionError)),
            ('Error', False, tk.BooleanVar(value=False), pytest.raises(AssertionError)),

            ('Error', tk.Tk(), 123, pytest.raises(AssertionError)),
            ('Error', tk.Tk(), 'string', pytest.raises(AssertionError)),
            ('Error', tk.Tk(), {1, 2, 3}, pytest.raises(AssertionError)),
            ('Error', tk.Tk(), (1, 2, 3), pytest.raises(AssertionError)),
            ('Error', tk.Tk(), [], pytest.raises(AssertionError)),
            ('Error', tk.Tk(), [1, 2, 3], pytest.raises(AssertionError)),
            ('Error', tk.Tk(), {1: 2}, pytest.raises(AssertionError)),
            ('Error', tk.Tk(), None, pytest.raises(AssertionError)),
            ('Error', tk.Tk(), tk.Tk(), pytest.raises(AssertionError)),

        ]
    )
    def test_set_error(self, test_listbox_adder, text, window, error_status, expectation):
        with expectation:
            error = test_listbox_adder.set_error(text=text, window=window, error_status=error_status)
            assert isinstance(error, tk.Label)

    def test_clear_error(self, test_listbox_adder):
        with nullcontext():
            test_listbox_adder.set_error(text='error', window=tk.Tk(), error_status=test_listbox_adder.error)
            assert test_listbox_adder.error.get() is True
            test_listbox_adder.clear_error()
            assert test_listbox_adder.error.get() is False

    def test_check_err(self, test_listbox_adder):
        with nullcontext():
            test_listbox_adder.error_add_win.set(True)
            assert test_listbox_adder.create_new_window(root=tk.Tk(), geometry='800x600', title='title') is None

    @pytest.mark.parametrize(
        'root, geometry, title, expectation',
        [
            (tk.Tk(), '800x600', 'test_title', nullcontext()),
            (123, '800x600', 'test_title', pytest.raises(AssertionError)),
            ('string', '800x600', 'test_title', pytest.raises(AssertionError)),
            ({1, 2, 3}, '800x600', 'test_title', pytest.raises(AssertionError)),
            ((1, 2, 3), '800x600', 'test_title', pytest.raises(AssertionError)),
            ([], '800x600', 'test_title', pytest.raises(AssertionError)),
            ([1, 2, 3], '800x600', 'test_title', pytest.raises(AssertionError)),
            ({1: 2}, '800x600', 'test_title', pytest.raises(AssertionError)),
            (None, '800x600', 'test_title', nullcontext()),
            (False, '800x600', 'test_title', pytest.raises(AssertionError)),

            (tk.Tk(), 123, 'test_title', pytest.raises(AssertionError)),
            (tk.Tk(), 'string', 'test_title', pytest.raises(AssertionError)),
            (tk.Tk(), {1, 2, 3}, 'test_title', pytest.raises(AssertionError)),
            (tk.Tk(), (1, 2, 3), 'test_title', pytest.raises(AssertionError)),
            (tk.Tk(), [], 'test_title', nullcontext()),
            (tk.Tk(), [1, 2, 3], 'test_title', pytest.raises(AssertionError)),
            (tk.Tk(), {1: 2}, 'test_title', pytest.raises(AssertionError)),
            (tk.Tk(), None, 'test_title', nullcontext()),
            (tk.Tk(), False, 'test_title', pytest.raises(AssertionError)),
            (tk.Tk(), tk.Tk(), 'test_title', pytest.raises(AssertionError)),

            (tk.Tk(), '800x600', 123, nullcontext()),
            (tk.Tk(), '800x600', 'string', nullcontext()),
            (tk.Tk(), '800x600', {1, 2, 3}, nullcontext()),
            (tk.Tk(), '800x600', (1, 2, 3), nullcontext()),
            (tk.Tk(), '800x600', [], nullcontext()),
            (tk.Tk(), '800x600', [1, 2, 3], nullcontext()),
            (tk.Tk(), '800x600', {1: 2}, nullcontext()),
            (tk.Tk(), '800x600', None, nullcontext()),
            (tk.Tk(), '800x600', False, nullcontext()),
            (tk.Tk(), '800x600', tk.Tk(), nullcontext()),

        ]
    )
    def test_create_new_window(self, test_listbox_adder, root, geometry, title, expectation):
        with expectation:
            assert isinstance(test_listbox_adder.create_new_window(root=root, geometry=geometry, title=title),
                              tk.Toplevel)

    @pytest.mark.skip(reason='In this test, confirmation is required on the messagebox.')
    @pytest.mark.parametrize(
        'window, title, message',
        [
            (tk.Tk(), 'title', 'message'),
            (123, 'title', 'message'),
            ('string', 'title', 'message'),
            ({1, 2, 3}, 'title', 'message'),
            ((1, 2, 3), 'title', 'message'),
            ([], 'title', 'message'),
            ([1, 2, 3], 'title', 'message'),
            ({1: 2}, 'title', 'message'),
            (None, 'title', 'message'),
            (False, 'title', 'message'),

            (tk.Tk(), 123, 'message'),
            (tk.Tk(), {1, 2, 3}, 'message'),
            (tk.Tk(), (1, 2, 3), 'message'),
            (tk.Tk(), [], 'message'),
            (tk.Tk(), [1, 2, 3], 'message'),
            (tk.Tk(), {1: 2}, 'message'),
            (tk.Tk(), None, 'message'),
            (tk.Tk(), False, 'message'),
            (tk.Tk(), tk.Tk(), 'message'),

            (tk.Tk(), 'title', 123),
            (tk.Tk(), 'title', {1, 2, 3}),
            (tk.Tk(), 'title', (1, 2, 3)),
            (tk.Tk(), 'title', []),
            (tk.Tk(), 'title', [1, 2, 3]),
            (tk.Tk(), 'title', {1: 2}),
            (tk.Tk(), 'title', None),
            (tk.Tk(), 'title', False),
            (tk.Tk(), 'title', tk.Tk()),

        ]
    )
    def test_confirm_cancel(self, test_listbox_adder, window, title, message):
        with nullcontext():
            test_listbox_adder.confirm_cancel(window, title=title, message=message)

    @pytest.mark.parametrize(
        'word_widget, current_list, current_window',
        [
            (TEST_ENTRY, ['a', 'b', 'c'], tk.Tk()),
            (123, ['a', 'b', 'c'], tk.Tk()),
            ('string', ['a', 'b', 'c'], tk.Tk()),
            ({1, 2, 3}, ['a', 'b', 'c'], tk.Tk()),
            ((1, 2, 3), ['a', 'b', 'c'], tk.Tk()),
            ([], ['a', 'b', 'c'], tk.Tk()),
            ([1, 2, 3], ['a', 'b', 'c'], tk.Tk()),
            ({1: 2}, ['a', 'b', 'c'], tk.Tk()),
            (None, ['a', 'b', 'c'], tk.Tk()),
            (False, ['a', 'b', 'c'], tk.Tk()),
            (tk.Tk(), ['a', 'b', 'c'], tk.Tk()),

            (TEST_ENTRY, 123, tk.Tk()),
            (TEST_ENTRY, 'string', tk.Tk()),
            (TEST_ENTRY, {1, 2, 3}, tk.Tk()),
            (TEST_ENTRY, (1, 2, 3), tk.Tk()),
            (TEST_ENTRY, [], tk.Tk()),
            (TEST_ENTRY, [1, 2, 3], tk.Tk()),
            (TEST_ENTRY, {1: 2}, tk.Tk()),
            (TEST_ENTRY, None, tk.Tk()),
            (TEST_ENTRY, False, tk.Tk()),
            (TEST_ENTRY, tk.Tk(), tk.Tk()),

            (TEST_ENTRY, ['a', 'b', 'c'], 123),
            (TEST_ENTRY, ['a', 'b', 'c'], 'string'),
            (TEST_ENTRY, ['a', 'b', 'c'], {1, 2, 3}),
            (TEST_ENTRY, ['a', 'b', 'c'], (1, 2, 3)),
            (TEST_ENTRY, ['a', 'b', 'c'], []),
            (TEST_ENTRY, ['a', 'b', 'c'], [1, 2, 3]),
            (TEST_ENTRY, ['a', 'b', 'c'], {1: 2}),
            (TEST_ENTRY, ['a', 'b', 'c'], None),
            (TEST_ENTRY, ['a', 'b', 'c'], False),
            (TEST_ENTRY, ['a', 'b', 'c'], tk.Tk()),

        ]
    )
    def test_add_word_to_list(self, test_listbox_adder, word_widget, current_list, current_window):
        with nullcontext():
            test_listbox_adder.add_word_to_list(word_widget=word_widget, current_list=current_list,
                                                current_window=current_window)
            self.TEST_ENTRY.insert(0, 'v')

    @pytest.mark.parametrize(
        'new_window, label_text, words_list, is_second',
        [
            (tk.Toplevel(tk.Tk()), 'test_label', ['a', 'b', 'c'], False),
            (123, 'test_label', ['a', 'b', 'c'], False),
            ('string', 'test_label', ['a', 'b', 'c'], False),
            ({1, 2, 3}, 'test_label', ['a', 'b', 'c'], False),
            ((1, 2, 3), 'test_label', ['a', 'b', 'c'], False),
            ([], 'test_label', ['a', 'b', 'c'], False),
            ([1, 2, 3], 'test_label', ['a', 'b', 'c'], False),
            ({1: 2}, 'test_label', ['a', 'b', 'c'], False),
            (None, 'test_label', ['a', 'b', 'c'], False),
            (False, 'test_label', ['a', 'b', 'c'], False),
            (tk.Tk(), 'test_label', ['a', 'b', 'c'], False),

            (tk.Toplevel(tk.Tk()), 123, ['a', 'b', 'c'], False),
            (tk.Toplevel(tk.Tk()), {1, 2, 3}, ['a', 'b', 'c'], False),
            (tk.Toplevel(tk.Tk()), (1, 2, 3), ['a', 'b', 'c'], False),
            (tk.Toplevel(tk.Tk()), [], ['a', 'b', 'c'], False),
            (tk.Toplevel(tk.Tk()), [1, 2, 3], ['a', 'b', 'c'], False),
            (tk.Toplevel(tk.Tk()), {1: 2}, ['a', 'b', 'c'], False),
            (tk.Toplevel(tk.Tk()), None, ['a', 'b', 'c'], False),
            (tk.Toplevel(tk.Tk()), False, ['a', 'b', 'c'], False),
            (tk.Toplevel(tk.Tk()), tk.Tk(), ['a', 'b', 'c'], False),

            (tk.Toplevel(tk.Tk()), 'test_label', ['a', 'b', 'c'], 123),
            (tk.Toplevel(tk.Tk()), 'test_label', ['a', 'b', 'c'], 'string'),
            (tk.Toplevel(tk.Tk()), 'test_label', ['a', 'b', 'c'], {1, 2, 3}),
            (tk.Toplevel(tk.Tk()), 'test_label', ['a', 'b', 'c'], (1, 2, 3)),
            (tk.Toplevel(tk.Tk()), 'test_label', ['a', 'b', 'c'], []),
            (tk.Toplevel(tk.Tk()), 'test_label', ['a', 'b', 'c'], [1, 2, 3]),
            (tk.Toplevel(tk.Tk()), 'test_label', ['a', 'b', 'c'], {1: 2}),
            (tk.Toplevel(tk.Tk()), 'test_label', ['a', 'b', 'c'], None),
            (tk.Toplevel(tk.Tk()), 'test_label', ['a', 'b', 'c'], False),
            (tk.Toplevel(tk.Tk()), 'test_label', ['a', 'b', 'c'], tk.Tk()),
        ]
    )
    def test_create_add_window(self, test_listbox_adder, new_window, label_text, words_list, is_second):
        with nullcontext():
            test_listbox_adder.create_add_window(new_window=new_window, label_text=label_text, words_list=words_list,
                                                 is_second=is_second)

    def test_add_to_listwords(self, test_listbox_adder):
        with nullcontext():
            test_listbox_adder.add_word_to_listwords()
            assert test_listbox_adder.window_is_active.get() is True

    def test_update_listboxes(self, test_listbox_adder):
        with nullcontext():
            test_listbox_adder.FIRST_LANGUAGE_LIST = [1, 2, 3]
            test_listbox_adder.SECOND_LANGUAGE_LIST = [1, 2, 3]
            test_listbox_adder.update_listbox()
            items = test_listbox_adder.first_words_list_widget.get(0, tk.END)
            assert tuple(test_listbox_adder.FIRST_LANGUAGE_LIST) == items
            assert tuple(test_listbox_adder.SECOND_LANGUAGE_LIST) == items

    def test_clear_lists(self, test_listbox_adder):
        with nullcontext():
            test_listbox_adder.FIRST_LANGUAGE_LIST = [1, 2, 3]
            test_listbox_adder.SECOND_LANGUAGE_LIST = [1, 2, 3]
            test_listbox_adder.update_listbox()
            test_listbox_adder.clear_lists()
            assert test_listbox_adder.FIRST_LANGUAGE_LIST == []
            assert test_listbox_adder.SECOND_LANGUAGE_LIST == []
            assert test_listbox_adder.first_words_list_widget.get(0, tk.END) == ()
            assert test_listbox_adder.second_words_list_widget.get(0, tk.END) == ()
