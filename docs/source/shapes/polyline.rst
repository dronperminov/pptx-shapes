.. _polyline:

Polyline
========

An polyline, positioned by its bounding box.

.. image:: /_static/shapes/polyline.png
   :alt: Polyline example
   :align: center

.. autoclass:: pptx_shapes.shapes.Polyline

**Parameters**

- ``points`` (`List[Tuple[float, float]]`) – a list of tuples of ``(x, y)`` coordinates that define the vertices of the polyline.
- ``angle`` (`float`, optional) – rotation in degrees, default is ``0``.
- ``stroke`` (:ref:`StrokeStyle <stroke-style>`, optional) – stroke style.


**Example**

.. code-block:: python

   from pptx_shapes.shapes import Polyline
   from pptx_shapes.style import StrokeStyle

   polyline = Polyline(
       points=[(15, 5), (16, 6), (15, 7), (12, 7), (11, 6), (12, 5)],
       angle=45,
       stroke=StrokeStyle(color="magenta", thickness=2.5)
   )

:ref:`← Back to all shapes <shapes-index>`
