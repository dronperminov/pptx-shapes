Scatter Plot
============

The ``ScatterPlot`` chart allows you to render a 2D scatter plot using customizable points and axis configuration.
This chart is ideal for visualizing distributions, clusters, or geometric patterns in data.

.. autoclass:: pptx_shapes.charts.scatter.ScatterPlot
    :members:
    :undoc-members:

A scatter plot consists of the following elements:

- A list of :ref:`ScatterPoint <scatter-plot-point>` plotted by their (x, y) coordinates
- Optional X and Y axes with ticks and labels
- Configurable spacing, dimensions, and visual styles

Configuration
-------------

Configuration is managed through :ref:`ScatterPlotConfig <scatter-plot-config>`, which includes:

- :ref:`Axes <scatter-plot-axes>` — controls axes appearance, labels, and ticks
- :ref:`Limits <scatter-plot-limits>` — defines data bounds and mapping to canvas

.. currentmodule:: pptx_shapes.charts.scatter.config

.. _scatter-plot-axes:

Axes
~~~~

.. autoclass:: pptx_shapes.charts.scatter.config.Axes
   :noindex:

**Attributes:**

- ``color`` (`str`) – axes color, default: ``"#555"``.
- ``show_x`` (`bool`) – whether to render X axis, default: ``True``.
- ``show_y`` (`bool`) – whether to render Y axis, default: ``True``.
- ``thickness`` (`float`) – stroke thickness of axes, default: ``1``.
- ``tick_length`` (`float`) – length of tick marks, default: ``0.3``.
- ``font`` (`AxesFont`) – font style for axis labels.
- ``text_size`` (`float`) – label text size in cm, default: ``1``.

.. autoclass:: pptx_shapes.charts.scatter.config.AxesFont
   :noindex:

**AxesFont attributes:**

- ``size`` (`float`) – font size in pt, default: ``8``.
- ``color`` (`str`) – font color, default: ``"#222"``.
- ``family`` (`str`) – font family, default: ``"Calibri"``.

.. _scatter-plot-limits:

Limits
~~~~~~

.. autoclass:: pptx_shapes.charts.scatter.config.Limits
   :noindex:

Limits define the bounding box of the data used for coordinate mapping.

**Attributes:**

- ``x_min``, ``x_max`` (`float`) – min/max for X axis.
- ``y_min``, ``y_max`` (`float`) – min/max for Y axis.

.. _scatter-plot-point:

ScatterPoint
~~~~~~~~~~~~

.. autoclass:: pptx_shapes.charts.scatter.point.ScatterPoint
   :members:

**Attributes:**

- ``x``, ``y`` (`float`) – data point coordinates.
- ``radius`` (`float`) – radius of the point in cm, default: ``0.5``.
- ``fill`` (:ref:`FillStyle <fill-style>`) – point fill style.
- ``stroke`` (:ref:`StrokeStyle <stroke-style>`) – point border style.

.. _scatter-plot-config:

ScatterPlotConfig
~~~~~~~~~~~~~~~~~

.. autoclass:: pptx_shapes.charts.scatter.config.ScatterPlotConfig
   :members:

**Attributes:**

- ``x``, ``y`` (`float`) – top-left position of the plot on slide.
- ``width``, ``height`` (`float`) – chart dimensions, default: ``8×8`` cm.
- ``padding`` (`float`) – inner padding (space from axes), default: ``0.2`` cm.
- ``axes`` (`Axes`) – axes style and visibility.
- ``limits`` (`Optional[Limits]`) – optional manual bounds, otherwise auto-computed.

Example usage
-------------

.. literalinclude:: ../../../examples/charts/scatter_plot.py
   :language: python
   :linenos:

Result
------

This script generates a file ``scatter_plot.pptx`` with a scatter plot on a blank slide.
Points are rendered as colored circles with configurable radius and style.

Axes, scale, and spacing are customizable via the config.

.. image:: /_static/charts/scatter.png
   :alt: Scatter plot example
   :align: center

.. note::
   If no limits are provided, bounds are automatically determined from the data.
