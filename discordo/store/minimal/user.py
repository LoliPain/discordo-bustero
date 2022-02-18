import typing

from ..abstract import AbstractStoreBase


class UsersParam(AbstractStoreBase):
    def __init__(self):
        self.file: str = 'users.txt'
        self.mixed: bool = False

    def set_data(
            self,
            user_data: typing.Any,
            **kwargs: typing.Any,
    ):
        self.file = user_data
        self.mixed = kwargs.get('mixed', False)
