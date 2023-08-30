from typing import Sized


def is_empty(value: Sized) -> bool:
    if len(value) == 0:
        return True
    return False


def is_not_empty(value: Sized) -> bool:
    if len(value) > 0:
        return True
    return False
