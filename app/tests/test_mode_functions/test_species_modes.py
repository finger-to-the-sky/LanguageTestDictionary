from contextlib import nullcontext
import pytest
from app.mode_functions.species_modes import onehudred_mode, red_test_mode, sentences_test_mode
import tkinter as tk
from app.config import red_list_db


@pytest.mark.parametrize(
    'root', [tk.Tk(), 123, 'string', {1, 2, 3}, (1, 2, 3), [], [1, 2, 3], {1: 2}, None, False]
)
def test_init_onehundred_mode(root):
    with nullcontext():
        onehudred_mode.OneHundredMode(root)


class TestRedListMode:

    @pytest.mark.parametrize(
        'root', [tk.Tk(), 123, 'string', {1, 2, 3}, (1, 2, 3), [], [1, 2, 3], {1: 2}, None, False]
    )
    def test_init_red_test_mode(self, root):
        with nullcontext():
            red_test_mode.RedTestWordsMode(root)

    @pytest.mark.parametrize(
        'db', [red_list_db, tk.Tk(), 123, 'string', {1, 2, 3}, (1, 2, 3), [], [1, 2, 3], {1: 2}, None, False]
    )
    def test_cache_loader(self, db):
        with nullcontext():
            cls = red_test_mode.RedTestWordsMode(tk.Tk())
            cls.cache_loader(db=db)


@pytest.mark.skip(reason="In current version this class does not using in app")
@pytest.mark.parametrize(
    'root', [tk.Tk(), 123, 'string', {1, 2, 3}, (1, 2, 3), [], [1, 2, 3], {1: 2}, None, False]
)
def test_init_sentences_test_mode(root):
    with nullcontext():
        sentences_test_mode.SentencesTest(root)
