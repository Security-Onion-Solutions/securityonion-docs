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

   so-import-pcap works differently on Security Onion 2 than it did in previous versions! 
      
This new version of so-import-pcap requires you to run through Setup and choose a configuration that supports so-import-pcap. This includes Import Node and other nodes that include sensor services like Eval and Standalone. The quickest and easiest option is to choose Import Node which gives you the minimal services necessary to import a pcap and view the resulting logs in :ref:`hunt` or :ref:`kibana`.

Once Setup completes, you can then run ``sudo so-import-pcap`` and supply the full path to at least one pcap file. For example, to import a single pcap named ``import.pcap``:

::

    sudo so-import-pcap /full/path/to/import.pcap

To import multiple pcaps:

::

    sudo so-import-pcap /full/path/to/import1.pcap /full/path/to/import2.pcap

If you don't already have some pcap files to import, see :ref:`pcaps` for a list of sites where you can download sample pcaps.
