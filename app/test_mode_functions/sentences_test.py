from app.config import SIZE_TEST_MODE_WINDOW
from tkinter import Label, Toplevel


class SentencesTest:
    _SIZE_WINDOW = SIZE_TEST_MODE_WINDOW
    TITLE = 'Работа с предложениями'

    def __init__(self, root):
        self.window = Toplevel(root)
        self.window.title(self.TITLE)
        self.window.geometry(self._SIZE_WINDOW)
        not_yet = Label(self.window, text='Эта функция находиться на стадии разработки')
        not_yet.pack()
