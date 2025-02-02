"""
Module: 'uasyncio.core' on micropython-v1.18-rp2
"""
# MCU: {'family': 'micropython', 'sysname': 'rp2', 'version': '1.18.0', 'build': '', 'mpy': 5637, 'port': 'rp2', 'platform': 'rp2', 'name': 'micropython', 'arch': 'armv7m', 'machine': 'Arduino Nano RP2040 Connect with RP2040', 'nodename': 'rp2', 'ver': 'v1.18', 'release': '1.18.0'}
# Stubber: 1.5.3
from typing import Any


class CancelledError(Exception):
    ''

class Task():
    ''
    def __init__(self, *argv, **kwargs) -> None:
        ''
        ...

class TaskQueue():
    ''
    def __init__(self, *argv, **kwargs) -> None:
        ''
        ...
    def remove(self, *args, **kwargs) -> Any:
        ...

    def peek(self, *args, **kwargs) -> Any:
        ...

    def pop_head(self, *args, **kwargs) -> Any:
        ...

    def push_head(self, *args, **kwargs) -> Any:
        ...

    def push_sorted(self, *args, **kwargs) -> Any:
        ...

def sleep(*args, **kwargs) -> Any:
    ...

def sleep_ms(*args, **kwargs) -> Any:
    ...

def ticks_add(*args, **kwargs) -> Any:
    ...

def ticks_diff(*args, **kwargs) -> Any:
    ...

def ticks(*args, **kwargs) -> Any:
    ...


class TimeoutError(Exception):
    ''

class SingletonGenerator():
    ''
    def __init__(self, *argv, **kwargs) -> None:
        ''
        ...

class IOQueue():
    ''
    def __init__(self, *argv, **kwargs) -> None:
        ''
        ...
    def remove(self, *args, **kwargs) -> Any:
        ...

    def queue_read(self, *args, **kwargs) -> Any:
        ...

    def queue_write(self, *args, **kwargs) -> Any:
        ...

    def wait_io_event(self, *args, **kwargs) -> Any:
        ...

def create_task(*args, **kwargs) -> Any:
    ...

def run_until_complete(*args, **kwargs) -> Any:
    ...

def run(*args, **kwargs) -> Any:
    ...


class Loop():
    ''
    def __init__(self, *argv, **kwargs) -> None:
        ''
        ...
    def close(self, *args, **kwargs) -> Any:
        ...

    def stop(self, *args, **kwargs) -> Any:
        ...

    def create_task(self, *args, **kwargs) -> Any:
        ...

    def run_until_complete(self, *args, **kwargs) -> Any:
        ...

    def call_exception_handler(self, *args, **kwargs) -> Any:
        ...

    def run_forever(self, *args, **kwargs) -> Any:
        ...

    def set_exception_handler(self, *args, **kwargs) -> Any:
        ...

    def get_exception_handler(self, *args, **kwargs) -> Any:
        ...

    def default_exception_handler(self, *args, **kwargs) -> Any:
        ...

def get_event_loop(*args, **kwargs) -> Any:
    ...

def current_task(*args, **kwargs) -> Any:
    ...

def new_event_loop(*args, **kwargs) -> Any:
    ...

