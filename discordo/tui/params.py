import colorama

from .abstract import AbstractUIBase


class ParamUIElement(AbstractUIBase):
    """Single param status element"""

    def __init__(self):
        """Create elem string"""
        self.elem: str = '{param}: {value}'

    def get_text(self, elem_data: dict) -> str:
        """Return formatted param

        :param elem_data: Context data

        :return: Colorama string
        """
        colorama.init(autoreset=True)
        elem_data['param'] = colorama.Fore.BLUE + elem_data['param']
        elem_data['value'] = colorama.Fore.RED + elem_data['value']
        elem = self.elem.format(**elem_data)
        if elem_data.get('selected'):
            elem += f'{colorama.Fore.MAGENTA} <-- '
        return elem
