import typing

RequestData = typing.Dict[str, str]
Scope = typing.Tuple[str, ...]
Entity = typing.TypedDict('Entity', {'scope': Scope, 'content': RequestData})
Proxy = typing.Dict[str, str]
