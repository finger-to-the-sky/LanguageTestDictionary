from tinydb import Query
from app.config import red_list_db, cache_files_db
from app.config import red_list_logger, cache_files_logger


def add_word_in_db(word=None, translate=None):
    if word is not None and translate is not None:
        red_list_db.insert({'word': word, 'translate': translate})
        red_list_logger.info(f'Вставка: {word} и {translate} в Красный список прошла успешно.')


def clear_cache_redlist():
    red_list_db.truncate()
    red_list_logger.info('База данных Красного списка была очищена успешно.')


def edit_word_in_db(current_word: str, word: str):
    cache = Query()
    red_list_db.update({'word': word}, cache.word == current_word) or \
    red_list_db.update({'translate': word}, cache.translate == current_word)
    red_list_logger.info(f'Редактирование слова: {current_word} на {word} было успешно выполнено.')


def delete_word_in_db(deleted_word):
    cache = Query()
    red_list_db.remove(cache.word == deleted_word) or \
    red_list_db.remove(cache.translate == deleted_word)
    red_list_logger.info(f'Удаление слова: {deleted_word} было успешно выполнено.')


def cache_current_file(filepath=None, words_list=None):
    caching_files = cache_files_db.all()
    if filepath is None:
        return
    if words_list is None:
        words_list = []
    if filepath in caching_files:
        return False
    if len(cache_files_db.all()) >= 10:
        fp = Query()
        cache_files_db.remove(fp.filepath == caching_files[0]['filepath'])
    cache_files_db.insert({'filepath': filepath, 'words': words_list})
    cache_files_logger.info(f'Кэширование файла: {filepath} прошло успешно.')


def download_file_from_cache(filepath: str = None):
    query = Query()
    result = cache_files_db.search(query.filepath == filepath)[0]
    cache_files_logger.info(f'Файл: {filepath} был успешно загружен.')
    return result['words']


def clear_cache_filenames_db():
    cache_files_db.truncate()
    cache_files_logger.info('База данных Кэширования файлов была очищена успешно.')

