import typing
from abc import ABC, abstractmethod

import requests

from api_client.objects import Content, Entity


class AbstractRequestBase(ABC):
    """Minimal API Request creator"""
    @abstractmethod
    def __init__(self):
        """Create API request creator object"""

    @abstractmethod
    def collect_content(
            self,
            body: typing.Optional[str] = '',
            **kwargs: typing.Any,
    ) -> Content:
        """Request content collector

        :param body: Data :str for creating request
        :param kwargs: Additional context data :typing.Any of body

        :return: Prepared for sending content :Content
        """

    @abstractmethod
    def collect_request(
            self,
            headers: Entity,
            action: Entity,
            content: Content,
    ) -> requests.Request:
        """Request collector

        :param headers: Headers :Entity with scope :tuple and Request.headers :dict
        :param action: Action :Entity with scope :tuple and :dict Request.method, Request.url
        :param content: Content of request

        :return: Compiled request :requests.Request
        """
