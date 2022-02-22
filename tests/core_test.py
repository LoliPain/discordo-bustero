import json
import os

import pytest

from discordo.api_client import *


@pytest.mark.requests
@pytest.mark.sensitive
def test_user_workflow():
    """Real work-case of Discordo usage
    Requires to be filled discordo_token in env
    """
    proxy = os.environ.get('discordo_proxy')
    # Create Get and Send (POST, PUT) clients
    get = GetHttpClient()
    send = SendHttpClient()
    # Set proxy from env to clients
    get.update_proxy(proxy)
    send.update_proxy(proxy)
    # Extract discord token from env
    token = os.environ.get('discordo_token')
    # Set up default auth headers with token
    headers = HeadersClient(token).entity
    # Join Discordo-Testing server
    invite = AdvancedAcceptInvite()
    invite.collect_content('https://discord.gg/P25cVbw36Q')
    _ = invite.rebuild_action()
    assert send.send_request(invite.collect_request(headers, _), mode='invite') == 200
    # Receive guild id from join data
    guild_id = json.loads(send.get_data).get('guild')['id']
    # Get server terms of use
    get_agreement = AdvancedGetAgreement()
    get_agreement.collect_content(guild_id)
    _ = get_agreement.rebuild_action()
    assert get.send_request(get_agreement.collect_request(headers, _)) == 200
    # Receive terms from server
    terms = get.get_data
    # Send terms agreement
    send_agreement = AdvancedConfirmAgreement()
    send_agreement.collect_content(terms)
    _ = send_agreement.rebuild_action(guild_id=guild_id)
    assert send.send_request(send_agreement.collect_request(headers, _), mode='agreement') == 410
    # Set :template: reaction on TEMPLATE message in test-reaction
    reaction = MinimalReaction()
    reaction.collect_content('template:945726428434022482')
    _ = ActionClient('https://discord.com/api/v9/channels/945726603818827916/messages/945726632021340210/reactions', 'PUT')
    assert send.send_request(reaction.collect_request(headers, _.entity), mode='reaction') == 204
    # Send TEST message to test-messages
    message = MinimalMessage()
    message.collect_content('TEST')
    _ = ActionClient('https://discord.com/api/v9/channels/945726237115056191/messages', 'POST')
    assert send.send_request(message.collect_request(headers, _.entity), mode='message') == 200
    # Close client
    send.close_client()
    get.close_client()
