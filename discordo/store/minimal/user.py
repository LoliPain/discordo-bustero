import typing

from ..abstract import AbstractStoreBase


class UsersParam(AbstractStoreBase):
    def __init__(self):
        """Create config param"""
        self.file: str = 'users.txt'
        self.mixed: bool = False

    def set_data(
            self,
            user_data: typing.Any,
            **kwargs: typing.Any,
    ):
        """Set passed data on param element

        :param user_data: Name and value
        :param kwargs: Additional data
        """
        self.file = user_data
        self.mixed = kwargs.get('mixed', False)
