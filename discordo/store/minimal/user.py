import typing

from ..abstract import AbstractStoreBase


class UsersParam(AbstractStoreBase):
    def __init__(self):
        """Create config param"""
        self.file: typing.Union[str, list] = 'users.txt'
        self.mixed: bool = False

    def set_data(
            self,
            user_data: typing.Any,
            **kwargs: typing.Any,
    ):
        """Set passed data on param element

        :param user_data: File name or value
        :param kwargs: Is file contains log:pass
        """
        self.file = user_data
        self.mixed = kwargs.get('mixed', False)
