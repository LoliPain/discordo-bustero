import json
import os.path
import typing

CONFIG_PRESET: dict = {
    "link": {
        "param": "Server invite URL",
        "value": "*",
    },
    "captcha": {
        "param": "Anti-Captcha token",
        "value": "*",
    },
    "user": {
        "param": "Path to users auth file",
        "value": "users.txt",
    },
    "dictionary": {
        "param": "Path to words list",
        "value": "*",
    },
    "channel_id": {
        "param": "ID of channel where to send messages",
        "value": "*"
    },
    "reaction": {
        "param": "Emoji reaction setting",
        "value": "*",
    },
    "message_id": {
        "param": "ID of message for reaction",
        "value": "*"
    },
    "confirmation": {
        "param": "Server agreement checkbox",
        "value": "*",
    },
    "proxy": {
        "param": "Path to proxy file",
        "value": "*",
    },
    "started": False,
}

LOGGER_FORMAT = '| %(filename)s || %(message)s'


class ConfigIO:
    """JSON config file operations"""

    def __init__(self, config: typing.Optional[str] = None):
        """Set config file path

        :param config: Custom file path
        """
        self.config: str = config or 'config.json'

    def read(self) -> dict:
        """Read from config file

        :return: Data from config
        """
        with open(self.config, mode='r') as config_file:
            config: dict = json.load(config_file)
        if CONFIG_PRESET.keys() == config.keys():
            return config
        raise RuntimeError(f'{self.config} seems broken, remove it.')

    def write(self, user_data: dict) -> str:
        """Write to config file

        :param user_data: Modified config data

        :return: Path to saved config
        """
        if CONFIG_PRESET.keys() == user_data.keys():
            with open(self.config, mode='w') as config_file:
                json.dump(user_data, config_file)
            return self.config
        raise RuntimeError(f'Data struct {user_data.keys()} is invalid')

    def create(self) -> str:
        """Create new config file only if not exist

        :return: Path to created config
        """
        if os.path.isfile(self.config):
            raise RuntimeError(f'{self.config} is already exist')
        with open(self.config, mode='x') as config_file:
            json.dump(CONFIG_PRESET, config_file)
        return self.config


class Screen:
    """UI output"""

    @staticmethod
    def clear():
        """Wipe current displayed data"""
        print('\n' * 100)

    @staticmethod
    def append(screen_data: str):
        """Append output to existing string

        :param screen_data: Data to be printed
        """
        print(f'{screen_data}\n')

    @staticmethod
    def show(screen_data: str):
        """Total refresh data on screen

        :param screen_data: Data to be printed
        """
        Screen.clear()
        Screen.append(screen_data)

    @staticmethod
    def skip():
        """Pass to next step interaction"""
        input('\nEnter ↵ ')

    @staticmethod
    def agreement() -> bool:
        """Verify the user choice

        :return: Bool of confirmation
        """
        return True if input('y/N: ').lower() == 'y' else False
