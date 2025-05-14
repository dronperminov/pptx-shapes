from typing import List

from pptx_shapes.charts.donut.config import DonutChartConfig
from pptx_shapes.shapes import Arch, Pie, TextBox
from pptx_shapes.shapes.shape import Shape
from pptx_shapes.style import FillStyle, FontFormat, FontStyle, StrokeStyle


class DonutChart:
    def __init__(self, config: DonutChartConfig) -> None:
        if config.inner_radius >= config.outer_radius:
            raise ValueError("The outer radius must be greater than the inner radius")

        self.config = config
        self.size = self.config.outer_radius * 2
        self.arch_thickness = self.config.outer_radius - self.config.inner_radius

    def render(self, data: List[dict], x: float, y: float) -> List[Shape]:
        total = sum([item["value"] for item in data])
        angle = self.config.start_angle
        shapes = []

        for item in data:
            value_angle = item["value"] / total * 360
            shapes.append(self.__get_segment(color=item["color"], value_angle=value_angle, angle=angle, x=x, y=y))
            angle += value_angle

        if self.config.label is not None:
            shapes.append(self.__get_label(total=total, x=x, y=y))

        return shapes

    def __get_segment(self, color: str, value_angle: float, angle: float, x: float, y: float) -> Shape:
        fill = FillStyle(color=color)
        stroke = StrokeStyle(color=self.config.gap.color, thickness=self.config.gap.thickness) if self.config.gap else None

        if self.config.inner_radius < 0.01:
            return Pie(x=x, y=y, width=self.size, height=self.size, end_angle=value_angle, angle=angle, fill=fill, stroke=stroke)

        return Arch(x=x, y=y, width=self.size, height=self.size, end_angle=value_angle, thickness=self.arch_thickness, angle=angle, fill=fill, stroke=stroke)

    def __get_label(self, total: float, x: float, y: float) -> TextBox:
        style = FontStyle(size=self.config.label.size, color=self.config.label.color, family=self.config.label.family)
        formatting = FontFormat(bold=self.config.label.bold)
        return TextBox(x=x, y=y, width=self.size, height=self.size, text=str(total), style=style, formatting=formatting)
