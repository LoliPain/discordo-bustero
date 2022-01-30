import re
import typing
from urllib.parse import quote_plus

import requests

from .abstract import AbstractRequestBase
from ..api_types import Content, Entity

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

        :ivar self.pattern: Regex pattern for string validation :re.Pattern
        """
        self.pattern: re.Pattern = re.compile(f'^{CUSTOM_EMOJI_PATTERN}|{EMOJI_PATTERN}$', re.UNICODE)

    def collect_content(
            self,
            body: typing.Optional[str] = '',
            **kwargs: typing.Any,
    ) -> Content:
        """Emoji reaction request converter
        Raises RuntimeError exception at validation fail

        :param body: Plain unvalidated Emoji ID :str NAME:ID or Unicode Emoji :str

        :return: HTTP escaped emoji string :Content
        """
        if self.pattern.match(body):
            return quote_plus(body)
        else:
            raise RuntimeError(f"Emoji {body} isn't valid emoji pattern. Excepted unicode or NAME:ID")

    def collect_request(
            self,
            headers: Entity,
            action: Entity,
            content: Content,
    ) -> requests.Request:
        """PUT Emoji reaction request collector
        Scope comparison fail raises RuntimeError

        :param headers: Headers :Entity with scope :tuple and Request.headers :dict
        :param action: Action :Entity with scope :tuple and :dict Request.method, Request.url to be modified
        :param content: Request.data :Content with parsed emoji data

        :return: Compiled PUT reaction request :request.Request
        """
        action['content'].update({'url': f"{action['content']['url']}/{content}/@me"})
        if {__name__}.intersection(headers.get('scope', ()), action.get('scope', ())):
            return requests.Request(headers=headers.get('content', ()), **action.get('content', ()))
        else:
            raise RuntimeError(f"{__name__} not in {action['scope']} or {headers['scope']}  scope list")
