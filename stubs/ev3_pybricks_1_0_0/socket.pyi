from typing import Any

AF_INET: int
AF_INET6: int
AF_UNIX: int
INADDR_ANY: int
IPPROTO_IP: int
IP_ADD_MEMBERSHIP: int
IP_DROP_MEMBERSHIP: int
MSG_DONTROUTE: int
MSG_DONTWAIT: int
SOCK_DGRAM: int
SOCK_RAW: int
SOCK_STREAM: int
SOL_SOCKET: int
SO_BROADCAST: int
SO_ERROR: int
SO_KEEPALIVE: int
SO_LINGER: int
SO_REUSEADDR: int
_GLOBAL_DEFAULT_TIMEOUT: int

def _resolve_addr() -> None: ...

_socket: Any

def create_connection() -> None: ...

class error: ...

def getaddrinfo() -> None: ...
def inet_aton() -> None: ...
def inet_ntop() -> None: ...
def inet_pton() -> None: ...
def sockaddr() -> None: ...

class socket:
    accept: Any
    bind: Any
    def close() -> None: ...
    connect: Any
    def fileno() -> None: ...
    def listen() -> None: ...
    def makefile() -> None: ...
    def read() -> None: ...
    def readinto() -> None: ...
    def readline() -> None: ...
    def recv() -> None: ...
    def recvfrom() -> None: ...
    def send() -> None: ...
    def sendall() -> None: ...
    sendto: Any
    def setblocking() -> None: ...
    def setsockopt() -> None: ...
    def write() -> None: ...
