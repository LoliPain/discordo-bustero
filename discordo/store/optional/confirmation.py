import typing

from ..abstract import AbstractStoreBase


class ConfirmationParam(AbstractStoreBase):
    def __init__(self):
        self.confirmation: bool = False

    def set_data(
            self,
            user_data: typing.Any,
            **kwargs: typing.Any,
    ):
        self.confirmation = user_data
