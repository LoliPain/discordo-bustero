import typing

import requests

from .abstract import AbstractHttpClient

if typing.TYPE_CHECKING:
    __class__: typing.Type


class GetHttpClient(AbstractHttpClient):
    """GET requests HTTP client"""
    scope = ('GET',)

    def send_request(
            self,
            request: requests.Request,
            **kwargs: typing.Any
    ) -> int:
        """GET data from API
        Request method scope validation

        :param request: Minimal client GET request
        :param kwargs: Response context action

        :return Resp status code
        """
        if request.method not in self.scope:
            raise RuntimeError(f'Request method {request.method}'
                               f' not available for {__class__.__name__}.{self.scope},'
                               f' use another HttpClient instead')
        resp: requests.Response = self.s.send(
            request.prepare(),
            proxies=self.proxies,
        )
        if not kwargs.get('no_save', False):
            self.get_data = resp.text

        return resp.status_code
