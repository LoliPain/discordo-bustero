from discordo.store import *


class ConfigStore:
    """Collection of stored params"""

    def __init__(self):
        """Implement new store"""
        self.link = LinkParam()
        self.captcha = CaptchaParam()
        self.user = UsersParam()
        self.dictionary = DictionaryParam()
        self.reaction = ReactionParam()
        self.confirmation = ConfirmationParam()
        self.proxy = ProxyParam()

    def parse_config_values(self, config_data: dict):
        """Parse config file json into store

        :param config_data: Config file data
        """
        self.link.set_data(config_data['link']['value'])
        self.captcha.set_data(config_data['captcha']['value'])
        self.user.set_data(config_data['user']['value'])
        self.dictionary.set_data(config_data['dictionary']['value'])
        self.reaction.set_data(config_data['reaction']['value'])
        self.confirmation.set_data(True if config_data['confirmation']['value'] != '*' else False)
        self.proxy.set_data(config_data['proxy']['value'])

    def get_required(self):
        """Return required params"""
        return self.link, self.user

    def file_based(self):
        """Return params file-linked"""
        return self.user, self.dictionary, self.proxy
