import typing

from api_client import AbstractClientObj, Content


class ActionClient(AbstractClientObj):
    """Action Object of API Client"""
    scope = ('api_client.minimal.message',
             'api_client.minimal.reaction')

    def __init__(self, url: str, method: typing.Optional[str] = 'GET'):
        """Create action object

        :param url: Link :str to API
        :param method: Optional http method name :str, using GET by default
        """
        self.url = url
        self.method = method

    @property
    def content(self) -> Content:
        """Unique Action content

        :return: Parsed :Content action data
        """
        return {'method': self.method, 'url': self.url}
