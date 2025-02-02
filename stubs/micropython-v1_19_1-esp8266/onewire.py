"""
Module: 'onewire' on micropython-v1.19.1-esp8266
"""
# MCU: {'ver': 'v1.19.1', 'build': '', 'platform': 'esp8266', 'port': 'esp8266', 'machine': 'ESP module (1M) with ESP8266', 'release': '1.19.1', 'nodename': 'esp8266', 'name': 'micropython', 'family': 'micropython', 'sysname': 'esp8266', 'version': '1.19.1'}
# Stubber: 1.5.6
from typing import Any


class OneWireError(Exception):
    """"""


class OneWire:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...

    def readinto(self, *args, **kwargs) -> Any:
        ...

    def write(self, *args, **kwargs) -> Any:
        ...

    def crc8(self, *args, **kwargs) -> Any:
        ...

    def readbit(self, *args, **kwargs) -> Any:
        ...

    def readbyte(self, *args, **kwargs) -> Any:
        ...

    def reset(self, *args, **kwargs) -> Any:
        ...

    def scan(self, *args, **kwargs) -> Any:
        ...

    def writebit(self, *args, **kwargs) -> Any:
        ...

    def writebyte(self, *args, **kwargs) -> Any:
        ...

    def select_rom(self, *args, **kwargs) -> Any:
        ...

    MATCH_ROM = 85  # type: int
    SEARCH_ROM = 240  # type: int
    SKIP_ROM = 204  # type: int
