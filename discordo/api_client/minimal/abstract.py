import typing
from abc import ABC, abstractmethod

import requests

from ..api_types import RequestData, Entity


class AbstractRequestBase(ABC):
    """Minimal API Request creator"""

    @abstractmethod
    def collect_content(
            self,
            body: str = '',
            **kwargs: typing.Any,
    ) -> RequestData:
        """Request content collector

        :param body: Data for creating request
        :param kwargs: Additional context data of body

        :return: Content prepared for sending
        """

    @abstractmethod
    def collect_request(
            self,
            headers: Entity,
            action: Entity,
            content: typing.Optional[RequestData] = None,
    ) -> requests.Request:
        """Request collector

        :param headers: Headers :Entity with scope and Request.headers
        :param action: Action :Entity with scope and Request.method, Request.url
        :param content: Content of request

        :return: Compiled request
        """

    def __init__(self):
        """Create client method

        :ivar self.content: Share content between methods of instance
        """
        self.content = {}
