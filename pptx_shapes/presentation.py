import os
import tempfile
import types
import zipfile

from lxml import etree

from pptx_shapes.entities.namespace_helper import NamespaceHelper
from pptx_shapes.entities.slide import Slide
from pptx_shapes.shapes.shape import Shape


class Presentation:
    def __init__(self, presentation_path: str) -> None:
        self.presentation_path = presentation_path
        self.work_directory = None

        self.namespaces = {
            "p": "http://schemas.openxmlformats.org/presentationml/2006/main",
            "a": "http://schemas.openxmlformats.org/drawingml/2006/main",
            "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
        }

        self.ns_helper = NamespaceHelper(namespaces=self.namespaces)
        self.slides = {}
        self.shape_id = 1

    def add(self, shape: Shape, slide: str = "slide1") -> None:
        node = shape.to_xml(shape_id=self.shape_id, ns_helper=self.ns_helper)
        self.__add_to_slide(slide=slide, node=node)
        self.shape_id += shape.count()

    def save(self, path: str, compress_level: int = 9) -> None:
        for name, slide in self.slides.items():
            slide.tree.write(os.path.join(self.work_directory.name, "ppt", "slides", f"{name}.xml"))

        with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED, compresslevel=compress_level) as f:
            for root, _, files in os.walk(self.work_directory.name):
                for file in files:
                    f.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), self.work_directory.name))

    def __enter__(self) -> "Presentation":
        if not os.path.exists(self.presentation_path):
            raise FileNotFoundError(f'No such file "{self.presentation_path}"')

        if not os.path.isfile(self.presentation_path):
            raise IsADirectoryError(f'"{self.presentation_path}" is a directory')

        if not zipfile.is_zipfile(self.presentation_path):
            raise zipfile.BadZipFile(f'File "{self.presentation_path}" is not a pptx presentation')

        self.work_directory = tempfile.TemporaryDirectory()

        with zipfile.ZipFile(self.presentation_path, "r") as f:
            f.extractall(self.work_directory.name)

        return self

    def __exit__(self, exc_type: type[BaseException], exc_val: BaseException, exc_tb: types.TracebackType) -> None:
        if self.work_directory is not None:
            self.work_directory.cleanup()

    def __add_to_slide(self, slide: str, node: etree.Element) -> None:
        if slide not in self.slides:
            tree = etree.parse(os.path.join(self.work_directory.name, "ppt", "slides", f"{slide}.xml"))
            sp_tree = tree.getroot().find("p:cSld", self.namespaces).find("p:spTree", self.namespaces)
            self.slides[slide] = Slide(tree=tree, sp_tree=sp_tree)

        self.slides[slide].sp_tree.append(node)
