from dataclasses import dataclass, field
from typing import Optional

from pptx_shapes.style import FillStyle, StrokeStyle


@dataclass
class ScatterPoint:
    x: float
    y: float
    radius: float = 0.5
    fill: Optional[FillStyle] = field(default_factory=lambda: FillStyle(color="#dd7373"))
    stroke: Optional[StrokeStyle] = field(default_factory=lambda: StrokeStyle(color="#fff", thickness=0.5))
