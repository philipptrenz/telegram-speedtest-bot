import json
from datetime import datetime


class Utils:

    def __init__(self, config_path='config.json'):
        # load config
        with open(config_path, 'r') as f:
            self.config = json.load(f)

    def get_config(self):
        return self.config

    def log(self, string):
        now = datetime.now()
        print('[' + now.strftime("%Y-%m-%d %H:%M:%S") + ']', string)  # logs are in system time zone

