import tkinter as tk
from tkinter import Label, filedialog
from app.text_field_functionality import russian_add_hotkeys, create_context_menu


class ListboxWordRedactor:
    is_visible = False

    def __init__(self, master, words_list):
        # main variables
        self.window = master
        self.words_list = words_list

        # error text field
        self.text_var = tk.StringVar()
        self.error = Label(self.window, textvariable=self.text_var, fg='red')
        self.error.pack()

        # listbox words settings
        self.words_list_widget = tk.Listbox(self.window, selectmode=tk.SINGLE, width=30, height=20)
        self.words_list_widget.pack(side=tk.LEFT)
        self.frame = tk.Frame(self.window)
        self.frame.pack(side=tk.LEFT,
                        anchor=tk.S,
                        pady=(0, 60),
                        padx=(15, 0)
                        )
        self.update_listbox()

        # from for upload word to listbox(with additional settings)
        self.add_entry = tk.Entry(self.frame, width=30)
        self.add_entry.grid(column=0, row=2)
        russian_add_hotkeys(root=self.frame, text_widgets=[self.add_entry])
        create_context_menu(root=self.frame, text_widgets=[self.add_entry])

        self.add_confirm_button = tk.Button(self.frame, text="Добавить",
                                            command=self.add_word_to_listwords
                                            )
        self.add_confirm_button.grid(column=1, row=2, padx=(10, 15))

        self.upload_button = tk.Button(self.frame, text='Загрузить слова из файла',
                                       command=self.download_from_file, height=1, width=25)

        self.upload_button.grid(column=0, row=3, padx=5, pady=(20, 0))
        self.words_list_widget.bind('<<ListboxSelect>>', self.edit_selected_word)

    def change_error(self, text):
        self.text_var.set(text)

    def add_word_to_listwords(self):
        """
        Adding a word to listbox from form
        :return:
        """
        if len(self.words_list) >= 100:
            self.change_error('Ваш список уже полон!')
        else:
            added_word = self.add_entry.get().strip()
            if len(added_word) == 0:
                self.change_error('Нельзя добавить пустое поле')
            else:
                self.change_error('')
                self.words_list.append(added_word)
                self.update_listbox()
                self.add_entry.delete(0, tk.END)

    def edit_field_create(self):
        """
        Creating form for edit and delete any word from listbox
        :return:
        """
        if self.is_visible:
            return

        self.edit_entry = tk.Entry(self.frame, width=30)
        self.confirm_button = tk.Button(self.frame, text="Редактировать",
                                        command=self.confirm_edit)

        self.delete_word_button = tk.Button(self.frame, text="Удалить",
                                            command=self.delete_word)

        self.edit_entry.grid(column=0, row=1, pady=(0, 10))
        self.confirm_button.grid(column=1, row=1, padx=(10, 0), pady=(0, 15))
        self.delete_word_button.grid(column=2, row=1, padx=(10, 0), pady=(0, 15))
        self.is_visible = True

    def edit_field_destroy(self):
        self.edit_entry.destroy()
        self.confirm_button.destroy()
        self.delete_word_button.destroy()
        self.is_visible = False

    def update_listbox(self):
        """
        Update listbox of words_list in the code
        :return:
        """
        self.words_list_widget.delete(0, tk.END)
        for word in self.words_list:
            self.words_list_widget.insert(tk.END, word)

    def edit_selected_word(self, event):
        selected_index = self.words_list_widget.curselection()
        if selected_index:
            self.edit_field_create()
            selected_word = self.words_list_widget.get(selected_index[0])
            self.edit_entry.delete(0, tk.END)
            self.edit_entry.insert(tk.END, selected_word)

    def confirm_edit(self):
        """
        Safe edited word to listbox and words_list
        :return:
        """
        edited_word = self.edit_entry.get().strip()
        selected_index = self.words_list_widget.curselection()

        if selected_index:
            self.words_list[selected_index[0]] = edited_word
            self.update_listbox()
            self.edit_field_destroy()
        else:
            current_index = 0
            while current_index < self.words_list_widget.size():
                selected_word = self.words_list_widget.get(current_index)
                if edited_word in selected_word:
                    self.edit_entry.delete(0, tk.END)
                    self.edit_entry.insert(tk.END, selected_word)
                    break
                current_index += 1
            if current_index == self.words_list_widget.size():
                current_index = 0

    def delete_word(self):
        edited_word = self.edit_entry.get()
        selected_index = self.words_list_widget.curselection()
        if selected_index:
            self.words_list.remove(edited_word)
            self.update_listbox()
            self.edit_field_destroy()
        else:
            current_index = 0
            while current_index < self.words_list_widget.size():
                selected_word = self.words_list_widget.get(current_index)
                if edited_word in selected_word:
                    self.words_list_widget.delete(current_index)
                    break
                current_index += 1
            if current_index == self.words_list_widget.size():
                current_index = 0

    def download_from_file(self):
        """
        Download words from file of comma(temporarily)
        :return:
        """
        if len(self.words_list) >= 100:
            self.change_error('Ваш список уже полон!')
        else:
            file_path = filedialog.askopenfilename()
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    words = file.read()
                    words_file = words.split(',\n')
                    if len(words_file) == 1:
                        words_file = [w.strip() for w in words.split(',')]

                    count_words = 100 - len(self.words_list)
                    self.words_list.extend(words_file[:count_words])
                    self.update_listbox()
                    self.change_error('')

            except Exception:
                return

    def clear_list(self):
        self.words_list_widget.delete(0, tk.END)
        self.words_list.clear()
