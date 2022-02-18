import colorama

from .abstract import AbstractUIBase


class ParamUIElement(AbstractUIBase):
    def __init__(self):
        self.elem: str = '{param}: {value}'

    def get_text(self, user_data: dict) -> str:
        user_data['param'] = colorama.Fore.BLUE + user_data['param']
        user_data['value'] = colorama.Fore.RED + user_data['value']
        elem = self.elem.format(**user_data)
        if user_data.get('selected'):
            elem += f'{colorama.Fore.MAGENTA}{colorama.Back.BLUE} <-- '
        return elem
