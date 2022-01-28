import typing
from abc import ABC, abstractmethod
import requests

from api_client.objects import Content


class AbstractRequestBase(ABC):
    """Minimal API Request class"""

    @abstractmethod
    def collect_content(
            self,
            message_body: str = '',
            reaction: str = ''
    ) -> Content:
        """Request content collector

        :param message_body: Plain text :str for message that should be converted to JSON object
        :param reaction: SymID :str for direct reaction request should be converted to http-escaped string
        """

    @abstractmethod
    def collect_request(
            self,
            headers: typing.Dict[str, str],
            action: Content,
            content: Content = None,
    ) -> requests.Request:
        """Request data collector

        :param headers: Request headers :dict
        :param action: Plain url :str or {method: method, url: url} :dict
        :param content: JSON :dict | SymID :str or empty for GET requests
        """
