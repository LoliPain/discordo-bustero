import typing
from abc import ABC, abstractmethod

import requests

from ..api_types import Proxy, Scope


class AbstractHttpClient(ABC):
    """HTTP session client

    :var scope: Scope of client methods
    """
    scope: Scope

    @abstractmethod
    def send_request(
            self,
            request: requests.Request,
            **kwargs: typing.Any,
    ) -> int:
        """Send prepared request through instance session
        :param request: Minimal client request
        :param kwargs: Client context params

        :return Response status code
        """

    def __init__(self):
        """Create client session

        :ivar self.proxies: Instance proxy server
        :ivar self.s: Instance session
        """
        self.proxies: Proxy = {}
        self.get_data: str = ""
        self.s = requests.Session()

    def close_client(self):
        self.s.close()

    def update_proxy(self, proxies: typing.Optional[Proxy] = None):
        """Update proxy in following requests, when nothing is passed removes it

        :param proxies: SOCKS/HTTPS proxy server data
        """
        if proxies is None:
            proxies = {}
        self.proxies = proxies
