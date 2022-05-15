import os
from pathlib import Path
from typing import Dict

import yaml  # type: ignore

CONFIG_PATH = os.path.join(Path(__file__).parents[0], "config")


def load_config(f_name: str) -> Dict:
    """
    Retrieve configurations from a given file.
    :param f_name: Name of chosen config file.
    :return: Dictionary of YAML contents
    """
    with open(os.path.join(CONFIG_PATH, f_name)) as f:
        _config = yaml.safe_load(f)

    return _config


config = load_config("config.yml")
