import typing

from ..abstract import AbstractStoreBase


class ConfirmationParam(AbstractStoreBase):
    def __init__(self):
        """Create config param"""
        self.confirmation: bool = False

    def set_data(
            self,
            user_data: typing.Any,
            **kwargs: typing.Any,
    ):
        """Set passed data on param element

        :param user_data: Name and value
        :param kwargs: Additional data
        """
        self.confirmation = user_data
