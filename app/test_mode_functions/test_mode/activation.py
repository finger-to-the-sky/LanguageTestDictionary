from app.test_mode_functions.species_modes import red_test, sentences_test
from app.test_mode_functions.species_modes.onehudred_test import OneHundredMode
from app.test_mode_functions.test_mode_choose import TestModeChooseClass


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
