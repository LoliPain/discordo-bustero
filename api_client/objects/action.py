import typing
from api_client.objects import AbstractClientObj, Content


class ActionClient(AbstractClientObj):

    scope = ('message',)

    def __init__(self, url: str, method: typing.Optional[str] = 'GET'):
        self.url = url
        self.method = method

    @property
    def content(self) -> Content:
        return {'method': self.method, 'url': self.url}
