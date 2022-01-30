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
            message_body: typing.Optional[str] = '',
            reaction: typing.Optional[str] = '',
            **kwargs: typing.Any,
    ) -> Content:
        """Request content collector

        :param message_body: Plain text :str for message that should be converted to JSON object
        :param reaction: SymID :str for direct reaction request should be converted to http-escaped string
        :param kwargs: Additional context data of content

        :return: :Content with prepared for sending JSON :dict or escaped SymID :str
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
        :param content: Request.data :Content with JSON :dict or SymID :str

        :return: Compiled request :requests.Request
        """
