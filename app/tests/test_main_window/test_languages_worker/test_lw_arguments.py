import pytest
import tkinter as tk
from app.translator.languages_worker.languages_worker import LanguagesWorker
from app.translator.languages_worker.languages_worker_init import LanguagesWorkerInit
from contextlib import nullcontext
from app.tests.fixtures.test_root import test_root

root_init = tk.Tk()


class TestLanguagesWorkerInitArguments:

    @pytest.mark.parametrize("root, expectation",
                             [
                                 (root_init, nullcontext()),
                                 (123, pytest.raises(AttributeError)),
                                 ('hi', pytest.raises(AttributeError)),
                                 (None, pytest.raises(AttributeError)),
                                 (True, pytest.raises(AttributeError)),
                                 ([], pytest.raises(AttributeError)),
                                 ({}, pytest.raises(AttributeError))
                             ]
                             )
    def test_incorrect_root_type(self, root, expectation):
        with expectation:
            lw = LanguagesWorkerInit(root, user_text_widget=tk.Text(root_init),
                                     translated_text_widget=tk.Text(root_init), frame=tk.Frame(root_init))
            assert isinstance(lw.root, tk.Tk)

    @pytest.mark.parametrize("user_text_widget_value, expectation",
                             [
                                 (tk.Text(root_init), nullcontext()),
                                 (123, pytest.raises(AttributeError)),
                                 ('hi', pytest.raises(AttributeError)),
                                 (None, pytest.raises(AttributeError)),
                                 (True, pytest.raises(AttributeError)),
                                 ([], pytest.raises(AttributeError)),
                                 ({}, pytest.raises(AttributeError))
                             ]
                             )
    def test_incorrect_user_text_widget_type(self, test_root, user_text_widget_value, expectation):
        with expectation:
            lw = LanguagesWorkerInit(test_root, user_text_widget=user_text_widget_value,
                                     translated_text_widget=tk.Text(test_root), frame=tk.Frame(test_root))
            assert isinstance(lw.user_text_widget, tk.Text)

    @pytest.mark.parametrize("translated_text_widget, expectation",
                             [
                                 (tk.Text(root_init), nullcontext()),
                                 (123, pytest.raises(AttributeError)),
                                 ('hi', pytest.raises(AttributeError)),
                                 (None, pytest.raises(AttributeError)),
                                 (True, pytest.raises(AttributeError)),
                                 ([], pytest.raises(AttributeError)),
                                 ({}, pytest.raises(AttributeError))
                             ]
                             )
    def test_incorrect_translated_text_widget_type(self, test_root, translated_text_widget, expectation):
        with expectation:
            lw = LanguagesWorkerInit(test_root, user_text_widget=tk.Text(test_root),
                                     translated_text_widget=translated_text_widget, frame=tk.Frame(test_root))
            assert isinstance(lw.translated_text_widget, tk.Text)

    @pytest.mark.parametrize("frame, expectation",
                             [
                                 (tk.Frame(root_init), nullcontext()),
                                 (123, pytest.raises(AttributeError)),
                                 ('hi', pytest.raises(AttributeError)),
                                 (None, pytest.raises(AttributeError)),
                                 (True, pytest.raises(AttributeError)),
                                 ([], pytest.raises(AttributeError)),
                                 ({}, pytest.raises(AttributeError))
                             ]
                             )
    def test_incorrect_frame_type(self, test_root, frame, expectation):
        with expectation:
            lw = LanguagesWorkerInit(test_root, user_text_widget=tk.Text(test_root),
                                     translated_text_widget=tk.Text(test_root), frame=frame)
            assert isinstance(lw.frame, tk.Frame)


class TestLanguagesWorkerArguments:

    @pytest.mark.parametrize("root, expectation",
                             [
                                 (root_init, nullcontext()),
                                 (123, pytest.raises(AttributeError)),
                                 ('hi', pytest.raises(AttributeError)),
                                 (None, pytest.raises(AttributeError)),
                                 (True, pytest.raises(AttributeError)),
                                 ([], pytest.raises(AttributeError)),
                                 ({}, pytest.raises(AttributeError))
                             ]
                             )
    def test_incorrect_root_type(self, root, expectation):
        with expectation:
            lw = LanguagesWorker(root, user_text_widget=tk.Text(root_init),
                                 translated_text_widget=tk.Text(root_init), frame=tk.Frame(root_init))
            assert isinstance(lw.root, tk.Tk)

    @pytest.mark.parametrize("user_text_widget_value, expectation",
                             [
                                 (tk.Text(root_init), nullcontext()),
                                 (123, pytest.raises(AttributeError)),
                                 ('hi', pytest.raises(AttributeError)),
                                 (None, pytest.raises(AttributeError)),
                                 (True, pytest.raises(AttributeError)),
                                 ([], pytest.raises(AttributeError)),
                                 ({}, pytest.raises(AttributeError))
                             ]
                             )
    def test_incorrect_user_text_widget_type(self, test_root, user_text_widget_value, expectation):
        with expectation:
            lw = LanguagesWorker(test_root, user_text_widget=user_text_widget_value,
                                 translated_text_widget=tk.Text(test_root), frame=tk.Frame(test_root))
            assert isinstance(lw.user_text_widget, tk.Text)

    @pytest.mark.parametrize("translated_text_widget, expectation",
                             [
                                 (tk.Text(root_init), nullcontext()),
                                 (123, pytest.raises(AttributeError)),
                                 ('hi', pytest.raises(AttributeError)),
                                 (None, pytest.raises(AttributeError)),
                                 (True, pytest.raises(AttributeError)),
                                 ([], pytest.raises(AttributeError)),
                                 ({}, pytest.raises(AttributeError))
                             ]
                             )
    def test_incorrect_translated_text_widget_type(self, test_root, translated_text_widget, expectation):
        with expectation:
            lw = LanguagesWorker(test_root, user_text_widget=tk.Text(test_root),
                                 translated_text_widget=translated_text_widget, frame=tk.Frame(test_root))
            assert isinstance(lw.translated_text_widget, tk.Text)

    @pytest.mark.parametrize("frame, expectation",
                             [
                                 (tk.Frame(root_init), nullcontext()),
                                 (123, pytest.raises(AttributeError)),
                                 ('hi', pytest.raises(AttributeError)),
                                 (None, pytest.raises(AttributeError)),
                                 (True, pytest.raises(AttributeError)),
                                 ([], pytest.raises(AttributeError)),
                                 ({}, pytest.raises(AttributeError))
                             ]
                             )
    def test_incorrect_frame_type(self, test_root, frame, expectation):
        with expectation:
            lw = LanguagesWorker(test_root, user_text_widget=tk.Text(test_root),
                                 translated_text_widget=tk.Text(test_root), frame=frame)
            assert isinstance(lw.frame, tk.Frame)
