from tkinter import filedialog, messagebox
from docx import Document
from docx.opc.exceptions import PackageNotFoundError
from pandas import read_excel
from app.config import cache_files_db
from app.other.instruction.instructions import set_instruction_field
from app.other.db.json_functions import clear_cache_filenames_db, download_file_from_cache, add_word_in_db, \
    cache_current_file
from app.test_mode_functions.test_mode.listbox_worker.adder import ListBoxAdderClass
import tkinter as tk

from app.test_mode_functions.test_mode_choose import TestModeChooseClass


class FileLoaderClass(ListBoxAdderClass):

    def __init__(self, master, is_red_test):
        super().__init__(master=master, is_red_test=is_red_test)

        self.upload_button = tk.Button(self.frame, text='Загрузить слова из файла',
                                       height=2, width=30, command=self.download_words_from_file)
        self.cache_button = tk.Button(self.frame, text='История файлов',
                                      height=2, width=30, command=self.create_cache_window)
        self.upload_button.pack(pady=(0, 10))
        self.cache_button.pack(pady=(0, 10))
        self.cache_listbox = None

    def create_cache_window(self):
        if self.window_is_active.get() is False:
            self.window_is_active.set(True)
            win = self.create_new_window(self.window, geometry='700x500')
            win.protocol('WM_DELETE_WINDOW',
                         lambda: self.confirm_cancel(win,
                                                     message='Вы уверены, что хотите прервать загрузку слов?')),

            download_button = tk.Button(win, text='Загрузить', command=lambda: (self.download_from_cache(),
                                                                                win.destroy(),
                                                                                self.window_is_active.set(False),
                                                                                self.window.focus_set()))
            clear_button = tk.Button(win, text='Очистить кэш', command=lambda: (clear_cache_filenames_db(),
                                                                                self.cache_listbox.delete(0, tk.END),
                                                                                self.window_is_active.set(False),
                                                                                win.destroy(),
                                                                                self.window.focus_set()))
            self.cache_listbox = tk.Listbox(win, width=100, selectmode=tk.SINGLE)
            self.cache_listbox.pack(pady=(50, 10))
            download_button.pack(pady=15)
            clear_button.pack()

            files = cache_files_db.all()
            for data in files:
                self.cache_listbox.insert(tk.END, data['filepath'])

    def download_from_cache(self):
        selected_index = self.cache_listbox.curselection()
        try:
            filepath = self.cache_listbox.get(selected_index[0])
            words = download_file_from_cache(filepath)
            for w in words:
                self.FIRST_LANGUAGE_LIST.append(w['word'])
                self.SECOND_LANGUAGE_LIST.append(w['translate'])
            self.update_listbox()
        except IndexError:
            pass

    def download_words_from_file(self):
        if self.window_is_active.get() is False:
            self.window_is_active.set(True)

            win = TestModeChooseClass(self.window)
            win.window.protocol("WM_DELETE_WINDOW", lambda: (self.window_is_active.set(False), win.window.destroy()))
            win.label.configure(text='Выберите формат файла')

            set_instruction_field(window=win.window,
                                  text='Перед загрузкой ознакомьтесь с моей инструкцией по загрузке'),

            win.create_test_mode_button('TXT', func=(self.load_from_txt,), side='left', padx=15)
            win.create_test_mode_button('WORD', func=(self.load_from_word,), side='left', padx=45)
            win.create_test_mode_button('EXCEL', func=(self.load_from_excel,), side='right', padx=15)

    def packing_words(self, words_list, excel=False):
        cache_words_list = []

        for word in words_list:
            checker = self.check_len_list()
            if checker[0] is False:
                break
            if excel is True:
                try:
                    first_word = word[0].replace('\n', '').strip()
                    if first_word in self.FIRST_LANGUAGE_LIST:
                        continue

                    second_word = word[1].replace('\n', '').strip()
                    if self.is_red_test is True:
                        add_word_in_db(word=first_word, translate=second_word)

                    self.FIRST_LANGUAGE_LIST.append(first_word)
                    self.SECOND_LANGUAGE_LIST.append(second_word)
                    cache_words_list.append({'word': first_word, 'translate': second_word})

                except IndexError:
                    continue
            else:
                try:
                    dash = word.index('-')
                    first_word = word[:dash].replace('\n', '').strip()
                    if first_word in self.FIRST_LANGUAGE_LIST:
                        continue

                    second_word = word[dash + 1:].replace('\n', '').strip()
                    if second_word[-1] == ';':
                        second_word = second_word[:-1]

                    if self.is_red_test is True:
                        add_word_in_db(word=first_word, translate=second_word)

                    self.FIRST_LANGUAGE_LIST.append(first_word)
                    self.SECOND_LANGUAGE_LIST.append(second_word)
                    cache_words_list.append({'word': first_word, 'translate': second_word})
                except Exception:
                    pass

        self.update_listbox()
        return cache_words_list

    @staticmethod
    def enter_file(func):
        def wrapper(*args, **kwargs):
            filepath = filedialog.askopenfilename()
            result = None
            try:
                kwargs['filepath'] = filepath
                result = func(*args, **kwargs)
            except (FileNotFoundError, PackageNotFoundError, UnicodeDecodeError):
                messagebox.showerror(title='Ошибка', message='Некорректно выбран файл')

            args[0].window_is_active.set(False)
            args[0].window.focus_set()
            return result
        return wrapper

    @enter_file
    def load_from_txt(self, filepath=None):
        with open(filepath, 'r', encoding='utf-8') as file:
            words = file.read()
            list_words = words.split(';')
            words = self.packing_words(words_list=list_words)
            cache_current_file(filepath=filepath, words_list=words)

    @enter_file
    def load_from_word(self, filepath=None):
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

    @enter_file
    def load_from_excel(self, filepath=None):
        try:
            list_words_excel = read_excel(filepath).values
            words = self.packing_words(words_list=list_words_excel, excel=True)
            cache_current_file(filepath=filepath, words_list=words)
        except ValueError:
            messagebox.showerror(title='Ошибка',
                                 message='Функция загрузки excel поддерживает только формат xlsx')
