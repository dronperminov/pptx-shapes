.. _line:

Line
====

A straight line connecting two points.

.. image:: /_static/shapes/line.png
   :alt: Line example
   :align: center

.. autoclass:: pptx_shapes.shapes.Line

**Parameters**

- ``x1`` (`float`) – left position of the start point (in centimeters).
- ``y1`` (`float`) – top position of the start point (in centimeters).
- ``x2`` (`float`) – left position of the end point (in centimeters).
- ``y2`` (`float`) – top position of the end point (in centimeters).
- ``stroke`` (:ref:`StrokeStyle <stroke-style>`, optional) – stroke style.


**Example**

.. code-block:: python

   from pptx_shapes.shapes import Line
   from pptx_shapes.style import StrokeStyle

   Line(x1=13, y1=1, x2=1, y2=6, stroke=StrokeStyle(thickness=2, color="#89dd73"))

:ref:`← Back to all shapes <shapes-index>`
