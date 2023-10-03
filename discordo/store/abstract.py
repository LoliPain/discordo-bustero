import typing
from abc import ABC, abstractmethod


class AbstractStoreBase(ABC):
    @abstractmethod
    def __init__(self):
        """Create config param"""

    @abstractmethod
    def set_data(
            self,
            user_data: typing.Any,
            **kwargs: typing.Any,
    ):
        """

        :param user_data: Passed config data
        :param kwargs: Additional context data
        """

    @property
    def collect(self) -> dict:
        return self.__dict__
