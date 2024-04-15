import logging

from app.other.custom_print import colored_print
from app.other.get_path import get_path_project

loggers = {}


def get_logger(name: str, formatter: str = "%(name)s %(asctime)s %(levelname)s %(message)s", filemode: str = 'w',
               encoding: str = 'UTF-8'):
    try:
        if name in loggers:
            return loggers[name]
        logger = logging.getLogger(name)
        logger.setLevel(logging.INFO)
        handler2 = logging.FileHandler(f"{get_path_project()}\\app\\other\\logs\\{name}.log", mode=filemode,
                                       encoding=encoding)
        formatter2 = logging.Formatter(formatter)
        handler2.setFormatter(formatter2)
        logger.addHandler(handler2)

        loggers[name] = logger
        return logger
    except (TypeError,) as e:
        message = f'Функция: {get_logger.__name__} получила неверные аргументы {e}'
        colored_print(message, color='red', style='bright')


exceptions_logger = get_logger('exceptions', filemode='a')
tk_functions_logger = get_logger('tk_functions_logger')
red_list_logger = get_logger('red_list_db')
cache_files_logger = get_logger('cache_files_db')
