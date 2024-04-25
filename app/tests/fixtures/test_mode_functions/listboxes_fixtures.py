import pytest
import tkinter as tk
from app.mode_functions.mode_window.listbox_worker import listbox_editor, fileloader, adder


@pytest.fixture
def test_listbox_adder():
    return adder.ListBoxAdderClass(master=tk.Tk(), is_red_test=False)


@pytest.fixture
def test_fileloader():
    return fileloader.FileLoaderClass(tk.Tk(), is_red_test=False)


@pytest.fixture
def test_editor():
    return listbox_editor.ListBoxEditor(tk.Tk(), is_red_test=False)
