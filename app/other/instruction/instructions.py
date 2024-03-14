import webbrowser
from tkinter import Label
from app.config import FILE_INSTRUCTION_PATH


def set_instruction_field(window, text, font_size=12, *args, **kwargs):
    instruction = Label(window, text=text, fg='blue', cursor='hand2', font=('Helvetica', font_size))
    instruction.pack(*args, **kwargs)
    instruction.bind('<Button-1>', lambda event: webbrowser.open_new(FILE_INSTRUCTION_PATH))
