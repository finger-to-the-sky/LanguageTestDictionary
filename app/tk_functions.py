"""
Module containing processed functions for creating tkinter elements
"""

import tkinter as tk
from tkinter import ttk
from app.other.custom_print import colored_print
from app.logger import tk_functions_logger


def tk_exceptions(func):
    """
    Decorator for handling exceptions when creating tkinter objects.
    :param func:
    :return:
    """
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (AttributeError, tk.TclError, TypeError) as e:
            message = f'Ошибка входящих данных в функции {func.__name__} {e}'
            tk_functions_logger.error(message)
            if 'pyimage' in str(e):
                kwargs['image'] = None
                return func(*args, **kwargs)
            colored_print(message, color='red', style='bright')

    return wrapper


@tk_exceptions
def create_top_level(root, *args, **kwargs):
    tk_functions_logger.info('TopLevel успешно создан.')
    return tk.Toplevel(root, *args, **kwargs)


@tk_exceptions
def create_boolean_var(*args, **kwargs):
    tk_functions_logger.info('BooleanVar успешно создан.')
    return tk.BooleanVar(*args, **kwargs)


@tk_exceptions
def create_string_var(*args, **kwargs):
    tk_functions_logger.info('StringVar успешно создан.')
    return tk.StringVar(*args, **kwargs)


@tk_exceptions
def create_int_var(*args, **kwargs):
    tk_functions_logger.info('IntVar успешно создан.')
    return tk.IntVar(*args, **kwargs)


@tk_exceptions
def create_label(root, *args, **kwargs):
    tk_functions_logger.info('Label успешно создан.')
    return tk.Label(root, *args, **kwargs)


@tk_exceptions
def create_button(root, *args, **kwargs):
    tk_functions_logger.info('Button успешно создан.')
    return tk.Button(root, *args, **kwargs)


@tk_exceptions
def create_ttk_button(root, style: str = None, *args, **kwargs):
    tk_functions_logger.info('ttk.Button успешно создан.')
    return ttk.Button(root, style=style, *args, **kwargs)


@tk_exceptions
def create_radio_button(root, *args, **kwargs):
    tk_functions_logger.info('Radiobutton успешно создан.')
    return tk.Radiobutton(root, *args, **kwargs)


@tk_exceptions
def create_text_widget(root, *args, **kwargs):
    tk_functions_logger.info('Text успешно создан.')
    return tk.Text(root, *args, **kwargs)


@tk_exceptions
def create_listbox(root, *args, **kwargs):
    tk_functions_logger.info('Listbox успешно создан.')
    return tk.Listbox(root, *args, **kwargs)


@tk_exceptions
def create_entry(root, *args, **kwargs):
    tk_functions_logger.info('Entry успешно создан.')
    return tk.Entry(root, *args, **kwargs)


@tk_exceptions
def create_image(image_path, *args, **kwargs):
    tk_functions_logger.info('PhotoImage успешно создан.')
    return tk.PhotoImage(file=image_path, *args, **kwargs)


@tk_exceptions
def create_frame(root, *args, **kwargs):
    tk_functions_logger.info('Frame успешно создан.')
    return tk.Frame(root, *args, **kwargs)


@tk_exceptions
def create_ttk_combobox(root, *args, **kwargs):
    tk_functions_logger.info('Combobox успешно создан.')
    return ttk.Combobox(root, *args, **kwargs)


@tk_exceptions
def create_ttk_treeview(root, *args, **kwargs):
    tk_functions_logger.info('Treeview успешно создан.')
    return ttk.Treeview(root, *args, **kwargs)
