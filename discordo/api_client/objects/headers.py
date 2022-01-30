import typing

from .abstract import AbstractClientObj
from ..api_types import Content


class HeadersClient(AbstractClientObj):
    """Headers Object of API Client"""
    scope = ('discordo.api_client.minimal.message',
             'discordo.api_client.minimal.reaction')

    authorization: str
    user_agent: str = (
        "Mozilla/5.0 "
        "(Windows NT 10.0; WOW64) "
        "AppleWebKit/537.36 "
        "(KHTML, like Gecko) "
        "discord/1.0.9003 "
        "Chrome/91.0.4472.164 "
        "Electron/13.4.0 "
        "Safari/537.36")

    def __init__(self, token: str, user_agent: typing.Optional[str] = ''):
        """Create headers object

        :param token: Authorization token :str for API
        :param user_agent: Optional data of user-agent :str, using discord client by default
        """
        self.authorization = token
        self.user_agent = user_agent or self.user_agent

    @property
    def content(self) -> Content:
        """Unique Headers content

        :return: Parsed :Content headers data
        """
        return {'authorization': self.authorization, 'user-agent': self.user_agent}
