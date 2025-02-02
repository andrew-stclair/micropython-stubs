import os
from typing import Any

class LS:
    def __repr__(self): ...
    def __call__(self, path: str = ...) -> None: ...

class PWD:
    def __repr__(self): ...
    def __call__(self): ...

class CLEAR:
    def __repr__(self): ...
    def __call__(self): ...

def head(f, n: int = ...) -> None: ...
def cat(f) -> None: ...
def cp(s, t) -> None: ...
def newfile(path) -> None: ...
def rm(d, recursive: bool = ...) -> None: ...

class Man:
    def __repr__(self): ...

man: Any
pwd: Any
ls: Any
clear: Any
cd = os.chdir
mkdir = os.mkdir
mv = os.rename
rmdir = os.rmdir
