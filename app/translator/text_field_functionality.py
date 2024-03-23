import httpcore
import keyboard
import pyperclip
from googletrans import Translator
import tkinter as tk
from app.config import main_logger, exceptions_logger
from app.fonts import FontManager
from app.other.custom_print import colored_print


class TextFieldFunctionality:
    @staticmethod
    def copy_text(root, text_widgets):
        active_widget = root.focus_get()
        if active_widget in text_widgets:
            try:
                sel_indices = active_widget.tag_ranges(tk.SEL)
                if sel_indices:
                    selected_text = active_widget.get(sel_indices[0], sel_indices[1])
                    pyperclip.copy(selected_text)
            except IndexError:
                active_widget.event_generate("<<Copy>>")

    @staticmethod
    def paste_text(root, text_widgets):
        active_widget = root.focus_get()
        if active_widget in text_widgets:
            active_widget.insert(tk.INSERT, root.clipboard_get())

    @staticmethod
    def select_all(root, text_widgets):
        active_widget = root.focus_get()
        if active_widget in text_widgets:
            try:
                active_widget.tag_add(tk.SEL, "1.0", tk.END)
            except IndexError:
                active_widget.select_range(0, tk.END)

    @staticmethod
    def cut_text(root, text_widgets):
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

    @classmethod
    def create_context_menu(cls, root, text_widgets):
        def show_context_menu(event):
            context_menu.post(event.x_root, event.y_root)

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

    @classmethod
    def russian_add_hotkeys(cls, root, text_widgets):
        """
        Connect hotkeys for russian keyboard
        :param root:
        :param text_widgets:
        :return:
        """
        keyboard.add_hotkey('ctrl+alt+c', lambda: cls.copy_text(root=root, text_widgets=text_widgets))
        keyboard.add_hotkey('ctrl+alt+v', lambda: cls.paste_text(root=root, text_widgets=text_widgets))
        keyboard.add_hotkey('ctrl+a', lambda: cls.select_all(root=root, text_widgets=text_widgets))
        keyboard.add_hotkey('ctrl+alt+x', lambda: cls.cut_text(root=root, text_widgets=text_widgets))
        main_logger.info(f'Горячие клавиши для текстовых виджетов в окне {root.title()} были добавлены')


class TextWorker:
    def __init__(self, src=None, dest=None):
        self.translator = Translator()
        self.src = src
        self.dest = dest
        self.font_manager = FontManager()
        self.error = False
        self.error_label = None

    @staticmethod
    def check_exceptions(func):
        def wrapper(*args, **kwargs):
            self = args[0]
            try:
                if self.error is False:
                    self.error_label = tk.Label(kwargs['root'], fg='red', font=self.font_manager.LABEL_FONTS['Errors'])
                result = func(*args, **kwargs)
                self.error = False
                self.error_label.pack_forget()
                return result

            except (httpcore.ConnectTimeout, httpcore.ConnectError) as e:
                message = 'Проблемы с подключением к интернету. Проверьте ваше соединение.'
                exceptions_logger.error(f'{self.get_text_translator}\n'
                                        f'{message}')
                self.set_error_for_exceptions(message)
            except IndexError as e:
                message = 'Попытка перевода пустых полей.'
                exceptions_logger.error(f'{self.get_text_translator}\n'
                                        f'{message}')
                self.set_error_for_exceptions(message)
            except ValueError as e:
                message = 'Языка с таким названием нет в списке GoogleTrans'
                exceptions_logger.error(f'{self.get_text_translator}\n'
                                        f'{message}')
                colored_print(f'{e} {message} {self.create_audiofile}', color='red', style='bright')

        return wrapper

    @check_exceptions
    def get_text_translator(self, root, first_text_widget, second_text_widget):
        text = first_text_widget.get("1.0", "end")
        if self.error is True and len(text) <= 1:
            return
        result = self.translator.translate(src=self.src, dest=self.dest, text=text)
        second_text_widget.delete('1.0', 'end')
        second_text_widget.insert('1.0', result.text)

    def set_error_for_exceptions(self, text):
        if self.error is False:
            self.error = True
            self.error_label.configure(text=text)
            self.error_label.pack(pady=10)
