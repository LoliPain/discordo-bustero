import typing
from abc import ABC, abstractmethod

from ..api_types import Content, Entity


class AbstractClientObj(ABC):
    """Object of API Client

    :var scope: Scope of object responsibility :tuple
    """
    scope: tuple

    @abstractmethod
    def __init__(self, **kwargs: typing.Any):
        """Create client object

        :param kwargs: Content-based params :typing.Any
        """

    @property
    @abstractmethod
    def content(self) -> Content:
        """Unique content of ClientObj

        :return: Formed :Content request data
        """

    @property
    def entity(self) -> Entity:
        """Collect attributes of ClientObj

        :return: :Entity dict with ClientObj.scope :tuple and _ClientObj.content
        """
        return {'scope': self.scope, 'content': self.content}
