import json
import os


class Config:
    def __init__(self, file):
        with open(os.path.abspath(file), 'r') as conf_file:
            self._config = json.load(conf_file)

    def get_property(self, property_name):
        return self._config[property_name] if property_name in self._config.keys() else None


config = Config('config.json')
