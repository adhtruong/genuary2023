from typing import Iterable, TypeVar

from more_itertools import prepend

T = TypeVar("T")


def get_first(iterable: Iterable[T]) -> tuple[T, Iterable[T]]:
    iterable = iter(iterable)
    try:
        first = next(iterable)
    except StopIteration:
        raise RuntimeError("Iterable provided must be non-empty.")

    return first, prepend(first, iterable)
