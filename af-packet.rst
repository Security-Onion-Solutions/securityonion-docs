.. _af-packet:

AF-PACKET
=========

The following process use AF-PACKET for packet acquisition:

:ref:`stenographer`

:ref:`suricata`

:ref:`zeek`

.. warning::

   If you try to test AF-PACKET load balancing using tcpreplay locally, please note that load balancing will not work properly and all (or most) traffic will be handled by the first worker in the AF-PACKET cluster.  If you need to test AF-PACKET load balancing properly, you can run tcpreplay on another machine connected to your AF-PACKET machine.
