import typing

from ..abstract import AbstractStoreBase


class ProxyParam(AbstractStoreBase):
    def __init__(self):
        """Create config param"""
        self.file: str = ''

    def set_data(
            self,
            user_data: typing.Any,
            **kwargs: typing.Any,
    ):
        """Set passed data on param element

        :param user_data: File name
        :param kwargs: Additional data
        """
        self.file = user_data
