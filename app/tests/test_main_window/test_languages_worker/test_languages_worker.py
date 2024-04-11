import pytest
import tkinter as tk
from tkinter import ttk
from contextlib import nullcontext
from app.translator.speaker_functions import CreateSpeakerForText
from app.tests.fixtures.test_main_window.test_languages_worker import test_languages_worker, test_combobox


class TestLanguagesWorker:
    NEW_POSITION_VOICE_BTN1 = {"x": 915, "y": 175}
    NEW_POSITION_VOICE_BTN2 = {"x": 915, "y": 340}
    AUDIO_BUTTONS_ARGS = {'speaker': CreateSpeakerForText(tk.Tk()),
                          'voice_btn1_args': {'text_widget': tk.Text(tk.Tk()),
                                              'current_lang': 'English'},
                          'voice_btn2_args': {'text_widget': tk.Text(tk.Tk()),
                                              'current_lang': 'Russian'}}

    def test_elements_of_init(self, test_languages_worker):
        assert isinstance(test_languages_worker.combo_from, ttk.Combobox)
        assert isinstance(test_languages_worker.combo_to, ttk.Combobox)
        assert isinstance(test_languages_worker.voice_btn1, tk.Button)
        assert isinstance(test_languages_worker.voice_btn2, tk.Button)
        assert isinstance(test_languages_worker.translate_btn, tk.Button)
        assert isinstance(test_languages_worker.clear_btn, tk.Button)

    @pytest.mark.parametrize(
        'new_position_voice_btn1, new_position_voice_btn2, audio_buttons_args, expectation',
        [
            (NEW_POSITION_VOICE_BTN1, NEW_POSITION_VOICE_BTN2, AUDIO_BUTTONS_ARGS, nullcontext()),
            (123, NEW_POSITION_VOICE_BTN2, AUDIO_BUTTONS_ARGS, nullcontext()),
            ('string', NEW_POSITION_VOICE_BTN2, AUDIO_BUTTONS_ARGS, nullcontext()),
            ({1, 2, 3}, NEW_POSITION_VOICE_BTN2, AUDIO_BUTTONS_ARGS, nullcontext()),
            ((1, 2, 3), NEW_POSITION_VOICE_BTN2, AUDIO_BUTTONS_ARGS, nullcontext()),
            ([], NEW_POSITION_VOICE_BTN2, AUDIO_BUTTONS_ARGS, nullcontext()),
            ([1, 2, 3], NEW_POSITION_VOICE_BTN2, AUDIO_BUTTONS_ARGS, nullcontext()),
            ({1: 2}, NEW_POSITION_VOICE_BTN2, AUDIO_BUTTONS_ARGS, nullcontext()),
            (None, NEW_POSITION_VOICE_BTN2, AUDIO_BUTTONS_ARGS, nullcontext()),
            (False, NEW_POSITION_VOICE_BTN2, AUDIO_BUTTONS_ARGS, nullcontext()),
            (tk.Tk(), NEW_POSITION_VOICE_BTN2, AUDIO_BUTTONS_ARGS, nullcontext()),

            (NEW_POSITION_VOICE_BTN1, 123, AUDIO_BUTTONS_ARGS, nullcontext()),
            (NEW_POSITION_VOICE_BTN1, 'string', AUDIO_BUTTONS_ARGS, nullcontext()),
            (NEW_POSITION_VOICE_BTN1, {1, 2, 3}, AUDIO_BUTTONS_ARGS, nullcontext()),
            (NEW_POSITION_VOICE_BTN1, (1, 2, 3), AUDIO_BUTTONS_ARGS, nullcontext()),
            (NEW_POSITION_VOICE_BTN1, [], AUDIO_BUTTONS_ARGS, nullcontext()),
            (NEW_POSITION_VOICE_BTN1, [1, 2, 3], AUDIO_BUTTONS_ARGS, nullcontext()),
            (NEW_POSITION_VOICE_BTN1, {1: 2}, AUDIO_BUTTONS_ARGS, nullcontext()),
            (NEW_POSITION_VOICE_BTN1, None, AUDIO_BUTTONS_ARGS, nullcontext()),
            (NEW_POSITION_VOICE_BTN1, False, AUDIO_BUTTONS_ARGS, nullcontext()),
            (NEW_POSITION_VOICE_BTN1, tk.Tk(), AUDIO_BUTTONS_ARGS, nullcontext()),

            (NEW_POSITION_VOICE_BTN1, NEW_POSITION_VOICE_BTN2, 123, nullcontext()),
            (NEW_POSITION_VOICE_BTN1, NEW_POSITION_VOICE_BTN2, 'string', nullcontext()),
            (NEW_POSITION_VOICE_BTN1, NEW_POSITION_VOICE_BTN2, {1, 2, 3}, nullcontext()),
            (NEW_POSITION_VOICE_BTN1, NEW_POSITION_VOICE_BTN2, (1, 2, 3), nullcontext()),
            (NEW_POSITION_VOICE_BTN1, NEW_POSITION_VOICE_BTN2, [], nullcontext()),
            (NEW_POSITION_VOICE_BTN1, NEW_POSITION_VOICE_BTN2, [1, 2, 3], nullcontext()),
            (NEW_POSITION_VOICE_BTN1, NEW_POSITION_VOICE_BTN2, {1: 2}, nullcontext()),
            (NEW_POSITION_VOICE_BTN1, NEW_POSITION_VOICE_BTN2, None, nullcontext()),
            (NEW_POSITION_VOICE_BTN1, NEW_POSITION_VOICE_BTN2, False, nullcontext()),
            (NEW_POSITION_VOICE_BTN1, NEW_POSITION_VOICE_BTN2, tk.Tk(), nullcontext()),
        ]
    )
    def test_change_lang_voices(self, test_languages_worker, test_combobox, new_position_voice_btn1,
                                new_position_voice_btn2,
                                audio_buttons_args, expectation):
        with expectation:
            test_languages_worker.change_lang_voices(new_position_voice_btn1, new_position_voice_btn1,
                                                     audio_buttons_args)
            assert isinstance(test_languages_worker.voice_btn1, tk.Button)
            assert isinstance(test_languages_worker.voice_btn2, tk.Button)


