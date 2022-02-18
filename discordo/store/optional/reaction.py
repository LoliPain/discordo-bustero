import typing

from ..abstract import AbstractStoreBase


class ReactionParam(AbstractStoreBase):
    def __init__(self):
        self.message: str = ''
        self.emoji: str = ''

    def set_data(
            self,
            user_data: typing.Any,
            **kwargs: typing.Any,
    ):
        self.message = user_data
        self.emoji = kwargs.get('emoji', '')
