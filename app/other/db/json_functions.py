from tinydb import Query
from app.config import red_list_db, cache_files_db


def add_word_in_db(word=None, translate=None):
    if word is not None and translate is not None:
        red_list_db.insert({'word': word, 'translate': translate})


def clear_cache_redlist():
    red_list_db.truncate()


def edit_word_in_db(current_word: str, word: str):
    cache = Query()
    red_list_db.update({'word': word}, cache.word == current_word) or \
    red_list_db.update({'translate': word}, cache.translate == current_word)


def delete_word_in_db(deleted_word):
    cache = Query()
    red_list_db.remove(cache.word == deleted_word) or \
    red_list_db.remove(cache.translate == deleted_word)


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


def download_file_from_cache(filepath: str = None):
    query = Query()
    result = cache_files_db.search(query.filepath == filepath)[0]
    return result['words']


def clear_cache_filenames_db():
    cache_files_db.truncate()
