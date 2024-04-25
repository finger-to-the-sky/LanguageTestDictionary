from tkinter import Label, messagebox
import tkinter as tk
from app.fonts import FontManager
from app.logger import exceptions_logger
from app.other.custom_print import colored_print
from app.other.db.json_functions import add_word_in_db, clear_cache_redlist
from app.config import main_logger
from app.tk_functions import create_string_var, create_boolean_var, create_label, create_button, create_entry, \
    create_listbox, create_frame, create_top_level


class ListBoxAdderClass:
    """
    Creates word lists and mechanisms for adding words to them.
    """
    FIRST_LANGUAGE_LIST = []
    SECOND_LANGUAGE_LIST = []

    def __init__(self, master, is_red_test: bool):
        """
        :param master: tkinter.Tk(), tkinter.TopLevel() or any same object
        :param is_red_test: Status for determining the mode.
        """

        try:
            self.window = master
            self.is_red_test = is_red_test

            self.text_var = create_string_var()
            self.error_add_win = create_boolean_var()
            self.error_add_win.set(False)
            self.error = create_boolean_var()
            self.error.set(False)
            self.err = tk.Label()

            # fonts configuration
            self.fonts = FontManager()
            self.label_fonts = self.fonts.LABEL_FONTS
            self.button_fonts = self.fonts.BUTTON_FONTS
            self.listbox_fonts = self.fonts.LISTBOX_FONTS
            self.text_fonts = self.fonts.TEXT_FONTS

            self.window_is_active = create_boolean_var()
            self.window_is_active.set(False)

            self.first_label = create_label(root=self.window, text='Тестируемые слова',
                                            font=self.label_fonts['ListboxNames'])
            self.second_label = create_label(root=self.window, text='Перевод тестируемых слов',
                                             font=self.label_fonts['ListboxNames'])

            self.first_label.grid(column=0, row=0)
            self.second_label.grid(column=1, row=0)

            self.first_words_list_widget = create_listbox(self.window, selectmode=tk.SINGLE, width=50, height=30,
                                                          font=self.listbox_fonts['WordsList'])
            self.second_words_list_widget = create_listbox(self.window, selectmode=tk.SINGLE, width=50, height=30,
                                                           font=self.listbox_fonts['WordsList'])

            self.first_words_list_widget.bind('<Enter>', self.first_words_list_widget.config(cursor='hand2'))
            self.second_words_list_widget.bind('<Enter>', self.second_words_list_widget.config(cursor='hand2'))

            self.first_words_list_widget.grid(column=0, row=1, padx=(0, 10))
            self.second_words_list_widget.grid(column=1, row=1)

            self.frame = create_frame(self.window)
            self.frame.grid(column=2, row=1, pady=(0, 180), padx=(30, 0))
            self.add_word_btn = create_button(self.frame, text='Добавить слова', width=20, height=2,
                                              font=self.button_fonts['TestModeMenu']['WordsOperations']['Add_btn'],
                                              command=self.add_word_to_listwords)
            self.add_word_btn.pack(pady=(0, 10))
            main_logger.info(f'Класс {ListBoxAdderClass.__name__} был успешно инициализирован.')
        except (TypeError, AttributeError,) as e:
            message = f'Класс: {ListBoxAdderClass.__name__} получил неверные параметры {e}'
            colored_print(message, 'red', 'bright')
            exceptions_logger.error(message)

    def check_len_list(self) -> tuple:
        """
        Checks the number of words according to the software rules.
        :return:
        """
        if len(self.SECOND_LANGUAGE_LIST) >= 30 and self.is_red_test is True:
            return False, 'Вы не можете добавить больше 30 слов!'
        elif len(self.SECOND_LANGUAGE_LIST) >= 100:
            return False, 'Вы не можете добавить больше 100 слов!'
        else:
            return True,

    def set_error(self, text: str, window, error_status: tk.BooleanVar) -> tk.Label:
        """
        Generates an error for user display.

        :param text: Error text.
        :param window: tkinter.Tk(), tkinter.TopLevel() or any same object
        :param error_status:
        :return:
        """

        message = f'Функция: {self.set_error.__name__} получила неверные параметры.'
        try:
            self.text_var.set(text)
            error_label = create_label(root=window, textvariable=self.text_var, fg='red',
                                       font=self.label_fonts['Errors'])
            if error_label is None:
                raise AttributeError
            error_status.set(True)
            return error_label
        except (AttributeError,):
            colored_print(message, 'red', 'bright')
            exceptions_logger.error(message)

    def clear_error(self):
        """
        Delete an error from user display.

        :return:
        """

        self.error.set(False)
        if self.error.get() is False:
            try:
                self.err.destroy()
            except tk.TclError as e:
                colored_print(f'Ошибка удаления виджета - {self.clear_error}')
                pass

    @staticmethod
    def check_err(func):
        """
        Checks for errors before executing the function.
        :param func:
        :return:
        """
        def wrapper(*args, **kwargs):
            if args[0].error_add_win.get():
                return
            elif args[0].error.get():
                return
            result = func(*args, **kwargs)
            return result

        return wrapper

    @check_err
    def create_new_window(self, root, geometry: str = None, title: str = None):
        """
        Creates a window for adding words to lists.

        :param root: tkinter.Tk(), tkinter.TopLevel() or any same object
        :param geometry: size of window
        :param title: title of window
        :return:
        """

        message = f'Функция: {self.create_new_window.__name__} получила неверные параметры'
        try:
            new_window = create_top_level(root)
            if new_window is None:
                raise AttributeError
            new_window.geometry(geometry)
            new_window.title(title)
            new_window.lift(root)
            new_window.protocol('WM_DELETE_WINDOW',
                                lambda: self.confirm_cancel(new_window,
                                                            message='Вы уверены, что хотите прервать добавление слова?'))
            main_logger.info(f'Новое окно {title} было успешно создано')
            return new_window
        except (AttributeError, tk.TclError):
            colored_print(message, 'red', 'bright')
            exceptions_logger.error(message)

    def confirm_cancel(self, window, title='Подтвердите операцию', message: str = None):
        """
        Asks the user for confirmation to stop adding.

        :param window: tkinter.Tk(), tkinter.TopLevel() or any same object
        :param title: title of window
        :param message: text for displaying to user
        :return:
        """

        exception_message = f'Функция: {self.confirm_cancel.__name__} получила неверные параметры'
        try:
            if not isinstance(window, tk.Tk) or not isinstance(window, tk.Toplevel):
                raise AttributeError
            answer = messagebox.askquestion(title=title,
                                            message=message)
            window.focus_set()
            if self.window_is_active.get():
                self.window_is_active.set(False)

            self.error_add_win.set(False)
            if answer == 'yes':
                if len(self.FIRST_LANGUAGE_LIST) > len(self.SECOND_LANGUAGE_LIST):
                    self.FIRST_LANGUAGE_LIST.pop(-1)
                    self.update_listbox()
                window.destroy()
            main_logger.info('Операция была отменена')
        except (AttributeError,):
            exceptions_logger.error(exception_message)
            colored_print(message, color='red', style='bright')

    def add_word_to_list(self, word_widget, current_list: list, current_window):
        """
        Adds the written word to the word lists.

        :param word_widget: Widget for adding a word.
        :param current_list: List for adding a word.
        :param current_window:
        :return:
        """

        try:
            word = word_widget.get().strip().replace(', ', ',').replace(' , ', ',')

            if len(word) == 0:
                err = self.set_error(window=current_window, text='Вы не можете добавить пустое поле',
                                     error_status=self.error_add_win)
                err.grid(column=0, row=2)
                return
            elif word in self.FIRST_LANGUAGE_LIST:
                err = self.set_error(window=current_window, text='Это слово уже есть в списке',
                                     error_status=self.error_add_win)
                err.grid(column=0, row=2)
                return
            else:
                self.error_add_win.set(False)
                current_list.append(word)
                self.update_listbox()
                word_widget.delete(0, tk.END)
                current_window.destroy()

            if self.is_red_test is True and len(self.FIRST_LANGUAGE_LIST) == len(self.SECOND_LANGUAGE_LIST):
                add_word_in_db(word=self.FIRST_LANGUAGE_LIST[-1], translate=self.SECOND_LANGUAGE_LIST[-1])

            if current_list is self.SECOND_LANGUAGE_LIST:
                self.window_is_active.set(False)
            main_logger.info(f'Слово {word} было успешно добавлено.')
        except (AttributeError, TypeError) as e:
            message = f'Функция: {self.add_word_to_list.__name__} получила неверные параметры {e}'
            exceptions_logger.error(message)
            colored_print(message, 'red', 'bright')

    @check_err
    def create_add_window(self, new_window, label_text: str = None, words_list: list = None, is_second: bool = False):
        """
        Creates a new window for adding a word.

        :param new_window:
        :param label_text: title of window
        :param words_list: current list of window
        :param is_second: checker for sequential addition.
        :return:
        """

        try:
            label_for_adding_win = create_label(new_window, text=label_text, font=self.label_fonts['WordsOperation'])
            added_word = create_entry(new_window, width=30, font=self.text_fonts['EntryWidget'])
            add_button = create_button(new_window, text='Добавить',
                                       font=self.button_fonts['TestModeMenu']['WordsOperations']['Add_btn'],
                                       command=lambda: self.add_word_to_list(current_window=new_window,
                                                                             word_widget=added_word,
                                                                             current_list=words_list))

            if label_for_adding_win is None or added_word is None or add_button is None:
                raise AttributeError

            new_window.bind('<Return>',
                            lambda event: self.add_word_to_list(current_window=new_window, word_widget=added_word,
                                                                current_list=words_list))

            added_word.focus_set()
            label_for_adding_win.grid(column=0, row=0, sticky="nw", padx=10, pady=(15, 0))
            added_word.grid(column=0, row=1, padx=10, pady=10)
            add_button.grid(row=2, column=1, sticky="se", padx=10, pady=(0, 15))

            if is_second is False:
                add_button.configure(
                    command=lambda: (self.add_word_to_list(current_window=new_window, word_widget=added_word,
                                                           current_list=words_list), self.create_add_window(
                        new_window=self.create_new_window(
                            self.window,
                            geometry='400x120+800+400',
                            title='Добавление перевода'),
                        label_text='Добавьте перевод',
                        words_list=self.SECOND_LANGUAGE_LIST,
                        is_second=True)))

                new_window.bind('<Return>',
                                lambda event: (self.add_word_to_list(current_window=new_window, word_widget=added_word,
                                                                     current_list=words_list), self.create_add_window(
                                    new_window=self.create_new_window(
                                        self.window,
                                        geometry='400x120+800+400',
                                        title='Добавление перевода'),
                                    label_text='Добавьте перевод',
                                    words_list=self.SECOND_LANGUAGE_LIST,
                                    is_second=True)))

            main_logger.info('Функция добавления слова была запущена.')
        except (AttributeError,) as e:
            message = f'Функция: {self.create_add_window.__name__} получила неверные параметры {e}'
            exceptions_logger.error(message)
            colored_print(message, 'red', 'bright')

    @check_err
    def add_word_to_listwords(self):
        """
        Initiates the mechanism for adding a word to the word lists.
        :return:
        """

        if self.window_is_active.get() is False:
            self.window_is_active.set(True)
            checker = self.check_len_list()
            if checker[0] is False:
                self.err = self.set_error(checker[1], window=self.window,
                                          error_status=self.error)
                self.err.grid(column=0, row=4)

            win = self.create_new_window(self.window,
                                         geometry='400x120+800+400',
                                         title='Добавление тестируемого слова')

            self.create_add_window(win, label_text='Добавьте слово',
                                   words_list=self.FIRST_LANGUAGE_LIST)

    def update_listbox(self):
        """
        Updates the word lists in the user interface.
        :return:
        """

        self.first_words_list_widget.delete(0, tk.END)
        self.second_words_list_widget.delete(0, tk.END)

        for word in self.FIRST_LANGUAGE_LIST:
            self.first_words_list_widget.insert(tk.END, word)

        for word in self.SECOND_LANGUAGE_LIST:
            self.second_words_list_widget.insert(tk.END, word)

        main_logger.info('Listboxs были обновлены')

    def clear_lists(self):
        """
        Clears the word lists and errors.
        :return:
        """
        self.FIRST_LANGUAGE_LIST.clear()
        self.SECOND_LANGUAGE_LIST.clear()
        self.first_words_list_widget.delete(0, tk.END)
        self.second_words_list_widget.delete(0, tk.END)
        self.clear_error()
        if self.is_red_test is True:
            clear_cache_redlist()
        main_logger.info('Listboxes были очищены')
