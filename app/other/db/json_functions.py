from tinydb import Query
from app.config import red_list_db, cache_files_db
from app.logger import exceptions_logger, red_list_logger, cache_files_logger
from app.other.custom_print import colored_print


def add_word_in_db(word: str, translate: str, db=red_list_db):
    """
    Adding data to JSON

    :param word:
    :param translate:
    :param db: Database for adding
    :return:
    """

    try:
        db.insert({'word': word, 'translate': translate})
        red_list_logger.info(f'Вставка: {word} и {translate} прошла успешно.')
    except (TypeError, AttributeError) as e:
        message = f'Функция: {add_word_in_db.__name__} получила неверные аргументы {e}'
        exceptions_logger.error(message)
        colored_print(message, style='bright', color='red')


def clear_cache_redlist(db=red_list_db):
    """
    Database cleanup

    :param db: Database for clearing
    :return:
    """

    try:
        db.truncate()
        red_list_logger.info('База данных была очищена успешно.')
    except (TypeError, AttributeError) as e:
        message = f'Функция: {clear_cache_redlist.__name__} получила неверные аргументы {e}'
        exceptions_logger.error(message)
        colored_print(message, style='bright', color='red')


def edit_word_in_db(current_word: str, word: str, db=red_list_db):
    """
    Editing a word in the database

    :param current_word:
    :param word:
    :param db: Database for editing
    :return:
    """

    try:
        cache = Query()
        db.update({'word': word}, cache.word == current_word) or db.update({'translate': word},
                                                                           cache.translate == current_word)
        red_list_logger.info(f'Редактирование слова: {current_word} на {word} было успешно выполнено.')
    except (TypeError, AttributeError) as e:
        message = f'Функция: {edit_word_in_db.__name__} получила неверные аргументы {e}'
        exceptions_logger.error(message)
        colored_print(message, style='bright', color='red')


def delete_word_in_db(deleted_word: str, db=red_list_db):
    """
    Deleting a word in the database

    :param deleted_word:
    :param db: Database for deleting
    :return:
    """
    try:
        cache = Query()
        db.remove(cache.word == deleted_word) or \
        db.remove(cache.translate == deleted_word)
        red_list_logger.info(f'Удаление слова: {deleted_word} было успешно выполнено.')
    except (TypeError, AttributeError, KeyError, ValueError) as e:
        message = f'Функция: {delete_word_in_db.__name__} получила неверные аргументы {e}'
        exceptions_logger.error(message)
        colored_print(message, style='bright', color='red')


def cache_current_file(filepath: str = None, words_list: list = None, db=cache_files_db):
    """
    Caching words list by filepath which was downloaded.

    :param filepath:
    :param words_list: List of words for storage by file path
    :param db: Database for caching
    :return:
    """

    try:
        caching_files = cache_files_db.all()
        if filepath is None:
            return
        if words_list is None:
            words_list = []
        if filepath in caching_files:
            return False
        if len(db.all()) >= 10:
            fp = Query()
            db.remove(fp.filepath == caching_files[0]['filepath'])
        db.insert({'filepath': filepath, 'words': words_list})
        cache_files_logger.info(f'Кэширование файла: {filepath} прошло успешно.')
    except (TypeError, AttributeError) as e:
        message = f'Функция: {cache_current_file.__name__} получила неверные аргументы {e}'
        exceptions_logger.error(message)
        colored_print(message, style='bright', color='red')


def download_file_from_cache(filepath: str = None, db=cache_files_db):
    """
    Download words from the database by filepath

    :param filepath:
    :param db: Database for downloading
    :return:
    """

    try:
        query = Query()
        result = db.search(query.filepath == filepath)[0]
        cache_files_logger.info(f'Файл: {filepath} был успешно загружен.')
        return result['words']
    except (TypeError, AttributeError, IndexError) as e:
        message = f'Функция: {download_file_from_cache.__name__} получила неверные аргументы {e}'
        exceptions_logger.error(message)
        colored_print(message, style='bright', color='red')


def clear_cache_filenames_db(db=cache_files_db):
    """
    Clearing database with words lists and filepaths

    :param db: Database for clearing
    :return:
    """

    try:
        db.truncate()
        cache_files_logger.info('База данных Кэширования файлов была очищена успешно.')
    except (TypeError, AttributeError) as e:
        message = f'Функция: {delete_word_in_db.__name__} получила неверные аргументы {e}'
        exceptions_logger.error(message)
        colored_print(message, style='bright', color='red')
