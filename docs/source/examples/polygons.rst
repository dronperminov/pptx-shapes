Polygons split example
======================

This example demonstrates how to create a dynamic tiling of polygons on a PowerPoint slide.
It uses the :ref:`Polygon <polygon>` and :ref:`Group <group>` shapes,
as well as :ref:`FillStyle <fill-style>` and :ref:`StrokeStyle <stroke-style>` from the ``pptx_shapes`` library.

The script defines an iterative polygon-splitting algorithm. Starting with a single square,
it repeatedly splits polygons using lines and adds the result as groups of colored polygons to a slide.

Overview
--------

- Start from a single square polygon
- Iteratively split polygons using defined lines
- Assign new colors to sub-polygons after each split
- Map logical coordinates to slide coordinates
- Add results as grouped shapes to the slide

Example Code
------------

.. literalinclude:: ../../../examples/polygons.py
   :language: python
   :linenos:

Result
------

This example produces a grid of polygon patterns, each illustrating the effect of applying a new splitting line.

.. image:: /_static/examples/polygons.png
   :alt: Basic example
   :align: center

Each shape is created using:

- :ref:`Polygon <polygon>` – to represent each polygon
- :ref:`Group <group>` – to group multiple polygons as one object
- :ref:`FillStyle <fill-style>` and :ref:`StrokeStyle <stroke-style>` – for styling the fill and stroke

.. note::
   Logical coordinates are automatically transformed to slide coordinates using the provided limits and size parameters.

Output file: ``polygons.pptx``
