from app.config import SIZE_TEST_MODE_MAIN_WINDOW, red_list_db, main_logger
from app.logger import exceptions_logger
from app.other.custom_print import colored_print
from app.mode_functions.mode_window.mode_test_classes.mode_test_cls import ModeTestWordsClass


class RedTestWordsMode:
    """
    Class for creating a Red List window

    """

    _SIZE_WINDOW = SIZE_TEST_MODE_MAIN_WINDOW
    _TITLE = 'Красный тест'
    _FIRST_LIST_WORDS = []
    _SECOND_LIST_WORDS = []

    def __init__(self, root):

        try:
            self.root = root
            self.cache_loader()
            ModeTestWordsClass(root=self.root, title=self._TITLE,
                               size_window=self._SIZE_WINDOW,
                               first_list=self._FIRST_LIST_WORDS, second_list=self._SECOND_LIST_WORDS,
                               is_red_test=True)
            main_logger.info(f'Класс {RedTestWordsMode.__name__} был успешно проинициализирован')
        except (TypeError, AttributeError) as e:
            message = f'Класс: {RedTestWordsMode.__name__} получил неверные аргументы {e}'
            colored_print(message, color='red', style='bright')
            exceptions_logger.error(message)

    def cache_loader(self, db=red_list_db):
        try:
            words = db.all()
            for w in words:
                self._FIRST_LIST_WORDS.append(w['word'])
                self._SECOND_LIST_WORDS.append(w['translate'])

            message = f'Слова из кэша были успешно добавлены'
            main_logger.info(message)
            colored_print(message=message, color='green', style='bright')
        except (AttributeError,) as e:
            message = f'Функция: {self.cache_loader.__name__} получила неверные аргументы {e}'
            colored_print(message, color='red', style='bright')
            exceptions_logger.error(message)
