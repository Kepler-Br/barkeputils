from typing import Callable, Iterable, Iterator, Optional, TypeVar

_K = TypeVar("_K")
_V = TypeVar("_V")
_T = TypeVar("_T")


def apply_if_not_none(item: Optional[_T], consumer: Callable[[_T], None]):
    if item is not None:
        consumer(item)


def associate_by(key_producer: Callable[[_V], _K], items: Iterable[_V]) -> dict[_K, _V]:
    out_dict = dict()

    for item in items:
        out_dict[key_producer(item)] = item

    return out_dict


def flat_list(iterable: Iterable[_T]) -> _T:
    for sub_list in iterable:
        for item in sub_list:
            yield item
    # return [item for sublist in iterable for item in sublist]


def iter_batch(iterable: Iterator[_T], batch_size=1) -> list[_T]:
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


def if_none(val: Optional[_T], default: _T) -> _T:
    if val is None:
        return default
    return val


def none_if_key_not_exists(dictionary: dict[_K, _V], key: _K) -> Optional[_V]:
    if key not in dictionary:
        return None
    return dictionary[key]
