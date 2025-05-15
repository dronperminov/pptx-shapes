.. _arch:

Arch
====

A ring-shaped arc defined by the bounding box, thickness, and angular range. It is based on PowerPoint’s ``blockArc`` shape.

.. image:: /_static/shapes/arch.png
   :alt: Arch example
   :align: center

.. autoclass:: pptx_shapes.shapes.Arch

**Parameters**

- ``x`` (`float`) – left position (in centimeters).
- ``y`` (`float`) – top position (in centimeters).
- ``width`` (`float`) – width (in centimeters).
- ``height`` (`float`) – height (in centimeters).
- ``thickness`` (`float`) –  width of the ring (in centimeters).
- ``start_angle`` (`float`, optional) – start angle of the arch (in degrees, default ``0``)
- ``end_angle`` (`float`, optional) – end angle of the arch (in degrees, default ``180``)
- ``angle`` (`float`, optional) – rotation in degrees, default is ``0``.
- ``fill`` (:ref:`FillStyle <fill-style>`, optional) – fill style.
- ``stroke`` (:ref:`StrokeStyle <stroke-style>`, optional) – stroke style.


**Example**

.. code-block:: python

   from pptx_shapes.enums import LineDash
   from pptx_shapes.shapes import Arch
   from pptx_shapes.style import StrokeStyle

   arch = Arch(
       x=24, y=9, width=5, height=8,
       thickness=2,
       start_angle=90, end_angle=270,
       stroke=StrokeStyle(color="#f00", thickness=2.5, dash=LineDash.DASH_DOTTED)
   )

:ref:`← Back to all shapes <shapes-index>`
