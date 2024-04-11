from app.config import SIZE_TEST_MODE_CHOOSE_WINDOW
from tkinter import messagebox


class SentencesTest:
    _SIZE_WINDOW = SIZE_TEST_MODE_CHOOSE_WINDOW
    TITLE = 'Работа с предложениями'

    def __init__(self, root):
        messagebox.showinfo(message='Данный режим находится на стадии разработки')
        self.root = root
        # self.window = Toplevel(root)
        # self.window.title(self.TITLE)
        # self.window.geometry(self._SIZE_WINDOW)
