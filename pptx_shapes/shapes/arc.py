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
class Arc(Shape):
    x: float
    y: float
    width: float
    height: float
    start_angle: float = 0
    end_angle: float = 180
    angle: float = 0
    fill: Optional[FillStyle] = None
    stroke: Optional[StrokeStyle] = None

    def to_xml(self, shape_id: int, ns_helper: NamespaceHelper) -> etree.Element:
        node = ns_helper.element("p:sp")

        nvsppr = ns_helper.element("p:nvSpPr", parent=node)
        ns_helper.element("p:cNvPr", {"id": str(shape_id), "name": f"Arc {shape_id}"}, parent=nvsppr)
        ns_helper.element("p:cNvSpPr", parent=nvsppr)
        ns_helper.element("p:nvPr", parent=nvsppr)

        sppr = ns_helper.element("p:spPr", parent=node)
        sppr.append(self.make_xfrm(ns_helper, {"rot": units.angle_to_unit(self.angle)}, x=self.x, y=self.y, width=self.width, height=self.height))
        av_lst = ns_helper.element("a:avLst", parent=ns_helper.element("a:prstGeom", {"prst": "arc"}, parent=sppr))
        ns_helper.element("a:gd", {"fmla": f"val {units.angle_to_unit(self.start_angle)}", "name": "adj1"}, parent=av_lst)
        ns_helper.element("a:gd", {"fmla": f"val {units.angle_to_unit(self.end_angle)}", "name": "adj2"}, parent=av_lst)

        if self.fill:
            sppr.append(self.fill.to_xml(ns_helper))

        if self.stroke:
            sppr.append(self.stroke.to_xml(ns_helper))

        return node

    def bbox(self) -> BBox:
        if self.angle == 0:
            return BBox(x=self.x, y=self.y, width=self.width, height=self.height)

        cx, cy = self.x + self.width / 2, self.y + self.height / 2
        r = self.angle / 180 * math.pi
        t1 = math.atan(-self.height / self.width * math.tan(r))
        t2 = math.atan(self.height / self.width / math.tan(r))

        w = self.width * math.cos(t1) * math.cos(r) - self.height * math.sin(t1) * math.sin(r)
        h = -self.height * math.sin(t2) * math.cos(r) - self.width * math.cos(t2) * math.sin(r)

        return BBox(x=cx - w / 2, y=cy - h / 2, width=w, height=h)
