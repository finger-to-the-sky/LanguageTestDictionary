import tkinter as tk
from tkinter import Tk, Frame, Label, Text, Button
from app.test_mode_functions.activation import test_mode_activate
from app.translator.languages_worker import LanguagesWorker
from app.translator.text_field_functionality import TextFieldFunctionality
from app.config import TITLE, SIZE_WINDOW
from app.other.instruction.instructions import set_instruction_field

root = Tk()
root.title(TITLE)
root.geometry(SIZE_WINDOW)

frame = Frame(root)

# Header
label = Label(root, text=f'Добро пожаловать в {TITLE}',
              font=('Helvetica', 20))
label.pack()

# Temporary function for buttons
test_mode_button = Button(frame, text='Запустить режим тестирования', command=lambda: test_mode_activate(root=root))

first_button = Button(frame, text='Перевести файл')
frame.pack(pady=20)
first_button.grid(row=0, column=1, padx=20)

test_mode_button.grid(row=0, column=4, padx=20)

# Text Fields
user_text_widget = Text(root, width=100, height=10)
translated_text_widget = Text(root, width=100, height=10)

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
