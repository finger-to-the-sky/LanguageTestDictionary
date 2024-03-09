import random
import tkinter as tk
from tkinter import Label, Toplevel, messagebox, ttk, END

from app.config import SIZE_TEST_MODE_WINDOW
from app.text_field_functionality import russian_add_hotkeys, create_context_menu
from app.test_mode_functions.test_mode.listbox_worker.listbox_editor import ListBoxEditor
from app.other.db.json_functions import add_word_in_db


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

        self.window = Toplevel(self.root)
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
                                   font=10, bg='#DC6060',
                                   command=lambda: (self.words_worker.clear_lists(), self.clear_error()
                                                    ))
        self.start_btn = tk.Button(self.frame, text='Начать',
                                   width=20, height=3,
                                   font=10, bg='#60DC70',
                                   command=self.start_mode
                                   )
        self.clear_btn.grid(column=2, row=1, pady=(220, 0), padx=(20, 0))
        self.start_btn.grid(column=2, row=1, pady=(370, 0), padx=(20, 0))

    def set_error(self, text, window):
        self.error_text.set(text)
        error_label = Label(window, textvariable=self.error_text, fg='red')
        self.main_win_error.set(True)
        return error_label

    def clear_error(self):
        if self.main_win_error.get() is True:
            self.main_win_error.set(False)
        try:
            self.error.destroy()
        except AttributeError:
            pass

    @staticmethod
    def set_header(window, label_text):
        label = Label(window, text=label_text, font=('Helvetica', 20))
        label.pack()
        return label

    def start_mode(self):
        if not self.words_worker.FIRST_LANGUAGE_LIST:
            if self.main_win_error.get() is not True:
                self.error = self.set_error(text='Чтобы начать работу, добавьте слова', window=self.frame)
                self.error.grid()
        else:
            self.clear_error()
            self.window.destroy()

            self.window_mode = Toplevel(self.root)
            self.window_mode.title(self.title)
            self.window_mode.geometry(SIZE_TEST_MODE_WINDOW)

            self.set_header(self.window_mode, self.title)
            self.window_mode.lift()
            self.create_question()

    def finish_mode(self):
        self.window_mode.destroy()
        self.__init__(root=self.root, title=self.title, size_window=self.size_window,
                      first_list=self.first_list, second_list=self.second_list)

    def create_question(self):
        # Variables for working
        words_list = self.words_worker.FIRST_LANGUAGE_LIST
        counter = 1
        len_wl = len(words_list)

        # Labels
        counter_label = Label(self.window_mode, text=len_wl)
        question_label = Label(self.window_mode, font=15)

        # Entry widget for answering with needed instruments
        answer_entry = tk.Entry(self.window_mode, width=30)
        answer_entry.focus_set()
        russian_add_hotkeys(root=self.window_mode, text_widgets=[answer_entry])
        create_context_menu(root=self.window_mode, text_widgets=[answer_entry])

        # Radiobutton for not other mode questions
        selected_radio = tk.IntVar()
        selected_radio.set(-1)

        radio_button1 = tk.Radiobutton(self.window_mode,
                                       variable=selected_radio,
                                       font=10,
                                       value=0,
                                       command=lambda: selected_radio.get()
                                       )
        radio_button2 = tk.Radiobutton(self.window_mode,
                                       variable=selected_radio,
                                       font=10,
                                       value=1,
                                       command=lambda: selected_radio.get()
                                       )
        radio_button3 = tk.Radiobutton(self.window_mode,
                                       variable=selected_radio,
                                       font=10,
                                       value=2,
                                       command=lambda: selected_radio.get()
                                       )
        # Buttons
        continue_btn = tk.Button(self.window_mode, text='Далее',
                                 width=10, height=2, bg='#60DC70')
        quit_btn = tk.Button(self.window_mode, text='Завершить',
                             width=15, height=2, bg='#DC6060',
                             command=self.finish_mode)

        self.window_mode.bind("<Escape>", lambda event: self.finish_mode())

        # Main loop for working function
        for word in set(words_list):
            is_usually_question = random.choice([True, False])
            if len_wl <= 2:
                is_usually_question = True

            counter_label.configure(text=f'{counter}/{len_wl}')
            counter_label.pack(side=tk.LEFT, anchor=tk.N, padx=(15, 0), pady=15
                               )
            question_label.configure(text=f'{word} -')
            question_label.pack(side=tk.LEFT, anchor=tk.N, padx=(15, 0), pady=15
                                )
            # Settings for different questions
            if is_usually_question:
                answer_entry.pack(side=tk.LEFT, anchor=tk.N, padx=(15, 0), pady=(20, 15)
                                  )
                continue_btn.configure(command=lambda: self.check_correct_answer(word, answer_entry.get()))
                self.window_mode.bind('<Return>', lambda event: self.check_correct_answer(word, answer_entry.get()))
            else:
                # Randomize answers
                try:
                    other_words = random.sample(self.second_list, 2)

                    translated_for_word = self.second_list[words_list.index(word)]
                    if translated_for_word in other_words:
                        other_words[other_words.index(translated_for_word)] = random.choice(self.second_list)
                    answers_list = [
                        other_words[0],
                        translated_for_word,
                        other_words[1]
                    ]
                    random.shuffle(answers_list)

                    # Changing text in the Radiobuttons and pack them
                    radio_button1.configure(text=answers_list[0])
                    radio_button2.configure(text=answers_list[1])
                    radio_button3.configure(text=answers_list[2])

                    radio_button1.pack(anchor=tk.W, padx=(50, 0), pady=(15, 0))
                    radio_button2.pack(anchor=tk.W, padx=(50, 0))
                    radio_button3.pack(anchor=tk.W, padx=(50, 0))

                    continue_btn.configure(command=lambda: self.check_correct_answer(
                        word, answers_list[int(selected_radio.get())])
                                           )
                    self.window_mode.bind('<Return>', lambda event: self.check_correct_answer(
                        word, answers_list[int(selected_radio.get())])
                                          )
                except ValueError as e:
                    print(f'Error {e}')

            continue_btn.pack(side=tk.RIGHT, anchor=tk.S,
                              padx=15, pady=15)
            quit_btn.pack(side=tk.RIGHT, anchor=tk.S,
                          pady=15)
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
        user_word_id = None
        try:
            user_word_id = self.second_list.index(fixed_user_text)
        except ValueError as e:
            print(e)
            user_word_id = None

        if user_word_id is not None:
            user_word = self.second_list[user_word_id].lower().strip()
            checkword = self.first_list[checkword_id].lower().strip()

            if checkword_id == user_word_id:
                self.USER_LIST_WORDS['correct'].append(checkword)
                print(f"Correct {self.USER_LIST_WORDS['correct']}\n")
                return user_word
            else:
                self.USER_LIST_WORDS['incorrect']['incorrect_word'].append(checkword)
                self.USER_LIST_WORDS['incorrect']['user_word'].append(fixed_user_text)
                self.USER_LIST_WORDS['incorrect']['correct_answer'].append(
                    self.second_list[checkword_id]
                )
                print(f"Incorrect {self.USER_LIST_WORDS['incorrect']}")
        else:
            self.USER_LIST_WORDS['incorrect']['incorrect_word'].append(check_word)
            self.USER_LIST_WORDS['incorrect']['user_word'].append(user_text)
            self.USER_LIST_WORDS['incorrect']['correct_answer'].append(
                self.second_list[checkword_id]
            )
            print(f"Incorrect {self.USER_LIST_WORDS['incorrect']}")

    def on_click(self, event):
        item = event.widget.selection()[0]
        current_word = event.widget.item(item)['values'][0]

        idx = self.USER_LIST_WORDS['incorrect']['incorrect_word'].index(current_word)
        user_word = self.USER_LIST_WORDS['incorrect']['user_word'][idx]
        result = self.USER_LIST_WORDS['incorrect']['correct_answer'][idx]

        if self.is_red_test is True:
            messagebox.showinfo(current_word, f"Вы ввели: {user_word}\nПравильный перевод: {result}")
        else:
            answer = messagebox.askquestion(title=f'{current_word}',
                                            message=f"Вы ввели: {user_word}\nПравильный перевод: {result}"
                                                    "\nДобавить слово в Красный список?")
            if answer == 'yes':
                add_word_in_db(word=current_word, translate=result)

        self.window_mode.focus_set()

    def create_table(self, column_name: str, current_list: list, selectmode: str = 'browse'):
        style = ttk.Style()
        style.configure("Treeview.Heading", font=("Helvetica", 12, "bold"))

        tree = ttk.Treeview(self.window_mode, columns=column_name, show="headings", selectmode=selectmode, height=20)
        tree.heading(column_name, text=column_name, anchor=tk.W)
        tree.column("#1", stretch=False, width=350)

        for word in current_list:
            tree.insert("", END, values=word)
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

        incorrect_table.bind('<ButtonRelease-1>', self.on_click)
        incorrect_table.bind("<Enter>", incorrect_table.config(cursor="hand2"))

        hidden_btn = tk.Button(self.window_mode,
                               text='Показать результаты',
                               width=25, height=2,
                               command=toogle_table
                               )
        exit_btn = tk.Button(self.window_mode, text='Выйти', width=25, height=2,
                             command=lambda: (
                                 self.clear_user_answers_list(),
                                 self.finish_mode())
                             )
        restart_btn = tk.Button(self.window_mode, text='Начать заново', width=25, height=2,
                                command=lambda: (
                                    self.clear_user_answers_list(),
                                    self.window_mode.destroy(),
                                    self.start_mode())
                                )
        restart_btn.pack(pady=10)
        exit_btn.pack()
        hidden_btn.pack(pady=15)

    def clear_user_answers_list(self):
        self.USER_LIST_WORDS['correct'].clear()
        self.USER_LIST_WORDS['incorrect']['user_word'].clear()
        self.USER_LIST_WORDS['incorrect']['incorrect_word'].clear()
        self.USER_LIST_WORDS['incorrect']['correct_answer'].clear()
