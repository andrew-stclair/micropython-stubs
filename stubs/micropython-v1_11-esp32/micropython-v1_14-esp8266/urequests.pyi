from typing import Any

def get(*args) -> Any: ...
def put(*args) -> Any: ...
def head(*args) -> Any: ...

class Response:
    def __init__(self, *args) -> None: ...
    def close(self, *args) -> Any: ...
    text: Any
    def json(self, *args) -> Any: ...
    content: Any

def request(*args) -> Any: ...
def post(*args) -> Any: ...
def patch(*args) -> Any: ...
def delete(*args) -> Any: ...
