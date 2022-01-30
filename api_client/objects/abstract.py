import typing
from abc import ABC, abstractmethod

Content = typing.Union[typing.Dict[str, str], str]
Entity = typing.Dict[str, typing.Union[tuple, Content]]


class AbstractClientObj(ABC):
    """Object of API Client

    :param scope: Scope of object responsibility :tuple
    """
    scope: tuple

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
