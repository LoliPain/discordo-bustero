import typing
from abc import ABC, abstractmethod

from ..api_types import Entity
from ..minimal.abstract import AbstractRequestBase


class AbstractAdvancedRequest(AbstractRequestBase, ABC):
    """Advanced API Requests creator"""

    @staticmethod
    @abstractmethod
    def rebuild_action(
            action: typing.Optional[Entity] = None,
            **kwargs: typing.Any,
    ) -> Entity:
        """Rebuild action URL due to mode

        :param action: Base action URL
        :param kwargs: Passed context of mode data

        :return: Refactored advanced action
        """
