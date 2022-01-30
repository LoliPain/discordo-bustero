import typing
from abc import ABC, abstractmethod

from ..api_types import Scope, RequestData, Entity


class AbstractClientObj(ABC):
    """Object of API Client

    :var scope: Scope of object responsibility
    """
    scope: Scope

    @abstractmethod
    def __init__(self, **kwargs: typing.Any):
        """Create client object

        :param kwargs: Object-based params
        """

    @property
    @abstractmethod
    def content(self) -> RequestData:
        """Unique content of ClientObj

        :return: Parsed request data
        """

    @property
    def entity(self) -> Entity:
        """Collect attributes of ClientObj

        :return: Entity dict with ClientObj.scope and ClientObj.content
        """
        return {'scope': self.scope, 'content': self.content}
