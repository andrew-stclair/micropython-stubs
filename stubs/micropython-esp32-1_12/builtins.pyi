from typing import Any

Node = Any

class ArithmeticError: ...
class AssertionError: ...
class AttributeError: ...
class BaseException: ...
class EOFError: ...
class Exception: ...
class GeneratorExit: ...
class ImportError: ...
class IndentationError: ...
class IndexError: ...
class KeyError: ...
class KeyboardInterrupt: ...
class LookupError: ...
class MemoryError: ...
class NameError: ...
class NotImplementedError: ...
class OSError: ...
class OverflowError: ...
class RuntimeError: ...
class StopAsyncIteration: ...
class StopIteration: ...
class SyntaxError: ...
class SystemExit: ...
class TypeError: ...
class UnicodeError: ...
class ValueError: ...
class ViperTypeError: ...
class ZeroDivisionError: ...

def abs() -> None: ...
def all() -> None: ...
def any() -> None: ...
def bin() -> None: ...

class bool: ...

class bytearray:
    def append() -> None: ...
    def decode() -> None: ...
    def extend() -> None: ...

class bytes:
    def center() -> None: ...
    def count() -> None: ...
    def decode() -> None: ...
    def endswith() -> None: ...
    def find() -> None: ...
    def format() -> None: ...
    def index() -> None: ...
    def isalpha() -> None: ...
    def isdigit() -> None: ...
    def islower() -> None: ...
    def isspace() -> None: ...
    def isupper() -> None: ...
    def join() -> None: ...
    def lower() -> None: ...
    def lstrip() -> None: ...
    def partition() -> None: ...
    def replace() -> None: ...
    def rfind() -> None: ...
    def rindex() -> None: ...
    def rpartition() -> None: ...
    def rsplit() -> None: ...
    def rstrip() -> None: ...
    def split() -> None: ...
    def splitlines() -> None: ...
    def startswith() -> None: ...
    def strip() -> None: ...
    def upper() -> None: ...

def callable() -> None: ...
def chr() -> None: ...

class classmethod: ...

def compile() -> None: ...

class complex: ...

def delattr() -> None: ...

class dict:
    def clear() -> None: ...
    def copy() -> None: ...
    def fromkeys() -> None: ...
    def get() -> None: ...
    def items() -> None: ...
    def keys() -> None: ...
    def pop() -> None: ...
    def popitem() -> None: ...
    def setdefault() -> None: ...
    def update() -> None: ...
    def values() -> None: ...

def dir() -> None: ...
def divmod() -> None: ...

class enumerate: ...

def eval() -> None: ...
def exec() -> None: ...
def execfile() -> None: ...

class filter: ...
class float: ...

class frozenset:
    def copy() -> None: ...
    def difference() -> None: ...
    def intersection() -> None: ...
    def isdisjoint() -> None: ...
    def issubset() -> None: ...
    def issuperset() -> None: ...
    def symmetric_difference() -> None: ...
    def union() -> None: ...

def getattr() -> None: ...
def globals() -> None: ...
def hasattr() -> None: ...
def hash() -> None: ...
def help() -> None: ...
def hex() -> None: ...
def id() -> None: ...
def input() -> None: ...

class int:
    def from_bytes() -> None: ...
    def to_bytes() -> None: ...

def isinstance() -> None: ...
def issubclass() -> None: ...
def iter() -> None: ...
def len() -> None: ...

class list:
    def append() -> None: ...
    def clear() -> None: ...
    def copy() -> None: ...
    def count() -> None: ...
    def extend() -> None: ...
    def index() -> None: ...
    def insert() -> None: ...
    def pop() -> None: ...
    def remove() -> None: ...
    def reverse() -> None: ...
    def sort() -> None: ...

def locals() -> None: ...

class map: ...

def max() -> None: ...

class memoryview: ...

def min() -> None: ...
def next() -> None: ...

class object: ...

def oct() -> None: ...
def open() -> None: ...
def ord() -> None: ...
def pow() -> None: ...
def print() -> None: ...

class property:
    def deleter() -> None: ...
    def getter() -> None: ...
    def setter() -> None: ...

class range: ...

def repr() -> None: ...

class reversed: ...

def round() -> None: ...

class set:
    def add() -> None: ...
    def clear() -> None: ...
    def copy() -> None: ...
    def difference() -> None: ...
    def difference_update() -> None: ...
    def discard() -> None: ...
    def intersection() -> None: ...
    def intersection_update() -> None: ...
    def isdisjoint() -> None: ...
    def issubset() -> None: ...
    def issuperset() -> None: ...
    def pop() -> None: ...
    def remove() -> None: ...
    def symmetric_difference() -> None: ...
    def symmetric_difference_update() -> None: ...
    def union() -> None: ...
    def update() -> None: ...

def setattr() -> None: ...

class slice: ...

def sorted() -> None: ...

class staticmethod: ...

class str:
    def center() -> None: ...
    def count() -> None: ...
    def encode() -> None: ...
    def endswith() -> None: ...
    def find() -> None: ...
    def format() -> None: ...
    def index() -> None: ...
    def isalpha() -> None: ...
    def isdigit() -> None: ...
    def islower() -> None: ...
    def isspace() -> None: ...
    def isupper() -> None: ...
    def join() -> None: ...
    def lower() -> None: ...
    def lstrip() -> None: ...
    def partition() -> None: ...
    def replace() -> None: ...
    def rfind() -> None: ...
    def rindex() -> None: ...
    def rpartition() -> None: ...
    def rsplit() -> None: ...
    def rstrip() -> None: ...
    def split() -> None: ...
    def splitlines() -> None: ...
    def startswith() -> None: ...
    def strip() -> None: ...
    def upper() -> None: ...

def sum() -> None: ...

class super: ...

class tuple:
    def count() -> None: ...
    def index() -> None: ...

class type: ...
class zip: ...
