import math
from dataclasses import dataclass
from typing import Optional

from lxml import etree

from pptx_shapes import units
from pptx_shapes.entities.bbox import BBox
from pptx_shapes.entities.namespace_helper import NamespaceHelper
from pptx_shapes.shapes.shape import Shape
from pptx_shapes.style.fill_style import FillStyle
from pptx_shapes.style.font_format import FontFormat
from pptx_shapes.style.font_style import FontStyle
from pptx_shapes.style.margin import Margin
from pptx_shapes.style.stroke_style import StrokeStyle


@dataclass
class TextBox(Shape):
    x: float
    y: float
    width: float
    height: float
    text: str
    style: FontStyle = FontStyle()
    formatting: FontFormat = FontFormat()
    margin: Margin = Margin(left=0, right=0, top=0, bottom=0)
    auto_fit: bool = False
    angle: float = 0
    fill: Optional[FillStyle] = None
    stroke: Optional[StrokeStyle] = None

    def to_xml(self, shape_id: int, ns_helper: NamespaceHelper) -> etree.Element:
        node = ns_helper.element("p:sp")

        nvsppr = ns_helper.element("p:nvSpPr", parent=node)
        ns_helper.element("p:cNvPr", {"id": str(shape_id), "name": f"TextBox {shape_id}"}, parent=nvsppr)
        ns_helper.element("p:cNvSpPr", {"txBox": "1"}, parent=nvsppr)
        ns_helper.element("p:nvPr", parent=nvsppr)

        sppr = ns_helper.element("p:spPr", parent=node)
        sppr.append(self.make_xfrm(ns_helper, {"rot": units.angle_to_unit(self.angle)}, x=self.x, y=self.y, width=self.width, height=self.height))
        ns_helper.element("a:avLst", parent=ns_helper.element("a:prstGeom", {"prst": "rect"}, parent=sppr))

        self.__make_body(ns_helper, node)

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

    def __make_body(self, ns_helper: NamespaceHelper, node: etree.Element) -> etree.Element:
        tx_body = ns_helper.element("p:txBody", parent=node)
        body_attributes = {
            "anchor": self.style.vertical_align.value,
            "anchorCtr": "0",
            "rtlCol": "0",
            "wrap": "square",
            **self.margin.to_pptx()
        }

        body_pr = ns_helper.element("a:bodyPr", body_attributes, parent=tx_body)
        ns_helper.element("a:spAutoFit" if self.auto_fit else "a:noAutoFit", parent=body_pr)
        ns_helper.element("a:lstStyle", parent=tx_body)

        self.__make_paragraphs(ns_helper, body=tx_body)
        return tx_body

    def __make_paragraphs(self, ns_helper: NamespaceHelper, body: etree.Element) -> None:
        text_attributes = {"dirty": "0", "sz": units.pt_to_font(self.style.size), **self.formatting.to_pptx()}

        for paragraph in self.text.split("\n"):
            p = ns_helper.element("a:p", parent=body)
            ns_helper.element("a:pPr", {"algn": self.style.align.value}, parent=p)
            r = ns_helper.element("a:r", parent=p)
            rpr = ns_helper.element("a:rPr", {"smtClean": "0", **text_attributes}, parent=r)

            if self.style.family != "Calibri":
                ns_helper.element("a:latin", {"typeface": self.style.family}, parent=rpr)

            ns_helper.element("a:srgbClr", {"val": units.parse_color(self.style.color)}, parent=ns_helper.element("a:solidFill", parent=rpr))
            ns_helper.element("a:t", parent=r).text = paragraph
            ns_helper.element("a:endParaRPr", text_attributes, parent=p)
