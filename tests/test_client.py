import json

import pytest
import requests

from discordo.api_client import *


@pytest.mark.object
def test_action_url_method():
    """Create example POST request Action"""
    action_entity = ActionClient('URL', method='POST').entity
    assert action_entity.get('content') == {'method': 'POST', 'url': 'URL'}


@pytest.mark.objects
def test_headers_token():
    """Create example Headers"""
    headers_entity = HeadersClient('TOKEN', 'UA').entity
    assert headers_entity.get('content') == {'authorization': 'TOKEN', 'user-agent': 'UA'}


@pytest.mark.requests
def request_entities(token, ua, url, method):
    """Create example Headers-Action pair """
    return HeadersClient(token, ua).entity, ActionClient(url, method).entity


@pytest.mark.requests
def test_message_request(
        token='TOKEN',
        ua='UA',
        url='URL',
        method='POST',
):
    """Build example of message send request"""
    ref_request = requests.Request(
        headers={
            'authorization': token,
            'user-agent': ua,
            'Content-type': 'application/json',
        },
        method=method,
        url=url,
        data='{"content": "Content", "nonce": "1", "tts": "true"}'
    )
    message = MinimalMessage()
    headers, action = request_entities(token, ua, url, method)
    message.collect_content('Content', tts=True, nonce=1)
    request = message.collect_request(headers, action)
    assert request.__dict__ == ref_request.__dict__


@pytest.mark.requests
def test_reaction_fail_content():
    """Invalid emoji pattern exception"""
    with pytest.raises(RuntimeError):
        MinimalReaction().collect_content('mismatch pattern')


@pytest.mark.requests
@pytest.mark.parametrize("emoji, escaped_emoji", [('match:123', 'match%3A123'), ('😀', '%F0%9F%98%80')])
def test_reaction_content(emoji, escaped_emoji):
    """Valid emoji patterns"""
    assert MinimalReaction().collect_content(emoji)['emoji'] == escaped_emoji


@pytest.mark.requests
def test_reaction_emoji(
        token='TOKEN',
        ua='UA',
        url='URL',
        method='PUT',
):
    """Build example of message reaction request"""
    ref_request = requests.Request(
        headers={
            'authorization': token,
            'user-agent': ua,
        },
        method=method,
        url=f'{url}/emoji%3A1/@me',
    )
    reaction = MinimalReaction()
    headers, action = request_entities(token, ua, url, method)
    reaction.collect_content('emoji:1')
    request = reaction.collect_request(headers, action)
    assert request.__dict__ == ref_request.__dict__


@pytest.mark.requests
def test_invite_fail_content():
    """Invalid invite URL pattern"""
    with pytest.raises(RuntimeError):
        AdvancedAcceptInvite().collect_content('mismatch pattern')


@pytest.mark.requests
@pytest.mark.parametrize(
    "invite_link, invite_code",
    [
        ('https://discord.gg/INVITE', 'INVITE'),
        ('https://discord.com/invite/CODE', 'CODE')
    ])
def test_invite_content(invite_link, invite_code):
    """Valid invite URL patterns"""
    assert AdvancedAcceptInvite().collect_content(invite_link)['code'] == invite_code


@pytest.mark.requests
def test_invite(
        token='TOKEN',
        ua='UA',
        url='URL',
        method='POST',
):
    """Build example of accept invite request"""
    ref_request = requests.Request(
        headers={
            'authorization': token,
            'user-agent': ua,
        },
        method=method,
        url=f'{url}/INVITE',
    )
    invite = AdvancedAcceptInvite()
    headers, action = request_entities(token, ua, url, method)
    invite.collect_content('https://discord.gg/INVITE')
    request = invite.collect_request(headers, action)
    assert request.__dict__ == ref_request.__dict__


@pytest.mark.requests
def agreement():
    """Example of terms"""
    return """{
        "version": "2021-11-08T12:21:16.941000+00:00",
        "form_fields": [{
            "field_type": "TERMS",
            "label": "Read and agree to the server rules",
            "description": null,
            "automations": null,
            "required": true,
            "values": [""]
        }],
        "description": "desk"
    }"""


@pytest.mark.requests
def test_send_agreement(
        token='TOKEN',
        ua='UA',
        url='URL',
        method='POST',
):
    """Build example of confirming agreement request"""
    ref_data = json.loads(agreement())
    del ref_data['description']
    ref_data['form_fields'][0]['response'] = "true"
    ref_data = json.dumps(ref_data)
    ref_request = requests.Request(
        headers={
            'authorization': token,
            'user-agent': ua,
            'Content-type': 'application/json',
        },
        method=method,
        url=url,
        data=ref_data,
    )
    send_agreement = AdvancedConfirmAgreement()
    headers, action = request_entities(token, ua, url, method)
    send_agreement.collect_content(agreement())
    request = send_agreement.collect_request(headers, action)
    assert request.__dict__ == ref_request.__dict__


@pytest.mark.requests
def test_get_agreement(
        token='TOKEN',
        ua='UA',
        url='URL',
        method='POST',
):
    """Build example of get server terms request"""
    ref_request = requests.Request(
        headers={
            'authorization': token,
            'user-agent': ua,
        },
        method=method,
        url=f'{url}/1/member-verification',
    )
    get_agreement = AdvancedGetAgreement()
    headers, action = request_entities(token, ua, url, method)
    get_agreement.collect_content(1)
    request = get_agreement.collect_request(headers, action)
    assert request.__dict__ == ref_request.__dict__


