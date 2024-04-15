import tkinter

from app.config import SIZE_TEST_MODE_CHOOSE_WINDOW, main_logger
from app.logger import exceptions_logger
from tkinter.ttk import Style
from app.fonts import FontManager
from app.other.custom_print import colored_print
from app.tk_functions import create_top_level, create_label, create_ttk_button


class WindowChooseClass:
    _SIZE_WINDOW = SIZE_TEST_MODE_CHOOSE_WINDOW
    _TITLE = 'Режим тестирования'

    def __init__(self, root):
        try:
            self.root = root
            self.window = create_top_level(root=root)
            self.window.title(self._TITLE)
            self.window.geometry(self._SIZE_WINDOW)

            self.label_font = FontManager().LABEL_FONTS
            self.label = create_label(self.window, text='Выберите режим', font=self.label_font['Header'])
            self.label.pack(pady=15)
            main_logger.info(f'Класс {WindowChooseClass.__name__} был успешно инициализирован.')
        except (AttributeError, TypeError) as e:
            message = f'Класс {WindowChooseClass.__name__} провалил инициализацию {e}'
            colored_print(message, color='red', style='bright')
            exceptions_logger.error(message)

    def create_choose_button(self, text_button: str, style_button='ChooseButton.TButton'):
        try:
            default_button_style = Style()
            default_button_style.configure(style=style_button, padding=(10, 5, 10, 5),
                                           font=self.label_font['Header'], background='#d3d3d3', wraplength=220)
            button = create_ttk_button(self.window, text=text_button, style=style_button, width=15)
            if button:
                main_logger.info(f'Выборочная кнопка {text_button} была успешно создана.')
                return button
            raise AttributeError('Incorrect arguments for create_ttk_button')
        except (tkinter.TclError, AttributeError) as e:
            message = f'Функция: {self.create_choose_button.__name__} получила неверные аргументы {e}'
            colored_print(message)
            exceptions_logger.error(message)

            new_button = self.create_choose_button(text_button=text_button)
            main_logger.info(f'Выборочная кнопка {text_button} была успешно создана по стандрту.')
            return new_button
