.. _stenographer:

Stenographer
============

From https://github.com/google/stenographer:

    Stenographer is a full-packet-capture utility for buffering packets to disk for intrusion detection and incident response purposes. It provides a high-performance implementation of NIC-to-disk packet writing, handles deleting those files as disk fills up, and provides methods for reading back specific sets of packets quickly and easily.

Stenographer uses :ref:`af-packet` for packet acquisition.

Output
------
Stenographer writes full packet capture to ``/nsm/pcap/``. It will automatically start purging old data once the partition reaches 90%.

Analysis
--------
You can access full packet capture via the :ref:`pcap` interface:

.. image:: images/pcap-transcript.png
  :target: _images/pcap-transcript.png

:ref:`alerts`, :ref:`hunt`, and :ref:`kibana` allow you to easily pivot to the :ref:`pcap` interface.

Alternatively, you can access packet capture from the command line using ``stenoread`` and a steno query as defined at https://github.com/google/stenographer#querying. In the following example, replace "YourStenoQueryHere" with your actual steno query:

::

    sudo docker exec -it so-steno stenoread "YourStenoQueryHere" -w /tmp/new.pcap

You can then find the resulting pcap file in ``/nsm/pcaptmp/`` in the host filesystem.

Configuration
-------------
Stenographer reads its configuration from ``/opt/so/conf/steno/``. However, please keep in mind that if you make any changes to this directory they may be overwritten since the configuration is managed with :ref:`salt`.

Diagnostic Logging
------------------
Diagnostic logging for Stenographer can be found at ``/opt/so/log/stenographer/``.

Disabling
---------
If you need to disable Stenographer, you can set the :ref:`salt` pillar ``steno:enabled:false`` in the ``global.sls`` or in the sensor's ``minion.sls`` file.

More Information
----------------

.. seealso::

    For more information about stenographer, please see https://github.com/google/stenographer.
