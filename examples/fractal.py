import math
from dataclasses import dataclass
from typing import List

from pptx_shapes import Presentation
from pptx_shapes.shapes import Group, Line, Rectangle, Shape
from pptx_shapes.style import FillStyle, StrokeStyle


@dataclass
class Config:
    start_color: str
    end_color: str
    depth: int
    start_branch_num: int
    branch_num: int
    branch_angle: float
    length: float

    def get_stroke(self, depth: int) -> StrokeStyle:
        ratio = depth / self.depth

        r1, g1, b1 = int(self.start_color[1:3], 16), int(self.start_color[3:5], 16), int(self.start_color[5:7], 16)
        r2, g2, b2 = int(self.end_color[1:3], 16), int(self.end_color[3:5], 16), int(self.end_color[5:7], 16)

        r = math.floor(r1 * (1 - ratio) + r2 * ratio)
        g = math.floor(g1 * (1 - ratio) + g2 * ratio)
        b = math.floor(b1 * (1 - ratio) + b2 * ratio)

        return StrokeStyle(color=f"#{r:02X}{g:02X}{b:02X}", opacity=1 - math.pow(depth / (self.depth + 1), 2), thickness=0.1)


def draw_fractal_line(config: Config, start_x: float, start_y: float, depth: int, degree: float, length: float, shapes: List[Shape]) -> None:
    if depth > config.depth:
        return

    start_angle = -(config.branch_num - 1) * config.branch_angle / 2 + degree

    for _ in range(config.branch_num):
        angle = start_angle * math.pi / 180
        x = start_x + math.cos(angle) * length
        y = start_y + math.sin(angle) * length

        shapes.append(Line(x1=start_x, y1=start_y, x2=x, y2=y, stroke=config.get_stroke(depth=depth)))
        draw_fractal_line(config, x, y, depth + 1, start_angle, length * math.pow(config.length, depth), shapes)
        start_angle += config.branch_angle


def draw_fractal(config: Config, x0: float, y0: float, length: float) -> List[Shape]:
    shapes = []
    degree = 360 / config.start_branch_num

    for i in range(config.start_branch_num):
        angle = degree * i * math.pi / 180
        x = x0 + math.cos(angle) * length
        y = y0 + math.sin(angle) * length

        shapes.append(Line(x1=x0, y1=y0, x2=x, y2=y, stroke=config.get_stroke(0)))
        draw_fractal_line(config, x, y, 1, degree * i, length, shapes)

    return shapes


def main() -> None:
    config = Config(
        start_color="#ff0000",
        end_color="#ffff00",
        depth=5,
        start_branch_num=7,
        branch_num=4,
        branch_angle=75,  # 20..90
        length=0.93  # 0.6..1.3
    )

    width = 33.867
    height = 19.05

    with Presentation(presentation_path="empty.pptx") as presentation:
        shapes = draw_fractal(config=config, x0=width / 2, y0=height / 2, length=2)
        presentation.add(shape=Rectangle(x=0, y=0, width=width, height=height, fill=FillStyle(color="#000")))
        presentation.add(shape=Group(shapes))
        presentation.save("fractal.pptx")


if __name__ == "__main__":
    main()
