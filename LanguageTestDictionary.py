import tkinter as tk
from tkinter import Tk, Frame, Label, Text, Button
from app.test_mode_functions.test_mode.activation import test_mode_activate
from app.tk_functions import create_label, create_button, create_text_widget
from app.translator.languages_worker import LanguagesWorker
from app.translator.text_field_functionality import TextFieldFunctionality
from app.config import TITLE, SIZE_WINDOW, main_logger
from app.other.instruction.instructions import set_instruction_field
from app.fonts import FontManager


class MainWindow:
    def __init__(self, title: str = None, size: str = None):
        self.title = title
        self.size = size

    def create_root(self):
        root = Tk()
        root.title(self.title)
        root.geometry(self.size)
        return root

    def run(self):
        root = self.create_root()
        main_logger.info('Приложение запущено')

        font_manager = FontManager()
        label_font = font_manager.LABEL_FONTS
        button_font = font_manager.BUTTON_FONTS['TranslatorButtons']
        text_font = font_manager.TEXT_FONTS

        header = create_label(root=root, text=f'Добро пожаловать в {self.title}', font=label_font['Header'])
        header.pack(pady=(0, 20))

        frame = Frame(root)
        test_mode_button = create_button(root=frame, text='Режим тестирования',
                                              font=button_font['StartChoosing_btn'],
                                              command=lambda: test_mode_activate(root=root))
        translate_file_btn = create_button(root=frame, text='Перевести файл',
                                                font=button_font['TranslateFile_btn'])

        frame.pack(pady=20)
        translate_file_btn.grid(row=0, column=1, padx=(0, 30))
        test_mode_button.grid(row=0, column=4, padx=(30, 0))

        user_text_widget = create_text_widget(root=root, width=80, height=10, font=text_font['TextWidget'])
        translated_text_widget = create_text_widget(root=root, width=80, height=10, font=text_font['TextWidget'])

        user_text_widget.pack(pady=(15, 0))
        translated_text_widget.pack(pady=(15, 15))

        lw = LanguagesWorker(root=root, user_text_widget=user_text_widget,
                             translated_text_widget=translated_text_widget, frame=frame)

        # Hotkeys for russian keyboard
        TextFieldFunctionality.russian_add_hotkeys(root=root, text_widgets=(user_text_widget, translated_text_widget))

        # Create context menu for right mouse button
        TextFieldFunctionality.create_context_menu(root=root, text_widgets=(user_text_widget, translated_text_widget))

        set_instruction_field(root, text=f'Инструкция по работе с {self.title}', side=tk.BOTTOM, pady=30)

        root.mainloop()


if __name__ == '__main__':
    main = MainWindow(title=TITLE, size=SIZE_WINDOW)
    main.run()
