import typing

RequestData = typing.Dict[str, str]
Scope = typing.Tuple[str, str]
Entity = typing.TypedDict('Entity', {'scope': Scope, 'content': RequestData})
