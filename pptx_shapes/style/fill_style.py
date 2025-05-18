from dataclasses import dataclass

from lxml import etree

from pptx_shapes import units
from pptx_shapes.entities.namespace_helper import NamespaceHelper


@dataclass
class FillStyle:
    color: str
    opacity: float = 1.0

    def to_xml(self, ns_helper: NamespaceHelper) -> etree.Element:
        node = ns_helper.element("a:solidFill")
        color = ns_helper.element("a:srgbClr", {"val": units.parse_color(self.color)}, parent=node)

        if self.opacity < 1:
            ns_helper.element("a:alpha", {"val": units.fraction_to_unit(self.opacity)}, parent=color)

        return node
