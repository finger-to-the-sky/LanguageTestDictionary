from contextlib import nullcontext
from app.config import LANGUAGES_LIST
from app.fonts import FontManager
from app.translator.languages_worker.languages_worker_init import LanguagesWorkerInit
from app.translator.speaker_functions import CreateSpeakerForText
from app.translator.text_field_functionality import TextWorker
from app.tests.fixtures.test_main_window.test_languages_worker import test_languages_worker_init
import pytest
import tkinter as tk


class TestLanguagesWorkerInit:
    FONTS = FontManager()
    TRANSLATOR_BUTTONS_FONTS = FONTS.BUTTON_FONTS['TranslatorButtons']

    COMBOBOX_BUTTON_FONTS = TRANSLATOR_BUTTONS_FONTS['ComboBox_btn']
    COMBOBOX_START_VALUES = ('English', 'Russian')
    COMBOBOX_ARGS = {'values': LANGUAGES_LIST, 'state': 'readonly', 'font': COMBOBOX_BUTTON_FONTS}
    COMBOBOX_BIND = ('<<ComboboxSelected>>', lambda: 123)

    TRANSLATE_BTN_ARGS = {"text": 'Перевести',
                          "width": 20,
                          "font": TRANSLATOR_BUTTONS_FONTS['Translate_btn'],
                          "command": lambda: TextWorker(src='English', dest='Russian').get_text_translator(
                              root=tk.Tk(),
                              first_text_widget=tk.Text(),
                              second_text_widget=tk.Text())
                          }
    CLEAR_BTN_ARGS = {
        "borderwidth": 0,
        "command": lambda: (tk.Text().delete("1.0", tk.END),
                            tk.Text().delete("1.0", tk.END),
                            CreateSpeakerForText.stop_speaker())
    }

    VOICE_BUTTONS_ARGS = {"text_widget": tk.Text(), "current_lang": 'Italy'}

    def test_elements_of_init(self, test_languages_worker_init):
        assert isinstance(test_languages_worker_init.clear_image, tk.PhotoImage)
        assert isinstance(test_languages_worker_init.font_manager, FontManager)
        assert isinstance(test_languages_worker_init.translator_fonts, dict)
        assert isinstance(test_languages_worker_init.speaker, CreateSpeakerForText)

    @pytest.mark.parametrize(
        'start_values, combo_from_args, combo_to_args, bind_arguments, expectation',
        [
            (COMBOBOX_START_VALUES, COMBOBOX_ARGS, COMBOBOX_ARGS, COMBOBOX_BIND, nullcontext()),
            ([1, 2], COMBOBOX_ARGS, COMBOBOX_ARGS, COMBOBOX_BIND, nullcontext()),
            ('[1, 2]', COMBOBOX_ARGS, COMBOBOX_ARGS, COMBOBOX_BIND, nullcontext()),
            ([], COMBOBOX_ARGS, COMBOBOX_ARGS, COMBOBOX_BIND, pytest.raises(AssertionError)),
            ({1, 2}, COMBOBOX_ARGS, COMBOBOX_ARGS, COMBOBOX_BIND, pytest.raises(AssertionError)),
            ({1: 2}, COMBOBOX_ARGS, COMBOBOX_ARGS, COMBOBOX_BIND, pytest.raises(AssertionError)),
            (123, COMBOBOX_ARGS, COMBOBOX_ARGS, COMBOBOX_BIND, pytest.raises(AssertionError)),
            (None, COMBOBOX_ARGS, COMBOBOX_ARGS, COMBOBOX_BIND, pytest.raises(AssertionError)),
            (True, COMBOBOX_ARGS, COMBOBOX_ARGS, COMBOBOX_BIND, pytest.raises(AssertionError)),
            (tk.Tk(), COMBOBOX_ARGS, COMBOBOX_ARGS, COMBOBOX_BIND, pytest.raises(AssertionError)),

            (COMBOBOX_START_VALUES, [1, 2], COMBOBOX_ARGS, COMBOBOX_BIND, pytest.raises(AssertionError)),
            (COMBOBOX_START_VALUES, '[1, 2]', COMBOBOX_ARGS, COMBOBOX_BIND, pytest.raises(AssertionError)),
            (COMBOBOX_START_VALUES, [], COMBOBOX_ARGS, COMBOBOX_BIND, pytest.raises(AssertionError)),
            (COMBOBOX_START_VALUES, {1, 2}, COMBOBOX_ARGS, COMBOBOX_BIND, pytest.raises(AssertionError)),
            (COMBOBOX_START_VALUES, {1: 2}, COMBOBOX_ARGS, COMBOBOX_BIND, pytest.raises(AssertionError)),
            (COMBOBOX_START_VALUES, 123, COMBOBOX_ARGS, COMBOBOX_BIND, pytest.raises(AssertionError)),
            (COMBOBOX_START_VALUES, None, COMBOBOX_ARGS, COMBOBOX_BIND, pytest.raises(AssertionError)),
            (COMBOBOX_START_VALUES, True, COMBOBOX_ARGS, COMBOBOX_BIND, pytest.raises(AssertionError)),
            (COMBOBOX_START_VALUES, tk.Tk(), COMBOBOX_ARGS, COMBOBOX_BIND, pytest.raises(AssertionError)),

            (COMBOBOX_START_VALUES, COMBOBOX_ARGS, [1, 2], COMBOBOX_BIND, pytest.raises(AssertionError)),
            (COMBOBOX_START_VALUES, COMBOBOX_ARGS, '[1, 2]', COMBOBOX_BIND, pytest.raises(AssertionError)),
            (COMBOBOX_START_VALUES, COMBOBOX_ARGS, [], COMBOBOX_BIND, pytest.raises(AssertionError)),
            (COMBOBOX_START_VALUES, COMBOBOX_ARGS, {1, 2}, COMBOBOX_BIND, pytest.raises(AssertionError)),
            (COMBOBOX_START_VALUES, COMBOBOX_ARGS, {1: 2}, COMBOBOX_BIND, pytest.raises(AssertionError)),
            (COMBOBOX_START_VALUES, COMBOBOX_ARGS, 123, COMBOBOX_BIND, pytest.raises(AssertionError)),
            (COMBOBOX_START_VALUES, COMBOBOX_ARGS, None, COMBOBOX_BIND, pytest.raises(AssertionError)),
            (COMBOBOX_START_VALUES, COMBOBOX_ARGS, True, COMBOBOX_BIND, pytest.raises(AssertionError)),
            (COMBOBOX_START_VALUES, COMBOBOX_ARGS, tk.Tk(), COMBOBOX_BIND, pytest.raises(AssertionError)),

            (COMBOBOX_START_VALUES, COMBOBOX_ARGS, COMBOBOX_BIND, [1, 2], pytest.raises(AssertionError)),
            (COMBOBOX_START_VALUES, COMBOBOX_ARGS, COMBOBOX_BIND, '[1, 2]', pytest.raises(AssertionError)),
            (COMBOBOX_START_VALUES, COMBOBOX_ARGS, COMBOBOX_BIND, [], pytest.raises(AssertionError)),
            (COMBOBOX_START_VALUES, COMBOBOX_ARGS, COMBOBOX_BIND, {1, 2}, pytest.raises(AssertionError)),
            (COMBOBOX_START_VALUES, COMBOBOX_ARGS, COMBOBOX_BIND, {1: 2}, pytest.raises(AssertionError)),
            (COMBOBOX_START_VALUES, COMBOBOX_ARGS, COMBOBOX_BIND, 123, pytest.raises(AssertionError)),
            (COMBOBOX_START_VALUES, COMBOBOX_ARGS, COMBOBOX_BIND, None, pytest.raises(AssertionError)),
            (COMBOBOX_START_VALUES, COMBOBOX_ARGS, COMBOBOX_BIND, True, pytest.raises(AssertionError)),
            (COMBOBOX_START_VALUES, COMBOBOX_ARGS, COMBOBOX_BIND, tk.Tk(), pytest.raises(AssertionError)),

        ]
    )
    def test_lw_create_languages_lists(self, test_languages_worker_init, start_values, combo_from_args, combo_to_args,
                                       bind_arguments, expectation):
        with expectation:
            result = test_languages_worker_init.create_languages_lists(
                root=test_languages_worker_init.root,
                start_values=start_values,
                combo_from_args=combo_from_args,
                combo_to_args=combo_to_args,
                bind_arguments=bind_arguments
            )
            assert type(result) is list

    @pytest.mark.parametrize(
        'speaker, voice_btn1_args, voice_btn2_args, expectation',
        [
            (CreateSpeakerForText(tk.Tk()), VOICE_BUTTONS_ARGS, VOICE_BUTTONS_ARGS, nullcontext()),
            (LanguagesWorkerInit, VOICE_BUTTONS_ARGS, VOICE_BUTTONS_ARGS, pytest.raises(AssertionError)),
            (123, VOICE_BUTTONS_ARGS, VOICE_BUTTONS_ARGS, pytest.raises(AssertionError)),
            ('string', VOICE_BUTTONS_ARGS, VOICE_BUTTONS_ARGS, pytest.raises(AssertionError)),
            ({1, 2, 3}, VOICE_BUTTONS_ARGS, VOICE_BUTTONS_ARGS, pytest.raises(AssertionError)),
            ((1, 2, 3), VOICE_BUTTONS_ARGS, VOICE_BUTTONS_ARGS, pytest.raises(AssertionError)),
            ([], VOICE_BUTTONS_ARGS, VOICE_BUTTONS_ARGS, pytest.raises(AssertionError)),
            ([1, 2, 3], VOICE_BUTTONS_ARGS, VOICE_BUTTONS_ARGS, pytest.raises(AssertionError)),
            ({1: 2}, VOICE_BUTTONS_ARGS, VOICE_BUTTONS_ARGS, pytest.raises(AssertionError)),
            (None, VOICE_BUTTONS_ARGS, VOICE_BUTTONS_ARGS, pytest.raises(AssertionError)),
            (False, VOICE_BUTTONS_ARGS, VOICE_BUTTONS_ARGS, pytest.raises(AssertionError)),
            (tk.Tk(), VOICE_BUTTONS_ARGS, VOICE_BUTTONS_ARGS, pytest.raises(AssertionError)),

            (CreateSpeakerForText(tk.Tk()), LanguagesWorkerInit, VOICE_BUTTONS_ARGS, pytest.raises(AssertionError)),
            (CreateSpeakerForText(tk.Tk()), 123, VOICE_BUTTONS_ARGS, pytest.raises(AssertionError)),
            (CreateSpeakerForText(tk.Tk()), 'string', VOICE_BUTTONS_ARGS, pytest.raises(AssertionError)),
            (CreateSpeakerForText(tk.Tk()), {1, 2, 3}, VOICE_BUTTONS_ARGS, pytest.raises(AssertionError)),
            (CreateSpeakerForText(tk.Tk()), (1, 2, 3), VOICE_BUTTONS_ARGS, pytest.raises(AssertionError)),
            (CreateSpeakerForText(tk.Tk()), [], VOICE_BUTTONS_ARGS, pytest.raises(AssertionError)),
            (CreateSpeakerForText(tk.Tk()), [1, 2, 3], VOICE_BUTTONS_ARGS, pytest.raises(AssertionError)),
            (CreateSpeakerForText(tk.Tk()), {1: 2}, VOICE_BUTTONS_ARGS, pytest.raises(AssertionError)),
            (CreateSpeakerForText(tk.Tk()), None, VOICE_BUTTONS_ARGS, pytest.raises(AssertionError)),
            (CreateSpeakerForText(tk.Tk()), False, VOICE_BUTTONS_ARGS, pytest.raises(AssertionError)),
            (CreateSpeakerForText(tk.Tk()), tk.Tk(), VOICE_BUTTONS_ARGS, pytest.raises(AssertionError)),

            (CreateSpeakerForText(tk.Tk()), VOICE_BUTTONS_ARGS, LanguagesWorkerInit, pytest.raises(AssertionError)),
            (CreateSpeakerForText(tk.Tk()), VOICE_BUTTONS_ARGS, 123, pytest.raises(AssertionError)),
            (CreateSpeakerForText(tk.Tk()), VOICE_BUTTONS_ARGS, 'string', pytest.raises(AssertionError)),
            (CreateSpeakerForText(tk.Tk()), VOICE_BUTTONS_ARGS, {1, 2, 3}, pytest.raises(AssertionError)),
            (CreateSpeakerForText(tk.Tk()), VOICE_BUTTONS_ARGS, (1, 2, 3), pytest.raises(AssertionError)),
            (CreateSpeakerForText(tk.Tk()), VOICE_BUTTONS_ARGS, [], pytest.raises(AssertionError)),
            (CreateSpeakerForText(tk.Tk()), VOICE_BUTTONS_ARGS, [1, 2, 3], pytest.raises(AssertionError)),
            (CreateSpeakerForText(tk.Tk()), VOICE_BUTTONS_ARGS, {1: 2}, pytest.raises(AssertionError)),
            (CreateSpeakerForText(tk.Tk()), VOICE_BUTTONS_ARGS, None, pytest.raises(AssertionError)),
            (CreateSpeakerForText(tk.Tk()), VOICE_BUTTONS_ARGS, False, pytest.raises(AssertionError)),
            (CreateSpeakerForText(tk.Tk()), VOICE_BUTTONS_ARGS, tk.Tk(), pytest.raises(AssertionError)),

        ]
    )
    def test_lw_create_workers_audio_buttons(self, test_languages_worker_init, speaker, voice_btn1_args,
                                             voice_btn2_args,
                                             expectation):
        with expectation:
            result = test_languages_worker_init.create_workers_audio_buttons(
                speaker, voice_btn1_args, voice_btn2_args
            )
            assert type(result) is dict

    @pytest.mark.parametrize(
        'translate_btn_args, clear_btn_args, expectation',
        [
            (TRANSLATE_BTN_ARGS, CLEAR_BTN_ARGS, nullcontext()),
            (123, CLEAR_BTN_ARGS, pytest.raises(AssertionError)),
            ('string', CLEAR_BTN_ARGS, pytest.raises(AssertionError)),
            ({1, 2, 3}, CLEAR_BTN_ARGS, pytest.raises(AssertionError)),
            ((1, 2, 3), CLEAR_BTN_ARGS, pytest.raises(AssertionError)),
            ([], CLEAR_BTN_ARGS, pytest.raises(AssertionError)),
            ([1, 2, 3], CLEAR_BTN_ARGS, pytest.raises(AssertionError)),
            ({1: 2}, CLEAR_BTN_ARGS, pytest.raises(AssertionError)),
            (None, CLEAR_BTN_ARGS, pytest.raises(AssertionError)),
            (False, CLEAR_BTN_ARGS, pytest.raises(AssertionError)),
            (tk.Tk(), CLEAR_BTN_ARGS, nullcontext()),

            (TRANSLATE_BTN_ARGS, 123, pytest.raises(AssertionError)),
            (TRANSLATE_BTN_ARGS, 'string', pytest.raises(AssertionError)),
            (TRANSLATE_BTN_ARGS, {1, 2, 3}, pytest.raises(AssertionError)),
            (TRANSLATE_BTN_ARGS, (1, 2, 3), pytest.raises(AssertionError)),
            (TRANSLATE_BTN_ARGS, [], pytest.raises(AssertionError)),
            (TRANSLATE_BTN_ARGS, [1, 2, 3], pytest.raises(AssertionError)),
            (TRANSLATE_BTN_ARGS, {1: 2}, pytest.raises(AssertionError)),
            (TRANSLATE_BTN_ARGS, None, pytest.raises(AssertionError)),
            (TRANSLATE_BTN_ARGS, False, pytest.raises(AssertionError)),
            (TRANSLATE_BTN_ARGS, tk.Tk(), pytest.raises(AssertionError)),

        ]
    )
    def test_lw_create_workers_buttons(self, test_languages_worker_init, translate_btn_args, clear_btn_args,
                                       expectation):
        with expectation:
            result = test_languages_worker_init.create_workers_buttons(root=test_languages_worker_init.root,
                                                                       translate_btn_args=translate_btn_args,
                                                                       clear_btn_args=clear_btn_args)
            assert type(result) is dict
