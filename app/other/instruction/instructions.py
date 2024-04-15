import webbrowser
import tkinter as tk
from app.config import FILE_INSTRUCTION_PATH, main_logger
from app.fonts import FontManager
from app.other.custom_print import colored_print

instruction_font = FontManager().LABEL_FONTS['Instruction']


def set_instruction_field(window, text: str, *args, **kwargs):
    """
    Sets up a user guide for users

    :param window: tkinter.Tk(), tkinter.Toplevel() or any same objects
    :param text: Text for setting
    :param args: Arguments for position tk.Label()
    :param kwargs: Arguments for position tk.Label()
    :return:
    """
    try:
        instruction = tk.Label(window, text=text, fg='blue', cursor='hand2', font=instruction_font)
        instruction.pack(*args, **kwargs)
        instruction.bind('<Button-1>', lambda event: webbrowser.open_new(FILE_INSTRUCTION_PATH))
        main_logger.info(f'Инструкция в окне {window.winfo_toplevel().title()} успешно добавлена')
    except (TypeError, tk.TclError, AttributeError) as e:
        message = f'Функция: {set_instruction_field.__name__} приняла неверные агрументы {e}'
        colored_print(message, color='red', style='bright')