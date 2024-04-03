import tkinter as tk
from app.test_mode_functions.test_mode.activation import test_mode_activate
from app.tk_functions import create_label, create_button, create_text_widget, create_frame
from app.translator.languages_worker import LanguagesWorker
from app.translator.text_field_functionality import TextFieldFunctionality
from app.config import TITLE, SIZE_WINDOW, main_logger
from app.other.instruction.instructions import set_instruction_field
from app.fonts import FontManager


class MainWindow:
    def __init__(self, title: str = None, size: str = None):
        self.title = title
        self.size = size
        self.font_manager = FontManager()
        self.label_font = self.font_manager.LABEL_FONTS
        self.button_font = self.font_manager.BUTTON_FONTS['TranslatorButtons']
        self.text_font = self.font_manager.TEXT_FONTS

        self.root = self.create_root()
        self.header = create_label(root=self.root, text=f'Добро пожаловать в {self.title}',
                                   font=self.label_font['Header'])
        self.frame = create_frame(self.root)
        self.test_mode_button = create_button(root=self.frame, text='Режим тестирования',
                                              font=self.button_font['StartChoosing_btn'],
                                              command=lambda: test_mode_activate(root=self.root))
        self.translate_file_btn = create_button(root=self.frame, text='Перевести файл',
                                                font=self.button_font['TranslateFile_btn'])
        self.user_text_widget = create_text_widget(root=self.root, width=80, height=10,
                                                   font=self.text_font['TextWidget'])
        self.translated_text_widget = create_text_widget(root=self.root, width=80, height=10,
                                                         font=self.text_font['TextWidget'])

        main_logger.info('Приложение запущено')

    def create_root(self):
        root = tk.Tk()
        root.title(self.title)
        root.geometry(self.size)
        return root

    def show_elements(self):
        self.header.pack(pady=(0, 20))
        self.frame.pack(pady=20)
        self.translate_file_btn.grid(row=0, column=1, padx=(0, 30))
        self.test_mode_button.grid(row=0, column=4, padx=(30, 0))
        self.user_text_widget.pack(pady=(15, 0))
        self.translated_text_widget.pack(pady=(15, 15))

    def other_functions(self):
        LanguagesWorker(root=self.root, user_text_widget=self.user_text_widget,
                        translated_text_widget=self.translated_text_widget, frame=self.frame)

        # Hotkeys for russian keyboard
        TextFieldFunctionality.russian_add_hotkeys(root=self.root,
                                                   text_widgets=(self.user_text_widget, self.translated_text_widget))

        # Create context menu for right mouse button
        TextFieldFunctionality.create_context_menu(root=self.root,
                                                   text_widgets=(self.user_text_widget, self.translated_text_widget))

        set_instruction_field(self.root, text=f'Инструкция по работе с {self.title}', side=tk.BOTTOM, pady=30)

    def run(self):
        self.show_elements()
        self.other_functions()
        self.root.mainloop()


if __name__ == '__main__':
    main = MainWindow(title=TITLE, size=SIZE_WINDOW)
    main.run()
