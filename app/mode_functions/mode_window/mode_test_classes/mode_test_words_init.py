import tkinter as tk

from app.config import main_logger, SIZE_TEST_MODE_WINDOW
from app.fonts import FontManager
from app.logger import exceptions_logger
from app.mode_functions.mode_window.listbox_worker.listbox_editor import ListBoxEditor
from app.other.custom_print import colored_print
from app.tk_functions import create_boolean_var, create_string_var, create_top_level, create_frame, create_label


class ModeTestWordsInit:
    """
    Class initializer for testing words.
    """
    USER_LIST_WORDS = {'correct': [], 'incorrect': {'user_word': [], 'incorrect_word': [],
                                                    'correct_answer': []}}

    def __init__(self, root, title: str, size_window: str, first_list: list, second_list: list,
                 is_red_test: bool = False):
        """

        :param root: tkinter.Tk(), tkinter.TopLevel() or any same object
        :param title:
        :param size_window:
        :param first_list: List of words for translation.
        :param second_list: List of words with translations for the first list.
        :param is_red_test: Status of the Red List mode.
        """

        try:
            self.root = root
            self.title = title
            self.size_window = size_window
            self.is_red_test = is_red_test
            self.first_list = first_list
            self.second_list = second_list

            # fonts settings
            self.font = FontManager()
            self.label_fonts = self.font.LABEL_FONTS
            self.button_fonts = self.font.BUTTON_FONTS
            self.text_fonts = self.font.TEXT_FONTS
            self.listbox_font = self.font.LISTBOX_FONTS

            self.window_mode = None
            self.text_worker = None
            self.is_visible_results = create_boolean_var()
            self.is_visible_results.set(False)
            self.button_clicked = create_boolean_var()
            self.button_clicked.set(False)

            # error text field
            self.error = None
            self.error_text = create_string_var()
            self.main_win_error = create_boolean_var()
            self.main_win_error.set(False)

            self.window = create_top_level(root=self.root)
            self.frame = create_frame(root=self.window)
            self.window.focus_set()
            self.window.title(self.title)
            self.window.geometry(self.size_window)

            self.header = self.set_header(self.window, self.title)
            self.header.pack()
            self.frame.pack(side=tk.LEFT, padx=(10, 0))

            self.words_worker = ListBoxEditor(master=self.frame,
                                              is_red_test=self.is_red_test)
            self.words_worker.FIRST_LANGUAGE_LIST = self.first_list
            self.words_worker.SECOND_LANGUAGE_LIST = self.second_list
            self.words_worker.update_listbox()

            main_logger.info(f'Инициализация класса {ModeTestWordsInit.__name__} прошла успешно.')

        except (AttributeError, tk.TclError, TypeError) as e:
            message = (f'Класс: {ModeTestWordsInit.__name__} не смог завершить инициализацию.\n'
                       f'Были переданы неверные параметры {e}')
            exceptions_logger.error(message)
            colored_print(message, color='red', style='bright')

    def set_error(self, text: str, window) -> tk.Label:
        """
        Sets an error on the client window.

        :param text: Error message.
        :param window: Display window.
        :return:
        """

        self.error_text.set(text)
        error_label = create_label(root=window, textvariable=self.error_text, fg='red',
                                   font=self.label_fonts['Errors'])
        if error_label is None:
            message = f"Неверно указаны параметры к методу {self.set_error.__name__}"
            exceptions_logger.error(message)
            colored_print(message, color='red', style='bright')
            return message
        self.main_win_error.set(True)
        return error_label

    def clear_error(self):
        """
        Removes the error if it's not needed.

        :return:
        """
        if self.main_win_error.get() is True:
            self.main_win_error.set(False)
        try:
            self.error.destroy()
        except AttributeError:
            exceptions_logger.error(f'self.error = {self.error} был не найден')

    def set_header(self, window, label_text: str) -> tk.Label:
        """
        Sets the title for modes.

        :param window: Installation window.
        :param label_text: Text for the title.
        :return:
        """
        label = create_label(root=window, text=label_text, font=self.label_fonts['Header'])
        if label is None:
            message = f"Неверно указаны параметры к методу {self.set_header.__name__}"
            exceptions_logger.error(message)
            colored_print(message, color='red', style='bright')
            return message
        return label

    def create_window_mode(self):
        """
        Creates a word testing window.

        :return:
        """

        self.window_mode = create_top_level(root=self.root)
        self.window_mode.title(self.title)
        self.window_mode.geometry(SIZE_TEST_MODE_WINDOW)
        self.set_header(self.window_mode, self.title).pack()
        self.window_mode.lift()
        main_logger.info(f'Новое окно было создано {self.window_mode}')
