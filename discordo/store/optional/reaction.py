import typing

from ..abstract import AbstractStoreBase


class ReactionParam(AbstractStoreBase):
    def __init__(self):
        """Create config param"""
        self.emoji: str = ''
        self.message: str = ''

    def set_data(
            self,
            user_data: typing.Any,
            **kwargs: typing.Any,
    ):
        """Set passed data on param element

        :param user_data: Emoji
        :param kwargs: Message ID
        """
        self.emoji = user_data
        self.message = kwargs.get('message', '')
