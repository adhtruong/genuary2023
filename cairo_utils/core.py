import math
from contextlib import contextmanager
from typing import ContextManager, Generic, Iterator, TypeVar, Union, overload

from cairo import Context as _Context
from cairo import Format, ImageSurface, Surface


@contextmanager
def _save_context(context: "Context") -> Iterator[None]:
    yield
    context.restore()


BLACK = (0, 0, 0)
WHITE = (1, 1, 1)


_SomeSurface = TypeVar("_SomeSurface", bound=Surface)


class _TypedContext(_Context, Generic[_SomeSurface]):  # type: ignore[type-arg]
    ...


class Context(_TypedContext[ImageSurface]):
    def new(self) -> "Context":
        return Context(self.get_target())

    def save(self) -> ContextManager[None]:  # type: ignore[override]
        super().save()
        return _save_context(self)

    @property
    def size(self) -> int:
        surface = self.get_target()
        if not isinstance(surface, ImageSurface):
            raise RuntimeError(f"Unable to get size for {surface = }")
        width = surface.get_width()
        height = surface.get_height()
        if width != height:
            raise RuntimeError("Unable to calculate size")
        return width

    def square(self, x: float, y: float, size: float) -> None:
        self.rectangle(x, y, size, size)
        self.close_path()

    def circle(self, xc: float, yc: float, radius: float) -> None:
        self.arc(xc, yc, radius, 0, 2 * math.pi)

    def set_grey(self, grey: float, alpha: float = 1) -> None:
        self.set_source_rgba(grey, grey, grey, alpha)

    def set_black(self, alpha: float = 1) -> None:
        self.set_grey(0, alpha)

    def set_white(self, alpha: float = 1) -> None:
        self.set_grey(1, alpha)


@overload
def write_to_png(
    size: int,
    output: str,
    /,
) -> ContextManager[Context]:
    ...


@overload
def write_to_png(
    width: int,
    height: int,
    output: str,
    /,
) -> ContextManager[Context]:
    ...


@contextmanager
def write_to_png(
    *args: Union[str, int],
) -> Iterator[Context]:
    width: int
    height: int
    output: str
    if len(args) == 3:
        width, height, output = args  # type: ignore[assignment]
    elif len(args) == 2:
        width, output = args  # type: ignore[assignment]
        height = width
    else:
        raise RuntimeError(f"Unable to initialise with {args = }")

    with ImageSurface(Format.ARGB32, width, height) as surface:
        context = Context(surface)
        yield context
        surface.write_to_png(output)
