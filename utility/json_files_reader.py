import json
import os


def read_config():  # open the config file for read
    script_directory = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    absolute_path = os.path.join(script_directory, "config/config.json")
    with open(absolute_path, 'r') as f:
        config = json.load(f)
    return config


def read_from_secret_file():  # open the secret json , and read it
    script_directory = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    absolute_path = os.path.join(script_directory, "config/secrets.json")
    with open(absolute_path, 'r') as f:
        config = json.load(f)
    return config
