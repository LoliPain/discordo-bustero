import typing
from abc import ABC, abstractmethod

import requests

from ..api_types import RequestData, Entity


class AbstractRequestBase(ABC):
    """Minimal API Request creator"""

    @staticmethod
    @abstractmethod
    def collect_content(
            body: str = '',
            **kwargs: typing.Any,
    ) -> RequestData:
        """Request content collector

        :param body: Data for creating request
        :param kwargs: Additional context data of body

        :return: Content prepared for sending
        """

    @staticmethod
    @abstractmethod
    def collect_request(
            headers: Entity,
            action: Entity,
            content: RequestData,
    ) -> requests.Request:
        """Request collector

        :param headers: Headers :Entity with scope and Request.headers
        :param action: Action :Entity with scope and Request.method, Request.url
        :param content: Content of request

        :return: Compiled request
        """
