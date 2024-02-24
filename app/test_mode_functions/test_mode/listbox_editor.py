import tkinter as tk
from tkinter import Label, filedialog, messagebox
from app.other.instruction.instructions import set_instruction_field
from app.test_mode_functions.test_mode_choose import TestModeChooseClass
from docx import Document
from pandas import read_excel
from app.other.json_functions import add_words_to_lists, delete_word_from_cache, clear_cache, edit_word_in_json


class ListBoxAdderClass:
    is_visible = False
    FIRST_LANGUAGE_LIST = []
    SECOND_LANGUAGE_LIST = []

    def __init__(self, master, is_red_test):
        self.window = master
        self.is_red_test = is_red_test

        # error text field
        self.text_var = tk.StringVar()

        self.first_label = Label(self.window, text='Тестируемые слова')
        self.second_label = Label(self.window, text='Перевод тестируемых слов')

        self.first_label.grid(column=0, row=0)
        self.second_label.grid(column=1, row=0)

        self.first_words_list_widget = tk.Listbox(self.window, selectmode=tk.SINGLE, width=30, height=20)
        self.first_words_list_widget.grid(column=0, row=1, padx=(0, 10))

        self.second_words_list_widget = tk.Listbox(self.window, selectmode=tk.SINGLE, width=30, height=20)
        self.second_words_list_widget.grid(column=1, row=1)
        self.add_word_btn = tk.Button(self.window, text='Добавить слова', width=20, height=2,
                                      command=self.add_word_to_listwords)

        self.add_word_btn.grid(column=0, row=2, columnspan=2, pady=(15, 0))

        self.error_add_win = tk.BooleanVar()
        self.error_add_win.set(False)
        self.error = tk.BooleanVar()
        self.error.set(False)

    def set_error(self, text, window, error_status):
        self.text_var.set(text)
        error_label = Label(window, textvariable=self.text_var, fg='red')
        error_status.set(True)
        return error_label

    def clear_error(self):
        self.error.set(False)
        if self.error.get() is False:
            try:
                self.err.destroy()
            except Exception:
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
        new_window.protocol('WM_DELETE_WINDOW', lambda: self.cancel_adding(new_window))
        return new_window

    def cancel_adding(self, window):
        answer = messagebox.askquestion(title='Подтвердите операцию',
                                        message="Вы уверены, что хотите прервать добавление слова?")
        window.focus_set()
        if answer == 'yes':
            if len(self.FIRST_LANGUAGE_LIST) > len(self.SECOND_LANGUAGE_LIST):
                self.FIRST_LANGUAGE_LIST.pop(-1)
                self.update_listbox()
            window.destroy()
        else:
            pass

    def add_word_to_list(self, word_widget, current_list: list, current_window):
        word = word_widget.get().strip()

        if len(word) == 0:
            err = self.set_error(window=current_window, text='Вы не можете добавить пустое поле',
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
            add_words_to_lists(word=self.FIRST_LANGUAGE_LIST[-1], translate=self.SECOND_LANGUAGE_LIST[-1])

    @check_err
    def create_add_window(self, new_window,
                          label_text: str = None,
                          words_list: list = None,
                          is_second=False):

        label_for_adding_win = Label(new_window, text=label_text)
        label_for_adding_win.grid(column=0, row=0, sticky="nw", padx=10, pady=(15, 0))

        added_word = tk.Entry(new_window, width=30)
        added_word.grid(column=0, row=1, padx=10, pady=10)

        add_button = tk.Button(new_window, text='Добавить',
                               command=lambda: self.add_word_to_list(current_window=new_window, word_widget=added_word,
                                                                     current_list=words_list))
        add_button.grid(row=2, column=1, sticky="se", padx=10, pady=(0, 15))

        if not is_second:
            add_button.configure(
                command=lambda: (self.add_word_to_list(current_window=new_window, word_widget=added_word,
                                                       current_list=words_list), self.create_add_window(
                    new_window=self.create_new_window(
                        self.window,
                        geometry='300x120+800+400',
                        title='Добавление перевода'),
                    label_text='Добавьте перевод',
                    words_list=self.SECOND_LANGUAGE_LIST,
                    is_second=True)))

    @check_err
    def add_word_to_listwords(self):

        if len(self.SECOND_LANGUAGE_LIST) >= 100:
            self.err = self.set_error('Вы не можете добавить больше 100 слов!', window=self.window,
                                      error_status=self.error)
            self.err.grid(column=0, row=4)
        elif len(self.SECOND_LANGUAGE_LIST) >= 2 and self.is_red_test is True:
            self.err = self.set_error('Вы не можете добавить больше 30 слов!', window=self.window,
                                      error_status=self.error)
            self.err.grid(column=0, row=4)

        win = self.create_new_window(self.window,
                                     geometry='300x120+800+400',
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

        print('ListBoxes has been updated')

    def clear_lists(self):
        self.FIRST_LANGUAGE_LIST.clear()
        self.SECOND_LANGUAGE_LIST.clear()
        self.first_words_list_widget.delete(0, tk.END)
        self.second_words_list_widget.delete(0, tk.END)
        self.clear_error()
        self.is_visible = False
        if self.is_red_test is True:
            clear_cache()


class FileLoaderClass(ListBoxAdderClass):

    def __init__(self, master, is_red_test):
        super().__init__(master=master, is_red_test=is_red_test)

        self.upload_button = tk.Button(self.window, text='Загрузить слова из файла',
                                       height=2, width=30, command=self.download_words_from_file)
        self.upload_button.grid(column=0, row=3, columnspan=2, pady=(15, 0))
        self.error_file = tk.BooleanVar()
        self.error_file.set(False)

    def download_words_from_file(self):
        win = TestModeChooseClass(self.window)
        win.label.configure(text='Выберите формат файла')

        set_instruction_field(window=win.window, text='Перед загрузкой ознакомьтесь с моей инструкцией по загрузке'),

        win.create_test_mode_button('TXT', func=(self.load_from_txt,), side_button='left', padx=15)
        win.create_test_mode_button('WORD', func=(self.load_from_word,), side_button='left', padx=45)
        win.create_test_mode_button('EXCEL', func=(self.load_from_excel,), side_button='right', padx=15)

    def packing_words(self, words_list, excel=False):
        if excel is True:
            for word in words_list:
                if len(self.FIRST_LANGUAGE_LIST) >= 100 or len(self.SECOND_LANGUAGE_LIST) >= 100:
                    break
                elif (len(self.FIRST_LANGUAGE_LIST) >= 30 and self.is_red_test is True
                      or len(self.SECOND_LANGUAGE_LIST) >= 30 and self.is_red_test is True):
                    break
                try:
                    first_word = word[0].replace('\n', '').strip()
                    second_word = word[1].replace('\n', '').strip()
                    self.FIRST_LANGUAGE_LIST.append(first_word)
                    self.SECOND_LANGUAGE_LIST.append(second_word)
                except IndexError:
                    continue
        else:
            for word in words_list:
                if len(self.FIRST_LANGUAGE_LIST) >= 100 or len(self.SECOND_LANGUAGE_LIST) >= 100:
                    break
                elif (len(self.FIRST_LANGUAGE_LIST) >= 30 and self.is_red_test is True
                      or len(self.SECOND_LANGUAGE_LIST) >= 30 and self.is_red_test is True):
                    break
                try:
                    dash = word.index('-')
                    first_word = word[:dash].replace('\n', '').strip()
                    second_word = word[dash + 1:].replace('\n', '').strip()
                    self.FIRST_LANGUAGE_LIST.append(first_word)
                    self.SECOND_LANGUAGE_LIST.append(second_word)
                except Exception as e:
                    pass
        self.update_listbox()

    @staticmethod
    def enter_file(func):
        def wrapper(*args, **kwargs):
            filepath = filedialog.askopenfilename()
            try:
                kwargs['filepath'] = filepath
                result = func(*args, **kwargs)
                return result
            except FileNotFoundError:
                error = args[0].set_error(text='Некорректно выбран файл', window=args[0].window,
                                          error_status=args[0].error_add_win)
                error.grid(column=0, row=4)

        return wrapper

    @enter_file
    def load_from_txt(self, filepath=None):
        with open(filepath, 'r', encoding='utf-8') as file:
            words = file.read()
            list_words = words.split(';')
            self.packing_words(words_list=list_words)

    @enter_file
    def load_from_word(self, filepath=None):
        doc = Document(filepath)
        list_words = [paragraph.text for paragraph in doc.paragraphs]
        if len(list_words) == 1:
            list_words = list_words[0].split(';')
        self.packing_words(list_words)

    @enter_file
    def load_from_excel(self, filepath=None):
        list_words_excel = read_excel(filepath).values
        self.packing_words(words_list=list_words_excel, excel=True)


class ListBoxEditor(FileLoaderClass):

    def __init__(self, master, is_red_test):
        super().__init__(master, is_red_test)

        self.first_words_list_widget.bind('<<ListboxSelect>>', self.edit_selected_word)
        self.second_words_list_widget.bind('<<ListboxSelect>>', self.edit_selected_word)

    def edit_selected_word(self, event):
        selected_index = event.widget.curselection()
        if selected_index:
            self.edit_field_create(event.widget)
            selected_word = event.widget.get(selected_index[0])
            self.edit_entry.delete(0, tk.END)
            self.edit_entry.insert(tk.END, selected_word)

    def edit_field_create(self, current_listbox=None):
        if self.is_visible:
            return

        self.edit_entry = tk.Entry(self.window, width=30)
        self.confirm_button = tk.Button(self.window, text="Редактировать")
        self.delete_word_button = tk.Button(self.window, text="Удалить")

        if current_listbox:
            self.confirm_button.configure(command=lambda: self.confirm_edit(current_widget=current_listbox))
            self.delete_word_button.configure(command=lambda: self.delete_word(current_widget=current_listbox))
        else:
            print('Error')

        self.edit_entry.grid(column=3, row=1, pady=(0, 10))
        self.confirm_button.grid(column=4, row=1, padx=(10, 0), pady=(0, 15))
        self.delete_word_button.grid(column=5, row=1, padx=(10, 0), pady=(0, 15))
        self.is_visible = True

    def edit_field_destroy(self):
        self.edit_entry.destroy()
        self.confirm_button.destroy()
        self.delete_word_button.destroy()
        self.is_visible = False

    def confirm_edit(self, current_widget=None):
        edited_word = self.edit_entry.get().strip()
        selected_index = current_widget.curselection()
        widget_name = str(current_widget)

        if widget_name[-1] != '2':
            current_list = self.FIRST_LANGUAGE_LIST
        else:
            current_list = self.SECOND_LANGUAGE_LIST

        if selected_index:
            if self.is_red_test is True:
                edit_word_in_json(current_list[selected_index[0]], edited_word)
            current_list[selected_index[0]] = edited_word
            self.update_listbox()
            self.edit_field_destroy()

    def delete_word(self, current_widget=None):
        selected_index = current_widget.curselection()

        if selected_index:
            if self.is_red_test is True:
                delete_word_from_cache(deleted_word=self.FIRST_LANGUAGE_LIST[selected_index[0]])

            self.FIRST_LANGUAGE_LIST.pop(selected_index[0])
            self.SECOND_LANGUAGE_LIST.pop(selected_index[0])
            self.update_listbox()
            self.edit_field_destroy()

        self.is_visible = False
        self.clear_error()
