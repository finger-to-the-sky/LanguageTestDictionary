import json
from json import JSONDecodeError
from app.config import JSON_REDLIST_FILE


def add_words_to_lists(word=None, translate=None):
    words = get_words()
    if word is None or translate is None:
        return
    if len(words) >= 30:
        return
    else:
        words.append({'word': word, 'translate': translate})

    with open(JSON_REDLIST_FILE, 'w', encoding='utf-8') as f:
        json.dump(words, f, sort_keys=True, indent=2)


def get_words():
    with open(JSON_REDLIST_FILE, 'r', encoding='utf-8') as f:
        try:
            result = json.load(f)
        except JSONDecodeError:
            result = []
        return result


def clear_cache():
    with open(JSON_REDLIST_FILE, 'w', encoding='utf-8') as f:
        json.dump([], f, sort_keys=True, indent=2)


def edit_word_in_json(word, edited):
    words = get_words()

    for i, w in enumerate(words):
        if w['word'] == word:
            w['word'] = edited
            break
        elif w['translate'] == word:
            w['translate'] = edited
            break

    with open(JSON_REDLIST_FILE, 'w', encoding='utf-8') as f:
        json.dump(words, f, sort_keys=True, indent=2)


def delete_word_from_cache(deleted_word):
    words = get_words()
    for i, w in enumerate(words):
        print(i, w)
        if w['word'] == deleted_word or w['translate'] == deleted_word:
            words.pop(i)
            break

    with open(JSON_REDLIST_FILE, 'w', encoding='utf-8') as f:
        json.dump(words, f, sort_keys=True, indent=2)
