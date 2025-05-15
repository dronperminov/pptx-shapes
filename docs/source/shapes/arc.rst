.. _arc:

Arc
===

A curved segment defined by the bounding box and start/end angles.

.. image:: /_static/shapes/arc.png
   :alt: Arc example
   :align: center

.. image:: /_static/shapes/arc_fill.png
   :alt: Arc example
   :align: center

.. autoclass:: pptx_shapes.shapes.Arc

**Parameters**

- ``x`` (`float`) – left position (in centimeters).
- ``y`` (`float`) – top position (in centimeters).
- ``width`` (`float`) – width (in centimeters).
- ``height`` (`float`) – height (in centimeters).
- ``start_angle`` (`float`, optional) – start angle of the arc (in degrees, default ``0``)
- ``end_angle`` (`float`, optional) – end angle of the arc (in degrees, default ``180``)
- ``angle`` (`float`, optional) – rotation in degrees, default is ``0``.
- ``fill`` (:ref:`FillStyle <fill-style>`, optional) – fill style.
- ``stroke`` (:ref:`StrokeStyle <stroke-style>`, optional) – stroke style.


**Example**

.. code-block:: python

   from pptx_shapes.enums import LineDash
   from pptx_shapes.shapes import Arc
   from pptx_shapes.style import StrokeStyle

   arc = Arc(
       x=24, y=9,
       width=5, height=8,
       start_angle=90, end_angle=270,
       stroke=StrokeStyle(color="#f00", thickness=2.5, dash=LineDash.DASH_DOTTED)
   )

:ref:`← Back to all shapes <shapes-index>`
