import logging

loggers = {}


def get_logger(name, formatter: str = "%(name)s %(asctime)s %(levelname)s %(message)s", filemode: str = 'w'):
    if name in loggers:
        return loggers[name]
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    handler2 = logging.FileHandler(f"{name}.log", mode=filemode, encoding='UTF-8')
    formatter2 = logging.Formatter(formatter)
    handler2.setFormatter(formatter2)
    logger.addHandler(handler2)

    loggers[name] = logger
    return logger
