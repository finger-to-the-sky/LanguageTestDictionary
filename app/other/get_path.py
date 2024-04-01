import os


def get_path_project():
    current_file_path = os.path.abspath(__file__)
    current_directory = current_file_path
    while not os.path.exists(os.path.join(current_directory, 'README.md')):
        current_directory = os.path.dirname(current_directory)
    return current_directory