import re
import typing
from urllib.parse import quote_plus

import requests

from .abstract import AbstractRequestBase
from ..api_types import RequestData, Entity

CUSTOM_EMOJI_PATTERN: str = r"([^.\: ]+:[0-9]+$)"
EMOJI_PATTERN: str = (
    "^(["
    "\U0001F1E0-\U0001F1FF"  # flags (iOS)
    "\U0001F300-\U0001F5FF"  # symbols & pictographs
    "\U0001F600-\U0001F64F"  # emoticons
    "\U0001F680-\U0001F6FF"  # transport & map symbols
    "\U0001F700-\U0001F77F"  # alchemical symbols
    "\U0001F780-\U0001F7FF"  # Geometric Shapes Extended
    "\U0001F800-\U0001F8FF"  # Supplemental Arrows-C
    "\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
    "\U0001FA00-\U0001FA6F"  # Chess Symbols
    "\U0001FA70-\U0001FAFF"  # Symbols and Pictographs Extended-A
    "\U00002702-\U000027B0"  # Dingbats
    "\U000024C2-\U0001F251"
    "]+)"
)


class MinimalReaction(AbstractRequestBase):
    """Minimal Reaction request creator"""

    def __init__(self):
        """Create reaction object

        :ivar self.pattern: Regex pattern for emoji validation
        """
        self.pattern: re.Pattern = re.compile(f'^{CUSTOM_EMOJI_PATTERN}|{EMOJI_PATTERN}$', re.UNICODE)

    def collect_content(
            self,
            body: str = '',
            **kwargs: typing.Any,
    ) -> RequestData:
        """Emoji reaction request converter
        Raises RuntimeError exception at validation fail

        :param body: Plain unvalidated Emoji NAME:ID or Unicode Emoji

        :return: HTTP escaped emoji string
        """
        if self.pattern.match(body):
            return {'emoji': quote_plus(body)}
        else:
            raise RuntimeError(f"Emoji {body} isn't valid emoji pattern. Excepted unicode or NAME:ID")

    def collect_request(
            self,
            headers: Entity,
            action: Entity,
            content: RequestData,
    ) -> requests.Request:
        """PUT Emoji reaction request collector
        Scope comparison fail raises RuntimeError

        :param headers: Headers with scope and Request.headers
        :param action: Action with scope and Request.method, Request.url
        :param content: Parsed emoji data

        :return: Compiled PUT reaction request
        """
        action_data: RequestData = action.get('content', {})
        headers_data: RequestData = headers.get('content', {})

        action_data.update({'url': f"{action_data['url']}/{content['emoji']}/@me"})

        if not {__name__}.intersection(headers.get('scope', ()), action.get('scope', ())):
            raise RuntimeError(f"{__name__} not in {action['scope']} or {headers['scope']} scope list")

        return requests.Request(headers=headers_data, **action_data)
