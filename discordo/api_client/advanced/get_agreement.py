import typing

import requests

from .abstract import AbstractAdvancedRequest
from ..api_types import RequestData, Entity

if typing.TYPE_CHECKING:
    __class__: typing.Type


class AdvancedGetAgreement(AbstractAdvancedRequest):
    """Get server agreement data"""

    @staticmethod
    def rebuild_action(
            action: typing.Optional[Entity] = None,
            **kwargs: typing.Any,
    ) -> Entity:
        """Rebuild GET action into get server agreement

        :param action: Any action

        :return: Get agreement action
        """
        if not action:
            action = {'scope': (__class__.__name__,), 'content': {}}
        action['content']['method'] = 'GET'
        action['content']['url'] = 'https://discord.com/api/v9/guilds'

        return action

    def collect_content(
            self,
            body: str = '',
            **kwargs: typing.Any,
    ) -> RequestData:
        """Verify type of guild id

        :param body: Passed guild id

        :return: Ready for request guild id
        """
        body_: int = int(body)

        self.content = {'guild_id': str(body_)}
        return self.content

    def collect_request(
            self,
            headers: Entity,
            action: Entity,
            content: typing.Optional[RequestData] = None,
    ) -> requests.Request:
        """Get server agreement request collector

        :param headers: Headers with scope and Request.headers
        :param action: Action with scope and Request.method, Request.url
        :param content: Guild id

        :return: Compiled get agreement request
        """
        content = content or self.content

        action_data: RequestData = action.get('content', {})
        headers_data: RequestData = headers.get('content', {})

        action_data.update({'url': f"{action_data['url']}/{content['guild_id']}/member-verification"})

        if (
                not {__class__.__name__}.intersection(
                    headers.get('scope', ()),
                    action.get('scope', ()),
                )
        ):
            raise RuntimeError(f"{__class__.__name__} not in {action['scope']} or {headers['scope']} scope list")

        return requests.Request(headers=headers_data, **action_data)
