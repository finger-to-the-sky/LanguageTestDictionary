from contextlib import nullcontext
from app.tests.fixtures.test_other_functions.test_db import test_db
import tkinter as tk
import pytest
from app.other.db.json_functions import add_word_in_db, clear_cache_redlist, edit_word_in_db, delete_word_in_db, \
    cache_current_file, download_file_from_cache, clear_cache_filenames_db
from app.config import red_list_db, updated_path


class TestJSONFunctions:
    WORDS_LIST = [
        {'word': 'English', 'translate': 'Английский'},
        {'word': 'Korean', 'translate': 'Корейский'}
    ]
    FILEPATH = f'{updated_path}/app/other/db/test_db.json'

    @pytest.mark.parametrize(
        'db',
        [red_list_db, 123, 'string', {1, 2, 3}, (1, 2, 3), [], [1, 2, 3], {1: 2}, None, False, tk.Tk()]
    )
    def test_db_json_functions(self, db):
        with nullcontext():
            add_word_in_db('english', 'russian', db=db)
            clear_cache_redlist(db=db)
            edit_word_in_db(db=db, current_word='russian', word='english')
            delete_word_in_db(db=db, deleted_word='english')
            cache_current_file(db=db)
            download_file_from_cache(db=db)
            clear_cache_filenames_db(db=db)

    @pytest.mark.parametrize(
        'word, translate, expectation',
        [
            ('English', 'Английский', nullcontext()),
            (123, 'Английский', nullcontext()),
            ({1, 2, 3}, 'Английский', pytest.raises(AssertionError)),
            ((1, 2, 3), 'Английский', pytest.raises(AssertionError)),
            ([], 'Английский', nullcontext()),
            ([1, 2, 3], 'Английский', nullcontext()),
            ({1: 2}, 'Английский', pytest.raises(AssertionError)),
            (None, 'Английский', nullcontext()),
            (False, 'Английский', nullcontext()),
            (tk.Tk(), 'Английский', pytest.raises(AssertionError)),

            ('English', 123, nullcontext()),
            ('English', {1, 2, 3}, pytest.raises(AssertionError)),
            ('English', (1, 2, 3), pytest.raises(AssertionError)),
            ('English', [], nullcontext()),
            ('English', [1, 2, 3], nullcontext()),
            ('English', {1: 2}, pytest.raises(AssertionError)),
            ('English', False, nullcontext()),
            ('English', tk.Tk(), pytest.raises(AssertionError)),
        ]

    )
    def test_add_word_in_db(self, test_db, word, translate, expectation):
        with expectation:
            add_word_in_db(db=test_db, word=word, translate=translate)
            if {'word': word, 'translate': translate} in test_db.all():
                assert True
            else:
                assert False

    @pytest.mark.parametrize(
        'current_word, word',
        [
            ('English', 'Английский'),
            (123, 'Английский'),
            ({1, 2, 3}, 'Английский'),
            ((1, 2, 3), 'Английский'),
            ([], 'Английский'),
            ([1, 2, 3], 'Английский'),
            ({1: 2}, 'Английский'),
            (None, 'Английский'),
            (False, 'Английский'),
            (tk.Tk(), 'Английский'),

            ('English', 123),
            ('English', {1, 2, 3}),
            ('English', (1, 2, 3)),
            ('English', []),
            ('English', [1, 2, 3]),
            ('English', {1: 2}),
            ('English', False),
            ('English', tk.Tk()),

        ]
    )
    def test_edit_word_in_db(self, test_db, current_word, word):
        with nullcontext():
            edit_word_in_db(db=test_db, current_word=current_word, word=word)

    @pytest.mark.parametrize(
        'deleted_word',
        ['English', 123, {1, 2, 3}, (1, 2, 3), [], [1, 2, 3], {1: 2}, None, False, tk.Tk() ]
    )
    def test_delete_word_in_db(self, test_db, deleted_word):
        with nullcontext():
            delete_word_in_db(db=test_db, deleted_word=deleted_word)

    @pytest.mark.parametrize(
        'filepath, words_list',
        [
            (FILEPATH, WORDS_LIST),
            (123, WORDS_LIST),
            ({1, 2, 3}, WORDS_LIST),
            ((1, 2, 3), WORDS_LIST),
            ([], WORDS_LIST),
            ([1, 2, 3], WORDS_LIST),
            ({1: 2}, WORDS_LIST),
            (None, WORDS_LIST),
            (False, WORDS_LIST),
            (tk.Tk(), WORDS_LIST),

            (FILEPATH, 123),
            (FILEPATH, 'string'),
            (FILEPATH, {1, 2, 3}),
            (FILEPATH, (1, 2, 3)),
            (FILEPATH, []),
            (FILEPATH, {1: 2}),
            (FILEPATH, None),
            (FILEPATH, False),
            (FILEPATH, tk.Tk()),
        ]
    )
    def test_cache_current_file(self, test_db, filepath, words_list):
        with nullcontext():
            cache_current_file(filepath=filepath, words_list=words_list, db=test_db)

    @pytest.mark.parametrize(
        'filepath',
        [FILEPATH, 123, 'string', {1, 2, 3}, (1, 2, 3), [], [1, 2, 3], {1: 2}, None, False, tk.Tk()]
    )
    def test_download_file_from_cache(self, test_db, filepath):
        with nullcontext():
            download_file_from_cache(db=test_db, filepath=filepath)
