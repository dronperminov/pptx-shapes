import abc
from dataclasses import dataclass

from lxml import etree

from pptx_shapes import units
from pptx_shapes.entities.bbox import BBox
from pptx_shapes.entities.namespace_helper import NamespaceHelper


@dataclass
class Shape:
    @abc.abstractmethod
    def to_xml(self, shape_id: int, ns_helper: NamespaceHelper) -> etree.Element:
        pass

    @abc.abstractmethod
    def bbox(self) -> BBox:
        pass

    def make_xfrm(self, ns_helper: NamespaceHelper, attrib: dict, x: float, y: float, width: float, height: float) -> etree.Element:
        xfrm = ns_helper.element("a:xfrm", attrib)
        ns_helper.element("a:off", {"x": units.cm_to_emu(x), "y": units.cm_to_emu(y)}, parent=xfrm)
        ns_helper.element("a:ext", {"cx": units.cm_to_emu(width), "cy": units.cm_to_emu(height)}, parent=xfrm)
        return xfrm

    def count(self) -> int:
        return 1
