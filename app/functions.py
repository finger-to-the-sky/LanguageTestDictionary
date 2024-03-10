from tkinter import Button
from tkinter import ttk
from app.test_mode_functions.onehudred_test import OneHundredMode
from app.test_mode_functions import red_test, sentences_test
from app.test_mode_functions.test_mode_choose import TestModeChooseClass
from app.text_field_functionality import TextWorkerTranslator
from app.config import LANGUAGES_LIST

translate_button = None


def set_languages(root, button_frame, user_text, translated_text):
    """
    Create two combobox with button for running translate
    :param root:
    :param button_frame:
    :param user_text:
    :param translated_text:
    :return:
    """

    def on_select(event):
        global translate_button
        from_language = combo_from.get()
        to_language = combo_to.get()

        text_worker = TextWorkerTranslator(fl=from_language, tl=to_language)

        if translate_button is not None:
            translate_button.destroy()

        if from_language != 'Ваш язык' and to_language != 'Язык для перевода':
            translate_button = Button(root, text='Перевести', width=20,
                                      command=lambda: text_worker.get_text_translator(user_textfield=user_text,
                                                                                      tr_textfield=translated_text)
                                      )
            root.bind('<Return>', lambda event: text_worker.get_text_translator(user_textfield=user_text,
                                                                                tr_textfield=translated_text))
            translate_button.pack(pady=15)

    combo_from = ttk.Combobox(button_frame, values=LANGUAGES_LIST, state='readonly')
    combo_from.set("Ваш язык")

    combo_to = ttk.Combobox(button_frame, values=LANGUAGES_LIST, state='readonly')
    combo_to.set("Язык для перевода")

    combo_from.grid(row=0, column=2, padx=20)
    combo_to.grid(row=0, column=3, padx=20)

    combo_from.bind('<<ComboboxSelected>>', on_select)
    combo_to.bind('<<ComboboxSelected>>', on_select)


def test_mode_activate(root):
    win = TestModeChooseClass(root=root)
    win.create_test_mode_button(text_button='100 слов',
                                cls_worker=OneHundredMode,
                                side='left', padx=15
                                )
    win.create_test_mode_button(text_button='Красный Тест',
                                cls_worker=red_test.RedTestWordsMode,
                                side='left', padx=45
                                )
    win.create_test_mode_button(text_button='Работа с предложениями',
                                cls_worker=sentences_test.SentencesTest,
                                side='right', padx=15
                                )
