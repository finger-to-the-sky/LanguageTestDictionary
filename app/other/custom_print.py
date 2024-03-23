from colorama import init, Fore, Style


def colored_print(message, color="white", style="normal"):
    init()
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

    color_code = color_map.get(color, Fore.WHITE)
    style_code = style_map.get(style, Style.NORMAL)

    colored_message = f"{color_code}{style_code}{message}{Style.RESET_ALL}"
    print(colored_message)
