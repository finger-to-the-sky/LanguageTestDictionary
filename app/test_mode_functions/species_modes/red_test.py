from app.config import SIZE_TEST_MODE_MAIN_WINDOW, red_list_db, main_logger
from app.other.custom_print import colored_print
from app.test_mode_functions.test_mode.test_mode_cls import ModeTestWordsClass


class RedTestWordsMode:
    _SIZE_WINDOW = SIZE_TEST_MODE_MAIN_WINDOW
    TITLE = 'Красный тест'
    FIRST_LIST_WORDS = []
    SECOND_LIST_WORDS = []

    def __init__(self, root):
        self.root = root
        self.cache_loader()
        ModeTestWordsClass(root=self.root, title=self.TITLE,
                           size_window=self._SIZE_WINDOW,
                           first_list=self.FIRST_LIST_WORDS, second_list=self.SECOND_LIST_WORDS,
                           is_red_test=True)
        main_logger.info(f'Класс {RedTestWordsMode.__name__} был успешно проинициализирован')

    def cache_loader(self):
        words = red_list_db.all()
        for w in words:
            self.FIRST_LIST_WORDS.append(w['word'])
            self.SECOND_LIST_WORDS.append(w['translate'])

        message = f'Слова из кэша были успешно добавлены'
        main_logger.info(message)
        colored_print(message=message, color='green', style='bright')