from contextlib import nullcontext
from app.tests.fixtures.test_main_window.test_text_field_functionality import test_text_field_functionality
import pytest
import tkinter as tk


class TestTextFieldFunctionality:

    @pytest.mark.parametrize(
        'root, text_widgets, expectation',
        [
            (tk.Tk(), (tk.Text(tk.Tk()), tk.Text(tk.Tk())), nullcontext()),
            (123, (tk.Text(tk.Tk()), tk.Text(tk.Tk())), pytest.raises(AssertionError)),
            ('string', (tk.Text(tk.Tk()), tk.Text(tk.Tk())), pytest.raises(AssertionError)),
            ({1, 2, 3}, (tk.Text(tk.Tk()), tk.Text(tk.Tk())), pytest.raises(AssertionError)),
            ((1, 2, 3), (tk.Text(tk.Tk()), tk.Text(tk.Tk())), pytest.raises(AssertionError)),
            ([], (tk.Text(tk.Tk()), tk.Text(tk.Tk())), pytest.raises(AssertionError)),
            ([1, 2, 3], (tk.Text(tk.Tk()), tk.Text(tk.Tk())), pytest.raises(AssertionError)),
            ({1: 2}, (tk.Text(tk.Tk()), tk.Text(tk.Tk())), pytest.raises(AssertionError)),
            (None, (tk.Text(tk.Tk()), tk.Text(tk.Tk())), pytest.raises(AssertionError)),
            (False, (tk.Text(tk.Tk()), tk.Text(tk.Tk())), pytest.raises(AssertionError)),

            (tk.Tk(), (123, tk.Text(tk.Tk())), nullcontext()),
            (tk.Tk(), ('string', tk.Text(tk.Tk())), nullcontext()),
            (tk.Tk(), ({1, 2, 3}, tk.Text(tk.Tk())), nullcontext()),
            (tk.Tk(), ((1, 2, 3), tk.Text(tk.Tk())), nullcontext()),
            (tk.Tk(), ([], tk.Text(tk.Tk())), nullcontext()),
            (tk.Tk(), ([1, 2, 3], tk.Text(tk.Tk())), nullcontext()),
            (tk.Tk(), ({1: 2}, tk.Text(tk.Tk())), nullcontext()),
            (tk.Tk(), (None, tk.Text(tk.Tk())), pytest.raises(AssertionError)),
            (tk.Tk(), (False, tk.Text(tk.Tk())), nullcontext()),
            (tk.Tk(), (tk.Tk(), tk.Text(tk.Tk())), nullcontext()),

            (tk.Tk(), (tk.Text(tk.Tk()), 123), nullcontext()),
            (tk.Tk(), (tk.Text(tk.Tk()), 'string'), nullcontext()),
            (tk.Tk(), (tk.Text(tk.Tk()), {1, 2, 3}), nullcontext()),
            (tk.Tk(), (tk.Text(tk.Tk()), (1, 2, 3)), nullcontext()),
            (tk.Tk(), (tk.Text(tk.Tk()), []), nullcontext()),
            (tk.Tk(), (tk.Text(tk.Tk()), [1, 2, 3]), nullcontext()),
            (tk.Tk(), (tk.Text(tk.Tk()), {1: 2}), nullcontext()),
            (tk.Tk(), (tk.Text(tk.Tk()), None), pytest.raises(AssertionError)),
            (tk.Tk(), (tk.Text(tk.Tk()), False), nullcontext()),
            (tk.Tk(), (tk.Text(tk.Tk()), tk.Tk()), nullcontext()),

            (tk.Tk(), 123, pytest.raises(AssertionError)),
            (tk.Tk(), 'string', pytest.raises(AssertionError)),
            (tk.Tk(), {1, 2, 3}, nullcontext()),
            (tk.Tk(), (1, 2, 3), nullcontext()),
            (tk.Tk(), [], nullcontext()),
            (tk.Tk(), [1, 2, 3], nullcontext()),
            (tk.Tk(), {1: 2}, nullcontext()),
            (tk.Tk(), None, pytest.raises(AssertionError)),
            (tk.Tk(), False, pytest.raises(AssertionError)),
            (tk.Tk(), tk.Tk(), pytest.raises(AssertionError)),
        ]
    )
    def test_text_operations(self, test_text_field_functionality, root, text_widgets, expectation):
        with expectation:
            copy = test_text_field_functionality.copy_text(root, text_widgets)
            paste = test_text_field_functionality.paste_text(root, text_widgets)
            select = test_text_field_functionality.select_all(root, text_widgets)
            cut = test_text_field_functionality.cut_text(root, text_widgets)
            assert copy is True
            assert paste is True
            assert select is True
            assert cut is True

    @pytest.mark.parametrize(
        'root, text_widgets, expectation',
        [
            (tk.Tk(), (tk.Text(tk.Tk()), tk.Text(tk.Tk())), nullcontext()),
            (123, (tk.Text(tk.Tk()), tk.Text(tk.Tk())), pytest.raises(AssertionError)),
            ('string', (tk.Text(tk.Tk()), tk.Text(tk.Tk())), pytest.raises(AssertionError)),
            ({1, 2, 3}, (tk.Text(tk.Tk()), tk.Text(tk.Tk())), pytest.raises(AssertionError)),
            ((1, 2, 3), (tk.Text(tk.Tk()), tk.Text(tk.Tk())), pytest.raises(AssertionError)),
            ([], (tk.Text(tk.Tk()), tk.Text(tk.Tk())), pytest.raises(AssertionError)),
            ([1, 2, 3], (tk.Text(tk.Tk()), tk.Text(tk.Tk())), pytest.raises(AssertionError)),
            ({1: 2}, (tk.Text(tk.Tk()), tk.Text(tk.Tk())), pytest.raises(AssertionError)),
            (None, (tk.Text(tk.Tk()), tk.Text(tk.Tk())), pytest.raises(AssertionError)),
            (False, (tk.Text(tk.Tk()), tk.Text(tk.Tk())), pytest.raises(AssertionError)),

            (tk.Tk(), 123, pytest.raises(AssertionError)),
            (tk.Tk(), 'string', pytest.raises(AssertionError)),
            (tk.Tk(), {1, 2, 3}, pytest.raises(AssertionError)),
            (tk.Tk(), (1, 2, 3), pytest.raises(AssertionError)),
            (tk.Tk(), [], nullcontext()),
            (tk.Tk(), [1, 2, 3], pytest.raises(AssertionError)),
            (tk.Tk(), {1: 2}, pytest.raises(AssertionError)),
            (tk.Tk(), None, pytest.raises(AssertionError)),
            (tk.Tk(), False, pytest.raises(AssertionError)),
            (tk.Tk(), tk.Tk(), pytest.raises(AssertionError)),

            (tk.Tk(), (123, tk.Text(tk.Tk())), pytest.raises(AssertionError)),
            (tk.Tk(), ('string', tk.Text(tk.Tk())), pytest.raises(AssertionError)),
            (tk.Tk(), ({1, 2, 3}, tk.Text(tk.Tk())), pytest.raises(AssertionError)),
            (tk.Tk(), ((1, 2, 3), tk.Text(tk.Tk())), pytest.raises(AssertionError)),
            (tk.Tk(), ([], tk.Text(tk.Tk())), pytest.raises(AssertionError)),
            (tk.Tk(), ([1, 2, 3], tk.Text(tk.Tk())), pytest.raises(AssertionError)),
            (tk.Tk(), ({1: 2}, tk.Text(tk.Tk())), pytest.raises(AssertionError)),
            (tk.Tk(), (None, tk.Text(tk.Tk())), pytest.raises(AssertionError)),
            (tk.Tk(), (False, tk.Text(tk.Tk())), pytest.raises(AssertionError)),
            (tk.Tk(), (tk.Tk(), tk.Text(tk.Tk())), nullcontext()),

            (tk.Tk(), (tk.Text(tk.Tk()), 123), pytest.raises(AssertionError)),
            (tk.Tk(), (tk.Text(tk.Tk()), 'string'), pytest.raises(AssertionError)),
            (tk.Tk(), (tk.Text(tk.Tk()), {1, 2, 3}), pytest.raises(AssertionError)),
            (tk.Tk(), (tk.Text(tk.Tk()), (1, 2, 3)), pytest.raises(AssertionError)),
            (tk.Tk(), (tk.Text(tk.Tk()), []), pytest.raises(AssertionError)),
            (tk.Tk(), (tk.Text(tk.Tk()), [1, 2, 3]), pytest.raises(AssertionError)),
            (tk.Tk(), (tk.Text(tk.Tk()), {1: 2}), pytest.raises(AssertionError)),
            (tk.Tk(), (tk.Text(tk.Tk()), None), pytest.raises(AssertionError)),
            (tk.Tk(), (tk.Text(tk.Tk()), False), pytest.raises(AssertionError)),
            (tk.Tk(), (tk.Text(tk.Tk()), tk.Tk()), nullcontext()),
        ]
    )
    def test_context_menu(self, test_text_field_functionality, root, text_widgets, expectation):
        with expectation:
            result = test_text_field_functionality.create_context_menu(root=root, text_widgets=text_widgets)
            assert result is True

    @pytest.mark.parametrize(
        'root, text_widgets, expectation',
        [
            (tk.Tk(), (tk.Text(tk.Tk()), tk.Text(tk.Tk())), nullcontext()),
            (123, (tk.Text(tk.Tk()), tk.Text(tk.Tk())), pytest.raises(AssertionError)),
            ('string', (tk.Text(tk.Tk()), tk.Text(tk.Tk())), nullcontext()),
            ({1, 2, 3}, (tk.Text(tk.Tk()), tk.Text(tk.Tk())), pytest.raises(AssertionError)),
            ((1, 2, 3), (tk.Text(tk.Tk()), tk.Text(tk.Tk())), pytest.raises(AssertionError)),
            ([], (tk.Text(tk.Tk()), tk.Text(tk.Tk())), pytest.raises(AssertionError)),
            ([1, 2, 3], (tk.Text(tk.Tk()), tk.Text(tk.Tk())), pytest.raises(AssertionError)),
            ({1: 2}, (tk.Text(tk.Tk()), tk.Text(tk.Tk())), pytest.raises(AssertionError)),
            (None, (tk.Text(tk.Tk()), tk.Text(tk.Tk())), pytest.raises(AssertionError)),
            (False, (tk.Text(tk.Tk()), tk.Text(tk.Tk())), pytest.raises(AssertionError)),

            (tk.Tk(), (123, tk.Text(tk.Tk())), nullcontext()),
            (tk.Tk(), ('string', tk.Text(tk.Tk())), nullcontext()),
            (tk.Tk(), ({1, 2, 3}, tk.Text(tk.Tk())), nullcontext()),
            (tk.Tk(), ((1, 2, 3), tk.Text(tk.Tk())), nullcontext()),
            (tk.Tk(), ([], tk.Text(tk.Tk())), nullcontext()),
            (tk.Tk(), ([1, 2, 3], tk.Text(tk.Tk())), nullcontext()),
            (tk.Tk(), ({1: 2}, tk.Text(tk.Tk())), nullcontext()),
            (tk.Tk(), (None, tk.Text(tk.Tk())), nullcontext()),
            (tk.Tk(), (False, tk.Text(tk.Tk())), nullcontext()),
            (tk.Tk(), (tk.Tk(), tk.Text(tk.Tk())), nullcontext()),

            (tk.Tk(), (tk.Text(tk.Tk()), 123), nullcontext()),
            (tk.Tk(), (tk.Text(tk.Tk()), 'string'), nullcontext()),
            (tk.Tk(), (tk.Text(tk.Tk()), {1, 2, 3}), nullcontext()),
            (tk.Tk(), (tk.Text(tk.Tk()), (1, 2, 3)), nullcontext()),
            (tk.Tk(), (tk.Text(tk.Tk()), []), nullcontext()),
            (tk.Tk(), (tk.Text(tk.Tk()), [1, 2, 3]), nullcontext()),
            (tk.Tk(), (tk.Text(tk.Tk()), {1: 2}), nullcontext()),
            (tk.Tk(), (tk.Text(tk.Tk()), None), nullcontext()),
            (tk.Tk(), (tk.Text(tk.Tk()), False), nullcontext()),
            (tk.Tk(), (tk.Text(tk.Tk()), tk.Tk()), nullcontext()),

            (tk.Tk(), 123, nullcontext()),
            (tk.Tk(), 'string', nullcontext()),
            (tk.Tk(), {1, 2, 3}, nullcontext()),
            (tk.Tk(), (1, 2, 3), nullcontext()),
            (tk.Tk(), [], nullcontext()),
            (tk.Tk(), [1, 2, 3], nullcontext()),
            (tk.Tk(), {1: 2}, nullcontext()),
            (tk.Tk(), None, nullcontext()),
            (tk.Tk(), False, nullcontext()),
            (tk.Tk(), tk.Tk(), nullcontext()),
        ]
    )
    def test_add_hotkeys(self, test_text_field_functionality, root, text_widgets, expectation):
        with expectation:
            add_hotkeys = test_text_field_functionality.russian_add_hotkeys(root, text_widgets)
            assert add_hotkeys is True
