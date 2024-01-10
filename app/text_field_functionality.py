import pyperclip
from googletrans import Translator
from tkinter import SEL, END, INSERT


class TextWorker:
    def __init__(self, fl, tl):
        self.t = Translator()
        self.fl = fl
        self.tl = tl

    def get_text(self, user_textfield, tr_textfield):
        result = self.t.translate(src=self.fl, dest=self.tl, text=user_textfield.get("1.0", "end"))
        tr_textfield.delete('1.0', 'end')
        tr_textfield.insert('1.0', result.text)

    @staticmethod
    def copy_text(root, text_widgets):
        active_widget = root.focus_get()
        if active_widget in text_widgets:
            sel_indices = active_widget.tag_ranges(SEL)
            if sel_indices:
                selected_text = active_widget.get(sel_indices[0], sel_indices[1])
                pyperclip.copy(selected_text)

    @staticmethod
    def paste_text(root, text_widgets):
        active_widget = root.focus_get()
        if active_widget in text_widgets:
            active_widget.insert(INSERT, root.clipboard_get())

    @staticmethod
    def select_all(root, text_widgets):
        active_widget = root.focus_get()
        if active_widget in text_widgets:
            active_widget.tag_add(SEL, "1.0", END)

    @staticmethod
    def cut_text(root, text_widgets):
        active_widget = root.focus_get()
        if active_widget in text_widgets:
            sel_indices = active_widget.tag_ranges(SEL)
            if sel_indices:
                selected_text = active_widget.get(sel_indices[0], sel_indices[1])
                pyperclip.copy(selected_text)
                active_widget.delete(sel_indices[0], sel_indices[1])
