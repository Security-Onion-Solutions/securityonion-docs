.. _stenographer:

Stenographer
============

From https://github.com/google/stenographer:

    Stenographer is a full-packet-capture utility for buffering packets to disk for intrusion detection and incident response purposes. It provides a high-performance implementation of NIC-to-disk packet writing, handles deleting those files as disk fills up, and provides methods for reading back specific sets of packets quickly and easily.

Stenographer uses :ref:`af-packet` for packet acquisition.

Analysis
--------
You can access full packet capture via :ref:`soc`. :ref:`kibana` and :ref:`hunt` allow you to easily pivot to SOC for pcap.

Configuration
-------------
Stenographer configuration can be found at ``/opt/so/conf/steno/``.

Logging
-------
Stenographer logging can be found at ``/opt/so/log/stenographer/``.

More Information
----------------

.. seealso::

    For more information about stenographer, please see https://github.com/google/stenographer.
