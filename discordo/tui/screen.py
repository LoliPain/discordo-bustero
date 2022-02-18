import colorama

from .abstract import AbstractUIBase
from .params import ParamUIElement


class TerminalUIScreen(AbstractUIBase):
    def __init__(self):
        self.link = ParamUIElement()
        self.captcha = ParamUIElement()
        self.user = ParamUIElement()
        self.dictionary = ParamUIElement()
        self.reaction = ParamUIElement()
        self.confirmation = ParamUIElement()
        self.proxy = ParamUIElement()

    def get_text(self, user_data: dict) -> str:
        screen_data = f'{colorama.Back.MAGENTA}{colorama.Fore.BLACK}Discordo-Bustero-Configo!\n\n'
        screen_data += self.link.get_text(user_data['link']) + '\n'
        screen_data += self.captcha.get_text(user_data['captcha']) + '\n'
        screen_data += self.user.get_text(user_data['user']) + '\n'
        screen_data += self.dictionary.get_text(user_data['dictionary']) + '\n'
        screen_data += self.reaction.get_text(user_data['reaction']) + '\n'
        screen_data += self.confirmation.get_text(user_data['confirmation']) + '\n'
        screen_data += self.proxy.get_text(user_data['proxy']) + '\n'
        if user_data['started']:
            screen_data += f'{colorama.Back.MAGENTA}{colorama.Fore.BLACK}Bustero in progresso!'
        return screen_data
