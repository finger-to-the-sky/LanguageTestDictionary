import os
from tinydb import TinyDB

TITLE = 'English Test Dictionary'
SIZE_WINDOW = '1024x800+400+100'
SIZE_TEST_MODE_CHOOSE_WINDOW = '900x400+400+200'
SIZE_TEST_MODE_MAIN_WINDOW = '900x650'
SIZE_TEST_MODE_WINDOW = '700x250+600+400'

LANGUAGES = {
    'English': 'en',
    'Russian': 'ru',
    'Korean': 'ko',
    'Polish': 'pl',
    'German': 'de'
}

LANGUAGES_LIST = list(LANGUAGES.keys())

current_directory = os.getcwd()

if 'dist' in current_directory:
    current_directory = current_directory.replace('\\dist', '')

FILE_INSTRUCTION_PATH = f'{current_directory}\\app\\other\\instruction\\instruction.pdf'

updated_path = current_directory.replace('\\', '/')
red_list_db = TinyDB(f'{updated_path}/app/other/db/red_list.json')
cache_files_db = TinyDB(f'{updated_path}/app/other/db/cache_files.json')
