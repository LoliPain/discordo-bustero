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
            action: Entity,
            **kwargs: typing.Any,
    ) -> Entity:
        """Rebuild GET action into get server agreement

        :param action: Any action

        :return: Get agreement action
        """
        action['content']['method'] = 'GET'
        action['content']['url'] = 'https://discord.com/api/v9/guilds'

        return action

    @staticmethod
    def collect_content(
            body: str = '',
            **kwargs: typing.Any,
    ) -> RequestData:
        """Verify type of guild id

        :param body: Passed guild id

        :return: Ready for request guild id
        """
        body_: int = int(body)

        return {'guild_id': str(body_)}

    @staticmethod
    def collect_request(
            headers: Entity,
            action: Entity,
            content: RequestData,
    ) -> requests.Request:
        """Get server agreement request collector

        :param headers: Headers with scope and Request.headers
        :param action: Action with scope and Request.method, Request.url
        :param content: Guild id

        :return: Compiled get agreement request
        """
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
