from tkinter import Label, messagebox
import tkinter as tk
from app.fonts import FontManager
from app.other.db.json_functions import add_word_in_db, clear_cache_redlist
from app.config import main_logger, exceptions_logger


class ListBoxAdderClass:
    FIRST_LANGUAGE_LIST = []
    SECOND_LANGUAGE_LIST = []

    def __init__(self, master, is_red_test):
        self.window = master
        self.is_red_test = is_red_test

        self.text_var = tk.StringVar()
        self.error_add_win = tk.BooleanVar()
        self.error_add_win.set(False)
        self.error = tk.BooleanVar()
        self.error.set(False)
        self.err = tk.Label()

        # fonts configuration
        self.fonts = FontManager()
        self.label_fonts = self.fonts.LABEL_FONTS
        self.button_fonts = self.fonts.BUTTON_FONTS
        self.listbox_fonts = self.fonts.LISTBOX_FONTS
        self.text_fonts = self.fonts.TEXT_FONTS

        self.window_is_active = tk.BooleanVar()
        self.window_is_active.set(False)

        self.first_label = Label(self.window, text='Тестируемые слова', font=self.label_fonts['ListboxNames'])
        self.second_label = Label(self.window, text='Перевод тестируемых слов', font=self.label_fonts['ListboxNames'])

        self.first_label.grid(column=0, row=0)
        self.second_label.grid(column=1, row=0)

        self.first_words_list_widget = tk.Listbox(self.window, selectmode=tk.SINGLE, width=50, height=30,
                                                  font=self.listbox_fonts['WordsList'])
        self.second_words_list_widget = tk.Listbox(self.window, selectmode=tk.SINGLE, width=50, height=30,
                                                   font=self.listbox_fonts['WordsList'])

        self.first_words_list_widget.bind('<Enter>', self.first_words_list_widget.config(cursor='hand2'))
        self.second_words_list_widget.bind('<Enter>', self.second_words_list_widget.config(cursor='hand2'))

        self.first_words_list_widget.grid(column=0, row=1, padx=(0, 10))
        self.second_words_list_widget.grid(column=1, row=1)

        self.frame = tk.Frame(self.window)
        self.frame.grid(column=2, row=1, pady=(0, 180), padx=(30, 0))
        self.add_word_btn = tk.Button(self.frame, text='Добавить слова', width=20, height=2,
                                      font=self.button_fonts['TestModeMenu']['WordsOperations']['Add_btn'],
                                      command=self.add_word_to_listwords)
        self.add_word_btn.pack(pady=(0, 10))
        main_logger.info(f'Класс {ListBoxAdderClass.__name__} был успешно инициализирован.')

    def check_len_list(self):
        if len(self.SECOND_LANGUAGE_LIST) >= 30 and self.is_red_test is True:
            return False, 'Вы не можете добавить больше 30 слов!'
        elif len(self.SECOND_LANGUAGE_LIST) >= 100:
            return False, 'Вы не можете добавить больше 100 слов!'
        else:
            return True,

    def set_error(self, text, window, error_status):
        self.text_var.set(text)
        error_label = Label(window, textvariable=self.text_var, fg='red', font=self.label_fonts['Errors'])
        error_status.set(True)
        return error_label

    def clear_error(self):
        self.error.set(False)
        if self.error.get() is False:
            try:
                self.err.destroy()
            except tk.TclError as e:
                print(e, self.clear_error)
                pass

    @staticmethod
    def check_err(func):
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
        new_window = tk.Toplevel(root)
        new_window.geometry(geometry)
        new_window.title(title)
        new_window.lift(root)
        new_window.protocol('WM_DELETE_WINDOW',
                            lambda: self.confirm_cancel(new_window,
                                                        message='Вы уверены, что хотите прервать добавление слова?'))
        main_logger.info(f'Новое окно {title} было успешно создано')
        return new_window

    def confirm_cancel(self, window, title='Подтвердите операцию', message=None):
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

    def add_word_to_list(self, word_widget, current_list: list, current_window):
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

    @check_err
    def create_add_window(self, new_window,
                          label_text: str = None,
                          words_list: list = None,
                          is_second=False):

        label_for_adding_win = Label(new_window, text=label_text, font=self.label_fonts['WordsOperation'])
        label_for_adding_win.grid(column=0, row=0, sticky="nw", padx=10, pady=(15, 0))

        added_word = tk.Entry(new_window, width=30, font=self.text_fonts['EntryWidget'])
        added_word.focus_set()
        added_word.grid(column=0, row=1, padx=10, pady=10)

        add_button = tk.Button(new_window, text='Добавить',
                               font=self.button_fonts['TestModeMenu']['WordsOperations']['Add_btn'],
                               command=lambda: self.add_word_to_list(current_window=new_window, word_widget=added_word,
                                                                     current_list=words_list))
        new_window.bind('<Return>',
                        lambda event: self.add_word_to_list(current_window=new_window, word_widget=added_word,
                                                            current_list=words_list))

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

    @check_err
    def add_word_to_listwords(self):
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
        self.first_words_list_widget.delete(0, tk.END)
        self.second_words_list_widget.delete(0, tk.END)

        for word in self.FIRST_LANGUAGE_LIST:
            self.first_words_list_widget.insert(tk.END, word)

        for word in self.SECOND_LANGUAGE_LIST:
            self.second_words_list_widget.insert(tk.END, word)

        main_logger.info('Listboxs были обновлены')

    def clear_lists(self):
        self.FIRST_LANGUAGE_LIST.clear()
        self.SECOND_LANGUAGE_LIST.clear()
        self.first_words_list_widget.delete(0, tk.END)
        self.second_words_list_widget.delete(0, tk.END)
        self.clear_error()
        if self.is_red_test is True:
            clear_cache_redlist()
        main_logger.info('Listboxs были очищены')
