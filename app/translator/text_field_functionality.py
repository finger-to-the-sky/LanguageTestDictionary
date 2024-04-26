import re

import httpcore
import keyboard
import pyperclip
from googletrans import Translator
import tkinter as tk
from app.config import main_logger
from app.logger import exceptions_logger
from app.fonts import FontManager
from app.other.custom_print import colored_print
from app.tk_functions import create_label


class TextFieldFunctionality:
    """
    Class for extending the functionality of text fields
    """

    @staticmethod
    def copy_text(root, text_widgets: tuple):
        """
        Method for copying text

        :param root: tkinter.Tk(), tkinter.Toplevel() or any same object
        :param text_widgets: tkinter.Text() - Tuple of text widgets for binding functionality
        :return:
        """

        try:
            active_widget = root.focus_get()
            if active_widget in text_widgets:
                try:
                    sel_indices = active_widget.tag_ranges(tk.SEL)
                    if sel_indices:
                        selected_text = active_widget.get(sel_indices[0], sel_indices[1])
                        pyperclip.copy(selected_text)
                except IndexError:
                    active_widget.event_generate("<<Copy>>")
            return True
        except (AttributeError, TypeError) as e:
            message = f'Функция: {TextFieldFunctionality.copy_text.__name__} получила неверные аргументы {e}'
            main_logger.error(message)
            colored_print(message)

    @staticmethod
    def paste_text(root, text_widgets: tuple):
        """
        Method for inserting text

        :param root: tkinter.Tk(), tkinter.Toplevel() or any same object
        :param text_widgets: tkinter.Text() - Tuple of text widgets for binding functionality
        :return:
        """

        try:
            active_widget = root.focus_get()
            if active_widget in text_widgets:
                active_widget.insert(tk.INSERT, root.clipboard_get())
            return True
        except (AttributeError, TypeError) as e:
            message = f'Функция: {TextFieldFunctionality.paste_text.__name__} получила неверные аргументы {e}'
            main_logger.error(message)
            colored_print(message)

    @staticmethod
    def select_all(root, text_widgets: tuple):
        """
        Method for selecting text

        :param root: tkinter.Tk(), tkinter.Toplevel() or any same object
        :param text_widgets: tkinter.Text() - Tuple of text widgets for binding functionality
        :return:
        """

        try:
            active_widget = root.focus_get()
            if active_widget in text_widgets:
                try:
                    active_widget.tag_add(tk.SEL, "1.0", tk.END)
                except IndexError:
                    active_widget.select_range(0, tk.END)
            return True
        except (AttributeError, TypeError) as e:
            message = f'Функция: {TextFieldFunctionality.select_all.__name__} получила неверные аргументы {e}'
            main_logger.error(message)
            colored_print(message)

    @staticmethod
    def cut_text(root, text_widgets: tuple):
        """
        Method for cutting text

        :param root: tkinter.Tk(), tkinter.Toplevel() or any same object
        :param text_widgets: tkinter.Text() - Tuple of text widgets for binding functionality
        :return:
        """

        try:
            active_widget = root.focus_get()
            if active_widget in text_widgets:
                try:
                    sel_indices = active_widget.tag_ranges(tk.SEL)
                    if sel_indices:
                        selected_text = active_widget.get(sel_indices[0], sel_indices[1])
                        pyperclip.copy(selected_text)
                        active_widget.delete(sel_indices[0], sel_indices[1])
                except IndexError:
                    active_widget.event_generate("<<Cut>>")
            return True
        except (AttributeError, TypeError) as e:
            message = f'Функция: {TextFieldFunctionality.cut_text.__name__} получила неверные аргументы {e}'
            main_logger.error(message)
            colored_print(message)

    @classmethod
    def create_context_menu(cls, root, text_widgets: tuple):
        """
        Method for creating a context menu on right-click

        :param root: tkinter.Tk(), tkinter.Toplevel() or any same object
        :param text_widgets: tkinter.Text() - Tuple of text widgets for binding functionality
        :return:
        """

        def show_context_menu(event):
            context_menu.post(event.x_root, event.y_root)

        try:
            for widget in text_widgets:
                context_menu = tk.Menu(root, tearoff=0)
                context_menu.add_command(label="Вырезать",
                                         command=lambda: cls.cut_text(root=root, text_widgets=text_widgets))
                context_menu.add_command(label="Копировать",
                                         command=lambda: cls.copy_text(root=root, text_widgets=text_widgets))
                context_menu.add_command(label="Вставить",
                                         command=lambda: cls.paste_text(root=root, text_widgets=text_widgets))
                widget.bind("<Button-3>", show_context_menu)

            main_logger.info(f'Контекстное меню для текстовых виджетов в окне {root.title()} было создано')
            return True
        except (AttributeError, TypeError) as e:
            message = f'Функция: {TextFieldFunctionality.cut_text.__name__} получила неверные аргументы {e}'
            main_logger.error(message)
            colored_print(message)

    @classmethod
    def russian_add_hotkeys(cls, root, text_widgets: tuple):
        """
        Method for adding new hotkeys for the Russian keyboard layout

        :param root: tkinter.Tk(), tkinter.Toplevel() or any same object
        :param text_widgets: tkinter.Text() - Tuple of text widgets for binding functionality
        :return:
        """
        try:
            keyboard.add_hotkey('ctrl+alt+c', lambda: cls.copy_text(root=root, text_widgets=text_widgets))
            keyboard.add_hotkey('ctrl+alt+v', lambda: cls.paste_text(root=root, text_widgets=text_widgets))
            keyboard.add_hotkey('ctrl+a', lambda: cls.select_all(root=root, text_widgets=text_widgets))
            keyboard.add_hotkey('ctrl+alt+x', lambda: cls.cut_text(root=root, text_widgets=text_widgets))
            main_logger.info(f'Горячие клавиши для текстовых виджетов в окне {root.title()} были добавлены')
            return True
        except (AttributeError, TypeError) as e:
            message = f'Функция: {TextFieldFunctionality.russian_add_hotkeys.__name__} получила неверные аргументы {e}'
            main_logger.error(message)
            colored_print(message)


