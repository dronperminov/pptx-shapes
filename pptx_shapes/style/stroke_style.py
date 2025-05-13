from dataclasses import dataclass
from typing import Optional

from lxml import etree

from pptx_shapes import units
from pptx_shapes.entities.namespace_helper import NamespaceHelper


@dataclass
class StrokeStyle:
    color: str = "transparent"
    thickness: float = 1.0
    opacity: float = 1.0
    dash: Optional[str] = None

    def to_xml(self, ns_helper: NamespaceHelper) -> etree.Element:
        node = ns_helper.element("a:ln", {"w": units.pt_to_emu(self.thickness)})
        color = ns_helper.element("a:srgbClr", {"val": units.parse_color(self.color)}, parent=ns_helper.element("a:solidFill", parent=node))

        if self.dash is not None:
            ns_helper.element("a:prstDash", {"val": self.__get_dash()}, parent=node)

        if self.opacity < 1:
            ns_helper.element("a:alpha", {"val": units.fraction_to_unit(self.opacity)}, parent=color)

        return node

    def __get_dash(self) -> str:
        dash2pptx = {
            "solid": "solid",
            "dashed": "dash",
            "dotted": "sysDot",
            "short-dashed": "sysDash",
            "dash-dotted": "dashDot",
            "long-dash": "lgDash",
            "long-dash-dotted": "lgDashDot",
            "long-dash-dot-dotted": "lgDashDotDot"
        }
        return dash2pptx[self.dash]
