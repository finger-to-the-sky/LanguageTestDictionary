import keyboard
import pyperclip
from googletrans import Translator
from tkinter import SEL, END, INSERT, Menu


class TextWorker:
    def __init__(self, fl=None, tl=None):
        self.t = Translator()
        self.fl = fl
        self.tl = tl

    def text_translate(self, text, reverse=False):
        try:
            if reverse:
                result = self.t.translate(src=self.tl, dest=self.fl, text=text)
            else:
                result = self.t.translate(src=self.fl, dest=self.tl, text=text)
            return result.text
        except TypeError:
            pass
        return None

    @staticmethod
    def copy_text(root, text_widgets):
        active_widget = root.focus_get()
        if active_widget in text_widgets:
            try:
                sel_indices = active_widget.tag_ranges(SEL)
                if sel_indices:
                    selected_text = active_widget.get(sel_indices[0], sel_indices[1])
                    pyperclip.copy(selected_text)
            except:
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
            except:
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
            except:
                active_widget.event_generate("<<Cut>>")


class TextWorkerTranslator(TextWorker):

    def __init__(self, fl, tl):
        super().__init__(fl, tl)

    def get_text_translator(self, user_textfield, tr_textfield):
        result = self.t.translate(src=self.fl, dest=self.tl, text=user_textfield.get("1.0", "end"))
        tr_textfield.delete('1.0', 'end')
        tr_textfield.insert('1.0', result.text)


def create_context_menu(root, text_widgets):
    """
    Create context menu for work with the text in any text field
    :param root:
    :param text_widgets:
    :return:
    """

    def show_context_menu(event):
        context_menu.post(event.x_root, event.y_root)

    for widget in text_widgets:
        context_menu = Menu(root, tearoff=0)
        context_menu.add_command(label="Вырезать",
                                 command=lambda: TextWorker.cut_text(root=root, text_widgets=text_widgets))
        context_menu.add_command(label="Копировать",
                                 command=lambda: TextWorker.copy_text(root=root, text_widgets=text_widgets))
        context_menu.add_command(label="Вставить",
                                 command=lambda: TextWorker.paste_text(root=root, text_widgets=text_widgets))

        widget.bind("<Button-3>", show_context_menu)


def russian_add_hotkeys(root, text_widgets):
    """
    Connect hotkeys for russian keyboard
    :param root:
    :param text_widgets:
    :return:
    """
    keyboard.add_hotkey('ctrl+alt+c', lambda: TextWorker.copy_text(root=root, text_widgets=text_widgets))
    keyboard.add_hotkey('ctrl+alt+v', lambda: TextWorker.paste_text(root=root, text_widgets=text_widgets))
    keyboard.add_hotkey('ctrl+a', lambda: TextWorker.select_all(root=root, text_widgets=text_widgets))
    keyboard.add_hotkey('ctrl+alt+x', lambda: TextWorker.cut_text(root=root, text_widgets=text_widgets))
