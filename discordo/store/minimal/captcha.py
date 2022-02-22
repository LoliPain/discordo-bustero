import typing

from ..abstract import AbstractStoreBase


class CaptchaParam(AbstractStoreBase):
    def __init__(self):
        """Create config param"""
        self.token: str = ''

    def set_data(
            self,
            user_data: typing.Any,
            **kwargs: typing.Any,
    ):
        """Set passed data on param element

        :param user_data: Captcha token
        :param kwargs: Additional data
        """
        self.token = user_data