class TestShowElementsLanguagesWorker:
    COMBO_FROM_POS = {"row": 0, "column": 2, "padx": (0, 40)}
    COMBO_TO_POS = {"row": 0, "column": 3, "padx": (0, 0)}
    TRANSLATE_BTN_POS = {}
    VOICE_BTN1_POS = {"x": 915, "y": 175}
    VOICE_BTN2_POS = {"x": 915, "y": 340}
    CLEAR_BTN_POS = {"x": 915, "y": 140}

    @pytest.mark.parametrize(
        'combo_from_pos, combo_to_pos, translate_btn_pos, voice_btn1_pos, voice_btn2_pos, clear_btn_pos, expectation',
        [
            (COMBO_FROM_POS, COMBO_TO_POS, TRANSLATE_BTN_POS, VOICE_BTN1_POS, VOICE_BTN2_POS,
             CLEAR_BTN_POS, nullcontext()),

            (123, COMBO_TO_POS, TRANSLATE_BTN_POS, VOICE_BTN1_POS, VOICE_BTN2_POS,
             CLEAR_BTN_POS, pytest.raises(AssertionError)),
            ('string', COMBO_TO_POS, TRANSLATE_BTN_POS, VOICE_BTN1_POS, VOICE_BTN2_POS,
             CLEAR_BTN_POS, pytest.raises(AssertionError)),
            ({1, 2, 3}, COMBO_TO_POS, TRANSLATE_BTN_POS, VOICE_BTN1_POS, VOICE_BTN2_POS,
             CLEAR_BTN_POS, pytest.raises(AssertionError)),
            ((1, 2, 3), COMBO_TO_POS, TRANSLATE_BTN_POS, VOICE_BTN1_POS, VOICE_BTN2_POS,
             CLEAR_BTN_POS, pytest.raises(AssertionError)),
            ([], COMBO_TO_POS, TRANSLATE_BTN_POS, VOICE_BTN1_POS, VOICE_BTN2_POS,
             CLEAR_BTN_POS, pytest.raises(AssertionError)),
            ([1, 2, 3], COMBO_TO_POS, TRANSLATE_BTN_POS, VOICE_BTN1_POS, VOICE_BTN2_POS,
             CLEAR_BTN_POS, pytest.raises(AssertionError)),
            ({1: 2}, COMBO_TO_POS, TRANSLATE_BTN_POS, VOICE_BTN1_POS, VOICE_BTN2_POS,
             CLEAR_BTN_POS, pytest.raises(AssertionError)),
            (None, COMBO_TO_POS, TRANSLATE_BTN_POS, VOICE_BTN1_POS, VOICE_BTN2_POS,
             CLEAR_BTN_POS, pytest.raises(AssertionError)),
            (False, COMBO_TO_POS, TRANSLATE_BTN_POS, VOICE_BTN1_POS, VOICE_BTN2_POS,
             CLEAR_BTN_POS, pytest.raises(AssertionError)),
            (tk.Button(tk.Tk()), COMBO_TO_POS, TRANSLATE_BTN_POS, VOICE_BTN1_POS, VOICE_BTN2_POS,
             CLEAR_BTN_POS, pytest.raises(AssertionError)),

            (COMBO_FROM_POS, 123, TRANSLATE_BTN_POS, VOICE_BTN1_POS, VOICE_BTN2_POS,
             CLEAR_BTN_POS, pytest.raises(AssertionError)),
            (COMBO_FROM_POS, 'string', TRANSLATE_BTN_POS, VOICE_BTN1_POS, VOICE_BTN2_POS,
             CLEAR_BTN_POS, pytest.raises(AssertionError)),
            (COMBO_FROM_POS, {1, 2, 3}, TRANSLATE_BTN_POS, VOICE_BTN1_POS, VOICE_BTN2_POS,
             CLEAR_BTN_POS, pytest.raises(AssertionError)),
            (COMBO_FROM_POS, (1, 2, 3), TRANSLATE_BTN_POS, VOICE_BTN1_POS, VOICE_BTN2_POS,
             CLEAR_BTN_POS, pytest.raises(AssertionError)),
            (COMBO_FROM_POS, [], TRANSLATE_BTN_POS, VOICE_BTN1_POS, VOICE_BTN2_POS,
             CLEAR_BTN_POS, pytest.raises(AssertionError)),
            (COMBO_FROM_POS, [1, 2, 3], TRANSLATE_BTN_POS, VOICE_BTN1_POS, VOICE_BTN2_POS,
             CLEAR_BTN_POS, pytest.raises(AssertionError)),
            (COMBO_FROM_POS, {1: 2}, TRANSLATE_BTN_POS, VOICE_BTN1_POS, VOICE_BTN2_POS,
             CLEAR_BTN_POS, pytest.raises(AssertionError)),
            (COMBO_FROM_POS, None, TRANSLATE_BTN_POS, VOICE_BTN1_POS, VOICE_BTN2_POS,
             CLEAR_BTN_POS, pytest.raises(AssertionError)),
            (COMBO_FROM_POS, False, TRANSLATE_BTN_POS, VOICE_BTN1_POS, VOICE_BTN2_POS,
             CLEAR_BTN_POS, pytest.raises(AssertionError)),
            (COMBO_FROM_POS, tk.Button(tk.Tk()), TRANSLATE_BTN_POS, VOICE_BTN1_POS, VOICE_BTN2_POS,
             CLEAR_BTN_POS, pytest.raises(AssertionError)),

            (COMBO_FROM_POS, COMBO_TO_POS, 123, VOICE_BTN1_POS, VOICE_BTN2_POS,
             CLEAR_BTN_POS, pytest.raises(AssertionError)),
            (COMBO_FROM_POS, COMBO_TO_POS, 'string', VOICE_BTN1_POS, VOICE_BTN2_POS,
             CLEAR_BTN_POS, pytest.raises(AssertionError)),
            (COMBO_FROM_POS, COMBO_TO_POS, {1, 2, 3}, VOICE_BTN1_POS, VOICE_BTN2_POS,
             CLEAR_BTN_POS, pytest.raises(AssertionError)),
            (COMBO_FROM_POS, COMBO_TO_POS, (1, 2, 3), VOICE_BTN1_POS, VOICE_BTN2_POS,
             CLEAR_BTN_POS, pytest.raises(AssertionError)),
            (COMBO_FROM_POS, COMBO_TO_POS, [], VOICE_BTN1_POS, VOICE_BTN2_POS,
             CLEAR_BTN_POS, pytest.raises(AssertionError)),
            (COMBO_FROM_POS, COMBO_TO_POS, [1, 2, 3], VOICE_BTN1_POS, VOICE_BTN2_POS,
             CLEAR_BTN_POS, pytest.raises(AssertionError)),
            (COMBO_FROM_POS, COMBO_TO_POS, {1: 2}, VOICE_BTN1_POS, VOICE_BTN2_POS,
             CLEAR_BTN_POS, pytest.raises(AssertionError)),
            (COMBO_FROM_POS, COMBO_TO_POS, None, VOICE_BTN1_POS, VOICE_BTN2_POS,
             CLEAR_BTN_POS, pytest.raises(AssertionError)),
            (COMBO_FROM_POS, COMBO_TO_POS, False, VOICE_BTN1_POS, VOICE_BTN2_POS,
             CLEAR_BTN_POS, pytest.raises(AssertionError)),
            (COMBO_FROM_POS, COMBO_TO_POS, tk.Button(tk.Tk()), VOICE_BTN1_POS, VOICE_BTN2_POS,
             CLEAR_BTN_POS, pytest.raises(AssertionError)),

            (COMBO_FROM_POS, COMBO_TO_POS, TRANSLATE_BTN_POS, 123, VOICE_BTN2_POS,
             CLEAR_BTN_POS, pytest.raises(AssertionError)),
            (COMBO_FROM_POS, COMBO_TO_POS, TRANSLATE_BTN_POS, 'string', VOICE_BTN2_POS,
             CLEAR_BTN_POS, pytest.raises(AssertionError)),
            (COMBO_FROM_POS, COMBO_TO_POS, TRANSLATE_BTN_POS, {1, 2, 3}, VOICE_BTN2_POS,
             CLEAR_BTN_POS, pytest.raises(AssertionError)),
            (COMBO_FROM_POS, COMBO_TO_POS, TRANSLATE_BTN_POS, (1, 2, 3), VOICE_BTN2_POS,
             CLEAR_BTN_POS, pytest.raises(AssertionError)),
            (COMBO_FROM_POS, COMBO_TO_POS, TRANSLATE_BTN_POS, [], VOICE_BTN2_POS,
             CLEAR_BTN_POS, pytest.raises(AssertionError)),
            (COMBO_FROM_POS, COMBO_TO_POS, TRANSLATE_BTN_POS, [1, 2, 3], VOICE_BTN2_POS,
             CLEAR_BTN_POS, pytest.raises(AssertionError)),
            (COMBO_FROM_POS, COMBO_TO_POS, TRANSLATE_BTN_POS, {1: 2}, VOICE_BTN2_POS,
             CLEAR_BTN_POS, pytest.raises(AssertionError)),
            (COMBO_FROM_POS, COMBO_TO_POS, TRANSLATE_BTN_POS, None, VOICE_BTN2_POS,
             CLEAR_BTN_POS, pytest.raises(AssertionError)),
            (COMBO_FROM_POS, COMBO_TO_POS, TRANSLATE_BTN_POS, False, VOICE_BTN2_POS,
             CLEAR_BTN_POS, pytest.raises(AssertionError)),
            (COMBO_FROM_POS, COMBO_TO_POS, TRANSLATE_BTN_POS, tk.Button(tk.Tk()), VOICE_BTN2_POS,
             CLEAR_BTN_POS, pytest.raises(AssertionError)),

            (COMBO_FROM_POS, COMBO_TO_POS, TRANSLATE_BTN_POS, VOICE_BTN1_POS, 123,
             CLEAR_BTN_POS, pytest.raises(AssertionError)),
            (COMBO_FROM_POS, COMBO_TO_POS, TRANSLATE_BTN_POS, VOICE_BTN1_POS, 'string',
             CLEAR_BTN_POS, pytest.raises(AssertionError)),
            (COMBO_FROM_POS, COMBO_TO_POS, TRANSLATE_BTN_POS, VOICE_BTN1_POS, {1, 2, 3},
             CLEAR_BTN_POS, pytest.raises(AssertionError)),
            (COMBO_FROM_POS, COMBO_TO_POS, TRANSLATE_BTN_POS, VOICE_BTN1_POS, (1, 2, 3),
             CLEAR_BTN_POS, pytest.raises(AssertionError)),
            (COMBO_FROM_POS, COMBO_TO_POS, TRANSLATE_BTN_POS, VOICE_BTN1_POS, [],
             CLEAR_BTN_POS, pytest.raises(AssertionError)),
            (COMBO_FROM_POS, COMBO_TO_POS, TRANSLATE_BTN_POS, VOICE_BTN1_POS, [1, 2, 3],
             CLEAR_BTN_POS, pytest.raises(AssertionError)),
            (COMBO_FROM_POS, COMBO_TO_POS, TRANSLATE_BTN_POS, VOICE_BTN1_POS, {1: 2},
             CLEAR_BTN_POS, pytest.raises(AssertionError)),
            (COMBO_FROM_POS, COMBO_TO_POS, TRANSLATE_BTN_POS, VOICE_BTN1_POS, None,
             CLEAR_BTN_POS, pytest.raises(AssertionError)),
            (COMBO_FROM_POS, COMBO_TO_POS, TRANSLATE_BTN_POS, VOICE_BTN1_POS, False,
             CLEAR_BTN_POS, pytest.raises(AssertionError)),
            (COMBO_FROM_POS, COMBO_TO_POS, TRANSLATE_BTN_POS, VOICE_BTN1_POS, tk.Button(tk.Tk()),
             CLEAR_BTN_POS, pytest.raises(AssertionError)),

            (COMBO_FROM_POS, COMBO_TO_POS, TRANSLATE_BTN_POS, VOICE_BTN1_POS, VOICE_BTN2_POS,
             123, pytest.raises(AssertionError)),
            (COMBO_FROM_POS, COMBO_TO_POS, TRANSLATE_BTN_POS, VOICE_BTN1_POS, VOICE_BTN2_POS,
             'string', pytest.raises(AssertionError)),
            (COMBO_FROM_POS, COMBO_TO_POS, TRANSLATE_BTN_POS, VOICE_BTN1_POS, VOICE_BTN2_POS,
             {1, 2, 3}, pytest.raises(AssertionError)),
            (COMBO_FROM_POS, COMBO_TO_POS, TRANSLATE_BTN_POS, VOICE_BTN1_POS, VOICE_BTN2_POS,
             (1, 2, 3), pytest.raises(AssertionError)),
            (COMBO_FROM_POS, COMBO_TO_POS, TRANSLATE_BTN_POS, VOICE_BTN1_POS, VOICE_BTN2_POS,
             [], pytest.raises(AssertionError)),
            (COMBO_FROM_POS, COMBO_TO_POS, TRANSLATE_BTN_POS, VOICE_BTN1_POS, VOICE_BTN2_POS,
             [1, 2, 3], pytest.raises(AssertionError)),
            (COMBO_FROM_POS, COMBO_TO_POS, TRANSLATE_BTN_POS, VOICE_BTN1_POS, VOICE_BTN2_POS,
             {1: 2}, pytest.raises(AssertionError)),
            (COMBO_FROM_POS, COMBO_TO_POS, TRANSLATE_BTN_POS, VOICE_BTN1_POS, VOICE_BTN2_POS,
             None, pytest.raises(AssertionError)),
            (COMBO_FROM_POS, COMBO_TO_POS, TRANSLATE_BTN_POS, VOICE_BTN1_POS, VOICE_BTN2_POS,
             False, pytest.raises(AssertionError)),
            (COMBO_FROM_POS, COMBO_TO_POS, TRANSLATE_BTN_POS, VOICE_BTN1_POS, VOICE_BTN2_POS,
             tk.Button(tk.Tk()), pytest.raises(AssertionError)),
        ]
    )
    def test_show_elements(self, test_languages_worker, combo_from_pos, combo_to_pos, translate_btn_pos, voice_btn1_pos,
                           voice_btn2_pos, clear_btn_pos, expectation):
        with expectation:
            test_languages_worker.show_elements(combo_from_pos=combo_from_pos, combo_to_pos=combo_to_pos,
                                                translate_btn_pos=translate_btn_pos, voice_btn2_pos=voice_btn2_pos,
                                                voice_btn1_pos=voice_btn1_pos, clear_btn_pos=clear_btn_pos)

            assert test_languages_worker.combo_from.winfo_manager() == 'grid'
            assert test_languages_worker.combo_to.winfo_manager() == 'grid'
            assert test_languages_worker.translate_btn.winfo_manager() == 'pack'
            assert test_languages_worker.voice_btn1.winfo_manager() == 'place'
            assert test_languages_worker.voice_btn2.winfo_manager() == 'place'
            assert test_languages_worker.clear_btn.winfo_manager() == 'place'
