from tkinter import Button, Menu
from tkinter import ttk
from text_field_functionality import TextWorker
from config import LANGUAGES_LIST
import keyboard

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

        text_worker = TextWorker(fl=from_language, tl=to_language)

        if translate_button is not None:
            translate_button.destroy()

        if from_language != 'Ваш язык' and to_language != 'Язык для перевода':
            translate_button = Button(root, text='Перевести', width=20,
                                      command=lambda: text_worker.get_text(user_textfield=user_text,
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


def other_functionality(frame):
    first_button = Button(frame, text='Перевести файл')
    second_button = Button(frame, text='Запустить режим тестирования')
    frame.pack(pady=20)
    first_button.grid(row=0, column=1, padx=20)
    second_button.grid(row=0, column=4, padx=20)


def create_context_menu(root, text_widgets):
    """
    Create context menu for work with the text in any text field
    :param root:
    :param text_widgets:
    :return:
    """
    def show_context_menu(event):
        context_menu.post(event.x_root, event.y_root)

    for widget in text_widgets:
        context_menu = Menu(root, tearoff=0)
        context_menu.add_command(label="Вырезать",
                                 command=lambda: TextWorker.cut_text(root=root, text_widgets=text_widgets))
        context_menu.add_command(label="Копировать",
                                 command=lambda: TextWorker.copy_text(root=root, text_widgets=text_widgets))
        context_menu.add_command(label="Вставить",
                                 command=lambda: TextWorker.paste_text(root=root, text_widgets=text_widgets))

        widget.bind("<Button-3>", show_context_menu)


def russian_add_hotkeys(root, text_widgets):
    """
    Connect hotkeys for russian keyboard
    :param root:
    :param text_widgets:
    :return:
    """
    keyboard.add_hotkey('ctrl+alt+c', lambda: TextWorker.copy_text(root=root, text_widgets=text_widgets))
    keyboard.add_hotkey('ctrl+alt+v', lambda: TextWorker.paste_text(root=root, text_widgets=text_widgets))
    keyboard.add_hotkey('ctrl+a', lambda: TextWorker.select_all(root=root, text_widgets=text_widgets))
    keyboard.add_hotkey('ctrl+alt+x', lambda: TextWorker.cut_text(root=root, text_widgets=text_widgets))
