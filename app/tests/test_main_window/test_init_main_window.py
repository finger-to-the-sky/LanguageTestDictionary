import tkinter as tk
from LanguageTestDictionary import MainWindow
import pytest


@pytest.fixture
def main_window():
    main = MainWindow()
    return main


class TestMainWindow:

    def test_root_main_window(self, main_window):
        assert isinstance(main_window.root, tk.Tk)

    def test_creation_root(self, main_window):
        root = main_window.create_root()
        assert isinstance(root, tk.Tk)

    def test_creation_elements(self, main_window):
        assert isinstance(main_window.header, tk.Label)
        assert isinstance(main_window.frame, tk.Frame)
        assert isinstance(main_window.test_mode_button, tk.Button)
        assert isinstance(main_window.translate_file_btn, tk.Button)
        assert isinstance(main_window.user_text_widget, tk.Text)
        assert isinstance(main_window.translated_text_widget, tk.Text)

    def test_show_elements(self, main_window):
        main_window.show_elements()
        assert main_window.header.winfo_manager() == 'pack'
        assert main_window.frame.winfo_manager() == 'pack'
        assert main_window.test_mode_button.winfo_manager() == 'grid'
        assert main_window.translate_file_btn.winfo_manager() == 'grid'
        assert main_window.user_text_widget.winfo_manager() == 'pack'
        assert main_window.translated_text_widget.winfo_manager() == 'pack'



