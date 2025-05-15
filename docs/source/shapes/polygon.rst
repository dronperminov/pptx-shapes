.. _polygon:

Polygon
=======

An polygon (oval or circle), positioned by its bounding box.

.. image:: /_static/shapes/polygon.png
   :alt: Polygon example
   :align: center

.. autoclass:: pptx_shapes.shapes.Polygon

**Parameters**

- ``points`` (`List[Tuple[float, float]]`) – a list of tuples of ``(x, y)`` coordinates that define the vertices of the polygon.
- ``angle`` (`float`, optional) – rotation in degrees, default is ``0``.
- ``fill`` (:ref:`FillStyle <fill-style>`, optional) – fill style.
- ``stroke`` (:ref:`StrokeStyle <stroke-style>`, optional) – stroke style.


**Example**

.. code-block:: python

   from pptx_shapes.shapes import Polygon
   from pptx_shapes.style import FillStyle, StrokeStyle

   polygon = Polygon(
       points=[(15, 5), (16, 6), (15, 7), (12, 7), (11, 6), (12, 5)],
       angle=45,
       fill=FillStyle(color="#88ff88"),
       stroke=StrokeStyle(color="magenta", thickness=2.5)
   )

:ref:`← Back to all shapes <shapes-index>`
