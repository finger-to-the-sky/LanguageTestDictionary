import tkinter as tk
from tkinter import ttk
from app.config import LANGUAGES_LIST, LANGUAGES
from app.translator.speaker_functions import CreateSpeakerForText
from app.translator.text_field_functionality import TextWorker


class LanguagesWorker:
    FROM_LANGUAGE = "English"
    TO_LANGUAGE = "Russian"
    TEXT_WORKER = TextWorker(fl=FROM_LANGUAGE, tl=TO_LANGUAGE)
    IMAGEPATH = './app/other/icons/clear/clear24.png'

    def __init__(self, root, user_text_widget, translated_text_widget, frame=None):
        self.root = root
        self.clear_image = tk.PhotoImage(file=self.IMAGEPATH)

        self.user_text_widget = user_text_widget
        self.translated_text_widget = translated_text_widget
        self.frame = frame

        self.combo_from = ttk.Combobox(self.frame, values=LANGUAGES_LIST, state='readonly')
        self.combo_to = ttk.Combobox(self.frame, values=LANGUAGES_LIST, state='readonly')
        self.combo_from.set(self.FROM_LANGUAGE)
        self.combo_to.set(self.TO_LANGUAGE)
        self.combo_from.bind('<<ComboboxSelected>>', lambda event: (self.on_select(self, event), self.change_lang_voices()))
        self.combo_to.bind('<<ComboboxSelected>>', lambda event: (self.on_select(self, event), self.change_lang_voices()))

        self.speaker = CreateSpeakerForText(root)
        self.voice_btn1 = self.speaker.create_btn(self.user_text_widget.get("1.0", tk.END), current_lang=LANGUAGES[self.FROM_LANGUAGE])
        self.voice_btn2 = self.speaker.create_btn(self.translated_text_widget.get("1.0", tk.END), current_lang=LANGUAGES[self.TO_LANGUAGE])

        self.translate_btn = tk.Button(root, text='Перевести', width=20,
                                       command=lambda: self.TEXT_WORKER.get_text_translator(
                                           first_text_widget=user_text_widget,
                                           second_text_widget=translated_text_widget))
        self.clear_btn = tk.Button(root, image=self.clear_image, background='white', borderwidth=0,
                                   command=lambda: (user_text_widget.delete("1.0", tk.END),
                                                    translated_text_widget.delete("1.0", tk.END),
                                                    self.speaker.stop_speaker()))

        self.combo_from.grid(row=0, column=2, padx=20)
        self.combo_to.grid(row=0, column=3, padx=20)
        self.translate_btn.pack()
        self.voice_btn1.place(x=845, y=120)
        self.voice_btn2.place(x=885, y=300)
        self.clear_btn.place(x=885, y=120)

    @classmethod
    def on_select(cls, self, event):
        cls.FROM_LANGUAGE = self.combo_from.get()
        cls.TO_LANGUAGE = self.combo_to.get()
        cls.TEXT_WORKER.__init__(fl=cls.FROM_LANGUAGE, tl=cls.TO_LANGUAGE)

    def change_lang_voices(self):
        self.voice_btn1.destroy()
        self.voice_btn2.destroy()
        self.voice_btn1 = self.speaker.create_btn(self.user_text_widget.get("1.0", tk.END),
                                                  current_lang=LANGUAGES[self.FROM_LANGUAGE])
        self.voice_btn2 = self.speaker.create_btn(self.translated_text_widget.get("1.0", tk.END),
                                                  current_lang=LANGUAGES[self.TO_LANGUAGE])
        self.voice_btn1.place(x=845, y=120)
        self.voice_btn2.place(x=885, y=300)
