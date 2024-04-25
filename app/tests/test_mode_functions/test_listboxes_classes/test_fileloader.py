from contextlib import nullcontext
import pytest
import tkinter as tk
from app.mode_functions.mode_window.listbox_worker.fileloader import FileLoaderClass
from app.tests.fixtures.test_mode_functions.listboxes_fixtures import test_fileloader


class TestFileLoaderClass:
    WORDS_LIST = ['sheep - овца;', 'gaps - пробелы;', 'rubber - резинка;']

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

            (tk.Tk(), 123),
            (tk.Tk(), 'string'),
            (tk.Tk(), {1, 2, 3}),
            (tk.Tk(), (1, 2, 3)),
            (tk.Tk(), []),
            (tk.Tk(), [1, 2, 3]),
            (tk.Tk(), {1: 2}),
            (tk.Tk(), None),
            (tk.Tk(), False),
            (tk.Tk(), tk.Tk()),

        ]
    )
    def test_init_fileloader_class(self, master, is_red_test):
        with nullcontext():
            FileLoaderClass(master=master, is_red_test=is_red_test)

    def test_elements_init_fileloader(self, test_fileloader):
        with nullcontext():
            assert isinstance(test_fileloader.upload_button, tk.Button)
            assert isinstance(test_fileloader.cache_button, tk.Button)
            assert test_fileloader.cache_listbox is None

    @pytest.mark.parametrize(
        'words_list, excel',
        [
            (WORDS_LIST, False),
            (123, False),
            ('string', False),
            ({1, 2, 3}, False),
            ((1, 2, 3), False),
            ([], False),
            ([1, 2, 3], False),
            ({1: 2}, False),
            (None, False),
            (False, False),
            (tk.Tk(), False),
            (WORDS_LIST, 123),
            (WORDS_LIST, 'string'),
            (WORDS_LIST, {1, 2, 3}),
            (WORDS_LIST, (1, 2, 3)),
            (WORDS_LIST, []),
            (WORDS_LIST, [1, 2, 3]),
            (WORDS_LIST, {1: 2}),
            (WORDS_LIST, None),
            (WORDS_LIST, True),
            (WORDS_LIST, tk.Tk()),
        ]
    )
    def test_packing_words(self, test_fileloader, words_list, excel):
        with nullcontext():
            test_fileloader.packing_words(words_list=words_list, excel=excel)
            assert 'sheep' in test_fileloader.FIRST_LANGUAGE_LIST
            assert 'овца' in test_fileloader.SECOND_LANGUAGE_LIST
            assert 'rubber' in test_fileloader.FIRST_LANGUAGE_LIST
            assert 'резинка' in test_fileloader.SECOND_LANGUAGE_LIST
            assert 'gaps' in test_fileloader.FIRST_LANGUAGE_LIST
            assert 'пробелы' in test_fileloader.SECOND_LANGUAGE_LIST

    @pytest.mark.skip(reason="This test creates several windows that need all time to closing")
    @pytest.mark.parametrize(
        'filepath',
        ['./file/to/path', 123, 'string', {1, 2, 3}, (1, 2, 3), [], [1, 2, 3], {1: 2}, None, False, tk.Tk()]
    )
    def test_load_functions(self, test_fileloader, filepath):
        with nullcontext():
            test_fileloader.load_from_txt(filepath=filepath)
            test_fileloader.load_from_word(filepath=filepath)
            test_fileloader.load_from_excel(filepath=filepath)
