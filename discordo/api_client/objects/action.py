from .abstract import AbstractClientObj
from ..api_types import RequestData, Scope


class ActionClient(AbstractClientObj):
    """Action Object of API Client"""
    scope: Scope = ('discordo.api_client.minimal.message',
                    'discordo.api_client.minimal.reaction')

    def __init__(self, url: str, method: str = 'GET'):
        """Create action object

        :param url: Link to API
        :param method: Custom http method name, using GET by default
        """
        self.url = url
        self.method = method

    @property
    def content(self) -> RequestData:
        """Action content

        :return: Parsed action data
        """
        return {'method': self.method, 'url': self.url}
