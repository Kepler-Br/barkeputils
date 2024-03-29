from typing import Callable, Iterable, Optional, TypeVar, Type, Any, List, Generator

_K = TypeVar("_K")
_V = TypeVar("_V")
_T = TypeVar("_T")
_TT = TypeVar("_TT")


def associate_by(key_producer: Callable[[_V], _K], items: Iterable[_V]) -> dict[_K, _V]:
    out_dict: dict[_K, List[_V]] = dict()

    for item in items:
        out_dict[key_producer(item)] = item

    return out_dict


def group_by(key_producer: Callable[[_V], _K], items: Iterable[_V]) -> dict[_K, List[_V]]:
    out_dict: dict[_K, List[_V]] = dict()

    for item in items:
        key = key_producer(item)
        if key in out_dict:
            out_dict[key].append(item)
        else:
            out_dict[key] = [item]

    return out_dict


def flat_list(iterable: Iterable[_T]) -> Generator[_T, None, None]:
    for sub_list in iterable:
        for item in sub_list:
            yield item


def iter_batch(iterable: Iterable[_T], batch_size=1) -> list[list[_T]]:
    batch_array = list()

    for val in iterable:
        batch_array.append(val)

        if len(batch_array) == batch_size:
            yield batch_array
            batch_array = list()

    if len(batch_array) != 0:
        yield batch_array


def none_if_empty_string(string: str) -> Optional[str]:
    if len(string.strip()) == 0:
        return None

    return string


def do_if_none(val: Optional[_T], fun: Callable[[], Optional[Any]]) -> Optional[Any]:
    if val is None:
        return fun()

    return val


def default_if_none(val: Optional[_T], default: _T) -> _T:
    if val is None:
        return default
    return val


def apply_if_not_none(val: Optional[_T], fun: Callable[[_T], _TT]) -> _TT:
    if val is not None:
        return fun(val)
    return None


def none_if_key_not_exists(dictionary: dict[_K, _V], key: _K) -> Optional[_V]:
    if key not in dictionary:
        return None
    return dictionary[key]


def default_if_key_not_exists(dictionary: dict[_K, _V], key: _K, default: _V) -> Optional[_V]:
    if key not in dictionary:
        return default
    return dictionary[key]


def run_catching(exception: Type[_T], runnable: Callable, on_exception: Callable[[_T], Any]) -> Any:
    try:
        return runnable()
    except exception as e:
        return on_exception(e)
