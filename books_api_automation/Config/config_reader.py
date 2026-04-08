import configparser
from logging import config


def read_config(section, key):
    config = configparser.ConfigParser()
    config.read("books_api_automation/Config/config.ini")

    BASE_URL = config["DEFAULT"]["BASE_URL"]
    ENV = config["DEFAULT"]["ENV"]
    return config.get(section, key)