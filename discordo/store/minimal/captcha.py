import typing

from ..abstract import AbstractStoreBase


class CaptchaParam(AbstractStoreBase):
    def __init__(self):
        self.token: str = ''

    def set_data(
            self,
            user_data: typing.Any,
            **kwargs: typing.Any,
    ):
        self.token = user_data
