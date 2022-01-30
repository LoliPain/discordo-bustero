import typing

Content = typing.Union[typing.Dict[str, str], str]
Entity = typing.Dict[str, typing.Union[tuple, Content]]
