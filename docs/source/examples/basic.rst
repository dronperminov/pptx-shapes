.. _basic-example:


Basic example
=============

This example demonstrates a variety of shape types, styling options, and layout techniques supported by `pptx-shapes`.

.. image:: /_static/examples/basic.png
   :alt: Basic example
   :align: center

Overview
--------

The script:

- Opens a base PowerPoint file with one empty slide (``empty.pptx``)
- Adds shapes such as ``TextBox``, ``Ellipse``, ``Arrow``, ``Arc``, ``Rectangle``, ``Polygon``, and ``Group``
- Demonstrates:
  - Filled and outlined shapes
  - Text with styling and rotation
  - Groups of multiple elements
  - Use of coordinates, angles, and alignment
  - Color and opacity settings

Key features illustrated
------------------------

- **Text and formatting**: bold, size, color, alignment, rotation
- **Stroke styles**: thickness, dashed lines, opacity
- **Fill styles**: colors including hex, named, opacity
- **Shapes**: rectangles (rounded or not), ellipses, arcs, arrows, polygons
- **Groups**: reusable composite structures (e.g., labeled triangle, histogram)
- **Alignment and layout**: both manual coordinates and automatic ``auto_fit``

Example code
------------

.. literalinclude:: ../../../examples/basic.py
   :language: python
   :linenos:

Output
------

The script generates a file ``basic.pptx`` with all the illustrated shapes. Below is a preview of what it might contain:

- A diagonal "Hello from pptx-shapes!" textbox
- Ellipses with fills and stroke transparency
- Colored and dashed arcs
- Classic arrows with arrowheads
- Rotated and grouped shapes with styled text
- Custom polygons with fill and outline
- A small histogram composed of styled rectangles

.. note::
   This example assumes you have an ``empty.pptx`` file to use as a base presentation template.
