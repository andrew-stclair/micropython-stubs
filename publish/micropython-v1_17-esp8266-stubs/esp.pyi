from typing import Any

SLEEP_LIGHT: int
SLEEP_MODEM: int
SLEEP_NONE: int

def apa102_write(*args, **kwargs) -> Any: ...
def check_fw(*args, **kwargs) -> Any: ...
def deepsleep(*args, **kwargs) -> Any: ...
def dht_readinto(*args, **kwargs) -> Any: ...
def esf_free_bufs(*args, **kwargs) -> Any: ...
def flash_erase(*args, **kwargs) -> Any: ...
def flash_id(*args, **kwargs) -> Any: ...
def flash_read(*args, **kwargs) -> Any: ...
def flash_size(*args, **kwargs) -> Any: ...
def flash_user_start(*args, **kwargs) -> Any: ...
def flash_write(*args, **kwargs) -> Any: ...
def free(*args, **kwargs) -> Any: ...
def freemem(*args, **kwargs) -> Any: ...
def info(*args, **kwargs) -> Any: ...
def malloc(*args, **kwargs) -> Any: ...
def meminfo(*args, **kwargs) -> Any: ...
def osdebug(*args, **kwargs) -> Any: ...
def set_native_code_location(*args, **kwargs) -> Any: ...
def sleep_type(*args, **kwargs) -> Any: ...
