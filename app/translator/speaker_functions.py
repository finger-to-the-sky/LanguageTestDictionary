import threading
import time
import gtts
from os import environ
import tkinter as tk
from gtts import gTTS
from app.config import LANGUAGES, PROJECT_DIR, main_logger, exceptions_logger
from app.fonts import FontManager
from app.other.custom_print import colored_print
from app.tk_functions import create_image, create_label, create_button

environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame


class CreateSpeakerForText:
    """
    Class for creating translation files, playing them back, and speech synthesizer buttons
    """

    _FILES_DIRECTORY = f'{PROJECT_DIR}\\app\\other\\audio\\'
    _DEFAULT_FILE = 'text.mp3'
    _FILEPATH = f'{_FILES_DIRECTORY}{_DEFAULT_FILE}'
    _IMAGEPATH = f'{PROJECT_DIR}\\app\\other\\icons\\speakers\\speaker24.png'

    def __init__(self, root):
        """
        :param root: tkinter.Tk(), tkinter.TopLevel() or any same object
        """
        try:
            self.root = root
            self.speaker_image = create_image(image_path=self._IMAGEPATH)
            self.font = FontManager()
            self.error = False
            self.error_label = create_label(root=self.root, fg='red', font=self.font.LABEL_FONTS['Errors'])
            main_logger.info(f'Класс: {CreateSpeakerForText.__name__} был проинициализирован в {self.root.title()}')
        except (TypeError, AttributeError) as e:
            message = (f'Класс: {CreateSpeakerForText.__name__} не смог инициализироваться. Неверно переданы параметры.'
                       f' {e}')
            main_logger.error(message)
            colored_print(message, color='red', style='bright')

    def set_error_for_exceptions(self, text: str):
        """
        Method for displaying errors to the user on the screen

        :param text:
        :return:
        """

        if self.error is False:
            self.error = True
            self.error_label.configure(text=text)
            self.error_label.pack(pady=10)

    def create_btn(self, text_widget: tk.Text, image=None, current_lang: str = 'English') -> tk.Button:
        """
        Method for creating a speech synthesizer button.

        :param text_widget: tkinter.Text() - Text widget from which text will be extracted for the speech synthesizer
        :param image: tk.PhotoImage() - tkinter object for setting an image for the button
        :param current_lang: - Current language for setting the accent of the speech synthesizer
        :return: tkinter.Button()
        """

        if image is None:
            image = self.speaker_image
        try:
            btn = create_button(root=self.root, image=image, borderwidth=0,
                                command=lambda: threading.Thread(target=self.play_audio,
                                                                 kwargs={
                                                                     'file': self.create_audiofile(
                                                                         text_widget.get("1.0", tk.END),
                                                                         filepath=self._FILEPATH,
                                                                         lang=current_lang)
                                                                 }).start())
            btn.bind("<Enter>", btn.config(cursor="hand2"))
            return btn
        except (AttributeError, TypeError) as e:
            message = f'Функция: {self.create_btn.__name__} получила неверные аргументы. {e}'
            main_logger.error(message)
            colored_print(message, color='red', style='bright')

    def create_audiofile(self, text: str, lang: str, filepath: str = None) -> str:
        """
        Method for recording speech synthesis of text to a file

        :param text: Text to be recorded
        :param lang: Language for accent
        :param filepath: Path to the resulting file
        :return:
        """

        if lang not in LANGUAGES.values():
            colored_print(message=f'{lang} - нет в списке языков для play_audio()', color='red', style='bright')

        try:
            tts = gTTS(text=text, lang=lang, slow=False)
            if filepath is not None:
                tts.save(filepath)
            else:
                tts.save(self._FILEPATH)

            self.error = False
            self.error_label.pack_forget()
            return filepath
        except (TypeError, AttributeError) as e:
            message = f'В функцию: {self.create_audiofile.__name__} переданы неверные аргументы {e}'
            exceptions_logger.error(message)
            colored_print(message, color='red', style='bright')
        except ValueError as e:
            message = f'Неподдерживаемый формат файла {self.create_audiofile.__name__} {e}'
            exceptions_logger.error(message)
            colored_print(message, color='red', style='bright')

        except AssertionError as e:
            message = 'Отстуствует текст для озвучивания'
            exceptions_logger.error(f'{message} {self.create_audiofile.__name__} {e}')
            self.set_error_for_exceptions(message)

        except gtts.gTTSError as e:
            message = 'Проблемы с подключением к интернету. Проверьте ваше соединение'
            exceptions_logger.error(f'{message} {self.create_audiofile.__name__} {e}')
            self.set_error_for_exceptions(message)

        except PermissionError:
            file = self.create_audiofile(text=text, filepath=f'{self._FILES_DIRECTORY}text1.mp3',
                                         lang=lang)
            return file

    def play_audio(self, file: str):
        """
        Method for playing back synthesized audio

        :param file: File path
        :return:
        """

        self.stop_speaker()
        try:
            pygame.mixer.init()
            pygame.mixer.music.load(file)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                time.sleep(1)
            pygame.mixer.music.stop()
            pygame.mixer.quit()
            return True
        except PermissionError:
            pass
        except (AssertionError, pygame.error) as e:
            message = f'Нет файлового обьекта для синтезатора {self.play_audio} {e}'
            exceptions_logger.error(message)
            colored_print(message, color='red', style='bright')
        except FileNotFoundError as e:
            message = f'Аудиофайл был не найден {self.play_audio} {e}'
            exceptions_logger.error(message)
            colored_print(message, color='red', style='bright')

    @staticmethod
    def stop_speaker():
        """
        Method for stopping audio playback

        :return:
        """
        try:
            pygame.mixer.music.stop()
        except pygame.error:
            pass
