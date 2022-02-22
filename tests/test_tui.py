import pytest

from discordo.tui import *
from discordo.service import CONFIG_PRESET


@pytest.fixture
def user_data():
    """Implement default config"""
    return CONFIG_PRESET


@pytest.mark.tui
def test_param(user_data):
    """Creating single UI param from config"""
    param = ParamUIElement()
    assert param.get_text(user_data['link'])


@pytest.mark.tui
def test_screen(user_data):
    """Creating screen UI from config"""
    screen = TerminalUIScreen()
    assert screen.get_text(user_data)
