import math
from dataclasses import dataclass
from typing import Optional

from lxml import etree

from pptx_shapes import units
from pptx_shapes.entities.bbox import BBox
from pptx_shapes.entities.namespace_helper import NamespaceHelper
from pptx_shapes.shapes.shape import Shape
from pptx_shapes.style.fill_style import FillStyle
from pptx_shapes.style.stroke_style import StrokeStyle


@dataclass
class Rectangle(Shape):
    x: float
    y: float
    width: float
    height: float
    angle: float = 0
    radius: float = 0
    fill: Optional[FillStyle] = None
    stroke: Optional[StrokeStyle] = None

    def to_xml(self, shape_id: int, ns_helper: NamespaceHelper) -> etree.Element:
        node = ns_helper.element("p:sp")

        nvsppr = ns_helper.element("p:nvSpPr", parent=node)
        ns_helper.element("p:cNvPr", {"id": str(shape_id), "name": f"Rectangle {shape_id}"}, parent=nvsppr)
        ns_helper.element("p:cNvSpPr", parent=nvsppr)
        ns_helper.element("p:nvPr", parent=nvsppr)

        sppr = ns_helper.element("p:spPr", parent=node)
        sppr.append(self.make_xfrm(ns_helper, {"rot": units.angle_to_unit(self.angle)}, x=self.x, y=self.y, width=self.width, height=self.height))

        geom = ns_helper.element("a:prstGeom", {"prst": "roundRect"}, parent=sppr)
        avlst = ns_helper.element("a:avLst", parent=geom)
        ns_helper.element("a:gd", {"name": "adj", "fmla": f"val {units.fraction_to_unit(self.radius / 2)}"}, parent=avlst)

        if self.fill:
            sppr.append(self.fill.to_xml(ns_helper))

        if self.stroke:
            sppr.append(self.stroke.to_xml(ns_helper))

        return node

    def bbox(self) -> BBox:
        if self.angle == 0:
            return BBox(x=self.x, y=self.y, width=self.width, height=self.height)

        cx, cy = self.x + self.width / 2, self.y + self.height / 2
        angle = self.angle / 180 * math.pi
        x_min = x_max = cx
        y_min = y_max = cy

        for px, py in [(self.x, self.y), (self.x + self.width, self.y), (self.x + self.width, self.y + self.height), (self.x, self.y + self.height)]:
            dx, dy = px - cx, py - cy

            x = cx + dx * math.cos(angle) - dy * math.sin(angle)
            y = cy + dx * math.sin(angle) + dy * math.cos(angle)

            x_min, y_min = min(x_min, x), min(y_min, y)
            x_max, y_max = max(x_max, x), max(y_max, y)

        return BBox(x=x_min, y=y_min, width=x_max - x_min, height=y_max - y_min)
