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

Command Line
------------
You can also access packet capture from the command line of the box where the pcap is stored using a steno query as defined at https://github.com/google/stenographer#querying. In the following examples, replace "YourStenoQueryHere" with your actual steno query.

The first option is using docker to run ``stenoread``. If the query succeeds, you can then find the resulting pcap file in ``/nsm/pcaptmp/`` in the host filesystem:

::

    sudo docker exec -it so-steno stenoread "YourStenoQueryHere" -w /tmp/new.pcap

Starting in Security Onion 2.3.70, we've included a wrapper script called ``so-pcap-export`` to make this a little easier. For example:

::

    sudo so-pcap-export "YourStenoQueryHere" output.pcap

Configuration
-------------
Stenographer reads its configuration from ``/opt/so/conf/steno/``. However, please keep in mind that if you make any changes to this directory they may be overwritten since the configuration is managed with :ref:`salt`.

Maximum Files
-------------
By default, Stenographer limits the number of files in the pcap directory to 30K to avoid limitations with the ext3 filesystem. However, if you're using the ext4 or xfs filesystems, then it is safe to increase this value. So if you have a large amount of storage and find that you only have 3 weeks worth of PCAP on disk while still having plenty of free space, then you may want to increase this default setting. Starting in Security Onion 2.3.80, this is controlled by the ``maxfiles`` option in the ``steno`` section of the :ref:`salt` pillar. In older versions, you can manually modify as follows:

- copy ``/opt/so/saltstack/default/salt/pcap/files/config`` to ``/opt/so/saltstack/local/salt/pcap/files/config``
- edit ``/opt/so/saltstack/local/salt/pcap/files/config`` and increase ``MaxDirectoryFiles`` to a higher value
- restart Stenographer using ``sudo so-pcap-restart``

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
