import threading
import time
import gtts
from os import environ
import tkinter as tk
from gtts import gTTS
from app.config import LANGUAGES
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame



class CreateSpeakerForText:
    FILES_DIRECTORY = './app/other/audio/'
    DEFAULT_FILE = 'text.mp3'
    FILEPATH = f'{FILES_DIRECTORY}{DEFAULT_FILE}'
    IMAGEPATH = './app/other/icons/speakers/speaker24.png'

    def __init__(self, root):
        self.root = root
        self.speaker_image = tk.PhotoImage(file=self.IMAGEPATH)

    def create_btn(self, text, image=None, current_lang: str = 'English'):
        if image is None:
            image = self.speaker_image
        btn = tk.Button(self.root, image=image, background='white', borderwidth=0,
                        command=lambda: threading.Thread(target=self.play_audio,
                                                         kwargs={
                                                             'text': text,
                                                             'current_language': current_lang}
                                                         ).start())
        return btn

    def create_audiofile(self, text: str, lang: str, filepath: str = None):
        if lang not in LANGUAGES.values():
            raise ValueError(f'{lang} - нет в списке языков play_audio()')
        try:
            tts = gTTS(text=text, lang=lang, slow=False)
            if filepath is not None:
                tts.save(filepath)
            else:
                tts.save(self.FILEPATH)
            return filepath

        except gtts.gTTSError as e:
            print(e, self.create_audiofile)
            print('Проблемы с подключением к интернету. Проверьте ваше соединение')

        except PermissionError as e:
            print(e, self.create_audiofile)

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
            print(e, self.play_audio)
        except FileNotFoundError:
            print('Аудиофайл был не найден')

    @staticmethod
    def stop_speaker():
        try:
            pygame.mixer.music.stop()
        except pygame.error as e:
            pass
