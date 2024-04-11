import pytest
import tkinter as tk
from tkinter import ttk
from app.translator.languages_worker.languages_worker_init import LanguagesWorkerInit
from app.translator.languages_worker.languages_worker import LanguagesWorker


@pytest.fixture
def test_languages_worker_init():
    root = tk.Tk()
    root.title('TestTitle')
    user_tw = tk.Text(root)
    translated_tw = tk.Text(root)
    frame = tk.Frame(root)
    lw = LanguagesWorkerInit(root=root, user_text_widget=user_tw, translated_text_widget=translated_tw, frame=frame)
    return lw


@pytest.fixture
def test_languages_worker():
    root = tk.Tk()
    root.title('TestTitle')
    user_tw = tk.Text(root)
    translated_tw = tk.Text(root)
    frame = tk.Frame(root)
    lw = LanguagesWorker(root=root, user_text_widget=user_tw, translated_text_widget=translated_tw, frame=frame)
    return lw


@pytest.fixture
def test_combobox(test_languages_worker):
    combobox = ttk.Combobox(test_languages_worker.root)
    return combobox
