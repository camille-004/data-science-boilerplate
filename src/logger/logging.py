# type: ignore
import logging
import sys

APP_LOGGER_NAME = "data-science-boilerplate"


def setup_app_level_logger(
    logger_name: str = APP_LOGGER_NAME, file_name: str = None
) -> logging.Logger:
    """
    Initialize root app-level logger.

    :param logger_name: The name of the app-level logger.
    :param file_name: The name of the file in which to store all log messages.
    :return: Return the logger.
    """
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    sh = logging.StreamHandler(sys.stdout)
    sh.setFormatter(formatter)

    logger.handlers.clear()
    logger.addHandler(sh)

    if file_name:
        fh = logging.FileHandler(APP_LOGGER_NAME)
        fh.setFormatter(formatter)
        logger.addHandler(fh)

    return logger


def get_logger(module_name: str) -> logging.Logger:
    """
    Make sure our modules can call the logger when needed.

    :param module_name: Module that will get this logger.
    :return: Return the logger.
    """
    return logging.getLogger(APP_LOGGER_NAME).getChild(module_name)