import inspect
from app.config import main_logger


class FontManager:
    """
    Class for configuring the fonts of the application.
    """

    MAIN_FONT = 'Georgia'
    LABEL_FONTS = {
        'Header': (MAIN_FONT, 20),
        'Instruction': (MAIN_FONT, 14),
        'ListboxNames': (MAIN_FONT, 12),
        'Errors': (MAIN_FONT, 10),
        'Counter': (MAIN_FONT, 10),
        'WordsOperation': (MAIN_FONT, 10),
        'TestModeWord': (MAIN_FONT, 14)
    }
    BUTTON_FONTS = {
        'TranslatorButtons': {
            'StartChoosing_btn': (MAIN_FONT, 10),
            'TranslateFile_btn': (MAIN_FONT, 10),
            'Translate_btn': (MAIN_FONT, 10),
            'ComboBox_btn': (MAIN_FONT, 10),
        },

        'TestModeMenu': {
            'WordsOperations': {
                'Add_btn': (MAIN_FONT, 10),
                'Edit_btn': (MAIN_FONT, 10),
                'Delete_btn': (MAIN_FONT, 10),
            },
            'Clear_btn': (MAIN_FONT, 12),
            'Start_btn': (MAIN_FONT, 12),
            'Download_btn': (MAIN_FONT, 10),
            'Cache_btn': (MAIN_FONT, 10),
        },
        'TestModeButtons': {
            'ExitMode_btn': (MAIN_FONT, 12),
            'ContinueMode_btn': (MAIN_FONT, 12),
            'RadioButtons': (MAIN_FONT, 12),
            'ResultButtons': {
                'ShowTable_btn': (MAIN_FONT, 12),
                'Restart_btn': (MAIN_FONT, 12),
                'Exit_btn': (MAIN_FONT, 12),
            }
        },
        'CacheWindowButtons': {
            'ClearCache_btn': (MAIN_FONT, 10),
            'DownloadCache_btn': (MAIN_FONT, 10)
        }
    }
    TEXT_FONTS = {
        'EntryWidget': (MAIN_FONT, 10),
        'TextWidget': (MAIN_FONT, 12)
    }
    LISTBOX_FONTS = {
        'WordsList': (MAIN_FONT, 10),
        'CachingWindow': (MAIN_FONT, 10),
        'ResultTableHeader': (MAIN_FONT, 12, "bold"),
        'ResultTableContent': (MAIN_FONT, 10),

    }

    def __init__(self, font: str = None):
        caller_frame = inspect.currentframe().f_back
        caller_module = inspect.getmodule(caller_frame)
        if '/' in caller_module.__file__:
            filepath = caller_module.__file__.split('/')
        else:
            filepath = caller_module.__file__.split('\\')
        self.font = font
        main_logger.info(f'Была произведена инициализация шрифтов в модуле: {filepath[-1]}')
