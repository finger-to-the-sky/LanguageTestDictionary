from app.config import SIZE_TEST_MODE_MAIN_WINDOW
from app.logger import exceptions_logger
from app.mode_functions.test_mode.test_mode_cls import ModeTestWordsClass
from app.config import main_logger
from app.other.custom_print import colored_print


class OneHundredMode:
    _SIZE_WINDOW = SIZE_TEST_MODE_MAIN_WINDOW
    _TITLE = '100 слов'
    _FIRST_LIST_WORDS = []
    _SECOND_LIST_WORDS = []

    def __init__(self, root):
        try:
            self.root = root
            ModeTestWordsClass(root=self.root, title=self._TITLE,
                               size_window=self._SIZE_WINDOW,
                               first_list=self._FIRST_LIST_WORDS, second_list=self._SECOND_LIST_WORDS)
            main_logger.info(f'Класс {OneHundredMode.__name__} был успешно проинициализирован')
        except (TypeError, AttributeError) as e:
            message = f'Класс: {OneHundredMode.__name__} получил неверные аргументы {e}'
            colored_print(message, color='red', style='bright')
            exceptions_logger.error(message)
