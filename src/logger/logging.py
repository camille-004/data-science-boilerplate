# type: ignore
import logging
import sys

APP_LOGGER_NAME = "data-science-boilerplate"


def setup_app_level_logger(
    logger_name: str = APP_LOGGER_NAME, file_name: str = None
) -> logging.Logger:
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
