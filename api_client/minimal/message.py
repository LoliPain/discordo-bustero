import requests
import typing

from api_client import AbstractRequestBase, Content, Entity
from .message_json import content_to_json, MESSAGE_JSON


class MinimalMessage(AbstractRequestBase):
    """Minimal Message request creator"""
    def collect_content(
            self,
            message_body: typing.Optional[str] = '',
            reaction: typing.Optional[str] = ''
    ) -> Content:
        """Message request content collector

        :param message_body: Plain text :str for message that should be converted to JSON object
        :param reaction: (Unused)

        :return: :Content with prepared for sending JSON
        """
        return content_to_json(MESSAGE_JSON, message_body)

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
        if (
                __name__ in action.get('scope', ()) and
                __name__ in headers.get('scope', ())
        ):
            return requests.Request(headers=headers.get('content', ()), data=content, **action.get('content', ()))
        else:
            raise RuntimeError(f"{__name__} not in {action['scope']} or {headers['scope']}  scope list")