class TextWorker:
    """
    Class for working with user text
    """

    def __init__(self, src: str = None, dest: str = None):
        """
        :param src: The language of the text
        :param dest: Language for translating the text
        """

        self.translator = Translator()
        self.src = src
        self.dest = dest
        self.font_manager = FontManager()
        self.error = False
        self.error_label = None

    @staticmethod
    def check_exceptions(func):
        """
        Decorator for handling exceptions during text translation
        :param func:
        :return:
        """

        def wrapper(*args, **kwargs):
            self = args[0]
            try:
                if self.error is False:
                    try:
                        self.error_label = create_label(root=kwargs['root'], fg='red',
                                                        font=self.font_manager.LABEL_FONTS['Errors'])
                    except KeyError as e:
                        message = f'Не удалось найти аргумент root {self.check_exceptions.__name__} {e}'
                        colored_print(message, color='red', style='bright')
                        main_logger.error(message)

                result = func(*args, **kwargs)
                self.error = False
                if self.error_label is not None:
                    self.error_label.pack_forget()
                return result

            except (httpcore.ConnectTimeout, httpcore.ConnectError) as e:
                message = 'Проблемы с подключением к интернету. Проверьте ваше соединение.'
                exceptions_logger.error(f'{self.get_text_translator.__name__} {message} {e}')
                self.set_error_for_exceptions(message)
            except IndexError as e:
                message = 'Попытка перевода пустых полей.'
                exceptions_logger.error(f'{self.get_text_translator.__name__} {message} {e}')
                self.set_error_for_exceptions(message)
            except ValueError as e:
                message = f'{self.get_text_translator.__name__} Языка с таким названием нет в списке GoogleTrans {e}'
                exceptions_logger.error(message)
                colored_print(message, color='red', style='bright')
            except (TypeError, AttributeError) as e:
                message = f'Функция {self.get_text_translator.__name__} приняла не верные параметры {e}'
                main_logger.error(message)
                colored_print(message, color='red', style='bright')

        return wrapper

    @check_exceptions
    def get_text_translator(self, root, first_text_widget: tk.Text, second_text_widget: tk.Text):
        """
        Method for extracting text from a widget, its translation, and inserting the translation into another text
        widget

        :param root: tkinter.Tk(), tkinter.Toplevel() or any same object for the exception decorator
        :param first_text_widget: tkinter.Text() - Text widget for extracting text
        :param second_text_widget: tkinter.Text() - Text widget for inserting translation
        :return:
        """

        text = first_text_widget.get("1.0", "end")
        if self.error is True and len(text) <= 1:
            return
        elif len(text) <= 1:
            raise IndexError

        result = self.translator.translate(src=self.src, dest=self.dest, text=text)
        second_text_widget.delete('1.0', 'end')
        second_text_widget.insert('1.0', result.text)
        return result.text

    def set_error_for_exceptions(self, text):
        """
        Method for displaying errors to the user on the screen

        :param text:
        :return:
        """
        if self.error is False:
            self.error = True
            self.error_label.configure(text=text)
            self.error_label.pack(pady=10)
