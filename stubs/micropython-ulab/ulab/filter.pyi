import ulab
from typing import Tuple, overload
from ulab import _ArrayLike as _ArrayLike

def convolve(a: ulab.array, v: ulab.array) -> ulab.array: ...
@overload
def sosfilt(sos: _ArrayLike, x: _ArrayLike) -> ulab.array: ...
@overload
def sosfilt(sos: _ArrayLike, x: _ArrayLike, zi: ulab.array) -> Tuple[ulab.array, ulab.array]: ...
