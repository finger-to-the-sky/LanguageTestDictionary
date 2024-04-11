import pytest
import tkinter as tk
from app.translator.speaker_functions import CreateSpeakerForText


@pytest.fixture
def speaker_class():
    speaker = CreateSpeakerForText(tk.Tk())
    return speaker
