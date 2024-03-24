from app.config import SIZE_TEST_MODE_MAIN_WINDOW
from app.test_mode_functions.test_mode.test_mode_cls import TestModeClass
from app.config import main_logger


class OneHundredMode:
    _SIZE_WINDOW = SIZE_TEST_MODE_MAIN_WINDOW
    TITLE = '100 слов'
    FIRST_LIST_WORDS = []
    SECOND_LIST_WORDS = []

    def __init__(self, root):
        self.root = root
        TestModeClass(root=self.root, title=self.TITLE,
                      size_window=self._SIZE_WINDOW,
                      first_list=self.FIRST_LIST_WORDS, second_list=self.SECOND_LIST_WORDS)
        main_logger.info(f'Класс {OneHundredMode.__name__} был успешно проинициализирован')
