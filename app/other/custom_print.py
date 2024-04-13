from colorama import init, Fore, Style

color_map = {
    "black": Fore.BLACK,
    "red": Fore.RED,
    "green": Fore.GREEN,
    "yellow": Fore.YELLOW,
    "blue": Fore.BLUE,
    "magenta": Fore.MAGENTA,
    "cyan": Fore.CYAN,
    "white": Fore.WHITE
}
style_map = {
    "normal": Style.NORMAL,
    "bright": Style.BRIGHT,
    "dim": Style.DIM,
    "reset_all": Style.RESET_ALL
}


def colored_print(message: str, color: str = "white", style: str = "normal"):
    """
    To display colored text for visualizing the application's workflow process.

    :param message: Text for display
    :param color: Text color
    :param style: Font style
    :return:
    """

    init()
    try:
        color_code = color_map.get(color, Fore.WHITE)
        style_code = style_map.get(style, Style.NORMAL)
        colored_message = f"{color_code}{style_code}{message}{Style.RESET_ALL}"
        print(colored_message)
        return True
    except (IndexError, TypeError) as e:
        message = f'Ошибка аргументов функции: {colored_print.__name__} {e}'
        print(message)
