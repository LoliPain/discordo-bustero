import json
import typing

import requests

from .abstract import AbstractAdvancedRequest
from ..api_types import RequestData, Entity

if typing.TYPE_CHECKING:
    __class__: typing.Type


class AdvancedConfirmAgreement(AbstractAdvancedRequest):
    """Server terms of use agreement request"""

    @staticmethod
    def rebuild_action(
            action: typing.Optional[Entity] = None,
            **kwargs: typing.Any,
    ) -> Entity:
        """Rebuild PUT action into terms of use agreement

        :param action: Any action
        :param kwargs: guild_id of discord server

        :return: New confirmation agreement url
        """
        if not action:
            action = {'scope': (__class__.__name__, ), 'content': {}}
        guild_id: int = int(kwargs.get('guild_id', ''))
        action['content']['method'] = 'PUT'
        action['content']['url'] = (
            f'https://discord.com/api/v9/guilds/'
            f'{guild_id}/requests/@me'
        )

        return action

    def collect_content(
            self,
            body: str = '',
            **kwargs: typing.Any,
    ) -> RequestData:
        """Collect confirmation using server agreement

        :param body: JSON of server user agreement

        :return: Built agreement confirmation
        """
        body_: dict = json.loads(body)
        del body_['description']
        body_['form_fields'][0]['response'] = 'true'

        self.content = {'agreement': json.dumps(body_)}
        return self.content

    def collect_request(
            self,
            headers: Entity,
            action: Entity,
            content: typing.Optional[RequestData] = None,
    ) -> requests.Request:
        """Confirmation request collector
        Request objects scope validation

        :param headers: Headers with scope and Request.headers
        :param action: Action with scope and Request.method, Request.url
        :param content: Request.data with prepared for sending JSON agreement

        :return: Compiled agreement request
        """
        content = content or self.content

        action_data: RequestData = action.get('content', {})
        headers_data: RequestData = headers.get('content', {})
        headers_data.update({'Content-type': 'application/json'})

        if (
                not {__class__.__name__}.intersection(
                    headers.get('scope', ()),
                    action.get('scope', ()),
                )
        ):
            raise RuntimeError(f"{__class__.__name__} not in {action['scope']} or {headers['scope']} scope list")

        return requests.Request(headers=headers_data, data=content['agreement'], **action_data)
