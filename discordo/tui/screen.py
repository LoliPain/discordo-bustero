import copy

import colorama

from .abstract import AbstractUIBase
from .params import ParamUIElement


class TerminalUIScreen(AbstractUIBase):
    """Collect of params"""

    def __init__(self):
        """Implement all elems"""
        self.link = ParamUIElement()
        self.captcha = ParamUIElement()
        self.user = ParamUIElement()
        self.dictionary = ParamUIElement()
        self.channel = ParamUIElement()
        self.reaction = ParamUIElement()
        self.message = ParamUIElement()
        self.confirmation = ParamUIElement()
        self.proxy = ParamUIElement()

    def get_text(self, user_data: dict) -> str:
        """Return formatted full screen text

        :param user_data: Escaped collection of all params data

        :return: Colorama string
        """
        _user_data = copy.deepcopy(user_data)
        colorama.init(autoreset=True)
        screen_data = f'{colorama.Fore.BLACK}Discordo-Bustero-Configo!\n\n'
        screen_data += self.link.get_text(_user_data['link']) + '\n'
        screen_data += self.captcha.get_text(_user_data['captcha']) + '\n'
        screen_data += self.user.get_text(_user_data['user']) + '\n'
        screen_data += self.dictionary.get_text(_user_data['dictionary']) + '\n'
        screen_data += '- ' + self.channel.get_text(_user_data['channel_id']) + '\n'
        screen_data += self.reaction.get_text(_user_data['reaction']) + '\n'
        screen_data += '- ' + self.message.get_text(_user_data['message_id']) + '\n'
        screen_data += self.confirmation.get_text(_user_data['confirmation']) + '\n'
        screen_data += self.proxy.get_text(_user_data['proxy']) + '\n'
        if _user_data['started']:
            screen_data += f'{colorama.Fore.BLACK}Bustero in progresso!'
        return screen_data
