from typing import List

from pptx_shapes.charts.bar.config import BarChartConfig
from pptx_shapes.enums import VerticalAlign
from pptx_shapes.shapes import Rectangle, Shape, TextBox
from pptx_shapes.style import FillStyle, FontStyle, StrokeStyle


class BarChart:
    def __init__(self, config: BarChartConfig) -> None:
        self.config = config

    def render(self, data: List[dict], x: float, y: float) -> List[Shape]:
        max_value = max([item["value"] for item in data], default=1)
        shapes = []

        for i, item in enumerate(data):
            bar_height = item["value"] / max_value * self.config.bar.height
            bar_x = x + i * self.config.bar.width
            bar_y = y + self.config.bar.height - bar_height

            if bar_height > 0:
                shapes.append(self.__get_bar(x=bar_x, y=bar_y, height=bar_height))
                shapes.append(self.__get_value_label(x=bar_x, y=bar_y, value=item["value"]))

            shapes.append(self.__get_label(x=bar_x, y=y + self.config.bar.height, label=item["label"]))

        return shapes

    def __get_bar(self, x: float, y: float, height: float) -> Rectangle:
        fill = FillStyle(color=self.config.bar.fill_color)
        stroke = StrokeStyle(color=self.config.bar.stroke_color, thickness=self.config.bar.thickness)
        return Rectangle(x=x, y=y, width=self.config.bar.width, height=height, radius=self.config.bar.radius, fill=fill, stroke=stroke)

    def __get_value_label(self, x: float, y: float, value: float) -> TextBox:
        style = FontStyle(size=self.config.value.size, color=self.config.value.color, family=self.config.value.family, vertical_align=VerticalAlign.BOTTOM)
        return TextBox(x=x, y=y - self.config.value.height, width=self.config.bar.width, height=self.config.value.height, text=str(value), style=style, auto_fit=True)

    def __get_label(self, x: float, y: float, label: str) -> TextBox:
        style = FontStyle(size=self.config.label.size, color=self.config.label.color, family=self.config.label.family, vertical_align=VerticalAlign.TOP)
        return TextBox(x=x, y=y, width=self.config.bar.width, height=self.config.label.height, text=label, style=style, auto_fit=True)
