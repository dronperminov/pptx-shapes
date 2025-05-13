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
class Ellipse(Shape):
    x: float
    y: float
    dx: float
    dy: float
    angle: float = 0
    fill: Optional[FillStyle] = None
    stroke: Optional[StrokeStyle] = None

    def to_xml(self, shape_id: int, ns_helper: NamespaceHelper) -> etree.Element:
        node = ns_helper.element("p:sp")

        nvsppr = ns_helper.element("p:nvSpPr", parent=node)
        ns_helper.element("p:cNvPr", {"id": str(shape_id), "name": f"Ellipse {shape_id}"}, parent=nvsppr)
        ns_helper.element("p:cNvSpPr", parent=nvsppr)
        ns_helper.element("p:nvPr", parent=nvsppr)

        sppr = ns_helper.element("p:spPr", parent=node)
        sppr.append(self.make_xfrm(ns_helper, {"rot": units.angle_to_unit(self.angle)}, x=self.x, y=self.y, width=self.dx, height=self.dy))
        ns_helper.element("a:avLst", parent=ns_helper.element("a:prstGeom", {"prst": "ellipse"}, parent=sppr))

        if self.fill:
            sppr.append(self.fill.to_xml(ns_helper))

        if self.stroke:
            sppr.append(self.stroke.to_xml(ns_helper))

        return node

    def bbox(self) -> BBox:
        if self.angle == 0:
            return BBox(x=self.x, y=self.y, width=self.dx, height=self.dy)

        cx, cy = self.x + self.dx / 2, self.y + self.dy / 2
        r = self.angle / 180 * math.pi
        t1 = math.atan(-self.dy / self.dx * math.tan(r))
        t2 = math.atan(self.dy / self.dx / math.tan(r))

        w = self.dx * math.cos(t1) * math.cos(r) - self.dy * math.sin(t1) * math.sin(r)
        h = -self.dy * math.sin(t2) * math.cos(r) - self.dx * math.cos(t2) * math.sin(r)

        return BBox(x=cx - w / 2, y=cy - h / 2, width=w, height=h)
