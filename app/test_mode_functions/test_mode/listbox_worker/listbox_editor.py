import tkinter as tk
from tkinter import Label
from app.test_mode_functions.test_mode.listbox_worker.fileloader import FileLoaderClass
from app.other.db.json_functions import edit_word_in_db, delete_word_in_db


class ListBoxEditor(FileLoaderClass):

    def __init__(self, master, is_red_test):
        super().__init__(master, is_red_test)
        self.edit_entry = None
        self.confirm_button = None
        self.delete_word_button = None
        self.label_for_edit_win = None
        self.first_words_list_widget.bind('<<ListboxSelect>>', self.edit_selected_word)
        self.second_words_list_widget.bind('<<ListboxSelect>>', self.edit_selected_word)

    def create_edit_window(self, new_window, current_listbox,
                           label_text: str = None,
                           words_list: list = None,
                           is_second=False):
        self.label_for_edit_win = Label(new_window, text=label_text)
        self.label_for_edit_win.grid(column=0, row=0, sticky="nw", padx=10, pady=(15, 0))

        self.edit_entry = tk.Entry(new_window, width=30)
        self.confirm_button = tk.Button(new_window, text="Редактировать")
        self.delete_word_button = tk.Button(new_window, text="Удалить")

        if current_listbox:
            self.confirm_button.configure(
                command=lambda: (self.confirm_edit(current_widget=current_listbox), new_window.destroy()))
            self.delete_word_button.configure(
                command=lambda: (self.delete_word(current_widget=current_listbox), new_window.destroy()))
        else:
            print('Undefined current listbox')

        self.edit_entry.grid(column=0, row=1, padx=10, pady=10)
        self.confirm_button.grid(row=2, column=1, sticky="se", padx=10, pady=(0, 15))
        self.delete_word_button.grid(row=2, column=2, sticky="se", padx=10, pady=(0, 15))

    def edit_selected_word(self, event):
        if len(self.FIRST_LANGUAGE_LIST) == 0:
            return

        if self.window_is_active.get() is False:
            selected_index = event.widget.curselection()
            nw = self.create_new_window(root=self.window, geometry='400x120+800+400',
                                        title='Редактирование тестируемого слова')

            nw.protocol('WM_DELETE_WINDOW',
                        lambda: self.confirm_cancel(nw,
                                                    message='Вы уверены, что хотите прервать редактирование слова?'))

            if selected_index:
                self.create_edit_window(new_window=nw, words_list=self.FIRST_LANGUAGE_LIST,
                                        label_text='Введите слово',
                                        current_listbox=event.widget)

                selected_word = event.widget.get(selected_index[0])
                self.edit_entry.delete(0, tk.END)
                self.edit_entry.insert(tk.END, selected_word)
                self.window_is_active.set(True)
            else:
                nw.destroy()
        else:
            return

    def confirm_edit(self, current_widget=None):
        edited_word = self.edit_entry.get().strip().replace(', ', ',').replace(' , ', ',')
        selected_index = current_widget.curselection()
        widget_name = str(current_widget)

        if widget_name[-1] != '2':
            current_list = self.FIRST_LANGUAGE_LIST
        else:
            current_list = self.SECOND_LANGUAGE_LIST

        if selected_index:
            if self.is_red_test is True:
                edit_word_in_db(current_list[selected_index[0]], edited_word)
            current_list[selected_index[0]] = edited_word
            self.update_listbox()
        self.window_is_active.set(False)

    def delete_word(self, current_widget=None):
        selected_index = current_widget.curselection()
        if selected_index:
            if self.is_red_test is True:
                delete_word_in_db(deleted_word=self.FIRST_LANGUAGE_LIST[selected_index[0]])

            self.FIRST_LANGUAGE_LIST.pop(selected_index[0])
            self.SECOND_LANGUAGE_LIST.pop(selected_index[0])
            self.update_listbox()
        self.window_is_active.set(False)
