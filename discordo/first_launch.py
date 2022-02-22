from discordo import ConfigIO, Screen
from discordo import TerminalUIScreen, ParamUIElement

c = ConfigIO()
s = Screen()
ps = TerminalUIScreen()


def select_param(user_data: dict, param: str):
    """Add selected value to param

    :param user_data: All params
    :param param: Specified param
    """
    user_data[param]['selected'] = True
    s.show(ps.get_text(user_data))


def unselect_param(user_data: dict, param: str):
    """Remove selected value to param

    :param user_data: All params
    :param param: Specified param
    """
    del user_data[param]['selected']
    s.show(ps.get_text(user_data))


def edit_param(user_data: dict, param: str) -> dict:
    """Edit with selection specified param in dict

    :param user_data: All params
    :param param: Specified param

    :return: All params modified
    """
    select_param(user_data, param)
    s.append(f'\n\nDo you want to use default param?'
             f'\n* equals leaving empty value')
    if not s.agreement():
        user_data[param]['value'] = input(f'\nNow specify the {param} value: ')
    unselect_param(user_data, param)
    return user_data


def create_config() -> str:
    """Create new config

    :return: Config file name
    """
    s.show(f'Is it good to call config file {c.config}?')
    if not s.agreement():
        c.config = input('Okay, call it whatever you want: ')
        s.append(f'Now the config name is {c.config}')
        s.skip()
    c.create()
    return c.config


def initial_setup() -> dict:
    """Fill all params

    :return: Filled params
    """
    s.show('Now you need to specify some Discordo settings there:')
    user_data = c.read()
    s.append(ps.get_text(user_data))
    s.skip()
    user_data = edit_param(user_data, 'link')
    user_data = edit_param(user_data, 'captcha')
    user_data = edit_param(user_data, 'user')
    user_data = edit_param(user_data, 'dictionary')
    if user_data['dictionary']['value'] != '*':
        user_data = edit_param(user_data, 'channel_id')
    user_data = edit_param(user_data, 'reaction')
    if user_data['reaction']['value'] != '*':
        user_data = edit_param(user_data, 'message_id')
    user_data = edit_param(user_data, 'confirmation')
    user_data = edit_param(user_data, 'proxy')
    return user_data


def pass_check(config: str, user_data: dict) -> bool:
    """User verify all params value

    :param config: Config name
    :param user_data: All params

    :return: Verify bool
    """
    s.show(ps.get_text(user_data))
    p = ParamUIElement().get_text({'param': 'Config name', 'value': config})
    s.append(p)
    s.append('\n\nIs everything right?')
    return s.agreement()


def first_launch():
    """Initial launch of Discordo

    :return: All configured params
    """
    s.clear()
    s.append("Discordo running for first time?")
    s.append("Let's create and fill up new config file!")
    s.skip()
    config = create_config()
    user_data = initial_setup()
    if pass_check(config, user_data):
        c.write(user_data)
        return user_data
    else:
        raise RuntimeError('Aborted by user')
