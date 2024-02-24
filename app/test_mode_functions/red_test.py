from tkinter import Toplevel
from app.config import SIZE_TEST_MODE_WINDOW


class RedTestWordsMode:
    _SIZE_WINDOW = SIZE_TEST_MODE_WINDOW
    TITLE = 'Красный тест'

    def __init__(self, root):
        self.window = Toplevel(root)
        self.window.title(self.TITLE)
        self.window.geometry(self._SIZE_WINDOW)
