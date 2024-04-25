from app.config import SIZE_TEST_MODE_CHOOSE_WINDOW
from tkinter import messagebox
from app.logger import exceptions_logger
from app.other.custom_print import colored_print


class SentencesTest:
    _SIZE_WINDOW = SIZE_TEST_MODE_CHOOSE_WINDOW
    TITLE = 'Работа с предложениями'

    def __init__(self, root):
        try:
            messagebox.showinfo(message='Данный режим находится на стадии разработки')
            self.root = root
            # self.window = Toplevel(root)
            # self.window.title(self.TITLE)
            # self.window.geometry(self._SIZE_WINDOW)
        except (TypeError, AttributeError) as e:
            message = f'Класс: {SentencesTest.__name__} получил неверные аргументы {e}'
            colored_print(message, color='red', style='bright')
            exceptions_logger.error(message)
