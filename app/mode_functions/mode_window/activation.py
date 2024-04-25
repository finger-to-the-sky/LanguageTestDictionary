from app.mode_functions.species_modes import red_test_mode, sentences_test_mode
from app.mode_functions.species_modes.onehudred_mode import OneHundredMode
from app.mode_functions.choose_window import WindowChooseClass


def mode_activate(root):
    win = WindowChooseClass(root=root)
    first = win.create_choose_button(text_button='100 слов')
    second = win.create_choose_button(text_button='Красный Тест')
    third = win.create_choose_button(text_button='Работа с предложениями')

    first.configure(command=lambda: (OneHundredMode(root), win.window.destroy()))
    second.configure(command=lambda: (red_test_mode.RedTestWordsMode(root), win.window.destroy()))
    third.configure(command=lambda: (sentences_test_mode.SentencesTest(root), win.window.destroy()))

    first.pack(side='left', padx=15, ipady=60)
    second.pack(side='left', padx=45, ipady=60)
    third.pack(side='right', padx=15, ipady=60)
