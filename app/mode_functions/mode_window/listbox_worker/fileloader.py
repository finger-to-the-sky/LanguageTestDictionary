from tkinter import filedialog, messagebox
from docx import Document
from docx.opc.exceptions import PackageNotFoundError
from pandas import read_excel
from app.config import cache_files_db, main_logger
from app.logger import exceptions_logger
from app.other.custom_print import colored_print
from app.other.instruction.instructions import set_instruction_field
from app.other.db.json_functions import clear_cache_filenames_db, download_file_from_cache, add_word_in_db, \
    cache_current_file
from app.mode_functions.mode_window.listbox_worker.adder import ListBoxAdderClass
import tkinter as tk
from app.mode_functions.choose_window import WindowChooseClass
from app.tk_functions import create_button, create_listbox


class FileLoaderClass(ListBoxAdderClass):

    def __init__(self, master, is_red_test: bool):
        """
        :param master: tkinter.Tk(), tkinter.TopLevel() or any same object
        :param is_red_test: Status for determining the mode.
        """

        try:
            super().__init__(master=master, is_red_test=is_red_test)

            self.upload_button = create_button(root=self.frame, text='Загрузить слова из файла',
                                               font=self.button_fonts['TestModeMenu']['Download_btn'],
                                               height=2, width=30, command=self.download_words_from_file)
            self.cache_button = create_button(root=self.frame, text='История файлов',
                                              font=self.button_fonts['TestModeMenu']['Cache_btn'],
                                              height=2, width=30, command=self.create_cache_window)
            self.upload_button.pack(pady=(0, 10))
            self.cache_button.pack(pady=(0, 10))
            self.cache_listbox = None
            if self.upload_button is None and self.cache_button is None:
                raise AttributeError
            main_logger.info(f'Класс {FileLoaderClass.__name__} был успешно инициализирован.')
        except (AttributeError,) as e:
            message = f'Класс: {FileLoaderClass.__name__} принял неверные параметры {e}'
            colored_print(message, 'red', 'bright')
            exceptions_logger.error(message)

    def create_cache_window(self):
        """
        Creates a window for managing cached files with words.
        :return:
        """
        if self.window_is_active.get() is False:
            self.window_is_active.set(True)
            win = self.create_new_window(self.window, geometry='800x500')
            win.protocol('WM_DELETE_WINDOW',
                         lambda: self.confirm_cancel(win,
                                                     message='Вы уверены, что хотите прервать загрузку слов?')),

            download_button = create_button(root=win, text='Загрузить',
                                            font=self.button_fonts['CacheWindowButtons']['DownloadCache_btn'],
                                            command=lambda: (self.download_from_cache(),
                                                             win.destroy(),
                                                             self.window_is_active.set(False),
                                                             self.window.focus_set()))
            clear_button = create_button(root=win, text='Очистить кэш',
                                         font=self.button_fonts['CacheWindowButtons']['ClearCache_btn'],
                                         command=lambda: (clear_cache_filenames_db(),
                                                          self.cache_listbox.delete(0, tk.END),
                                                          self.window_is_active.set(False),
                                                          win.destroy(),
                                                          self.window.focus_set()))
            self.cache_listbox = create_listbox(root=win, width=80, selectmode=tk.SINGLE,
                                                font=self.listbox_fonts['CachingWindow'])
            self.cache_listbox.pack(pady=(50, 10))
            download_button.pack(pady=15)
            clear_button.pack()

            files = cache_files_db.all()
            for data in files:
                self.cache_listbox.insert(tk.END, data['filepath'])
            main_logger.info("Окно кэширования файлов было успешно создано")

    def download_from_cache(self):
        """
        Loads the selected words from the list.
        :return:
        """
        selected_index = self.cache_listbox.curselection()
        try:
            filepath = self.cache_listbox.get(selected_index[0])
            words = download_file_from_cache(filepath)
            for w in words:
                self.FIRST_LANGUAGE_LIST.append(w['word'])
                self.SECOND_LANGUAGE_LIST.append(w['translate'])
            self.update_listbox()
            main_logger.info('Загрузка слов из кеширования прошла успешно')
        except IndexError:
            message = 'Ошибка выделенного обьекта. Пользователь не выделил обьект в Listbox'
            colored_print(message, color='red', style='bright')
            exceptions_logger.error(f'{message} {self.download_from_cache.__name__}')

    def download_words_from_file(self):
        """
        Loads words from a file in the selected format.
        :return:
        """
        if self.window_is_active.get() is False:
            self.window_is_active.set(True)

            win = WindowChooseClass(self.window)
            win.window.protocol("WM_DELETE_WINDOW", lambda: (self.window_is_active.set(False), win.window.destroy()))
            win.label.configure(text='Выберите формат файла')

            set_instruction_field(window=win.window,
                                  text='Перед загрузкой ознакомьтесь с моей инструкцией по загрузке'),

            first = win.create_choose_button('TXT')
            second = win.create_choose_button('WORD')
            third = win.create_choose_button('EXCEL')

            first.configure(command=lambda: (self.load_from_txt(), win.window.destroy()))
            second.configure(command=lambda: (self.load_from_word(), win.window.destroy()))
            third.configure(command=lambda: (self.load_from_excel(), win.window.destroy()))

            first.pack(side='left', padx=15, ipady=60)
            second.pack(side='left', padx=45, ipady=60)
            third.pack(side='right', padx=15, ipady=60)

    def packing_words(self, words_list, excel=False):
        """
        Validates the received list of words by splitting it into class lists according to the file format from which
         the words were obtained.

        :param words_list: Special word list obtained from a file.
        :param excel: Status for supporting work with xlsx files.
        :return:
        """

        try:
            cache_words_list = []

            for word in words_list:
                checker = self.check_len_list()
                if checker[0] is False:
                    break
                if excel is True:
                    try:
                        first_word = word[0].replace('\n', '').strip().replace(' , ', ',').replace(', ', ',')
                        if first_word in self.FIRST_LANGUAGE_LIST:
                            continue

                        second_word = word[1].replace('\n', '').strip().replace(' , ', ',').replace(', ', ',')
                        if self.is_red_test is True:
                            add_word_in_db(word=first_word, translate=second_word)

                        self.FIRST_LANGUAGE_LIST.append(first_word)
                        self.SECOND_LANGUAGE_LIST.append(second_word)
                        cache_words_list.append({'word': first_word, 'translate': second_word})

                    except IndexError:
                        message = 'Не было обнаружено перевода'
                        exceptions_logger.error(f'{message} {self.packing_words.__name__}')
                        continue
                else:
                    try:
                        dash = word.index('-')
                        first_word = word[:dash].replace('\n', '').strip().replace(' , ', ',').replace(', ', ',')
                        if first_word in self.FIRST_LANGUAGE_LIST:
                            continue

                        second_word = word[dash + 1:].replace('\n', '').strip().replace(' , ', ',').replace(', ', ',')
                        if second_word[-1] == ';':
                            second_word = second_word[:-1]

                        if self.is_red_test is True:
                            add_word_in_db(word=first_word, translate=second_word)

                        self.FIRST_LANGUAGE_LIST.append(first_word)
                        self.SECOND_LANGUAGE_LIST.append(second_word)
                        cache_words_list.append({'word': first_word, 'translate': second_word})
                    except ValueError:
                        pass

            self.update_listbox()
            main_logger.info('Все слова из файла были успешно загружены.')
            return cache_words_list
        except (AttributeError, TypeError) as e:
            message = f'{self.packing_words.__name__} {e}'
            colored_print(message, 'red', 'bright')
            exceptions_logger.error(message)

    @staticmethod
    def enter_file(func):
        """
        Decorator for requesting a file for file-handling functions.
        :param func:
        :return:
        """
        def wrapper(*args, **kwargs):
            filepath = filedialog.askopenfilename()
            result = None
            try:
                if filepath:
                    kwargs['filepath'] = filepath
                result = func(*args, **kwargs)
            except (FileNotFoundError, PackageNotFoundError, UnicodeDecodeError):
                messagebox.showerror(title='Ошибка', message='Некорректно выбран файл')
                exceptions_logger.error(f'Некорректно выбран файл. enter_file')
            except (TypeError, AttributeError, OSError, tk.TclError) as e:
                message = f'Функция: {func.__name__} получила неверные аргументы {e}'
                colored_print(message, 'red', 'bright')
                exceptions_logger.error(message)


            args[0].window_is_active.set(False)
            args[0].window.focus_set()

            return result

        return wrapper

    @enter_file
    def load_from_txt(self, filepath=None):
        """
        Function for retrieving words from a txt file.

        :param filepath:
        :return:
        """

        try:
            with open(filepath, 'r', encoding='utf-8') as file:
                words = file.read()
                list_words = words.split(';')
                words = self.packing_words(words_list=list_words)
                cache_current_file(filepath=filepath, words_list=words)
        except (TypeError, AttributeError, OSError) as e:
            message = f'Функция: {self.load_from_txt.__name__} получила неверные аргументы {e}'
            colored_print(message, 'red', 'bright')
            exceptions_logger.error(message)

    @enter_file
    def load_from_word(self, filepath=None):
        """
        Function for retrieving words from doc/docx file.

        :param filepath:
        :return:
        """

        try:
            doc = Document(filepath)
            list_words = [paragraph.text for paragraph in doc.paragraphs]
            if len(list_words) == 1:
                list_words = list_words[0].split(';')
            words = self.packing_words(list_words)
            cache_current_file(filepath=filepath, words_list=words)
        except ValueError:
            messagebox.showerror(title='Ошибка',
                                 message='Функция загрузки word поддерживает только форматы doc или docx')
            exceptions_logger.error(f'Выбран неверный формат файла. {self.load_from_word.__name__}')
        except (TypeError, AttributeError, OSError) as e:
            message = f'Функция: {self.load_from_word.__name__} получила неверные аргументы {e}'
            colored_print(message, 'red', 'bright')
            exceptions_logger.error(message)

    @enter_file
    def load_from_excel(self, filepath=None):
        """
        Function for retrieving words from a xlsx file.

        :param filepath:
        :return:
        """

        try:
            list_words_excel = read_excel(filepath).values
            words = self.packing_words(words_list=list_words_excel, excel=True)
            cache_current_file(filepath=filepath, words_list=words)
        except ValueError:
            messagebox.showerror(title='Ошибка',
                                 message='Функция загрузки excel поддерживает только формат xlsx')
            exceptions_logger.error(f'Выбран неверный формат файла. {self.load_from_excel.__name__}')
        except (TypeError, AttributeError, OSError) as e:
            message = f'Функция: {self.load_from_excel.__name__} получила неверные аргументы {e}'
            colored_print(message, 'red', 'bright')
            exceptions_logger.error(message)
