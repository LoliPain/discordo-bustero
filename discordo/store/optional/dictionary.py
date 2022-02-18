import typing

from ..abstract import AbstractStoreBase


class DictionaryParam(AbstractStoreBase):
    def __init__(self):
        self.dictionary: str = 'dict.txt'
        self.channel: str = ''

    def set_data(
            self,
            user_data: typing.Any,
            **kwargs: typing.Any,
    ):
        self.dictionary = user_data
        self.channel = kwargs.get('channel', '')
