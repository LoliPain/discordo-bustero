import typing

from ..abstract import AbstractStoreBase


class ProxyParam(AbstractStoreBase):
    def __init__(self):
        self.proxy: str = ''

    def set_data(
            self,
            user_data: typing.Any,
            **kwargs: typing.Any,
    ):
        self.proxy = user_data
