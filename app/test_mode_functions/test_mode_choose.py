from tkinter import Toplevel, Label
from app.config import SIZE_TEST_MODE_WINDOW
from tkinter.ttk import Style, Button


class TestModeChooseClass:
    _SIZE_WINDOW = SIZE_TEST_MODE_WINDOW
    TITLE = 'Режим тестирования'

    def __init__(self, root):
        self.root = root
        self.window = Toplevel(root)
        self.window.title(self.TITLE)
        self.window.geometry(self._SIZE_WINDOW)

        self.label = Label(self.window, text='Выберите режим', font=('Helvetica', 20))
        self.label.pack(pady=15)

    def create_test_mode_button(self, text_button: str, cls_worker=None, func: tuple = None,
                                style_button='TestButton.TButton',
                                side_button=None, anchor=None, padx=None, pady=None):

        default_button_style = Style()
        default_button_style.configure(style='TestButton.TButton',
                                       padding=(10, 5, 10, 5),
                                       font=('Helvetica', 20),
                                       background='#d3d3d3',
                                       wraplength=220
                                       )
        button = Button(self.window,
                        text=text_button,
                        style=style_button,
                        width=15)

        if cls_worker:
            button.configure(command=lambda: (cls_worker(root=self.root), self.window.destroy()))
        else:
            try:
                button.configure(command=lambda: (func[0](**func[1]), self.window.destroy()))
            except IndexError:
                print('aa')
            else:
                button.configure(command=lambda: (func[0](), self.window.destroy()))

        button.pack(side=side_button, anchor=anchor,
                    padx=padx, pady=pady, ipady=60)
