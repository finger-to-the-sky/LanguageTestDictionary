from tkinter import Toplevel, Label
from app.config import SIZE_TEST_MODE_CHOOSE_WINDOW, exceptions_logger, main_logger
from tkinter.ttk import Style, Button
from app.fonts import FontManager
from app.other.custom_print import colored_print


class TestModeChooseClass:
    _SIZE_WINDOW = SIZE_TEST_MODE_CHOOSE_WINDOW
    TITLE = 'Режим тестирования'

    def __init__(self, root):
        self.root = root
        self.window = Toplevel(root)
        self.window.title(self.TITLE)
        self.window.geometry(self._SIZE_WINDOW)

        self.label_font = FontManager().LABEL_FONTS
        self.label = Label(self.window, text='Выберите режим', font=self.label_font['Header'])
        self.label.pack(pady=15)
        main_logger.info(f'Класс {TestModeChooseClass.__name__} был успешно инициализирован.')

    def create_test_mode_button(self, text_button: str, cls_worker=None, func: tuple = None,
                                style_button='TestButton.TButton',
                                *args, **kwargs):

        default_button_style = Style()
        default_button_style.configure(style='TestButton.TButton', padding=(10, 5, 10, 5),
                                       font=self.label_font['Header'], background='#d3d3d3', wraplength=220)
        button = Button(self.window, text=text_button, style=style_button, width=15)
        if cls_worker:
            button.configure(command=lambda: (cls_worker(root=self.root), self.window.destroy()))
        else:
            try:
                button.configure(command=lambda: (func[0](**func[1]), self.window.destroy()))
            except IndexError:
                message = 'Функция или Класс не были найдены.'
                exceptions_logger.error(message)
                colored_print(message, color='red', style='bright')
            else:
                button.configure(command=lambda: (func[0](), self.window.destroy()))

        button.pack(*args, **kwargs, ipady=60)
        main_logger.info(f'Выборочная кнопка {text_button} была успешно создана.')
