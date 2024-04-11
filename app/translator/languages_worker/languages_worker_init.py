from app.other.custom_print import colored_print
from app.translator.speaker_functions import CreateSpeakerForText
from app.translator.text_field_functionality import TextWorker
from app.fonts import FontManager
from app.tk_functions import create_image, create_button, create_ttk_combobox
import tkinter as tk
from app.config import main_logger, PROJECT_DIR


class LanguagesWorkerInit:
    """
    Class for setting up language panels, synthesizer buttons, clearing, and translation.
    """

    FROM_LANGUAGE = "English"
    TO_LANGUAGE = "Russian"
    TEXT_WORKER = TextWorker(src=FROM_LANGUAGE, dest=TO_LANGUAGE)
    IMAGEPATH = f'{PROJECT_DIR}/app/other/icons/clear/clear24.png'

    def __init__(self, root, user_text_widget: tk.Text, translated_text_widget: tk.Text, frame: tk.Frame):
        """
        :param root: tkinter.Tk(), tkinter.TopLevel() or any same objects
        :param user_text_widget: tkinter.Text() - Text widget for entering text.
        :param translated_text_widget: tkinter.Text() - Text widget for displaying the translation of text from the
        first widget.
        :param frame: - tkinter.Frame() - For positioning objects created in this class.
        """

        if self.check_arguments_typing(root, user_text_widget, translated_text_widget, frame) is False:
            message = f'Класс {self.__str__()} не смог инициализировать объекты. Ошибка входящих данных.',
            colored_print(message, color='red', style='bright')
            main_logger.error(message)
            return

        self.root = root
        self.user_text_widget = user_text_widget
        self.translated_text_widget = translated_text_widget
        self.frame = frame

        self.clear_image = create_image(image_path=self.IMAGEPATH)
        self.font_manager = FontManager()
        self.translator_fonts = self.font_manager.BUTTON_FONTS['TranslatorButtons']
        self.speaker = CreateSpeakerForText(root)

        main_logger.info(f"Класс {self.__str__()} был успешно инициализирован в окне {self.root.title()}")

    @staticmethod
    def check_arguments_typing(root, user_text_widget: tk.Text, translated_text_widget: tk.Text,
                               frame: tk.Frame) -> bool:
        """
        A method for validating incoming objects in the `__init__` constructor.

        :param root: tkinter.Tk(), tkinter.TopLevel() or any same objects
        :param user_text_widget: tkinter.Text() - Text widget for entering text.
        :param translated_text_widget: tkinter.Text() - Text widget for displaying the translation of text from the
        first widget.
        :param frame: - tkinter.Frame() - For positioning objects created in this class.
        :return bool type.
        """

        is_root = isinstance(root, tk.Tk)
        is_user_text_widget = isinstance(user_text_widget, tk.Text)
        is_translated_text_widget = isinstance(translated_text_widget, tk.Text)
        is_frame = isinstance(frame, tk.Frame)
        if is_root and is_frame and is_translated_text_widget and is_user_text_widget:
            return True
        return False

    @staticmethod
    def create_languages_lists(root, start_values: tuple, combo_from_args: dict, combo_to_args: dict,
                               bind_arguments: tuple):
        """
        Method for creating language panels.

        :param root: tkinter.Tk(), tkinter.TopLevel() or any same objects
        :param start_values: Initial values to be set in the language panels.
        :param combo_from_args: Arguments for ttk.Combobox() objects.
        :param combo_to_args: Arguments for ttk.Combobox() objects.
        :param bind_arguments: Arguments for binding events to ttk.Combobox() objects.
        :return: [ttk.Combobox(), ttk.Combobox()]
        """

        try:
            combo_from = create_ttk_combobox(root=root, **combo_from_args)
            combo_to = create_ttk_combobox(root=root, **combo_to_args)
            if combo_from is None or combo_to is None:
                return
            combo_from.set(start_values[0])
            combo_to.set(start_values[1])
            combo_from.bind(bind_arguments[0], bind_arguments[1])
            combo_to.bind(bind_arguments[0], bind_arguments[1])
            main_logger.info(f'Функция {LanguagesWorkerInit.create_languages_lists.__name__} успешно отработала')
            return [combo_from, combo_to]
        except (IndexError, TypeError, KeyError) as e:
            message = f"Неверные аргументы к функции {LanguagesWorkerInit.create_languages_lists.__name__} {e}"
            colored_print(message, color='red', style='bright')
            main_logger.error(message)

    @staticmethod
    def create_workers_audio_buttons(speaker: CreateSpeakerForText, voice_btn1_args: dict,
                                     voice_btn2_args: dict) -> dict:
        """
        Method for creating speech synthesizer buttons.

        :param speaker: Object of the class CreateSpeakerForText()
        :param voice_btn1_args: Arguments for creating a speech synthesizer button
        :param voice_btn2_args: Arguments for creating a speech synthesizer button
        :return: {tk.Button(), tk.Button()}
        """

        try:
            voice_btn1 = speaker.create_btn(**voice_btn1_args)
            voice_btn2 = speaker.create_btn(**voice_btn2_args)
            return {'voice_button_1': voice_btn1, 'voice_button_2': voice_btn2}
        except (TypeError, AttributeError) as e:
            message = f"Неверные аргументы к функции {LanguagesWorkerInit.create_workers_audio_buttons.__name__} {e}"
            colored_print(message, color='red', style='bright')
            main_logger.error(message)

    @staticmethod
    def create_workers_buttons(root, translate_btn_args: dict, clear_btn_args: dict):
        """
        Method for creating buttons to clear text and its translation

        :param root: tkinter.Tk(), tkinter.TopLevel() or any same objects
        :param translate_btn_args: Arguments for creating a translation button
        :param clear_btn_args: Arguments for creating a clear button
        :return: {tk.Button(), tk.Button()}
        """

        message = f"Неверные аргументы к функции {LanguagesWorkerInit.create_workers_buttons.__name__}"
        try:
            translate_btn = create_button(root=root, **translate_btn_args)
            clear_btn = create_button(root=root, **clear_btn_args)
            if translate_btn is None and clear_btn is None:
                colored_print(message, color='red', style='bright')
                main_logger.error(message)
                return
            else:
                clear_btn.bind("<Enter>", clear_btn.config(cursor="hand2"))
                return {'translate_text_button': translate_btn, 'clear_text_button': clear_btn}
        except (TypeError, AttributeError) as e:
            colored_print(message, color='red', style='bright')
            main_logger.error(f'{message} {e}')
