from typing import Any

class Ev3devSensor:
    def _close_files() -> None: ...
    _default_mode: Any
    _ev3dev_driver_name: str
    def _mode() -> None: ...
    _number_of_values: int
    def _open_files() -> None: ...
    def _value() -> None: ...

class Ev3devUartSensor:
    def _close_files() -> None: ...
    _default_mode: Any
    _ev3dev_driver_name: str
    def _mode() -> None: ...
    _number_of_values: int
    def _open_files() -> None: ...
    def _reset() -> None: ...
    def _reset_port() -> None: ...
    def _value() -> None: ...

class StopWatch:
    def pause() -> None: ...
    def reset() -> None: ...
    def resume() -> None: ...
    def time() -> None: ...

def get_sensor_path() -> None: ...
def listdir() -> None: ...

path: Any

def read_int() -> None: ...
def read_str() -> None: ...
def wait() -> None: ...
def write_int() -> None: ...
def write_str() -> None: ...
