from dataclasses import dataclass

from lxml import etree


@dataclass
class Slide:
    tree: etree.ElementTree
    sp_tree: etree.ElementTree
