import webbrowser
from tkinter import Label
from app.config import FILE_INSTRUCTION_PATH
from app.fonts import FontManager

instruction_font = FontManager().LABEL_FONTS['Instruction']


def set_instruction_field(window, text, *args, **kwargs):
    instruction = Label(window, text=text, fg='blue', cursor='hand2', font=instruction_font)
    instruction.pack(*args, **kwargs)
    instruction.bind('<Button-1>', lambda event: webbrowser.open_new(FILE_INSTRUCTION_PATH))
