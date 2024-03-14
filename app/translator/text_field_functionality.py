import httpcore
import keyboard
import pyperclip
from googletrans import Translator
from tkinter import SEL, END, INSERT, Menu


class TextFieldFunctionality:
    @staticmethod
    def copy_text(root, text_widgets):
        active_widget = root.focus_get()
        if active_widget in text_widgets:
            try:
                sel_indices = active_widget.tag_ranges(SEL)
                if sel_indices:
                    selected_text = active_widget.get(sel_indices[0], sel_indices[1])
                    pyperclip.copy(selected_text)
            except IndexError:
                active_widget.event_generate("<<Copy>>")

    @staticmethod
    def paste_text(root, text_widgets):
        active_widget = root.focus_get()
        if active_widget in text_widgets:
            active_widget.insert(INSERT, root.clipboard_get())

    @staticmethod
    def select_all(root, text_widgets):
        active_widget = root.focus_get()
        if active_widget in text_widgets:
            try:
                active_widget.tag_add(SEL, "1.0", END)
            except IndexError:
                active_widget.select_range(0, END)

    @staticmethod
    def cut_text(root, text_widgets):
        active_widget = root.focus_get()
        if active_widget in text_widgets:
            try:
                sel_indices = active_widget.tag_ranges(SEL)
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
            context_menu = Menu(root, tearoff=0)
            context_menu.add_command(label="Вырезать",
                                     command=lambda: cls.cut_text(root=root, text_widgets=text_widgets))
            context_menu.add_command(label="Копировать",
                                     command=lambda: cls.copy_text(root=root, text_widgets=text_widgets))
            context_menu.add_command(label="Вставить",
                                     command=lambda: cls.paste_text(root=root, text_widgets=text_widgets))

            widget.bind("<Button-3>", show_context_menu)

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


class TextWorker:
    def __init__(self, fl=None, tl=None):
        self.t = Translator()
        self.fl = fl
        self.tl = tl

    def get_text_translator(self, first_text_widget, second_text_widget):
        try:
            result = self.t.translate(src=self.fl, dest=self.tl, text=first_text_widget.get("1.0", "end"))
            second_text_widget.delete('1.0', 'end')
            second_text_widget.insert('1.0', result.text)
        except (httpcore.ConnectTimeout, httpcore.ConnectError) as e:
            print(e)
            print('Проблемы с подключением к интернету. Проверьте ваше соединение')