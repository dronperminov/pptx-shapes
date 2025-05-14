from dataclasses import dataclass

from lxml import etree

from pptx_shapes import units
from pptx_shapes.entities.namespace_helper import NamespaceHelper
from pptx_shapes.enums import LineDash


@dataclass
class StrokeStyle:
    color: str = "black"
    thickness: float = 1.0
    opacity: float = 1.0
    dash: LineDash = LineDash.SOLID

    def to_xml(self, ns_helper: NamespaceHelper) -> etree.Element:
        node = ns_helper.element("a:ln", {"w": units.pt_to_emu(self.thickness)})
        color = ns_helper.element("a:srgbClr", {"val": units.parse_color(self.color)}, parent=ns_helper.element("a:solidFill", parent=node))

        ns_helper.element("a:prstDash", {"val": self.dash.value}, parent=node)

        if self.opacity < 1:
            ns_helper.element("a:alpha", {"val": units.fraction_to_unit(self.opacity)}, parent=color)

        return node
