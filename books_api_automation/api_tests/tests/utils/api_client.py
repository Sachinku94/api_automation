import logging
from attrs import inspect
import inspect
import requests
from books_api_automation.Config.config_reader import read_config
BASE_URL = read_config("DEFAULT", "BASE_URL")
class APIClient:

    def __init__(self):
        self.session = requests.Session()

    def get(self, endpoint):
        return self.session.get(f"{BASE_URL}{endpoint}")

    def post(self, endpoint, payload=None, headers=None):
        return self.session.post(f"{BASE_URL}{endpoint}", json=payload, headers=headers)

    def patch(self, endpoint, payload=None, headers=None):
        return self.session.patch(f"{BASE_URL}{endpoint}", json=payload, headers=headers)

    def delete(self, endpoint, headers=None):
        return self.session.delete(f"{BASE_URL}{endpoint}", headers=headers)
    



    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler("logfile.log")
        formatter = logging.Formatter(
            "%(asctime)s :%(levelname)s : %(name)s :%(message)s"
        )
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  # filehandler object

        logger.setLevel(logging.DEBUG)
        return logger