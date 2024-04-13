import os
from app.other.custom_print import colored_print


def get_path_project(file='README.md'):
    """
    Get path to main directory project from any file
    :return:
    """

    try:
        current_file_path = os.path.abspath(__file__)
        current_directory = current_file_path
        while not os.path.exists(os.path.join(current_directory, file)):
            current_directory = os.path.dirname(current_directory)
        return current_directory
    except (TypeError,) as e:
        message = f'Функция: {get_path_project.__name__} получила неверные аругменты {e}'
        colored_print(message, color='red', style='bright')