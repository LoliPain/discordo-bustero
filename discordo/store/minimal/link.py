import typing

from ..abstract import AbstractStoreBase


class LinkParam(AbstractStoreBase):
    def __init__(self):
        self.link: str = ''

    def set_data(
            self,
            user_data: typing.Any,
            **kwargs: typing.Any,
    ):
        self.link = user_data
