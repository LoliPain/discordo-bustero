import json
import typing

import requests

from .abstract import AbstractUtilsBase
from .captcha import ResolveCaptcha
from ..api_client import HeadersClient, SendHttpClient
from ..api_client.api_types import Proxy
from ..api_client.http_client import GetHttpClient


class TokenExtraction(AbstractUtilsBase):
    """Get discord token from log:pass"""

    def __init__(self, **kwargs: typing.Any):
        """Create extractor instance

        :param kwargs: Proxy and Anti-Captcha login data
        """
        self.proxies: Proxy = kwargs.get('proxies', {})
        self.captcha: str = kwargs.get('captcha', '')

    def process(self, **kwargs: typing.Any) -> str:
        """Reveal token from log:pass

        :param kwargs: Input account login and password

        :return: Auth account token
        """
        login: str = kwargs.get('login', '')
        password: str = kwargs.get('password', '')

        login_request = requests.Request(
            method='POST',
            url='https://discord.com/api/v9/auth/login',
            headers={'user-agent': HeadersClient.user_agent, 'Content-type': 'application/json'},
            data=json.dumps({
                "login": login,
                "password": password,
                "undelete": False,
                "captcha_key": None,
                "login_source": None,
                "gift_code_sku_id": None
            })
        )
        _ = SendHttpClient()
        _.update_proxy(self.proxies)
        if _.send_request(login_request, mode='login') == 400:
            site_key = json.loads(_.get_data).get('captcha_sitekey')
            if site_key:
                resolver = ResolveCaptcha(token=self.captcha)
                captcha_key = resolver.validate(resolver.process(body=site_key))
                login_request.data = json.loads(login_request.data)
                login_request.data['captcha_key'] = captcha_key
                login_request.data = json.dumps(login_request.data)
            else:
                return ''
        else:
            return json.loads(_.get_data).get('token', '')
        _.send_request(login_request, mode='login')
        return json.loads(_.get_data).get('token', '')

    def validate(
            self,
            body: str,
            refer: str = '',
    ) -> str:
        """Make a request with passed token

        :param body: Extracted token
        :param refer: Example of successful response

        :return: True, otherwise raise Exception
        """
        validate_request = requests.Request(
            method='GET',
            url='https://discord.com/api/v9/users/@me/activities/statistics/applications',
            headers={'user-agent': HeadersClient.user_agent, 'authorization': body},
        )
        _ = GetHttpClient()
        _.update_proxy(self.proxies)
        if not refer:
            assert _.send_request(validate_request, no_save=True) == 200
        else:
            _.send_request(validate_request)
            assert _.get_data == refer
        _.close_client()
        return body
