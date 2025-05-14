from dataclasses import dataclass

from pptx_shapes.enums import Align, VerticalAlign


@dataclass
class FontStyle:
    size: float = 14
    color: str = "#000000"
    align: Align = Align.CENTER
    vertical_align: VerticalAlign = VerticalAlign.CENTER
