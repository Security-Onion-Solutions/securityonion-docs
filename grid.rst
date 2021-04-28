.. _grid:

Grid
====

:ref:`soc` gives you access to our new Grid interface. This interface allows you to quickly check the status of all nodes in your grid. If you have purchased our official appliances, then the grid page will show pictures of the front and rear of the appliances, useful for walking through connectivity discussions with personnel in the data center.

.. image:: images/grid.png
  :target: _images/grid.png

This page includes a few different EPS (events per second) measurements:

- EPS (also shown as Production EPS) is how much a node is producing. This is taken from the number of events out in filebeat.

- Consumption EPS is how much a search node is consuming. 

- Grid EPS in the upper right corner is the sum of all Consumption EPS measurements in the entire grid.

