import typing
from api_client import AbstractClientObj, Content


class ActionClient(AbstractClientObj):
    """Action Object of API Client"""

    scope = ('api_client.minimal.message',)

    def __init__(self, url: str, method: typing.Optional[str] = 'GET'):
        """

        :param url: Link :str to API
        :param method: Optional http method name :str, using GET by default

        """

        self.url = url
        self.method = method

    @property
    def content(self) -> Content:
        """Unique content of Action

        :return: Formed :Content action data

        """

        return {'method': self.method, 'url': self.url}
