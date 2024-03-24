import random
import tkinter as tk
from copy import copy
from tkinter import messagebox, ttk
from app.config import SIZE_TEST_MODE_WINDOW, main_logger, exceptions_logger
from app.translator.text_field_functionality import TextFieldFunctionality
from app.test_mode_functions.test_mode.listbox_worker.listbox_editor import ListBoxEditor
from app.other.db.json_functions import add_word_in_db
from app.fonts import FontManager
from app.other.custom_print import colored_print


class TestModeClass:
    USER_LIST_WORDS = {'correct': [], 'incorrect': {'user_word': [], 'incorrect_word': [],
                                                    'correct_answer': []}}

    def __init__(self, root, title, size_window, first_list, second_list, is_red_test=False):
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
        self.is_visible_results = tk.BooleanVar()
        self.is_visible_results.set(False)
        self.button_clicked = tk.BooleanVar()
        self.button_clicked.set(False)

        # error text field
        self.error = None
        self.error_text = tk.StringVar()
        self.main_win_error = tk.BooleanVar()
        self.main_win_error.set(False)

        self.window = tk.Toplevel(self.root)
        self.frame = tk.Frame(self.window)
        self.window.focus_set()
        self.window.title(self.title)
        self.window.geometry(self.size_window)

        self.set_header(self.window, self.title)
        self.frame.pack(side=tk.LEFT, padx=(10, 0))

        self.words_worker = ListBoxEditor(master=self.frame,
                                          is_red_test=self.is_red_test)
        self.words_worker.FIRST_LANGUAGE_LIST = self.first_list
        self.words_worker.SECOND_LANGUAGE_LIST = self.second_list
        self.words_worker.update_listbox()

        self.clear_btn = tk.Button(self.frame, text='Очистить список',
                                   width=20, height=3,
                                   font=self.button_fonts['TestModeMenu']['Clear_btn'], bg='#DC6060',
                                   command=lambda: (self.words_worker.clear_lists(),
                                                    self.clear_error()
                                                    ))
        self.start_btn = tk.Button(self.frame, text='Начать',
                                   width=20, height=3,
                                   font=self.button_fonts['TestModeMenu']['Start_btn'], bg='#60DC70',
                                   command=self.start_mode
                                   )
        self.clear_btn.grid(column=2, row=1, pady=(220, 0), padx=(20, 0))
        self.start_btn.grid(column=2, row=1, pady=(370, 0), padx=(20, 0))
        main_logger.info(f'Инициализация класса {TestModeClass.__name__} прошла успешно.')

    def set_error(self, text, window):
        self.error_text.set(text)
        error_label = tk.Label(window, textvariable=self.error_text, fg='red', font=self.label_fonts['Errors'])
        self.main_win_error.set(True)
        return error_label

    def clear_error(self):
        if self.main_win_error.get() is True:
            self.main_win_error.set(False)
        try:
            self.error.destroy()
        except AttributeError:
            exceptions_logger.error(f'self.error = {self.error} был не найден')

    def set_header(self, window, label_text):
        label = tk.Label(window, text=label_text, font=self.label_fonts['Header'])
        label.pack()
        return label

    def create_window_mode(self):
        self.window_mode = tk.Toplevel(self.root)
        self.window_mode.title(self.title)
        self.window_mode.geometry(SIZE_TEST_MODE_WINDOW)
        self.set_header(self.window_mode, self.title)
        self.window_mode.lift()
        main_logger.info(f'Новое окно было создано {self.window_mode}')

    def start_mode(self):
        if not self.words_worker.FIRST_LANGUAGE_LIST:
            if self.main_win_error.get() is not True:
                self.error = self.set_error(text='Чтобы начать работу, добавьте слова', window=self.frame)
                self.error.grid()
        else:
            self.clear_error()
            self.window.destroy()
            self.create_window_mode()
            self.create_question()

    def finish_mode(self):
        self.window_mode.destroy()
        self.create_window_mode()
        self.result_table()
        main_logger.info(f'Тестовый режим был завершен {self.finish_mode}.')

    def exit(self):
        self.window_mode.destroy()
        self.__init__(root=self.root, title=self.title, size_window=self.size_window, first_list=self.first_list,
                      second_list=self.second_list, is_red_test=self.is_red_test)

    def create_question(self):
        self.clear_user_answers_list()
        # Variables for working
        words_list = copy(self.words_worker.FIRST_LANGUAGE_LIST)
        random.shuffle(words_list)
        counter = 1
        len_wl = len(words_list)

        # Labels
        counter_label = tk.Label(self.window_mode, text=len_wl, font=self.label_fonts['Counter'])
        question_label = tk.Label(self.window_mode, font=self.label_fonts['TestModeWord'], wraplength=150)

        # Entry widget for answering with needed instruments
        answer_entry = tk.Entry(self.window_mode, width=20, font=self.text_fonts['EntryWidget'])
        answer_entry.focus_set()
        TextFieldFunctionality.russian_add_hotkeys(root=self.window_mode, text_widgets=[answer_entry])
        TextFieldFunctionality.create_context_menu(root=self.window_mode, text_widgets=[answer_entry])

        # Radiobutton for not other mode questions
        selected_radio = tk.IntVar()
        selected_radio.set(-1)
        radio_button1 = tk.Radiobutton(
            self.window_mode, variable=selected_radio,
            font=self.button_fonts['TestModeButtons']['RadioButtons'], value=0,
            command=lambda: selected_radio.get()
        )
        radio_button2 = tk.Radiobutton(
            self.window_mode, variable=selected_radio,
            font=self.button_fonts['TestModeButtons']['RadioButtons'], value=1,
            command=lambda: selected_radio.get()
        )
        radio_button3 = tk.Radiobutton(
            self.window_mode, variable=selected_radio,
            font=self.button_fonts['TestModeButtons']['RadioButtons'], value=2,
            command=lambda: selected_radio.get()
        )
        # Buttons
        continue_btn = tk.Button(self.window_mode, text='Далее',
                                 font=self.button_fonts['TestModeButtons']['ContinueMode_btn'],
                                 width=10, height=2, bg='#60DC70')
        quit_btn = tk.Button(self.window_mode, text='Завершить',
                             font=self.button_fonts['TestModeButtons']['ExitMode_btn'],
                             width=15, height=2, bg='#DC6060',
                             command=self.finish_mode)

        self.window_mode.bind("<Escape>", lambda event: self.finish_mode())

        # Main loop for working function
        for word in words_list:
            is_usually_question = random.choice([True, False])
            if len_wl <= 2:
                is_usually_question = True

            counter_label.configure(text=f'{counter}/{len_wl}')
            question_label.configure(text=f'{word} -')
            counter_label.pack(side=tk.LEFT, anchor=tk.N, padx=(15, 0), pady=15)
            question_label.pack(side=tk.LEFT, anchor=tk.N, padx=(15, 0), pady=15)

            # Settings for different questions
            if is_usually_question:
                answer_entry.pack(side=tk.LEFT, anchor=tk.N, padx=(15, 0), pady=(20, 15))

                continue_btn.configure(command=lambda: self.check_correct_answer(word, answer_entry.get()))
                self.window_mode.bind('<Return>', lambda event: self.check_correct_answer(word, answer_entry.get()))
            else:
                # Randomize answers
                try:
                    other_words = random.sample(self.second_list, 2)

                    translated_for_word = self.second_list[self.words_worker.FIRST_LANGUAGE_LIST.index(word)]
                    if translated_for_word in other_words:
                        other_words[other_words.index(translated_for_word)] = random.choice(self.second_list)
                    answers_list = [other_words[0], translated_for_word, other_words[1]]
                    random.shuffle(answers_list)

                    # Changing text in the Radiobuttons and pack them
                    radio_button1.configure(text=answers_list[0])
                    radio_button2.configure(text=answers_list[1])
                    radio_button3.configure(text=answers_list[2])

                    radio_button1.pack(anchor=tk.W, padx=(50, 0), pady=(15, 0))
                    radio_button2.pack(anchor=tk.W, padx=(50, 0))
                    radio_button3.pack(anchor=tk.W, padx=(50, 0))

                    continue_btn.configure(command=lambda: self.check_correct_answer(
                        word, answers_list[int(selected_radio.get())]))
                    self.window_mode.bind('<Return>', lambda event: self.check_correct_answer(
                        word, answers_list[int(selected_radio.get())]))

                except ValueError as e:
                    message = f'Ошибка в рандомизации ответов {self.create_question.__name__}'
                    exceptions_logger.error(message)
                    colored_print(message, color='red', style='bright')

            continue_btn.pack(side=tk.RIGHT, anchor=tk.S, padx=15, pady=15)
            quit_btn.pack(side=tk.RIGHT, anchor=tk.S, pady=15)
            self.window_mode.wait_variable(self.button_clicked)

            # After click of button clear all elements and continue loop
            counter_label.pack_forget()
            answer_entry.delete(0, tk.END)
            answer_entry.pack_forget()

            question_label.pack_forget()
            continue_btn.pack_forget()
            quit_btn.pack_forget()
            selected_radio.set(-1)
            radio_button1.pack_forget()
            radio_button2.pack_forget()
            radio_button3.pack_forget()
            counter = counter + 1

        self.result_table()

    def check_correct_answer(self, check_word: str, user_text):
        self.button_clicked.set(True)
        checkword_id = self.first_list.index(check_word)
        fixed_user_text = user_text.strip().replace(', ', ',').replace(' , ', ',')
        count_words = []

        try:
            for idx, word in enumerate(self.second_list):
                if self.second_list.count(self.second_list[idx]) >= 2:
                    count_words.append(idx)
            user_word_id = self.second_list.index(fixed_user_text)

        except ValueError as e:
            user_word_id = None

        if user_word_id is not None:
            user_word = self.second_list[user_word_id].lower().strip()
            checkword = self.first_list[checkword_id].lower().strip()

            if checkword_id == user_word_id:
                self.USER_LIST_WORDS['correct'].append(checkword)
                colored_print(message=f"Correct: {checkword}; Translate: {user_word}\n", color='green')
                return user_word
            elif checkword_id in count_words:
                for word_id in count_words:
                    if checkword_id == word_id:
                        self.USER_LIST_WORDS['correct'].append(checkword)
                        colored_print(message=f"Correct: {checkword}; Translate: {user_word}\n", color='green')
                        return user_word
            else:
                self.USER_LIST_WORDS['incorrect']['incorrect_word'].append(checkword)
                self.USER_LIST_WORDS['incorrect']['user_word'].append(fixed_user_text)
                self.USER_LIST_WORDS['incorrect']['correct_answer'].append(self.second_list[checkword_id])
                colored_print(message=f"Incorrect word: {check_word}\nUser word: {user_text}\n"
                                      f"Correct answer: {self.second_list[checkword_id]}\n")
        else:
            self.USER_LIST_WORDS['incorrect']['incorrect_word'].append(check_word)
            self.USER_LIST_WORDS['incorrect']['user_word'].append(user_text)
            self.USER_LIST_WORDS['incorrect']['correct_answer'].append(self.second_list[checkword_id])

            print(f"Incorrect word: {check_word}\nUser word: {user_text}\n"
                  f"Correct answer: {self.second_list[checkword_id]}\n")

            main_logger.info('Слово успешно добавлено в список')

    def answer_redlist(self, event):
        item = event.widget.selection()[0]
        current_word = event.widget.item(item)['values'][0]

        idx = self.USER_LIST_WORDS['incorrect']['incorrect_word'].index(current_word)
        user_word = self.USER_LIST_WORDS['incorrect']['user_word'][idx]
        result = self.USER_LIST_WORDS['incorrect']['correct_answer'][idx]

        if self.is_red_test is True:
            messagebox.showinfo(current_word, f"Вы ввели: {user_word}\nПравильный перевод: {result}")
            main_logger.info('Запрос на добавление слова в Красный Список был произведен')

        else:
            answer = messagebox.askquestion(title=f'{current_word}',
                                            message=f"Вы ввели: {user_word}\nПравильный перевод: {result}"
                                                    "\nДобавить слово в Красный список?")

            main_logger.info('Запрос на добавление слова в Красный Список был произведен')
            if answer == 'yes':
                add_word_in_db(word=current_word, translate=result)
                main_logger.info('Слово было добавлено в Красный Список')
        self.window_mode.focus_set()

    def create_table(self, column_name: str, current_list: list, selectmode: str = 'browse'):
        style = ttk.Style()
        style.configure("Treeview.Heading", font=self.listbox_font['ResultTableHeader'])
        style.configure("Treeview.Cell", font=self.listbox_font['ResultTableContent'])

        tree = ttk.Treeview(self.window_mode, columns=column_name, show="headings", selectmode=selectmode, height=20)
        tree.tag_configure("Treeview.Cell", font=self.listbox_font['ResultTableContent'])

        tree.heading(column_name, text=column_name, anchor=tk.W)
        tree.column("#1", stretch=False, width=350)

        for word in current_list:
            tree.insert("", tk.END, values=word, tags="Treeview.Cell")
        main_logger.info(f'Таблица {column_name} была успешно создана.')
        return tree

    def result_table(self):
        def toogle_table():
            self.is_visible_results.set(not self.is_visible_results.get())
            if self.is_visible_results.get():
                hidden_btn.configure(text='Cкрыть результаты')
                correct_table.pack(side=tk.LEFT, padx=(90, 0))
                incorrect_table.pack(side=tk.RIGHT, padx=(0, 90))
            else:
                hidden_btn.configure(text='Показать результаты')
                correct_table.pack_forget()
                incorrect_table.pack_forget()

        self.window_mode.geometry('900x750+450+150')
        self.set_header(self.window_mode,
                        f'Правильных ответов: {len(self.USER_LIST_WORDS["correct"])} из {len(self.first_list)}')

        correct_list = self.USER_LIST_WORDS['correct']
        incorrect_list = self.USER_LIST_WORDS['incorrect']['incorrect_word']

        correct_table = self.create_table(
            column_name='Correct',
            current_list=correct_list,
            selectmode='none')

        incorrect_table = self.create_table(
            column_name='Incorrect',
            current_list=incorrect_list)

        incorrect_table.bind('<ButtonRelease-1>', self.answer_redlist)
        incorrect_table.bind("<Enter>", incorrect_table.config(cursor="hand2"))

        hidden_btn = tk.Button(self.window_mode, text='Показать результаты', width=25, height=2,
                               font=self.button_fonts['TestModeButtons']['ResultButtons']['ShowTable_btn'],
                               command=toogle_table
                               )
        exit_btn = tk.Button(self.window_mode, text='Выйти', width=25, height=2,
                             font=self.button_fonts['TestModeButtons']['ResultButtons']['Exit_btn'],
                             command=lambda: (
                                 self.clear_user_answers_list(),
                                 self.exit())
                             )
        restart_btn = tk.Button(self.window_mode, text='Начать заново', width=25, height=2,
                                font=self.button_fonts['TestModeButtons']['ResultButtons']['Restart_btn'],
                                command=lambda: (
                                    self.clear_user_answers_list(),
                                    self.window_mode.destroy(),
                                    self.start_mode())
                                )
        restart_btn.pack(pady=10)
        exit_btn.pack()
        hidden_btn.pack(pady=15)
        main_logger.info('Результирующие таблицы были успешно созданы и размещены')

    def clear_user_answers_list(self):
        self.USER_LIST_WORDS['correct'].clear()
        self.USER_LIST_WORDS['incorrect']['user_word'].clear()
        self.USER_LIST_WORDS['incorrect']['incorrect_word'].clear()
        self.USER_LIST_WORDS['incorrect']['correct_answer'].clear()
        message = 'Списки ответов были успешно очищены'
        main_logger.info(message)
        colored_print(message, color='green')
