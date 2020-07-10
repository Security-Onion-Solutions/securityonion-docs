.. _so-import-pcap:

so-import-pcap
==============

``so-import-pcap`` will import one or more pcaps into Security Onion and preserve original timestamps.

It will do the following:

-  generate IDS alerts using Suricata
-  generate Zeek logs
-  store IDS alerts and Zeek logs with original timestamps
-  store pcaps where :ref:`soc` can find them

Usage
-----

.. warning::

   so-import-pcap works differently on Security Onion 2.0 than it did in previous versions! 
   
   Please consider this new version to be experimental!

This new version of so-import-pcap currently requires you to run through Setup first. You can choose Eval or Standalone. Once Setup completes, you can then run ``so-import-pcap`` and supply the full path to at least one pcap file.

For example, to import a single pcap named ``import.pcap``:

::

    sudo so-import-pcap /full/path/to/import.pcap

To import multiple pcaps:

::

    sudo so-import-pcap /full/path/to/import1.pcap /full/path/to/import2.pcap
