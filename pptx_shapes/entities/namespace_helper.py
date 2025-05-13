from typing import Dict, Optional

from lxml import etree


class NamespaceHelper:
    def __init__(self, namespaces: Dict[str, str]) -> None:
        self.namespaces = namespaces

    def element(self, tag: str, attrib: Optional[dict] = None, parent: Optional[etree.Element] = None) -> etree.Element:
        namespace, tag_name = tag.split(":")
        node = etree.Element(etree.QName(self.namespaces[namespace], tag_name), attrib=attrib)

        if parent is not None:
            parent.append(node)

        return node
