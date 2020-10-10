.. _stenographer:

Stenographer
============

From https://github.com/google/stenographer:

    Stenographer is a full-packet-capture utility for buffering packets to disk for intrusion detection and incident response purposes. It provides a high-performance implementation of NIC-to-disk packet writing, handles deleting those files as disk fills up, and provides methods for reading back specific sets of packets quickly and easily.

Stenographer uses :ref:`af-packet` for packet acquisition.

Output
------
Stenographer writes full packet capture to ``/nsm/pcap/``.

Analysis
--------
You can access full packet capture via :ref:`pcap`:

.. image:: https://user-images.githubusercontent.com/1659467/92967656-a49f9a80-f447-11ea-9923-e0beaf39487d.png
  :target: https://user-images.githubusercontent.com/1659467/92967656-a49f9a80-f447-11ea-9923-e0beaf39487d.png

:ref:`alerts`, :ref:`hunt`, and :ref:`kibana` allow you to easily pivot to the :ref:`pcap` page

Configuration
-------------
Stenographer reads its configuration from ``/opt/so/conf/steno/``. However, please keep in mind that if you make any changes to this directory they may be overwritten since the configuration is managed with :ref:`salt`.

Diagnostic Logging
------------------
Diagnostic logging for Stenographer can be found at ``/opt/so/log/stenographer/``.

More Information
----------------

.. seealso::

    For more information about stenographer, please see https://github.com/google/stenographer.
