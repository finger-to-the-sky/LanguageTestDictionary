import random
import tkinter as tk
from tkinter import Label, Toplevel, messagebox
from app.config import SIZE_100_WORDS_WINDOW
from app.text_field_functionality import russian_add_hotkeys, create_context_menu
from app.test_mode_functions.onehungred.listbox_editor import ListBoxEditor


class OneHundredWordsMode:
    _SIZE_WINDOW = SIZE_100_WORDS_WINDOW
    TITLE = '100 слов'
    USER_LIST_WORDS = {'correct': [], 'incorrect': {'user_word': [], 'incorrect_word': [],
                                                    'correct_answer': []}}

    def __init__(self, root):
        self.root = root

        self.window = Toplevel(self.root)
        self.frame = tk.Frame(self.window)
        self.window.focus_set()
        self.window.title(self.TITLE)
        self.window.geometry(self._SIZE_WINDOW)

        self.window_mode = None
        self.text_worker = None

        self.is_visible_results = tk.BooleanVar()
        self.is_visible_results.set(False)
        self.button_clicked = tk.BooleanVar()
        self.button_clicked.set(False)

        self.set_header(self.window, self.TITLE)
        self.frame.pack(side=tk.LEFT, padx=(10, 0))

        self.words_worker = ListBoxEditor(master=self.frame)
        self.first_list = self.words_worker.FIRST_LANGUAGE_LIST
        self.second_list = self.words_worker.SECOND_LANGUAGE_LIST
        self.words_worker.update_listbox()

        self.clear_btn = tk.Button(self.window, text='Очистить список',
                                   width=30, height=5,
                                   font=10, bg='#DC6060',
                                   command=self.words_worker.clear_lists
                                   )
        self.start_btn = tk.Button(self.window, text='Начать',
                                   width=30, height=5,
                                   font=10, bg='#60DC70',
                                   command=self.start_mode
                                   )
        self.clear_btn.pack(pady=(150, 0))
        self.start_btn.pack(pady=15)

        # error text field
        self.error_text = tk.StringVar()
        self.main_win_error = tk.BooleanVar()
        self.main_win_error.set(False)

    def set_error(self, text, window):
        self.error_text.set(text)
        error_label = Label(window, textvariable=self.error_text, fg='red')
        self.main_win_error.set(True)
        return error_label

    @staticmethod
    def set_header(window, label_text):
        label = Label(window, text=label_text, font=('Helvetica', 20))
        label.pack()
        return label

    def start_mode(self):
        if not self.words_worker.FIRST_LANGUAGE_LIST:
            error = self.set_error(text='Чтобы начать работу, добавьте слова', window=self.window)
            error.pack()
        else:
            self.window.destroy()
            self.window_mode = Toplevel(self.root)
            self.window_mode.title(self.TITLE)
            self.window_mode.geometry(self._SIZE_WINDOW)
            self.set_header(self.window_mode, self.TITLE)
            self.window_mode.lift()
            self.create_question()

    def finish_mode(self):
        self.window_mode.destroy()
        self.__init__(root=self.root)

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
        continue_btn = tk.Button(
            self.window_mode,
            text='Далее',
            width=10, height=2,
            bg='#60DC70'
        )
        quit_btn = tk.Button(
            self.window_mode,
            text='Завершить',
            width=15, height=2,
            bg='#DC6060',
            command=self.finish_mode
        )
        # Main loop for working function
        for word in set(words_list):

            # Randomize current question
            is_usually_question = random.choice([True, False])
            if len_wl <= 2:
                is_usually_question = True

            # Change counter
            counter_label.configure(text=f'{counter}/{len_wl}')
            counter_label.pack(
                side=tk.LEFT,
                anchor=tk.N,
                padx=(15, 0), pady=15
            )
            question_label.configure(text=f'{word} -')
            question_label.pack(
                side=tk.LEFT,
                anchor=tk.N,
                padx=(15, 0), pady=15
            )
            # Settings for different questions
            if is_usually_question:
                answer_entry.pack(
                    side=tk.LEFT,
                    anchor=tk.N,
                    padx=(15, 0),
                    pady=(20, 15)
                )
                continue_btn.configure(command=lambda: self.check_correct_answer(word, answer_entry.get()))
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

    def check_correct_answer(self, check_word: str, entry_widget_text):
        self.button_clicked.set(True)
        cap_checkword_id = self.first_list.index(check_word)
        user_word_id = None

        try:
            user_word_id = self.second_list.index(entry_widget_text)
        except ValueError as e:
            print(e)

        if user_word_id is not None:
            user_word = self.second_list[user_word_id].capitalize().strip()
            checkword = self.first_list[user_word_id].capitalize().strip()

            if cap_checkword_id == user_word_id:
                self.USER_LIST_WORDS['correct'].append(checkword)
                print(f"Correct {self.USER_LIST_WORDS['correct']}\n")
                return user_word
        else:
            self.USER_LIST_WORDS['incorrect']['incorrect_word'].append(check_word)
            self.USER_LIST_WORDS['incorrect']['user_word'].append(entry_widget_text)
            self.USER_LIST_WORDS['incorrect']['correct_answer'].append(
                self.second_list[cap_checkword_id]
            )
            print(f"Incorrect {self.USER_LIST_WORDS['incorrect']}")

    def result_table(self):
        def toogle_table():
            self.is_visible_results.set(not self.is_visible_results.get())

            if self.is_visible_results.get():
                hidden_btn.configure(text='Cкрыть результаты')
                result_text_widget.pack()
            else:
                hidden_btn.configure(text='Показать результаты')
                result_text_widget.pack_forget()

        def show_notification(event):

            index = result_text_widget.index(tk.CURRENT)
            current_word = result_text_widget.get(index + " wordstart", index + " wordend")

            idx = self.USER_LIST_WORDS['incorrect']['incorrect_word'].index(current_word)
            user_word = self.USER_LIST_WORDS['incorrect']['user_word'][idx]
            result = self.USER_LIST_WORDS['incorrect']['correct_answer'][idx]

            messagebox.showinfo(current_word, f"Вы ввели: {user_word}\nПравильный перевод: {result}")

        self.window_mode.geometry('900x500')
        self.set_header(self.window_mode,
                        f'Правильных ответов: {len(self.USER_LIST_WORDS["correct"])} из {len(self.first_list)}')

        result_text_widget = tk.Text(self.window_mode, height=10, width=80)
        result_text_widget.tag_configure("color1", foreground="green")
        result_text_widget.tag_configure("color2", foreground="red")

        for word in self.first_list:
            correct_ulw_word = word.capitalize()

            if correct_ulw_word in self.USER_LIST_WORDS['correct']:
                result_text_widget.insert(tk.END,
                                          word + ' ',
                                          'color1')
            else:

                result_text_widget.tag_bind('hover', '<Button-1>', show_notification)
                result_text_widget.tag_configure('hover')

                result_text_widget.insert(tk.END,
                                          word + ' ',
                                          ('color2', 'hover'))

        hidden_btn = tk.Button(self.window_mode,
                               text='Показать результаты',
                               width=25, height=2,
                               command=toogle_table)

        result_text_widget.configure(state=tk.DISABLED)

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
