from pathlib import Path
from typing import Union

import pytest
from cairo import SVGSurface

from cairo_utils import Context, write_to_png


@pytest.mark.parametrize(
    ("args"),
    (
        (100,),
        (100, 100),
    ),
)
def test_write_to_png(tmp_path: Path, args: Union[tuple[int], tuple[int, int]]) -> None:
    output = tmp_path / "output.png"
    with write_to_png(*args, str(output)) as context:  # type: ignore[call-overload]
        assert isinstance(context, Context)

        context.set_white()
        context.square(0, 0, 100)
        context.fill()

        with context.save():
            context.set_black()
            context.circle(0, 0, 1)
            context.stroke()

        context.circle(1, 1, 1)
        assert context.size == 100


def test_invalid_args() -> None:
    with pytest.raises(
        RuntimeError,
        match=r"Unable to initialise with args = \(1,\)",
    ):
        with write_to_png(1):  # type: ignore[call-overload]
            pass


def test_size_raises_for_mismatch_in_size(tmp_path: Path) -> None:
    output = tmp_path / "output.png"
    with write_to_png(100, 200, str(output)) as context:
        with pytest.raises(
            RuntimeError,
            match="Unable to calculate size",
        ):
            context.size


def test_size_raises_for_other_surface(tmp_path: Path) -> None:
    surface = SVGSurface(str(tmp_path / "output.png"), 100, 100)
    context = Context(surface)
    with pytest.raises(RuntimeError):
        context.size
