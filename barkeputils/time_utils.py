from time import time
from typing import Callable, Tuple, TypeVar

_T = TypeVar("_T")


def time_this(fun: Callable[[], _T]) -> Tuple[float, _T]:
    tic = time()
    ret = fun()
    toc = time()

    return toc - tic, ret
