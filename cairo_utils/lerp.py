from typing import Any, Protocol, TypeVar, Union, overload

_LerpSelf = TypeVar("_LerpSelf", bound="_LerpInput")


class _LerpInput(Protocol):  # pragma: no cover
    def __rmul__(self: _LerpSelf, __other: float) -> _LerpSelf:
        ...

    def __add__(self: _LerpSelf, __other: _LerpSelf) -> _LerpSelf:
        ...


_LerpInputT = TypeVar("_LerpInputT", bound=_LerpInput)


@overload
def lerp(a: Union[int, float], b: Union[int, float], t: float) -> float:
    ...


@overload
def lerp(a: _LerpInputT, b: _LerpInputT, t: float) -> _LerpInputT:
    ...


def lerp(a: Any, b: Any, t: float) -> Any:
    """Linear interpolate on the scale given by a to b, using t as the point on that scale."""
    return (1 - t) * a + t * b


_InverseSelf = TypeVar("_InverseSelf", bound="_InverseLerpInput")


class _InverseLerpInput(Protocol):  # pragma: no cover
    def __sub__(self: _InverseSelf, __other: _InverseSelf) -> _InverseSelf:
        ...

    def __div__(self: _InverseSelf, __other: _InverseSelf) -> float:
        ...


_InverseLerpInputT = TypeVar("_InverseLerpInputT", _InverseLerpInput, float, int)


def inv_lerp(a: _InverseLerpInputT, b: _InverseLerpInputT, v: _InverseLerpInputT) -> float:
    """Inverse Linar Interpolation, get the fraction between a and b on which v resides."""
    return (v - a) / (b - a)  # type: ignore


def interpolate(
    i_min: _InverseLerpInputT,
    i_max: _InverseLerpInputT,
    o_min: _LerpInputT,
    o_max: _LerpInputT,
    v: _InverseLerpInputT,
) -> _LerpInputT:
    """Remap values from one linear scale to another, a combination of lerp and inv_lerp.
    i_min and i_max are the scale on which the original value resides,
    o_min and o_max are the scale to which it should be mapped.
    """
    return lerp(o_min, o_max, inv_lerp(i_min, i_max, v))
