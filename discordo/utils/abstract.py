import typing
from abc import ABC, abstractmethod


class AbstractUtilsBase(ABC):
    """Workflow utils"""

    @abstractmethod
    def __init__(self, **kwargs: typing.Any):
        """Create utility instance

        :param kwargs: Instance config data
        """

    @abstractmethod
    def process(self, **kwargs: typing.Any) -> str:
        """Processing body data

        :param kwargs: Input context data

        :return: Processed data
        """

    @abstractmethod
    def validate(
            self,
            body: str,
            refer: str = '',
    ) -> str:
        """Assert result data

        :param body: Input validate data
        :param refer: Reference to assert data

        :return: Returns body if validation success, otherwise raise Exception
        """
