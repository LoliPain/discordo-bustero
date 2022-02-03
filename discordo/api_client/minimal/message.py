import typing

import requests

from .abstract import AbstractRequestBase
from ..api_types import RequestData, Entity

if typing.TYPE_CHECKING:
    __class__: typing.Type


class MinimalMessage(AbstractRequestBase):
    """Minimal Message request creator"""

    @staticmethod
    def collect_content(
            body: str = '',
            **kwargs: typing.Any,
    ) -> RequestData:
        """Message request content collector

        :param body: Plain text for message that should be converted to JSON object
        :param kwargs: Contains tts and nonce

        :var tts: Enables Text-To-Speech for message
        :var nonce: Unique message ID

        :return: Prepared for sending JSON
        """
        message_json: dict = {
            "content": "",
            "nonce": "",
            "tts": "False"
        }

        tts: bool = kwargs.get('tts', False)
        nonce: int = kwargs.get('nonce', 0)

        message_json.update({"content": body})
        message_json.update({"tts": str(tts).lower()})
        message_json.pop("nonce") if not nonce else message_json.update({"nonce": str(nonce)})
        return message_json

    @staticmethod
    def collect_request(
            headers: Entity,
            action: Entity,
            content: RequestData,
    ) -> requests.Request:
        """Message request content collector
        Request objects scope validation

        :param headers: Headers with scope and Request.headers
        :param action: Action with scope and Request.method, Request.url
        :param content: Request.data with prepared for sending JSON

        :return: Compiled message request
        """
        action_data: RequestData = action.get('content', {})
        headers_data: RequestData = headers.get('content', {})

        if (
                not {__class__.__name__}.intersection(
                    headers.get('scope', ()),
                    action.get('scope', ()),
                )
        ):
            raise RuntimeError(f"{__class__.__name__} not in {action['scope']} or {headers['scope']} scope list")

        return requests.Request(headers=headers_data, data=content, **action_data)
