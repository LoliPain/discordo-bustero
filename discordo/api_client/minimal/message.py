import typing

import requests

from .abstract import AbstractRequestBase
from ..api_types import RequestData, Entity


class MinimalMessage(AbstractRequestBase):
    """Minimal Message request creator"""

    def __init__(self):
        """Create message object

        :ivar self.message_json: Template message JSON
        """
        self.message_json: dict = {
            "content": "",
            "nonce": "",
            "tts": "False"
        }

    def collect_content(
            self,
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
        tts: bool = kwargs.get('tts', False)
        nonce: int = kwargs.get('nonce', 0)

        self.message_json.update({"content": body})
        self.message_json.update({"tts": str(tts).lower()})
        self.message_json.pop("nonce") if not nonce else self.message_json.update({"nonce": str(nonce)})
        return self.message_json

    def collect_request(
            self,
            headers: Entity,
            action: Entity,
            content: RequestData,
    ) -> requests.Request:
        """Message request content collector
        Scope comparison fail raises RuntimeError

        :param headers: Headers with scope and Request.headers
        :param action: Action with scope and Request.method, Request.url
        :param content: Request.data with prepared for sending JSON

        :return: Compiled message request
        """
        action_data: RequestData = action.get('content', {})
        headers_data: RequestData = headers.get('content', {})

        if not {__name__}.intersection(headers.get('scope', ()), action.get('scope', ())):
            raise RuntimeError(f"{__name__} not in {action['scope']} or {headers['scope']} scope list")

        return requests.Request(headers=headers_data, data=content, **action_data)
