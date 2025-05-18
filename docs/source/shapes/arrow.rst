.. _arrow:

Arrow
=====

A straight arrow connecting two points.

.. image:: /_static/shapes/arrow.png
   :alt: Arrow example
   :align: center

.. autoclass:: pptx_shapes.shapes.Arrow

**Parameters**

- ``x1`` (`float`) – left position of the start point (in centimeters).
- ``y1`` (`float`) – top position of the start point (in centimeters).
- ``x2`` (`float`) – left position of the end point (in centimeters).
- ``y2`` (`float`) – top position of the end point (in centimeters).
- ``start_head`` (:ref:`ArrowHead <arrow-head>`, optional) – arrowhead at the start point.
- ``end_head`` (:ref:`ArrowHead <arrow-head>`, optional) – arrowhead at the end point.
- ``stroke`` (:ref:`StrokeStyle <stroke-style>`, optional) – stroke style.


**Example**

.. code-block:: python

   from pptx_shapes.shapes import Arrow
   from pptx_shapes.style import StrokeStyle, ArrowHead

   arrow = Arrow(
       x1=10, y1=9,
       x2=14, y2=11,
       start_head=ArrowHead(head=ArrowType.OVAL),
       end_head=ArrowHead(head=ArrowType.ARROW),
       stroke=StrokeStyle(thickness=2)
   )

:ref:`← Back to all shapes <shapes-index>`
