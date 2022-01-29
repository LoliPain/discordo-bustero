import typing

from api_client import Content

MESSAGE_JSON: Content = {
    "content": "",
    "nonce": "",
    "tts": "False"
}


def content_to_json(
        message: Content,
        content: str,
        tts: typing.Optional[bool] = False,
        nonce: typing.Optional[int] = 0
) -> Content:
    """JSON collector by template

    :param message: JSON :dict template
    :param content: Plain text :str for message that should be converted to JSON object
    :param tts: Enables :bool Text-To-Speech message
    :param nonce: Unique ID :int for message

    :return: :Content with prepared for sending JSON

    """

    if tts:
        message["tts"] = str(tts).lower()
    if not nonce:
        del message["nonce"]
    else:
        message["nonce"] = str(nonce)
    message["content"] = content

    return message
