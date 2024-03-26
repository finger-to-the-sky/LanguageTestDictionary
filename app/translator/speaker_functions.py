import threading
import time
import gtts
from os import environ
import tkinter as tk
from gtts import gTTS
from app.config import LANGUAGES
from app.config import main_logger, exceptions_logger
from app.fonts import FontManager
from app.other.custom_print import colored_print
from app.tk_functions import create_image, create_label, create_button

environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame


class CreateSpeakerForText:
    FILES_DIRECTORY = './app/other/audio/'
    DEFAULT_FILE = 'text.mp3'
    FILEPATH = f'{FILES_DIRECTORY}{DEFAULT_FILE}'
    IMAGEPATH = './app/other/icons/speakers/speaker24.png'

    def __init__(self, root):
        self.root = root
        self.speaker_image = create_image(image_path=self.IMAGEPATH)
        self.font = FontManager()
        self.error = False
        self.error_label = create_label(root=self.root, fg='red', font=self.font.LABEL_FONTS['Errors'])
        main_logger.info(f'Класс синтезатора был проинициализирован в {self.root.title()}')

    def set_error_for_exceptions(self, text):
        if self.error is False:
            self.error = True
            self.error_label.configure(text=text)
            self.error_label.pack(pady=10)

    def create_btn(self, text_widget, image=None, current_lang: str = 'English'):
        if image is None:
            image = self.speaker_image
        btn = create_button(root=self.root, image=image, borderwidth=0,
                            command=lambda: threading.Thread(target=self.play_audio,
                                                             kwargs={
                                                                 'text': text_widget.get("1.0", tk.END),
                                                                 'current_language': current_lang}
                                                             ).start())
        btn.bind("<Enter>", btn.config(cursor="hand2"))
        return btn

    def create_audiofile(self, text: str, lang: str, filepath: str = None):
        if lang not in LANGUAGES.values():
            colored_print(message=f'{lang} - нет в списке языков для play_audio()', color='red', style='bright')
        try:
            tts = gTTS(text=text, lang=lang, slow=False)
            if filepath is not None:
                tts.save(filepath)
            else:
                tts.save(self.FILEPATH)

            self.error = False
            self.error_label.pack_forget()
            return filepath
        except ValueError as e:
            message = 'Неподдерживаемый формат файла'
            exceptions_logger.error(f'{message} {self.create_audiofile}')
            colored_print(f'{message} {self.create_audiofile}', color='red', style='bright')

        except AssertionError as e:
            message = 'Отстуствует текст для озвучивания'
            exceptions_logger.error(f'{message} {self.create_audiofile}')
            self.set_error_for_exceptions(message)

        except gtts.gTTSError as e:
            message = 'Проблемы с подключением к интернету. Проверьте ваше соединение'
            exceptions_logger.error(f'{message} {self.create_audiofile}')
            self.set_error_for_exceptions(message)

        except PermissionError as e:
            file = self.create_audiofile(text=text, filepath=f'{self.FILES_DIRECTORY}text1.mp3',
                                         lang=lang)
            return file

    def play_audio(self, text: str, filepath: str = None, current_language: str = 'English'):
        self.stop_speaker()
        if filepath is not None:
            file = self.create_audiofile(text=text, filepath=filepath, lang=current_language)
        else:
            file = self.create_audiofile(text=text, filepath=self.FILEPATH, lang=current_language)
        try:
            pygame.mixer.init()
            pygame.mixer.music.load(file)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                time.sleep(1)

            pygame.mixer.music.stop()
            pygame.mixer.quit()

        except PermissionError:
            pass
        except (AssertionError, pygame.error) as e:
            message = 'Нет файлового обьекта для синтезатора'
            exceptions_logger.error(f'{message} {self.play_audio}')
            colored_print(f'{message} {self.play_audio}', color='red', style='bright')
        except FileNotFoundError:
            message = 'Аудиофайл был не найден'
            exceptions_logger.error(f'{message} {self.play_audio}')
            colored_print(f'{message} {self.play_audio}', color='red', style='bright')

    @staticmethod
    def stop_speaker():
        try:
            pygame.mixer.music.stop()
        except pygame.error as e:
            pass
