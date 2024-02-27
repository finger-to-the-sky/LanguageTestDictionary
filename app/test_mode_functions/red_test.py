from app.config import SIZE_TEST_MODE_MAIN_WINDOW
from app.test_mode_functions.test_mode.test_mode_cls import TestModeClass
from app.other.json_functions import get_words


class RedTestWordsMode:
    _SIZE_WINDOW = SIZE_TEST_MODE_MAIN_WINDOW
    TITLE = 'Красный тест'
    FIRST_LIST_WORDS = []
    SECOND_LIST_WORDS = []

    def __init__(self, root):
        self.root = root
        self.cache_loader()
        test_mode = TestModeClass(root=self.root, title=self.TITLE,
                                  size_window=self._SIZE_WINDOW,
                                  first_list=self.FIRST_LIST_WORDS, second_list=self.SECOND_LIST_WORDS,
                                  is_red_test=True)

    def cache_loader(self):
        words = get_words()
        for w in words:
            self.FIRST_LIST_WORDS.append(w['word'])
            self.SECOND_LIST_WORDS.append(w['translate'])
