import typing

from ..abstract import AbstractStoreBase


class DictionaryParam(AbstractStoreBase):
    def __init__(self):
        """Create config param"""
        self.dictionary: str = 'dict.txt'
        self.channel: str = ''

    def set_data(
            self,
            user_data: typing.Any,
            **kwargs: typing.Any,
    ):
        """Set passed data on param element

        :param user_data: Name and value
        :param kwargs: Additional data
        """
        self.dictionary = user_data
        self.channel = kwargs.get('channel', '')
