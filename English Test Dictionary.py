import tkinter as tk
from tkinter import Tk, Frame, Label, Text, Button
from app.test_mode_functions.test_mode.activation import test_mode_activate
from app.translator.languages_worker import LanguagesWorker
from app.translator.text_field_functionality import TextFieldFunctionality
from app.config import TITLE, SIZE_WINDOW, main_logger
from app.other.instruction.instructions import set_instruction_field
from app.fonts import FontManager


root = Tk()
root.title(TITLE)
root.geometry(SIZE_WINDOW)
main_logger.info('Приложение запущено')

font_manager = FontManager()
label_font = font_manager.LABEL_FONTS
button_font = font_manager.BUTTON_FONTS['TranslatorButtons']
text_font = font_manager.TEXT_FONTS

frame = Frame(root)

# Header
label = Label(root, text=f'Добро пожаловать в {TITLE}',
              font=label_font['Header'])
label.pack(pady=(0, 20))

# Temporary function for buttons
test_mode_button = Button(frame, text='Режим тестирования', font=button_font['StartChoosing_btn'],
                          command=lambda: test_mode_activate(root=root))

first_button = Button(frame, text='Перевести файл', font=button_font['TranslateFile_btn'])
frame.pack(pady=20)
first_button.grid(row=0, column=1, padx=(0, 30))

test_mode_button.grid(row=0, column=4, padx=(30, 0))

# Text Fields
user_text_widget = Text(root, width=80, height=10, font=text_font['TextWidget'])
translated_text_widget = Text(root, width=80, height=10, font=text_font['TextWidget'])

user_text_widget.pack(pady=(15, 0))
translated_text_widget.pack(pady=(15, 15))

lw = LanguagesWorker(root=root, user_text_widget=user_text_widget,
                     translated_text_widget=translated_text_widget, frame=frame)

# Hotkeys for russian keyboard
TextFieldFunctionality.russian_add_hotkeys(root=root, text_widgets=(user_text_widget, translated_text_widget))

# Create context menu for right mouse button
TextFieldFunctionality.create_context_menu(root=root, text_widgets=(user_text_widget, translated_text_widget))

set_instruction_field(root, text='Инструкция по работе с English Test Dictionary', side=tk.BOTTOM, pady=30)
root.mainloop()
