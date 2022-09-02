.. _af-packet:

AF-PACKET
=========

AF-PACKET is built into the Linux kernel and includes fanout capabilities enabling it to act as a flow-based load balancer.  This means, for example, if you configure Suricata for 4 AF-PACKET threads then each thread would receive about 25% of the total traffic that AF-PACKET is seeing.

.. warning::

   If you try to test AF-PACKET fanout using tcpreplay locally, please note that load balancing will not work properly and all (or most) traffic will be handled by the first worker in the AF-PACKET cluster.  If you need to test AF-PACKET load balancing properly, you can run tcpreplay on another machine connected to your AF-PACKET machine.

The following processes use AF-PACKET for packet acquisition:

- :ref:`stenographer`

- :ref:`suricata`

- :ref:`zeek`

VLAN tags
---------

.. warning::

   | Please note that :ref:`zeek` and :ref:`stenographer` should correctly analyze traffic on a VLAN but won't log the actual VLAN tags due to the way that :ref:`af-packet` works:
   | https://github.com/J-Gras/zeek-af_packet-plugin/issues/9
   | https://github.com/google/stenographer/issues/211

More Information
----------------

.. seealso::

   | For more information about AF-PACKET, please see:
   | https://www.kernel.org/doc/Documentation/networking/packet_mmap.txt
