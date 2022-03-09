.. _grid:

Grid
====

:ref:`soc` gives you access to our Grid interface. This interface allows you to quickly check the status of all nodes in your grid. It also includes a few different EPS (events per second) measurements:

- EPS (also shown as Production EPS) is how much a node is producing. This is taken from the number of events out in :ref:`filebeat`.

- Consumption EPS is how much a search node is consuming. 

- Grid EPS in the upper right corner is the sum of all Consumption EPS measurements in the entire grid.


.. image:: images/grid.png
  :target: _images/grid.png

If you have purchased our official Security Onion Solutions appliances, then the grid page will show pictures of the front and rear of the appliances, useful for walking through connectivity discussions with personnel in the data center. If you are not using official Security Onion Solutions appliances, then it will simply display a message to that effect.

If any nodes show anything other than ``OK``, then run :ref:`so-status` on the node and check logs in ``/opt/so/log/``.
