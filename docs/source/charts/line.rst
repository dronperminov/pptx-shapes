Line Chart
==========

The ``LineChart`` component renders a line chart with optional smoothing, markers, value labels, and category labels.
It is useful for visualizing time series or continuous numerical data.

.. autoclass:: pptx_shapes.charts.line.LineChart
    :members:
    :undoc-members:

A line chart consists of the following elements:

- A polyline connecting all data points (optionally smoothed)
- Optional background fill under the curve
- Circular markers at each point
- Value labels positioned above each point
- Category labels (e.g., months) below each point

Configuration
-------------

Configuration is done via the :ref:LineChartConfig <line-chart-config>, which includes:

- :ref:`LineConfig <line-chart-line-config>` – controls color, background and thickness of the line
- :ref:`MarkerConfig <line-chart-marker-config>` – controls appearance of point markers
- :ref:`LabelConfig <line-chart-label-config>` – controls font styles for value and category labels

.. currentmodule:: pptx_shapes.charts.line.config

.. _line-chart-line-config:

LineConfig
~~~~~~~~~~

.. autoclass:: pptx_shapes.charts.line.LineConfig
   :noindex:

**Attributes:**

- ``color`` (`str`) – color of the line, default: ``"#fe7a81"``.
- ``background`` (`str`) – fill color under the line, default: ``"#fe7a81"``.
- ``background_opacity`` (`float`) – opacity of the fill (0.0–1.0), default: ``0.1``.
- ``thickness`` (`float`) – thickness of the line, default: ``1.5``.

**Example:**

.. code-block:: python

    line = LineConfig(
        color="#fe7a81",
        background="#ffddd7",
        background_opacity=1,
        thickness=1.5
    )

.. _line-chart-marker-config:

MarkerConfig
~~~~~~~~~~~~

.. autoclass:: pptx_shapes.charts.line.MarkerConfig
   :members:

**Attributes:**

- ``color`` (`str`) – marker border color, default: ``"#fe7a81"``.
- ``background`` (`str`) – marker fill color, default: ``"#ffffff"``.
- ``radius`` (`float`) – marker radius, default: ``0.1``.
- ``width`` (`float`) – marker width, default: ``1.5``.
- ``height`` (`float`) – marker height, default: ``8``.
- ``thickness`` (`float`) – outline thickness, default: ``1.5``.

**Example:**

.. code-block:: python

    marker = MarkerConfig(
        radius=0.16,
        width=2.6,
        height=14,
        thickness=2
    )

.. _line-chart-label-config:

LabelConfig
~~~~~~~~~~~

.. autoclass:: pptx_shapes.charts.line.LabelConfig
   :members:

**Attributes:**

- ``size`` (`float`) – font size of the label, default: ``8``.
- ``color`` (`str`) – text color, default: ``"#222222"``.
- ``family`` (`str`) – font family used for the text, default: ``"Calibri"``.
- ``height`` (`float`) – vertical space reserved for the label, default: ``1``.

**Example:**

.. code-block:: python

    label = LabelConfig(
        color="#fe7a81",
        size=12
    )

.. _line-chart-config:

LineChartConfig
~~~~~~~~~~~~~~~

.. autoclass:: pptx_shapes.charts.line.LineChartConfig
   :members:

**Attributes**:

- ``line`` (:ref:`LineConfig <line-chart-line-config>`) – appearance of the line and background.
- ``marker`` (:ref:`MarkerConfig <line-chart-marker-config>`) – appearance of point markers.
- ``value`` (:ref:`LabelConfig <line-chart-label-config>`) – value text config.
- ``label`` (:ref:`LabelConfig <line-chart-label-config>`) – label text config.
- ``smooth_count`` (`int`) – number of interpolated points for smoothing, default: ``20``.

Example usage
-------------

.. literalinclude:: ../../../examples/charts/line_chart.py
   :language: python
   :linenos:

It creates a line chart where:

- Line is styled with a colored stroke and filled background
- Markers are placed at each data point
- Value labels appear above each marker
- Multi-line category labels appear below each marker

Result
------

This script produces a file ``line_chart.pptx`` with a line chart rendered on a blank slide.
Each point shows a value and a category label (typically a month and year).
The line is optionally smoothed and styled via config parameters.

.. image:: /_static/charts/line.png
   :alt: Line chart example
   :align: center

You can adjust smoothing, line appearance, markers and text styling via configuration.
