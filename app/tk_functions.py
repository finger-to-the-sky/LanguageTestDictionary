import tkinter as tk
from tkinter import ttk


def create_top_level(root, *args, **kwargs):
    return tk.Toplevel(root, *args, **kwargs)


def create_boolean_var(*args, **kwargs):
    return tk.BooleanVar(*args, **kwargs)


def create_string_var(*args, **kwargs):
    return tk.StringVar(*args, **kwargs)


def create_int_var(*args, **kwargs):
    return tk.IntVar(*args, **kwargs)


def create_label(root, *args, **kwargs):
    return tk.Label(root, *args, **kwargs)


def create_button(root, *args, **kwargs):
    return tk.Button(root, *args, **kwargs)


def create_ttk_button(root, *args, **kwargs):
    return ttk.Button(root, *args, **kwargs)


def create_radio_button(root, *args, **kwargs):
    return tk.Radiobutton(root, *args, **kwargs)


def create_text_widget(root, *args, **kwargs):
    return tk.Text(root, *args, **kwargs)


def create_listbox(root, *args, **kwargs):
    return tk.Listbox(root, *args, **kwargs)


def create_entry(root, *args, **kwargs):
    return tk.Entry(root, *args, **kwargs)


def create_image(image_path, *args, **kwargs):
    return tk.PhotoImage(file=image_path, *args, **kwargs)


def create_frame(root, *args, **kwargs):
    return tk.Frame(root, *args, **kwargs)


def create_ttk_combobox(root, *args, **kwargs):
    return ttk.Combobox(root, *args, **kwargs)


def create_ttk_treeview(root, *args, **kwargs):
    return ttk.Treeview(root, *args, **kwargs)
