from dataclasses import dataclass
from typing import List

from lxml import etree

from pptx_shapes import units
from pptx_shapes.entities.bbox import BBox
from pptx_shapes.entities.namespace_helper import NamespaceHelper
from pptx_shapes.shapes.shape import Shape


@dataclass
class Group(Shape):
    shapes: List[Shape]

    def to_xml(self, shape_id: int, ns_helper: NamespaceHelper) -> etree.Element:
        node = ns_helper.element("p:grpSp")
        bbox = self.bbox()

        nvgrpsppr = ns_helper.element("p:nvGrpSpPr", parent=node)
        ns_helper.element("p:cNvPr", {"id": str(shape_id), "name": f"Group {shape_id}"}, parent=nvgrpsppr)
        ns_helper.element("p:cNvGrpSpPr", parent=nvgrpsppr)
        ns_helper.element("p:nvPr", parent=nvgrpsppr)

        grpsppr = ns_helper.element("p:grpSpPr", parent=node)
        xfrm = ns_helper.element("a:xfrm", parent=grpsppr)
        ns_helper.element("a:off", {"x": units.cm_to_emu(bbox.x), "y": units.cm_to_emu(bbox.y)}, parent=xfrm)
        ns_helper.element("a:ext", {"cx": units.cm_to_emu(bbox.width), "cy": units.cm_to_emu(bbox.height)}, parent=xfrm)
        ns_helper.element("a:chOff", {"x": units.cm_to_emu(bbox.x), "y": units.cm_to_emu(bbox.y)}, parent=xfrm)
        ns_helper.element("a:chExt", {"cx": units.cm_to_emu(bbox.width), "cy": units.cm_to_emu(bbox.height)}, parent=xfrm)

        for i, shape in enumerate(self.shapes):
            node.append(shape.to_xml(shape_id=shape_id + i + 1, ns_helper=ns_helper))

        return node

    def bbox(self) -> BBox:
        x_min, y_min, x_max, y_max = float("inf"), float("inf"), float("-inf"), float("-inf")

        for shape in self.shapes:
            shape_bbox = shape.bbox()
            x_min, y_min = min(x_min, shape_bbox.x), min(y_min, shape_bbox.y)
            x_max, y_max = max(x_max, shape_bbox.x + shape_bbox.width), max(y_max, shape_bbox.y + shape_bbox.height)

        return BBox(x=x_min, y=y_min, width=x_max - x_min, height=y_max - y_min)

    def count(self) -> int:
        return 1 + sum([shape.count() for shape in self.shapes])
