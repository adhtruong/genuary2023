from dataclasses import dataclass
from typing import TypeVar

Self = TypeVar("Self", bound="Point")


@dataclass(frozen=True)
class Point:
    x: float
    y: float

    def __rmul__(self: Self, __other: float) -> Self:
        return self.__class__(self.x * __other, self.y * __other)

    def __add__(self: Self, __other: Self) -> Self:
        return self.__class__(self.x + __other.x, self.y + __other.y)

    def __sub__(self: Self, __other: Self) -> Self:
        return self.__class__(self.x - __other.x, self.y - __other.y)
