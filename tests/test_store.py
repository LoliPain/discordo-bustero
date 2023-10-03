import pytest

from discordo.store import *


@pytest.mark.store
def test_link():
    """Test storing of link param"""
    link = LinkParam()
    link.set_data('link')
    assert link.collect['link'] == 'link'


@pytest.mark.store
@pytest.mark.parametrize("user", ['users.txt', ['user1', 'user2']])
@pytest.mark.parametrize("mixed", [True, False])
def test_users(user, mixed):
    """Test users both str and list params"""
    users = UsersParam()
    users.set_data(user, mixed=mixed)
    assert users.collect == {'file': user, 'mixed': mixed}


@pytest.mark.store
def test_captcha():
    """Test storing of captcha token param"""
    captcha = CaptchaParam()
    captcha.set_data('captcha')
    assert captcha.collect['token'] == 'captcha'


@pytest.mark.store
def test_confirmation():
    """Test storing of confirmation checkbox param"""
    confirmation = ConfirmationParam()
    confirmation.set_data(True)
    assert confirmation.collect['confirmation'] is True


@pytest.mark.store
@pytest.mark.parametrize("dictionary", ['dict.txt', ['hello', 'hi']])
@pytest.mark.parametrize("channel_id", ['1', '2'])
def test_dict(dictionary, channel_id):
    """Test dictionary both str and list params"""
    dicts = DictionaryParam()
    dicts.set_data(dictionary, channel=channel_id)
    assert dicts.collect == {'file': dictionary, 'channel': channel_id}


@pytest.mark.store
def test_proxy():
    """Test storing of proxy file name param"""
    proxy = ProxyParam()
    proxy.set_data('proxy')
    assert proxy.collect['file'] == 'proxy'


@pytest.mark.store
def test_reaction():
    """Text storing of reaction params"""
    reaction = ReactionParam()
    reaction.set_data('reaction', message='id')
    assert reaction.collect == {'emoji': 'reaction', 'message': 'id'}



