import json
import time
import typing
from base64 import b64encode

import requests

from .abstract import AbstractUtilsBase


class ResolveCaptcha(AbstractUtilsBase):
    """Resolve image-bot or discord HCaptcha"""

    def __init__(self, **kwargs: typing.Any):
        """Create resolver

        :param kwargs: Anti-captcha token
        """
        self.token: str = kwargs.get('token', '')
        if not self.token:
            raise RuntimeError(f'Anti-captcha token in {kwargs} is not passed')

    def process(self, **kwargs: typing.Any) -> str:
        """Resolve captcha

        :param kwargs: Captcha key or image url
        """
        body: str = kwargs.get('body', '')
        image: bool = kwargs.get('image', False)
        resolve: typing.Union[int, str]

        if image:
            image_b64 = b64encode(requests.get(body).content).decode('ascii')
            task = requests.post(
                'https://api.anti-captcha.com/createTask',
                data=json.dumps({
                    "clientKey": self.token,
                    "task": {
                        "type": "ImageToTextTask",
                        "body": image_b64
                    }
                })
            ).json()['taskId']
            return self.resolve(task).get('text', 0)
        else:
            task = requests.post(
                'https://api.anti-captcha.com/createTask',
                data=json.dumps({
                    "clientKey": self.token,
                    "task": {
                        "type": "HCaptchaTaskProxyless",
                        "websiteURL": 'https://discord.com/api/v9/auth/login',
                        "websiteKey": body,
                    }
                })
            ).json()['taskId']
            return self.resolve(task).get('gRecaptchaResponse', 0)

    def validate(
            self,
            body: str,
            refer: str = '',
    ) -> str:
        """Validate captcha solution

        :param body: Captcha solution
        :param refer: Reference for solution

        :return: Body on pass otherwise raise Exception
        """
        if not refer:
            assert body != 0
        else:
            assert body == refer
        return body

    def resolve(self, task):
        """Check if captcha task resolved

        :param task: Task ID on anticaptcha
        :return: Solution
        """
        for _ in range(10):
            solution = requests.post(
                'https://api.anti-captcha.com/getTaskResult',
                data=json.dumps({
                    "clientKey": self.token,
                    "taskId": task
                })
            ).json().get('solution')
            if solution:
                return solution
            else:
                time.sleep(5)
        return {'': ''}
