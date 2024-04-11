import tkinter as tk
from app.config import LANGUAGES_LIST, LANGUAGES, main_logger
from app.other.custom_print import colored_print
from app.translator.languages_worker.languages_worker_init import LanguagesWorkerInit


class LanguagesWorker(LanguagesWorkerInit):
    """
    Class for positioning objects LanguagesWorkerInit and their configurations
    """

    def __init__(self, root, user_text_widget: tk.Text, translated_text_widget: tk.Text, frame: tk.Frame):
        super().__init__(root=root, user_text_widget=user_text_widget, translated_text_widget=translated_text_widget,
                         frame=frame)
        """
        :param root: tkinter.Tk(), tkinter.TopLevel() or any same objects
        :param user_text_widget: tkinter.Text() - Text widget for entering text.
        :param translated_text_widget: tkinter.Text() - Text widget for displaying the translation of text from the 
        first widget.
        :param frame: - tkinter.Frame() - For positioning objects created in this class.
        """

        try:
            self.combo_from, self.combo_to = self.create_languages_lists(
                root=self.frame,
                start_values=(self.FROM_LANGUAGE, self.TO_LANGUAGE),
                combo_from_args={'values': LANGUAGES_LIST, 'state': 'readonly',
                                 'font': self.translator_fonts['ComboBox_btn']},
                combo_to_args={'values': LANGUAGES_LIST, 'state': 'readonly',
                               'font': self.translator_fonts['ComboBox_btn']},
                bind_arguments=(
                    '<<ComboboxSelected>>', lambda event: (self.change_languages(self, event), self.change_lang_voices(
                        new_position_voice_btn1={"x": 915, "y": 175},
                        new_position_voice_btn2={"x": 915, "y": 340},
                        audio_buttons_args={"speaker": self.speaker,
                                            "voice_btn1_args": {"text_widget": self.user_text_widget,
                                                                "current_lang": LANGUAGES[self.FROM_LANGUAGE]},
                                            "voice_btn2_args": {
                                                "text_widget": self.translated_text_widget,
                                                "current_lang": LANGUAGES[self.TO_LANGUAGE]}}

                    )))
            )
        except TypeError:
            message = f"Функция: {LanguagesWorkerInit.create_languages_lists.__name__} не вернула ожидаемых результатов"
            colored_print(message, color='red', style='bright')
            main_logger.error(message)

        self.audio_buttons = self.create_workers_audio_buttons(
            speaker=self.speaker,
            voice_btn1_args={"text_widget": self.user_text_widget,
                             "current_lang": LANGUAGES[self.FROM_LANGUAGE]},
            voice_btn2_args={"text_widget": self.translated_text_widget,
                             "current_lang": LANGUAGES[self.TO_LANGUAGE]}
        )
        self.buttons = self.create_workers_buttons(
            root=self.root,
            translate_btn_args={"text": 'Перевести',
                                "width": 20,
                                "font": self.translator_fonts['Translate_btn'],
                                "command": lambda: self.TEXT_WORKER.get_text_translator(
                                    root=self.root,
                                    first_text_widget=self.user_text_widget,
                                    second_text_widget=self.translated_text_widget)
                                },
            clear_btn_args={"image": self.clear_image,
                            "borderwidth": 0,
                            "command": lambda: (self.user_text_widget.delete("1.0", tk.END),
                                                self.translated_text_widget.delete("1.0", tk.END),
                                                self.speaker.stop_speaker())
                            }
        )

        self.voice_btn1 = self.audio_buttons['voice_button_1']
        self.voice_btn2 = self.audio_buttons['voice_button_2']
        self.translate_btn = self.buttons['translate_text_button']
        self.clear_btn = self.buttons['clear_text_button']

        if self.check_complete_init_functions() is True:
            main_logger.info(f"Класс {self.__str__()} был успешно инициализирован в окне {self.root.title()}")

    def check_complete_init_functions(self):
        """
        Method for checking the successful creation of all necessary elements in the class
        :return: bool type
        """

        check_buttons_list = [self.voice_btn1, self.voice_btn2, self.translate_btn, self.clear_btn]
        for element in check_buttons_list:
            if element is None:
                if check_buttons_list.index(element) > 2:
                    message = f"Функция: {self.create_workers_audio_buttons.__name__} не вернула ожидаемых результатов"
                else:
                    message = f"Функция: {self.create_workers_buttons.__name__} не вернула ожидаемых результатов"
                colored_print(message, color='red', style='bright')
                main_logger.error(message)
                return False
        return True

    def change_lang_voices(self, new_position_voice_btn1: dict, new_position_voice_btn2: dict,
                           audio_buttons_args: dict):
        """
        Method for changing the language accent for speech synthesizer buttons

        :param new_position_voice_btn1: Arguments for positioning new speech synthesizer button
        :param new_position_voice_btn2: Arguments for positioning new speech synthesizer button
        :param audio_buttons_args: Arguments for creating a new speech synthesizer button
        :return:
        """

        if self.check_complete_init_functions() is False:
            return
        try:
            self.voice_btn1.destroy()
            self.voice_btn2.destroy()
            new_audio_buttons = self.create_workers_audio_buttons(**audio_buttons_args)
            self.voice_btn1 = new_audio_buttons['voice_button_1']
            self.voice_btn2 = new_audio_buttons['voice_button_2']
            self.voice_btn1.place(**new_position_voice_btn1)
            self.voice_btn2.place(**new_position_voice_btn2)

            main_logger.info(f'Функция {self.change_lang_voices} отработала корректно')
        except (TypeError, tk.TclError) as e:
            message = f'Функция: {self.change_lang_voices.__name__} получила невалидные аргументы {e}'
            colored_print(message, color='red', style='bright')
            main_logger.error(message)

    def show_elements(self, combo_from_pos: dict, combo_to_pos: dict, translate_btn_pos: dict, voice_btn1_pos: dict,
                      voice_btn2_pos: dict, clear_btn_pos: dict):
        """
        Method for displaying and positioning elements of the LanguagesWorker class

        :param combo_from_pos: Arguments for positioning language panel
        :param combo_to_pos: Arguments for positioning language panel
        :param translate_btn_pos: Arguments for positioning translate button
        :param voice_btn1_pos: Arguments for positioning speech synthesizer button
        :param voice_btn2_pos: Arguments for positioning speech synthesizer button
        :param clear_btn_pos: Arguments for positioning clear button
        :return:
        """

        if self.check_complete_init_functions() is False:
            return
        try:
            self.combo_from.grid(**combo_from_pos)
            self.combo_to.grid(**combo_to_pos)
            self.translate_btn.pack(**translate_btn_pos)
            self.voice_btn1.place(**voice_btn1_pos)
            self.voice_btn2.place(**voice_btn2_pos)
            self.clear_btn.place(**clear_btn_pos)
        except (TypeError, tk.TclError) as e:
            message = f'Функция: {self.show_elements.__name__} получила невалидные аргументы {e}'
            colored_print(message, color='red', style='bright')
            main_logger.error(message)

    @classmethod
    def change_languages(cls, self, event):
        """
        Method for changing languages from language panels

        :param self: LanguagesWorker object
        :param event: Event for changing languages
        :return:
        """
        try:
            cls.FROM_LANGUAGE = self.combo_from.get()
            cls.TO_LANGUAGE = self.combo_to.get()
            cls.TEXT_WORKER.__init__(src=cls.FROM_LANGUAGE, dest=cls.TO_LANGUAGE)
            main_logger.info(f'Функция {self.change_languages} отработала корректно')
        except AttributeError as e:
            message = f'Функция: {self.change_languages.__name__} получила невалидные аргументы {e}'
            colored_print(message, color='red', style='bright')
            main_logger.error(message)
