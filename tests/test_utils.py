import os

import pytest

from discordo.utils import *


@pytest.fixture
def captcha():
    """Get anti-captcha token from env"""
    return os.environ.get('discordo_captcha')


@pytest.mark.captcha
def test_invalid_token():
    """Captcha resolver requires token"""
    with pytest.raises(RuntimeError):
        ResolveCaptcha()


@pytest.mark.captcha
@pytest.mark.sensitive
def test_image_captcha(captcha):
    """Resolve 'smwm' captcha"""
    resolver = ResolveCaptcha(token=captcha)
    resolve = resolver.process(body='https://lolipa.in/img/discordo/captcha.png', image=True)
    assert resolver.validate(resolve, 'smwm')


@pytest.mark.token
@pytest.mark.sensitive
def test_token_extraction():
    """Extract token from env log:pass"""
    proxy = os.environ.get('discordo_proxy')
    log = os.environ.get('discordo_log')
    passwd = os.environ.get('discordo_passwd')
    extractor = TokenExtraction(proxies=proxy, captcha=captcha)
    token = extractor.process(login=log, password=passwd)
    assert extractor.validate(token)
