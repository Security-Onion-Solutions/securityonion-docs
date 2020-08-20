.. _so-import-pcap:

so-import-pcap
==============

``so-import-pcap`` will import one or more pcaps into Security Onion and preserve original timestamps.

It will do the following:

-  generate IDS alerts using :ref:`suricata`
-  generate network metadata using :ref:`zeek`
-  store IDS alerts and network metadata in :ref:`elasticsearch` with original timestamps
-  store pcaps where :ref:`soc` can find them

Usage
-----

.. warning::

   so-import-pcap works differently on Security Onion 2.1 than it did in previous versions! 
   
   Please consider this new version to be experimental!
   
This new version of so-import-pcap requires you to run through Setup first. You can choose an Import Node for a minimal configuration suitable for so-import-pcap. Once Setup completes, you can then run ``sudo so-import-pcap`` and supply the full path to at least one pcap file.

For example, to import a single pcap named ``import.pcap``:

::

    sudo so-import-pcap /full/path/to/import.pcap

To import multiple pcaps:

::

    sudo so-import-pcap /full/path/to/import1.pcap /full/path/to/import2.pcap
