from typing import Any

listen_s: Any
client_s: Any
DEBUG: int
_DEFAULT_STATIC_HOST: Any
static_host = _DEFAULT_STATIC_HOST

def server_handshake(cl): ...
def send_html(cl) -> None: ...
def setup_conn(port, accept_handler): ...
def accept_conn(listen_sock): ...
def stop() -> None: ...
def start(port: int = ..., password: Any | None = ..., accept_handler=...) -> None: ...
def start_foreground(port: int = ..., password: Any | None = ...) -> None: ...
