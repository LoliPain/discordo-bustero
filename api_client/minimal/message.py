import requests
import typing

from api_client import AbstractRequestBase, Content, Entity


class MinimalMessage(AbstractRequestBase):
    """Minimal Message request creator"""
    def __init__(self):
        """Create message object

        :ivar message_json: Template message JSON :dict for request data
        """
        self.message_json: dict = {
            "content": "",
            "nonce": "",
            "tts": "False"
        }

    def collect_content(
            self,
            message_body: typing.Optional[str] = '',
            reaction: typing.Optional[str] = '',
            tts: typing.Optional[bool] = False,
            nonce: typing.Optional[int] = 0,
    ) -> Content:
        """Message request content collector

        :param message_body: Plain text :str for message that should be converted to JSON object
        :param reaction: (Unused)
        :param tts: Enables :bool Text-To-Speech message
        :param nonce: Unique ID :int for message

        :return: :Content with prepared for sending JSON
        """
        self.message_json.update({"content": message_body})
        self.message_json.update({"tts": str(tts).lower()})
        self.message_json.pop("nonce") if not nonce else self.message_json.update({"nonce": str(nonce)})
        return self.message_json

    def collect_request(
            self,
            headers: Entity,
            action: Entity,
            content: Content,
    ) -> requests.Request:
        """Message request content collector
        Scope comparison fail raises RuntimeError

        :param headers: Headers :Entity with scope :tuple and Request.headers :dict
        :param action: Action :Entity with scope :tuple and :dict Request.method, Request.url
        :param content: Request.data :Content with prepared for sending JSON :dict

        :return: Compiled message request :requests.Request
        """
        if {__name__}.intersection(headers.get('scope', ()), action.get('scope', ())):
            return requests.Request(headers=headers.get('content', ()), data=content, **action.get('content', ()))
        else:
            raise RuntimeError(f"{__name__} not in {action['scope']} or {headers['scope']}  scope list")
