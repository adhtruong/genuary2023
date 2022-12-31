import os
import tempfile
from functools import partial
from typing import Iterable, Iterator, Union

import cv2  # type: ignore

from cairo_utils.core import Context, write_to_png
from cairo_utils.itertool_utils import get_first


def create_video_from_images(
    paths: Iterable[Union[os.PathLike, str]],
    output_path: Union[os.PathLike, str],
    frame_rate: float,
) -> None:
    if frame_rate <= 0:
        raise ValueError("Frame rate must be positive")

    first_path, paths = get_first(paths)
    width, height = cv2.imread(str(first_path)).shape[:2]
    codec = cv2.VideoWriter_fourcc(*"avc1")
    out = cv2.VideoWriter(output_path, codec, frame_rate, (width, height))
    try:
        for path in paths:
            out.write(cv2.imread(str(path)))
    finally:
        out.release()


def get_renderer(
    size: int,
    frames: int,
    frame_rate: float,
    output_path: Union[os.PathLike, str],
) -> Iterator[Context]:
    context_provider = partial(write_to_png, size)

    if frames <= 0:
        raise ValueError("frame must be positive")

    if frame_rate <= 0:
        raise ValueError("frame_rate must be positive")

    with tempfile.TemporaryDirectory() as directory:
        paths: list[str] = []
        for _ in range(frames):
            file, path = tempfile.mkstemp(dir=str(directory), suffix=".png")
            os.close(file)
            with context_provider(path) as context:
                yield context
            paths.append(path)

        create_video_from_images(paths, output_path, frame_rate)
