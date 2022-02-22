import argparse
import logging
import os.path
import typing

from discordo import ConfigIO, Screen
from discordo import ConfigStore
from discordo import LOGGER_FORMAT
from discordo import TerminalUIScreen
from first_launch import first_launch

s = Screen()
store = ConfigStore()
ps = TerminalUIScreen()


def collect_args() -> argparse.Namespace:
    """Collect passed to main.py arguments

    :return: Collected cmd arguments
    """
    args_parser = argparse.ArgumentParser()
    args_parser.add_argument(
        '--fresh',
        action='store_true',
        default=False,
        help='Force fresh launch (config file will be saved)',
    )
    args_parser.add_argument(
        '--log',
        action='store_true',
        default=False,
        help='Enable output log',
    )
    args_parser.add_argument(
        '-config',
        default=None,
        help='Specify custom config name',
    )
    return args_parser.parse_args()


def rebuild_file_store():
    """Rebuild file store params from file-name to file-content"""
    mixed_users: bool = False
    with open(store.user.file) as users_file:
        users_list: list = users_file.read().splitlines()
        for user in users_list:
            if ':' in user:
                logging.debug(f'Found log:pass {user}, mixed enabled')
                mixed_users = True
        store.user.set_data(users_list, mixed=mixed_users)
        logging.debug(f'Users {users_list} loaded into store')
    if store.dictionary.file != '*':
        if store.dictionary.channel == '*':
            raise RuntimeError(f'{store.dictionary.collect} is passed without channel id')
        with open(store.dictionary.file) as dict_file:
            dict_list: list = dict_file.read().splitlines()
            store.dictionary.set_data(dict_list, channel=store.dictionary.channel)
            logging.debug(f'Words {dict_list} loaded into store')
    if store.proxy.file != '*':
        with open(store.proxy.file) as proxy_file:
            proxy_list: list = proxy_file.read().splitlines()
            store.proxy.set_data(proxy_list)
            logging.debug(f'Proxy {proxy_list} loaded into store')


def initial_store(_config_data: dict):
    """Parse additional config data into store

    :param _config_data: JSON config data
    """
    store.parse_config_values(_config_data)
    logging.debug(f'Basic config data parsed into store {store}')
    if _config_data['dictionary']['value'] != '*':
        store.dictionary.set_data(store.dictionary.file, channel=_config_data['channel_id']['value'])
        logging.debug(f'{_config_data["channel_id"]} appended to {store.dictionary.collect}')
    if _config_data['reaction']['value'] != '*':
        if _config_data['message_id']['value'] != '*':
            store.reaction.set_data(store.reaction.emoji, message=_config_data['message_id']['value'])
            logging.debug(f'{_config_data["message_id"]} appended to {store.reaction.collect}')
        else:
            raise RuntimeError(f'{store.reaction.collect} passed without message_id')
    for param in store.get_required():
        if '*' in list(param.collect.values()):
            raise RuntimeError(f'{param.collect} is required')
    for file_param in store.file_based():
        if file_param.file != '*':
            if not os.path.isfile(file_param.file):
                raise RuntimeError(f'{file_param.collect} not found')


def initial(
        config: typing.Optional[str] = None,
        fresh: bool = False,
        log: bool = False,
) -> dict:
    """Load config data

    :param config: Custom config file
    :param fresh: Ignore existing config file
    :param log: Logging state

    :return: Loaded config file
    """
    if not fresh:
        c = ConfigIO()
        c.config = config or c.config
        try:
            return c.read()
        except FileNotFoundError:
            if log:
                logging.warning(f'File {c.config} not found, proceed to fresh launch')
                s.skip()
    return first_launch()


if __name__ == '__main__':
    args = collect_args()  # Collect startup arguments
    if args.log:
        logging.basicConfig(format=LOGGER_FORMAT, level=10)  # Enable custom logging format
    else:
        logging.basicConfig(level=100)  # Nothing goes to log
    logging.debug(f'Args {args.__dict__} collected')
    config_data = initial(
        args.config,
        args.fresh,
        args.log,
    )
    logging.debug(f'Config data collected, proceed to store parsing')
    initial_store(config_data)
    logging.debug(f'Store collected, proceed to rebuilding')
    rebuild_file_store()
    logging.debug(f'Store rebuild with files')
