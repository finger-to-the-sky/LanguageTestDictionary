import random
import tkinter as tk
from copy import copy
from tkinter import messagebox, ttk
from app.config import main_logger
from app.logger import exceptions_logger
from app.mode_functions.mode_window.mode_test_classes.mode_test_words_init import ModeTestWordsInit
from app.tk_functions import create_button, \
    create_label, create_entry, create_radio_button, create_int_var, create_ttk_treeview
from app.translator.text_field_functionality import TextFieldFunctionality
from app.other.db.json_functions import add_word_in_db
from app.other.custom_print import colored_print


class ModeTestWordsClass(ModeTestWordsInit):
    """
    Main class for test operations.
    """

    def __init__(self, root, title: str, size_window: str, first_list: list, second_list: list,
                 is_red_test: bool = False):
        """

        :param root: tkinter.Tk(), tkinter.TopLevel() or any same object
        :param title: Window title.
        :param size_window:
        :param first_list: List of words for translation.
        :param second_list: List of words for translations.
        :param is_red_test: Red list mode status.
        """

        super().__init__(root, title, size_window, first_list, second_list, is_red_test)

        try:
            self.clear_btn = create_button(root=self.frame, text='Очистить список',
                                           width=20, height=3,
                                           font=self.button_fonts['TestModeMenu']['Clear_btn'], bg='#DC6060',
                                           command=lambda: (self.words_worker.clear_lists(),
                                                            self.clear_error()
                                                            ))
            self.start_btn = create_button(root=self.frame, text='Начать',
                                           width=20, height=3,
                                           font=self.button_fonts['TestModeMenu']['Start_btn'], bg='#60DC70',
                                           command=self.start_mode
                                           )
            self.clear_btn.grid(column=2, row=1, pady=(220, 0), padx=(20, 0))
            self.start_btn.grid(column=2, row=1, pady=(370, 0), padx=(20, 0))

            main_logger.info(f'Инициализация класса {ModeTestWordsClass.__name__} прошла успешно.')
        except AttributeError as e:
            message = (f'Класс: {ModeTestWordsClass.__name__} не смог завершить инициализацию.\n'
                       f'Были переданы неверные параметры {e}')
            colored_print(message, color='red', style='bright')
            exceptions_logger.error(message)

    def start_mode(self):
        """
        Starts testing words.

        :return:
        """

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
        """
        Finishes testing words.
        :return:
        """

        self.window_mode.destroy()
        self.create_window_mode()
        self.result_table()
        main_logger.info(f'Тестовый режим был завершен {self.finish_mode}.')

    def exit(self):
        """
        Exits test mode.

        :return:
        """

        self.window_mode.destroy()
        self.__init__(root=self.root, title=self.title, size_window=self.size_window, first_list=self.first_list,
                      second_list=self.second_list, is_red_test=self.is_red_test)

    def create_question(self):
        """
        Creates necessary elements in the window for word testing and passes user responses to `check_correct_answer`.

        :return:
        """

        self.clear_user_answers_list()
        # Variables for working
        words_list = copy(self.words_worker.FIRST_LANGUAGE_LIST)
        random.shuffle(words_list)
        counter = 1
        len_wl = len(words_list)

        # Labels
        counter_label = create_label(root=self.window_mode, text=len_wl, font=self.label_fonts['Counter'])
        question_label = create_label(root=self.window_mode, font=self.label_fonts['TestModeWord'], wraplength=150)

        # Entry widget for answering with needed instruments
        answer_entry = create_entry(root=self.window_mode, width=20, font=self.text_fonts['EntryWidget'])
        answer_entry.focus_set()
        TextFieldFunctionality.russian_add_hotkeys(root=self.window_mode, text_widgets=(answer_entry,))
        TextFieldFunctionality.create_context_menu(root=self.window_mode, text_widgets=(answer_entry,))

        # Radiobutton for not other mode questions
        selected_radio = create_int_var()
        selected_radio.set(-1)
        radio_button1 = create_radio_button(
            root=self.window_mode, variable=selected_radio,
            font=self.button_fonts['TestModeButtons']['RadioButtons'], value=0,
            command=lambda: selected_radio.get()
        )
        radio_button2 = create_radio_button(
            root=self.window_mode, variable=selected_radio,
            font=self.button_fonts['TestModeButtons']['RadioButtons'], value=1,
            command=lambda: selected_radio.get()
        )
        radio_button3 = create_radio_button(
            root=self.window_mode, variable=selected_radio,
            font=self.button_fonts['TestModeButtons']['RadioButtons'], value=2,
            command=lambda: selected_radio.get()
        )
        # Buttons
        continue_btn = create_button(root=self.window_mode, text='Далее',
                                     font=self.button_fonts['TestModeButtons']['ContinueMode_btn'],
                                     width=10, height=2, bg='#60DC70')
        quit_btn = create_button(root=self.window_mode, text='Завершить',
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
                    message = f'Ошибка в рандомизации ответов {self.create_question.__name__} {e}'
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

    def check_correct_answer(self, check_word: str, user_text: str):
        """
        Checks if the user's answer matches the translation of the given word saving the results in USER_LIST_WORDS.

        :param check_word:  given word
        :param user_text:  user's answer
        :return:
        """

        try:
            self.button_clicked.set(True)
            checkword_id = self.first_list.index(check_word)
            fixed_user_text = user_text.strip().replace(', ', ',').replace(' , ', ',')
            count_words = []
        except (ValueError, AttributeError) as e:
            message = f'Функция: {self.check_correct_answer.__name__} получила неверные параметры {e}'
            exceptions_logger.error(message)
            colored_print(message, color='red', style='bright')
            return

        try:
            for idx, word in enumerate(self.second_list):
                if self.second_list.count(self.second_list[idx]) >= 2:
                    count_words.append(idx)
            user_word_id = self.second_list.index(fixed_user_text)

        except ValueError:
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
        """
        Adds incorrect user answers to the Red List.
        :param event:
        :return:
        """
        try:
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
        except IndexError as e:
            message = f'Функция: {self.answer_redlist.__name__}. Выделите пожалуйста слово. \nError: {e}'
            colored_print(message, 'red')

    def create_table(self, column_name: str, current_list: list, selectmode: str = 'browse'):
        """
        Creates a table based on the specified parameters.

        :param column_name: Table header.
        :param current_list: List with the contents of the table.
        :param selectmode: Table content selection mode.
        :return:
        """

        style = ttk.Style()
        style.configure("Treeview.Heading", font=self.listbox_font['ResultTableHeader'])
        style.configure("Treeview.Cell", font=self.listbox_font['ResultTableContent'])
        try:
            tree = create_ttk_treeview(root=self.window_mode, columns=column_name, show="headings",
                                       selectmode=selectmode,
                                       height=20)
            tree.tag_configure("Treeview.Cell", font=self.listbox_font['ResultTableContent'])

            tree.heading(column_name, text=column_name, anchor=tk.W)
            tree.column("#1", stretch=False, width=350)

            for word in current_list:
                tree.insert("", tk.END, values=word, tags="Treeview.Cell")
            main_logger.info(f'Таблица {column_name} была успешно создана.')
            return tree
        except (tk.TclError, TypeError, AttributeError) as e:
            message = f'Функция: {self.create_table.__name__} получила неверные параметры {e}'
            exceptions_logger.error(message)
            colored_print(message, color='red', style='bright')

    def result_table(self):
        """
        Creates content for the result window in the form of buttons and tables with test word results.
        :return:
        """
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

        hidden_btn = create_button(root=self.window_mode, text='Показать результаты', width=25, height=2,
                                   font=self.button_fonts['TestModeButtons']['ResultButtons']['ShowTable_btn'],
                                   command=toogle_table
                                   )
        exit_btn = create_button(root=self.window_mode, text='Выйти', width=25, height=2,
                                 font=self.button_fonts['TestModeButtons']['ResultButtons']['Exit_btn'],
                                 command=lambda: (
                                     self.clear_user_answers_list(),
                                     self.exit())
                                 )
        restart_btn = create_button(root=self.window_mode, text='Начать заново', width=25, height=2,
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
        """
        Clears user answer lists.
        :return:
        """
        self.USER_LIST_WORDS['correct'].clear()
        self.USER_LIST_WORDS['incorrect']['user_word'].clear()
        self.USER_LIST_WORDS['incorrect']['incorrect_word'].clear()
        self.USER_LIST_WORDS['incorrect']['correct_answer'].clear()
        message = 'Списки ответов были успешно очищены'
        main_logger.info(message)
        colored_print(message, color='green')
