import typing
from abc import ABC, abstractmethod

Content = typing.Union[typing.Dict[str, str], str]


class AbstractClientObj(ABC):
    """Object of API Client

    :param scope: Scope of object responsibility :tuple (only for reviewing purpose)

    """

    scope: tuple

    @property
    @abstractmethod
    def content(self) -> Content:
        """Returns special data of _ClientObj"""

    @property
    def entity(self) -> typing.Tuple[tuple, Content]:
        """Collect attributes of _ClientObj

        :return: :Tuple of _ClientObj.scope :tuple and _ClientObj.content with JSON/Request :dict or Plain URL :str
        """

        return self.scope, self.content
