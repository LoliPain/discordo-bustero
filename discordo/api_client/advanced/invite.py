import re
import typing

import requests

from .abstract import AbstractAdvancedRequest
from ..api_types import RequestData, Entity

if typing.TYPE_CHECKING:
    __class__: typing.Type


class AdvancedAcceptInvite(AbstractAdvancedRequest):
    """Accept invite to server request"""

    @staticmethod
    def rebuild_action(
            action: Entity,
            **kwargs: typing.Any,
    ) -> Entity:
        """Rebuild action for server invite

        :param action: Any action

        :return: Server invite action
        """
        action['content']['method'] = 'POST'
        action['content']['url'] = 'https://discord.com/api/v9/invites'

        return action

    @staticmethod
    def collect_content(
            body: str = '',
            **kwargs: typing.Any,
    ) -> RequestData:
        """Collect invite code from invite link

        :param body: Invite link

        :return: Invite code
        """
        invite_code = re.search(
            r'(https://discord\.com/invite/'
            r'|https://discord\.gg/)'
            r'(.*?)(/|\Z|\?)',
            body,
        )
        if invite_code:
            if invite_code.group(2):
                return {'code': invite_code.group(2)}
        raise RuntimeError(f'Invite URL {body} is not valid')

    @staticmethod
    def collect_request(
            headers: Entity,
            action: Entity,
            content: RequestData,
    ) -> requests.Request:
        """Accept invite request collector

        :param headers: Headers with scope and Request.headers
        :param action: Action with scope and Request.method, Request.url
        :param content: Invite code of server

        :return: Compiled join server request
        """
        action_data: RequestData = action.get('content', {})
        headers_data: RequestData = headers.get('content', {})

        action_data.update({'url': f"{action_data['url']}/{content['code']}"})

        if (
                not {__class__.__name__}.intersection(
                    headers.get('scope', ()),
                    action.get('scope', ()),
                )
        ):
            raise RuntimeError(f"{__class__.__name__} not in {action['scope']} or {headers['scope']} scope list")

        return requests.Request(headers=headers_data, **action_data)
