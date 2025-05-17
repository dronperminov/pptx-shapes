pptx-shapes
===========

**pptx-shapes** is a Python library for adding basic geometric shapes directly to PowerPoint (.pptx) slides by editing the underlying XML structure.

.. image:: https://github.com/dronperminov/pptx-shapes/raw/master/examples/main.png
    :alt: Example usage
    :align: center


Features
--------

- Add basic shapes (ellipse, line, polygon, etc.) to existing slides
- Control position, size, fill, stroke, rotation, and other styles
- Work directly with the slide XML
- Save as a ``.pptx`` file after editing


Installation
------------

Install via pip:

.. code-block:: bash

   pip install pptx-shapes


Quick Start
-----------

.. code-block:: python

   from pptx_shapes import Presentation
   from pptx_shapes.shapes import Ellipse, Rectangle, TextBox
   from pptx_shapes.style import FillStyle, FontFormat, FontStyle, StrokeStyle

   with Presentation(presentation_path="empty.pptx") as presentation:
       presentation.add(shape=TextBox(
           x=23, y=4, width=12, height=2, angle=45,
           text="Hello from pptx-shapes!",
           style=FontStyle(size=32),
           formatting=FontFormat(bold=True)
       ))

       presentation.add(shape=Ellipse(
           x=20, y=2, width=4, height=4,
           fill=FillStyle(color="#7699d4")
       ))

       presentation.add(shape=Rectangle(
           x=18, y=8, width=4, height=8.5, radius=0.25, angle=30,
           fill=FillStyle(color="#dd7373"),
           stroke=StrokeStyle(color="magenta", thickness=3)
       ))

       presentation.save("result.pptx")

How It Works
------------

PowerPoint ``.pptx`` files are ZIP archives containing XML files. This library:

- Unzips the archive
- Modifies the relevant slide XML (e.g., ``ppt/slides/slide1.xml``)
- Inserts new shape elements (e.g., ``<p:sp>``, ``<a:prstGeom>``, etc.)
- Repackages the content into a new ``.pptx`` file

This low-level approach is ideal for automated slide generation, data visualizations, and geometric illustrations –
especially when you need to create many shapes or apply programmatic styles.


Supported Shapes
----------------

- :ref:`Line <line>`
- :ref:`Arrow <arrow>`
- :ref:`Arc <arc>`
- :ref:`Arch <arch>`
- :ref:`Ellipse <ellipse>`
- :ref:`Rectangle <rectangle>`
- :ref:`Pie <pie>`
- :ref:`Polygon <polygon>`
- :ref:`TextBox <textBox>`
- :ref:`Group <group>`

Each shape supports style customization (e.g., stroke, fill, angle). See :doc:`shapes` for detailed parameters.


API Documentation
-----------------

.. toctree::
   :maxdepth: 2

   shapes
   charts
   style
   enums


Examples
--------

.. toctree::
   :maxdepth: 1

   examples/basic
   examples/text_boxes
   examples/polygons
