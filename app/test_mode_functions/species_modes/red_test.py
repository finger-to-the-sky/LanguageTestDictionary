from app.config import SIZE_TEST_MODE_MAIN_WINDOW, red_list_db
from app.test_mode_functions.test_mode.test_mode_cls import TestModeClass


class RedTestWordsMode:
    _SIZE_WINDOW = SIZE_TEST_MODE_MAIN_WINDOW
    TITLE = 'Красный тест'
    FIRST_LIST_WORDS = []
    SECOND_LIST_WORDS = []

    def __init__(self, root):
        self.root = root
        self.cache_loader()
        TestModeClass(root=self.root, title=self.TITLE,
                      size_window=self._SIZE_WINDOW,
                      first_list=self.FIRST_LIST_WORDS, second_list=self.SECOND_LIST_WORDS,
                      is_red_test=True)

    def cache_loader(self):
        words = red_list_db.all()
        for w in words:
            self.FIRST_LIST_WORDS.append(w['word'])
            self.SECOND_LIST_WORDS.append(w['translate'])
