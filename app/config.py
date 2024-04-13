from tinydb import TinyDB
from app.logger import get_logger
from app.other.get_path import get_path_project

TITLE = 'Language Test Dictionary'
SIZE_WINDOW = '1024x800+400+100'
SIZE_TEST_MODE_CHOOSE_WINDOW = '1000x400+400+200'
SIZE_TEST_MODE_MAIN_WINDOW = '1250x650'
SIZE_TEST_MODE_WINDOW = '750x250+600+400'

LANGUAGES = {
    'English': 'en',
    'Russian': 'ru',
    'Korean': 'ko',
    'Polish': 'pl',
    'German': 'de'
}
LANGUAGES_LIST = list(LANGUAGES.keys())

PROJECT_DIR = get_path_project()


if 'dist' in PROJECT_DIR:
    PROJECT_DIR = PROJECT_DIR.replace('\\dist', '')

FILE_INSTRUCTION_PATH = f'{PROJECT_DIR}\\app\\other\\instruction\\instruction.pdf'

updated_path = PROJECT_DIR.replace('\\', '/')
red_list_db = TinyDB(f'{updated_path}/app/other/db/red_list.json')
cache_files_db = TinyDB(f'{updated_path}/app/other/db/cache_files.json')

main_logger = get_logger('main')
