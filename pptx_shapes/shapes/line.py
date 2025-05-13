from dataclasses import dataclass
from typing import Optional

from lxml import etree

from pptx_shapes.entities.bbox import BBox
from pptx_shapes.entities.namespace_helper import NamespaceHelper
from pptx_shapes.shapes.shape import Shape
from pptx_shapes.style.stroke_style import StrokeStyle


@dataclass
class Line(Shape):
    x1: float
    y1: float
    x2: float
    y2: float
    stroke: Optional[StrokeStyle] = None

    def to_xml(self, shape_id: int, ns_helper: NamespaceHelper) -> etree.Element:
        node = ns_helper.element("p:cxnSp")

        nvcxnsppr = ns_helper.element("p:nvCxnSpPr", parent=node)
        ns_helper.element("p:cNvPr", {"id": str(shape_id), "name": f"Line {shape_id}"}, parent=nvcxnsppr)
        ns_helper.element("p:cNvCxnSpPr", parent=nvcxnsppr)
        ns_helper.element("p:nvPr", parent=nvcxnsppr)

        flips = {"flipH": "0" if self.x1 <= self.x2 else "1", "flipV": "0" if self.y1 <= self.y2 else "1"}
        bbox = self.bbox()

        sppr = ns_helper.element("p:spPr", parent=node)
        sppr.append(self.make_xfrm(ns_helper, flips, x=bbox.x, y=bbox.y, width=bbox.width, height=bbox.height))
        ns_helper.element("a:avLst", parent=ns_helper.element("a:prstGeom", {"prst": "line"}, parent=sppr))

        if self.stroke:
            sppr.append(self.stroke.to_xml(ns_helper))

        return node

    def bbox(self) -> BBox:
        x = min(self.x1, self.x2)
        y = min(self.y1, self.y2)
        width = abs(self.x2 - self.x1)
        height = abs(self.y2 - self.y1)

        return BBox(x=x, y=y, width=width, height=height)
