import typing

import requests

from .abstract import AbstractHttpClient

if typing.TYPE_CHECKING:
    __class__: typing.Type


class RequestStrict:
    """Validate request context and request params

    :var mode_list: Links from context to strict
    """
    mode_list = {
        'reaction': ('PUT',),
        'message': ('POST', 'DATA'),
        'agreement': ('PUT', 'DATA'),
        'invite': ('POST',),
        'login': ('POST', 'DATA'),
    }

    @staticmethod
    def mode_presence(mode: str):
        """Compare passed mode to actual modes

        :param mode: Request context
        """
        if mode not in list(RequestStrict.mode_list.keys()):
            raise RuntimeError(f'Passed mode {mode} not in'
                               f' {RequestStrict.mode_list.keys()}')

    @staticmethod
    def mode_validation(request: requests.Request, mode: str):
        """Validate strict of passed request by context

        :param request: Passed collected request
        :param mode: Request context
        """
        strict = RequestStrict.mode_list[mode]

        assert request.method == strict[0]

        if ('DATA' in strict) == bool(request.data):
            pass
        else:
            raise AssertionError


class SendHttpClient(AbstractHttpClient):
    """POST/PUT requests HTTP client"""
    scope = ('POST', 'PUT')

    def send_request(
            self,
            request: requests.Request,
            **kwargs: typing.Any
    ) -> int:
        """Send data to API
        Request method scope validation
        Request context validation

        :param request: Minimal client POST/PUT request
        :param kwargs: Request context action

        :return Resp status code
        """
        if request.method not in self.scope:
            raise RuntimeError(f'Request method {request.method}'
                               f' not available for {__class__.__name__}.{self.scope},'
                               f' use another HttpClient instead')

        _mode: str = kwargs.get('mode', '')
        RequestStrict.mode_presence(_mode)
        RequestStrict.mode_validation(request, _mode)

        resp: requests.Response = self.s.send(
            request.prepare(),
            proxies=self.proxies,
        )
        if not kwargs.get('no_save', False):
            self.get_data = resp.text

        return resp.status_code
