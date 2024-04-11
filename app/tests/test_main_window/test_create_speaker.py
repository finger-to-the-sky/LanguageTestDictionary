import pytest
import tkinter as tk
import os
from app.config import PROJECT_DIR
from app.translator.speaker_functions import CreateSpeakerForText
from contextlib import nullcontext
from app.tests.fixtures.test_main_window.test_create_speaker import speaker_class


class TestSpeakerClass:
    FILES_DIRECTORY = f'{PROJECT_DIR}\\app\\other\\audio\\'
    DEFAULT_FILE = 'text.mp3'
    FILEPATH = f'{FILES_DIRECTORY}{DEFAULT_FILE}'

    @pytest.mark.parametrize(
        'root, expectation', [
            (tk.Tk(), nullcontext()),
            (123, nullcontext()),
            ('string', nullcontext()),
            ({1, 2, 3}, nullcontext()),
            ((1, 2, 3), nullcontext()),
            ([], nullcontext()),
            ([1, 2, 3], nullcontext()),
            ({1: 2}, nullcontext()),
            (None, nullcontext()),
            (False, nullcontext()),
        ]
    )
    def test_init_speaker(self, root, expectation):
        with expectation:
            ins = CreateSpeakerForText(root)
            assert isinstance(ins, CreateSpeakerForText)

    @pytest.mark.parametrize(
        'text_widget, image, current_lang, expectation',
        [
            (tk.Text(tk.Tk()), None, 'English', nullcontext()),
            (123, None, 'English', nullcontext()),
            ('string', None, 'English', nullcontext()),
            ({1, 2, 3}, None, 'English', nullcontext()),
            ((1, 2, 3), None, 'English', nullcontext()),
            ([], None, 'English', nullcontext()),
            ([1, 2, 3], None, 'English', nullcontext()),
            ({1: 2}, None, 'English', nullcontext()),
            (None, None, 'English', nullcontext()),
            (False, None, 'English', nullcontext()),
            (tk.Tk(), None, 'English', nullcontext()),

            (tk.Text(tk.Tk()), 123, 'English', pytest.raises(AssertionError)),
            (tk.Text(tk.Tk()), 'string', 'English', pytest.raises(AssertionError)),
            (tk.Text(tk.Tk()), {1, 2, 3}, 'English', pytest.raises(AssertionError)),
            (tk.Text(tk.Tk()), (1, 2, 3), 'English', pytest.raises(AssertionError)),
            (tk.Text(tk.Tk()), [], 'English', nullcontext()),
            (tk.Text(tk.Tk()), [1, 2, 3], 'English', pytest.raises(AssertionError)),
            (tk.Text(tk.Tk()), {1: 2}, 'English', pytest.raises(AssertionError)),
            (tk.Text(tk.Tk()), None, 'English', nullcontext()),
            (tk.Text(tk.Tk()), False, 'English', pytest.raises(AssertionError)),
            (tk.Text(tk.Tk()), tk.Tk(), 'English', pytest.raises(AssertionError)),

            (tk.Text(tk.Tk()), None, 123, nullcontext()),
            (tk.Text(tk.Tk()), None, 'string', nullcontext()),
            (tk.Text(tk.Tk()), None, {1, 2, 3}, nullcontext()),
            (tk.Text(tk.Tk()), None, (1, 2, 3), nullcontext()),
            (tk.Text(tk.Tk()), None, [], nullcontext()),
            (tk.Text(tk.Tk()), None, [1, 2, 3], nullcontext()),
            (tk.Text(tk.Tk()), None, {1: 2}, nullcontext()),
            (tk.Text(tk.Tk()), None, None, nullcontext()),
            (tk.Text(tk.Tk()), None, False, nullcontext()),
            (tk.Text(tk.Tk()), None, tk.Tk(), nullcontext()),

        ]
    )
    def test_create_speaker_btn(self, speaker_class, text_widget, image, current_lang, expectation):
        with expectation:
            result = speaker_class.create_btn(text_widget=text_widget, image=image, current_lang=current_lang)
            assert isinstance(result, tk.Button)

    @pytest.mark.parametrize(
        'text, lang, filepath, expectation',
        [
            ('text', 'en', FILEPATH, nullcontext()),
            (123, 'en', FILEPATH, pytest.raises(AssertionError)),
            ('string', 'en', FILEPATH, nullcontext()),
            ({1, 2, 3}, 'en', FILEPATH, pytest.raises(AssertionError)),
            ((1, 2, 3), 'en', FILEPATH, pytest.raises(AssertionError)),
            ([], 'en', FILEPATH, pytest.raises(AssertionError)),
            ([1, 2, 3], 'en', FILEPATH, pytest.raises(AssertionError)),
            ({1: 2}, 'en', FILEPATH, pytest.raises(AssertionError)),
            (None, 'en', FILEPATH, pytest.raises(AssertionError)),
            (False, 'en', FILEPATH, pytest.raises(AssertionError)),
            (tk.Tk(), 'en', FILEPATH, pytest.raises(AssertionError)),

            ('text', 'string', FILEPATH, pytest.raises(AssertionError)),
            ('text', {1, 2, 3}, FILEPATH, pytest.raises(AssertionError)),
            ('text', (1, 2, 3), FILEPATH, pytest.raises(AssertionError)),
            ('text', [], FILEPATH, pytest.raises(AssertionError)),
            ('text', [1, 2, 3], FILEPATH, pytest.raises(AssertionError)),
            ('text', {1: 2}, FILEPATH, pytest.raises(AssertionError)),
            ('text', None, FILEPATH, pytest.raises(AssertionError)),
            ('text', False, FILEPATH, pytest.raises(AssertionError)),
            ('text', tk.Tk(), FILEPATH, pytest.raises(AssertionError)),
            ('text', 123, FILEPATH, pytest.raises(AssertionError)),

            ('text', 'en', 1234444, nullcontext()),
            ('text', 'en', 'string', nullcontext()),
            ('text', 'en', {1, 2, 3}, nullcontext()),
            ('text', 'en', (1, 2, 3), nullcontext()),
            ('text', 'en', [], nullcontext()),
            ('text', 'en', [1, 2, 3], nullcontext()),
            ('text', 'en', {1: 2}, nullcontext()),
            ('text', 'en', None, nullcontext()),
            ('text', 'en', False, nullcontext()),
            ('text', 'en', tk.Tk(), nullcontext()),
            ('text', 'en', 'asd.123', nullcontext()),
        ]
    )
    def test_create_audiofile(self, speaker_class, text, lang, filepath, expectation):
        with expectation:
            if filepath != self.FILEPATH:
                filepath = f'{filepath}.mp3'
                result = speaker_class.create_audiofile(text=text, lang=lang, filepath=filepath)
            else:
                result = speaker_class.create_audiofile(text=text, lang=lang, filepath=filepath)
            assert type(result) is str
            os.remove(filepath)
            if os.path.exists('{1'):
                os.remove('{1')

    @pytest.mark.parametrize(
        'file, expectation',
        [
            (CreateSpeakerForText(tk.Tk()).create_audiofile(
                text='Test', lang='en',
                filepath=f'{PROJECT_DIR}\\app\\other\\audio\\test.mp3'), nullcontext()),
            (123, pytest.raises(AssertionError)),
            ('string', pytest.raises(AssertionError)),
            ({1, 2, 3}, pytest.raises(AssertionError)),
            ((1, 2, 3), pytest.raises(AssertionError)),
            ([], pytest.raises(AssertionError)),
            ([1, 2, 3], pytest.raises(AssertionError)),
            ({1: 2}, pytest.raises(AssertionError)),
            (None, pytest.raises(AssertionError)),
            (False, pytest.raises(AssertionError)),
            (tk.Tk(), pytest.raises(AssertionError)),
        ]
    )
    def test_play_audio(self, speaker_class, file, expectation):
        with expectation:
            result = speaker_class.play_audio(file)
            assert result is True
