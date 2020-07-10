.. _so-import-pcap:

so-import-pcap
==============

``so-import-pcap`` will import one or more pcaps into Security Onion and preserve original timestamps.

It will do the following:

-  generate IDS alerts using Suricata
-  generate Zeek logs
-  store IDS alerts and Zeek logs with original timestamps
-  store pcaps where Security Onion Console (SOC) can find them

Minimum Requirements
--------------------

-  50GB storage
-  12GB RAM
-  4 CPU cores

Please note these are MINIMUM requirements.  If you can allocate more resources, please do so.

.. warning::

   so-import-pcap works differently on Security Onion 2.0 than it did in previous versions! Please consider this new version to be experimental!
   
   
Usage
-----

Run through Setup choosing Eval or Standalone. Then run ``so-import-pcap`` and supply the full path to at least one pcap file.

For example, to import a single pcap named ``import.pcap``:

::

    sudo so-import-pcap /full/path/to/import.pcap

To import multiple pcaps:

::

    sudo so-import-pcap /full/path/to/import1.pcap /full/path/to/import2.pcap
