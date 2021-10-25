from typing import Any

class OneWire:
    MATCH_ROM: int
    SEARCH_ROM: int
    SKIP_ROM: int
    def _search_rom() -> None: ...
    def crc8() -> None: ...
    def readbit() -> None: ...
    def readbyte() -> None: ...
    def readinto() -> None: ...
    def reset() -> None: ...
    def scan() -> None: ...
    def select_rom() -> None: ...
    def write() -> None: ...
    def writebit() -> None: ...
    def writebyte() -> None: ...

class OneWireError: ...

_ow: Any

def const() -> None: ...
