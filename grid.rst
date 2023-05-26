.. _grid:

Grid
====

:ref:`soc` includes a Grid interface which allows you to quickly check the status of all nodes in your grid.

.. image:: images/46_grid.png
  :target: _images/46_grid.png

Starting at the top of the page, there is a ``Grid EPS`` value in the upper right corner that shows the sum of all Consumption EPS measurements in the entire grid. Below that you will find a list of all nodes in your grid.

.. note::

  Please note that new nodes start off showing a red Fault and may take a few minutes to fully initialize before they show a green OK.

You can drill into individual nodes to see detailed information including Node Status, Container Status, and Appliance Images.

Node Status
-----------

This section includes an overview of node status.

Online Since
~~~~~~~~~~~~

The ``Online Since`` field shows how long the node has been online.

Production EPS
~~~~~~~~~~~~~~

The ``Production EPS`` field is how much a node is producing. This is taken from the number of events out in :ref:`elastic-agent`.

Consumption EPS
~~~~~~~~~~~~~~~

The ``Consumption EPS`` field is how much a search node is consuming. 

Process Status
~~~~~~~~~~~~~~

If the ``Process Status`` field shows ``Fault``, you can check the ``Container Status`` section to determine which process has failed.

Connection Status
~~~~~~~~~~~~~~~~~

The ``Connection Status`` field shows whether or not the node is currently connected to the grid.

RAID Status
~~~~~~~~~~~

If you are using an official Security Onion Solutions appliance with RAID support, then you will see the corresponding status appear in this field.

Description
~~~~~~~~~~~

The ``Description`` field shows the optional Description you may have entered during Setup.

Link to InfluxDB
~~~~~~~~~~~~~~~~

The first icon in the lower left of the ``Node Status`` section hyperlinks you to the InfluxDB dashboard for that particular node.

Link to Sensor Test
~~~~~~~~~~~~~~~~~~~

The second icon in the lower left of the ``Node Status`` section displays if the node is a sensor and allows you to send test data to the sensor.

Container Status
----------------

If any containers show anything other than ``running``, then you might want to double-check the configuration for that container and check the corresponding logs in ``/opt/so/log/``.

Appliance Images
----------------

If you have purchased our official Security Onion Solutions appliances, then the grid page will show pictures of the front and rear of the appliances, useful for walking through connectivity discussions with personnel in the data center. If you are not using official Security Onion Solutions appliances, then it will simply display a message to that effect.
