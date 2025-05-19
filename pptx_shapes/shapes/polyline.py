from dataclasses import dataclass
from typing import List, Optional, Tuple

from lxml import etree

from pptx_shapes import units
from pptx_shapes.entities.bbox import BBox
from pptx_shapes.entities.namespace_helper import NamespaceHelper
from pptx_shapes.shapes.shape import Shape
from pptx_shapes.style.stroke_style import StrokeStyle


@dataclass
class Polyline(Shape):
    points: List[Tuple[float, float]]
    angle: float = 0
    stroke: Optional[StrokeStyle] = None

    def to_xml(self, shape_id: int, ns_helper: NamespaceHelper) -> etree.Element:
        node = ns_helper.element("p:sp")
        xs, ys = [x for x, _ in self.points], [y for _, y in self.points]
        x_min, y_min, x_max, y_max = min(xs), min(ys), max(xs), max(ys)

        nvsppr = ns_helper.element("p:nvSpPr", parent=node)
        ns_helper.element("p:cNvPr", {"id": str(shape_id), "name": f"Polyline {shape_id}"}, parent=nvsppr)
        ns_helper.element("p:cNvSpPr", parent=nvsppr)
        ns_helper.element("p:nvPr", parent=nvsppr)

        sppr = ns_helper.element("p:spPr", parent=node)
        sppr.append(self.make_xfrm(ns_helper, {"rot": units.angle_to_unit(self.angle)}, x=x_min, y=y_min, width=x_max - x_min, height=y_max - y_min))

        cust_geom = ns_helper.element("a:custGeom", parent=sppr)
        ns_helper.element("a:avLst", parent=cust_geom)
        ns_helper.element("a:ahLst", parent=cust_geom)
        ns_helper.element("a:rect", {"b": "b", "l": "l", "r": "r", "t": "t"}, parent=cust_geom)

        path = ns_helper.element("a:path", {"w": units.cm_to_emu(x_max - x_min), "h": units.cm_to_emu(y_max - y_min)}, parent=ns_helper.element("a:pathLst", parent=cust_geom))
        for i, (px, py) in enumerate(self.points):
            to = ns_helper.element("a:moveTo" if i == 0 else "a:lnTo", parent=path)
            ns_helper.element("a:pt", {"x": units.cm_to_emu(px - x_min), "y": units.cm_to_emu(py - y_min)}, parent=to)

        if self.stroke:
            sppr.append(self.stroke.to_xml(ns_helper))

        return node

    def bbox(self) -> BBox:
        return BBox.from_points(points=self.points, angle=self.angle)
