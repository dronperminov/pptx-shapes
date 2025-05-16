from dataclasses import dataclass, field
from typing import List, Optional

from pptx_shapes.charts.scatter.point import ScatterPoint


@dataclass
class AxesFont:
    size: float = 8
    color: str = "#222"
    family: str = "Calibri"


@dataclass
class Axes:
    color: str = "#555"
    show_x: bool = True
    show_y: bool = True
    thickness: float = 1
    tick_length: float = 0.3
    font: AxesFont = field(default_factory=lambda: AxesFont())
    text_size: float = 1


@dataclass
class Limits:
    x_min: float
    y_min: float
    x_max: float
    y_max: float

    @classmethod
    def from_points(cls: "Limits", points: List[ScatterPoint]) -> "Limits":
        x = [point.x for point in points]
        y = [point.y for point in points]
        return Limits(
            x_min=min(x, default=0),
            y_min=min(y, default=0),
            x_max=max(x, default=1),
            y_max=max(y, default=1)
        )

    def map_x(self, x: float, x_min: float, dx: float) -> float:
        return x_min + (x - self.x_min) / (self.x_max - self.x_min) * dx

    def map_y(self, y: float, y_min: float, dy: float) -> float:
        return y_min + (self.y_max - y) / (self.y_max - self.y_min) * dy


@dataclass
class ScatterPlotConfig:
    x: float
    y: float
    width: float = 8
    height: float = 8
    padding: float = 0.2
    axes: Axes = field(default_factory=lambda: Axes())
    limits: Optional[Limits] = None
