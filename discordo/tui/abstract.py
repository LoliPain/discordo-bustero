from abc import ABC, abstractmethod


class AbstractUIBase(ABC):
    """Terminal UI element"""

    @abstractmethod
    def __init__(self):
        """Create UI element"""

    @abstractmethod
    def get_text(self, user_data: dict) -> str:
        """Format passed data on element

        :param user_data: Context data

        :return: Colorama string
        """
