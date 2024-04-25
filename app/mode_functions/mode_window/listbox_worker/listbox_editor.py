import tkinter as tk
from app.config import main_logger
from app.logger import exceptions_logger
from app.other.custom_print import colored_print
from app.mode_functions.mode_window.listbox_worker.fileloader import FileLoaderClass
from app.other.db.json_functions import edit_word_in_db, delete_word_in_db
from app.tk_functions import create_button, create_entry, create_label


class ListBoxEditor(FileLoaderClass):
    """
    Main class for working with word lists, which includes all the functionality + methods for editing words
    within the lists.
    """

    def __init__(self, master, is_red_test):
        """
        :param master: tkinter.Tk(), tkinter.TopLevel() or any same object
        :param is_red_test: Status for determining the mode.
        """

        try:
            super().__init__(master, is_red_test)
            self.edit_entry = None
            self.confirm_button = None
            self.delete_word_button = None
            self.label_for_edit_win = None
            self.first_words_list_widget.bind('<<ListboxSelect>>', self.edit_selected_word)
            self.second_words_list_widget.bind('<<ListboxSelect>>', self.edit_selected_word)
            main_logger.info(f'Класс: {ListBoxEditor.__name__} был успешно инициализирован.')
        except (AttributeError,) as e:
            message = f'Класс: {ListBoxEditor.__name__} получил неверные параметры {e}'
            colored_print(message, 'red', 'bright')
            exceptions_logger.error(message)

    def create_edit_window(self, new_window, current_listbox: tk.Listbox,
                           label_text: str = None):
        """
        Creates a window for editing words in the word list.

        :param new_window: tkinter.Tk(), tkinter.TopLevel() or any same object
        :param current_listbox: tk.Listbox() - Listbox in which user has edit word
        :param label_text: Text for desc
        :return:
        """
        try:
            self.label_for_edit_win = create_label(root=new_window, text=label_text,
                                                   font=self.label_fonts['WordsOperation'])
            self.label_for_edit_win.grid(column=0, row=0, sticky="nw", padx=10, pady=(15, 0))

            self.edit_entry = create_entry(root=new_window, width=30, font=('Helvetica', 10))
            self.confirm_button = create_button(root=new_window, text="Редактировать",
                                                font=self.button_fonts['TestModeMenu']['WordsOperations']['Edit_btn'])
            self.delete_word_button = create_button(root=new_window, text="Удалить",
                                                    font=self.button_fonts['TestModeMenu']['WordsOperations'][
                                                        'Delete_btn'])

            if current_listbox:
                self.confirm_button.configure(
                    command=lambda: (self.confirm_edit(current_widget=current_listbox), new_window.destroy()))
                self.delete_word_button.configure(
                    command=lambda: (self.delete_word(current_widget=current_listbox), new_window.destroy()))
            else:
                colored_print('Undefined current listbox', color='red', style='bright')

            self.edit_entry.grid(column=0, row=1, padx=10, pady=10)
            self.confirm_button.grid(row=2, column=1, sticky="se", padx=10, pady=(0, 15))
            self.delete_word_button.grid(row=2, column=2, sticky="se", padx=10, pady=(0, 15))
            main_logger.info(f'Окно редактирования {new_window.title()} было успешно создано.')
        except (AttributeError, TypeError) as e:
            message = f'Функция: {self.create_edit_window.__name__} получила неверные аргументы {e}'
            colored_print(message, 'red', 'bright')
            exceptions_logger.error(message)

    def edit_selected_word(self, event):
        """
        Creates an editing window when a user selects a word.

        :param event: Selecting a word
        :return:
        """

        if len(self.FIRST_LANGUAGE_LIST) == 0:
            return

        if self.window_is_active.get() is False:
            selected_index = event.widget.curselection()
            nw = self.create_new_window(root=self.window, geometry='460x120+800+400',
                                        title='Редактирование тестируемого слова')

            nw.protocol('WM_DELETE_WINDOW',
                        lambda: self.confirm_cancel(nw,
                                                    message='Вы уверены, что хотите прервать редактирование слова?'))

            if selected_index:
                self.create_edit_window(new_window=nw,
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
        """
        Replaces the selected word with the word entered by the user in the text field.

        :param current_widget: Current Listbox(List of words)
        :return:
        """

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
            message = f'Слово: {current_list[selected_index[0]]} было успешно отредактировано.'
            main_logger.info(message)
            colored_print(message, color='green')
        self.window_is_active.set(False)

    def delete_word(self, current_widget=None):
        """
        Deletes the selected word along with its translation from the lists.
        :param current_widget: Current Listbox(List of words)

        :return:
        """

        selected_index = current_widget.curselection()
        if selected_index:
            if self.is_red_test is True:
                delete_word_in_db(deleted_word=self.FIRST_LANGUAGE_LIST[selected_index[0]])

            self.FIRST_LANGUAGE_LIST.pop(selected_index[0])
            self.SECOND_LANGUAGE_LIST.pop(selected_index[0])
            self.update_listbox()
        self.window_is_active.set(False)
        message = 'Слово и его перевод было успешно удалены.'
        main_logger.info(message)
        colored_print(message, color='green')
