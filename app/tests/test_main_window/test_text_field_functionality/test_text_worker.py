from contextlib import nullcontext
import tkinter as tk
import pytest
from app.translator.text_field_functionality import TextWorker
from app.tests.fixtures.test_root import test_root
from app.tests.fixtures.test_main_window.test_text_field_functionality import test_text_worker


class TestTextWorker:
    FROM_LANGUAGE = "English"
    TO_LANGUAGE = 'Russian'
    ROOT = tk.Tk()
    FIRST_TEXT_WIDGET = tk.Text(ROOT)
    FIRST_TEXT_WIDGET.insert('1.0', 'Test')
    SECOND_TEXT_WIDGET = tk.Text(ROOT)

    @pytest.mark.parametrize(
        'src, dest, expectation',
        [
            (FROM_LANGUAGE, TO_LANGUAGE, nullcontext()),
            (123, TO_LANGUAGE, pytest.raises(AssertionError)),
            ('string', TO_LANGUAGE, pytest.raises(AssertionError)),
            ({1, 2, 3}, TO_LANGUAGE, pytest.raises(AssertionError)),
            ((1, 2, 3), TO_LANGUAGE, pytest.raises(AssertionError)),
            ([], TO_LANGUAGE, pytest.raises(AssertionError)),
            ([1, 2, 3], TO_LANGUAGE, pytest.raises(AssertionError)),
            ({1: 2}, TO_LANGUAGE, pytest.raises(AssertionError)),
            (None, TO_LANGUAGE, pytest.raises(AssertionError)),
            (False, TO_LANGUAGE, pytest.raises(AssertionError)),
            (tk.Tk(), TO_LANGUAGE, pytest.raises(AssertionError)),

            (FROM_LANGUAGE, 123, pytest.raises(AssertionError)),
            (FROM_LANGUAGE, 'string', pytest.raises(AssertionError)),
            (FROM_LANGUAGE, {1, 2, 3}, pytest.raises(AssertionError)),
            (FROM_LANGUAGE, (1, 2, 3), pytest.raises(AssertionError)),
            (FROM_LANGUAGE, [], pytest.raises(AssertionError)),
            (FROM_LANGUAGE, [1, 2, 3], pytest.raises(AssertionError)),
            (FROM_LANGUAGE, {1: 2}, pytest.raises(AssertionError)),
            (FROM_LANGUAGE, None, pytest.raises(AssertionError)),
            (FROM_LANGUAGE, False, pytest.raises(AssertionError)),
            (FROM_LANGUAGE, tk.Tk(), pytest.raises(AssertionError)),

        ]
    )
    def test_init_text_worker(self, test_root, src, dest, expectation):
        with expectation:
            result = TextWorker(src=src, dest=dest)
            assert isinstance(result, TextWorker)
            assert type(result.get_text_translator(root=test_root, first_text_widget=self.FIRST_TEXT_WIDGET,
                                                   second_text_widget=tk.Text(test_root))) is str

    @pytest.mark.parametrize(
        'root, first_text_widget, second_text_widget, expectation',
        [
            (ROOT, FIRST_TEXT_WIDGET, SECOND_TEXT_WIDGET, nullcontext()),
            (123, FIRST_TEXT_WIDGET, SECOND_TEXT_WIDGET, nullcontext()),
            ('string', FIRST_TEXT_WIDGET, SECOND_TEXT_WIDGET, nullcontext()),
            ({1, 2, 3}, FIRST_TEXT_WIDGET, SECOND_TEXT_WIDGET, nullcontext()),
            ((1, 2, 3), FIRST_TEXT_WIDGET, SECOND_TEXT_WIDGET, nullcontext()),
            ([], FIRST_TEXT_WIDGET, SECOND_TEXT_WIDGET, nullcontext()),
            ([1, 2, 3], FIRST_TEXT_WIDGET, SECOND_TEXT_WIDGET, nullcontext()),
            ({1: 2}, FIRST_TEXT_WIDGET, SECOND_TEXT_WIDGET, nullcontext()),
            (None, FIRST_TEXT_WIDGET, SECOND_TEXT_WIDGET, nullcontext()),
            (False, FIRST_TEXT_WIDGET, SECOND_TEXT_WIDGET, nullcontext()),
            (tk.Tk(), FIRST_TEXT_WIDGET, SECOND_TEXT_WIDGET, nullcontext()),

            (ROOT, 123, SECOND_TEXT_WIDGET, pytest.raises(AssertionError)),
            (ROOT, 'string', SECOND_TEXT_WIDGET, pytest.raises(AssertionError)),
            (ROOT, {1, 2, 3}, SECOND_TEXT_WIDGET, pytest.raises(AssertionError)),
            (ROOT, (1, 2, 3), SECOND_TEXT_WIDGET, pytest.raises(AssertionError)),
            (ROOT, [], SECOND_TEXT_WIDGET, pytest.raises(AssertionError)),
            (ROOT, [1, 2, 3], SECOND_TEXT_WIDGET, pytest.raises(AssertionError)),
            (ROOT, {1: 2}, SECOND_TEXT_WIDGET, nullcontext()),
            (ROOT, None, SECOND_TEXT_WIDGET, pytest.raises(AssertionError)),
            (ROOT, False, SECOND_TEXT_WIDGET, pytest.raises(AssertionError)),
            (ROOT, tk.Tk(), SECOND_TEXT_WIDGET, pytest.raises(AssertionError)),

            (ROOT, FIRST_TEXT_WIDGET, 123, pytest.raises(AssertionError)),
            (ROOT, FIRST_TEXT_WIDGET, 'string', pytest.raises(AssertionError)),
            (ROOT, FIRST_TEXT_WIDGET, {1, 2, 3}, pytest.raises(AssertionError)),
            (ROOT, FIRST_TEXT_WIDGET, (1, 2, 3), pytest.raises(AssertionError)),
            (ROOT, FIRST_TEXT_WIDGET, [], pytest.raises(AssertionError)),
            (ROOT, FIRST_TEXT_WIDGET, [1, 2, 3], pytest.raises(AssertionError)),
            (ROOT, FIRST_TEXT_WIDGET, {1: 2}, pytest.raises(AssertionError)),
            (ROOT, FIRST_TEXT_WIDGET, None, pytest.raises(AssertionError)),
            (ROOT, FIRST_TEXT_WIDGET, False, pytest.raises(AssertionError)),
            (ROOT, FIRST_TEXT_WIDGET, tk.Tk(), pytest.raises(AssertionError)),
        ]
    )
    def test_get_text_translator(self, test_text_worker, root, first_text_widget, second_text_widget, expectation):
        with expectation:
            result = test_text_worker.get_text_translator(root=root, first_text_widget=first_text_widget,
                                                          second_text_widget=second_text_widget)
            assert type(result) is str
