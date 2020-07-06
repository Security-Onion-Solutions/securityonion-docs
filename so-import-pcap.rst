.. _so-import-pcap:

so-import-pcap
==============

If you just want to analyze one or more pcap files, then ``so-import-pcap`` is the quickest and easiest way to get started with Security Onion!  It will import one or more pcaps into Security Onion and preserve original timestamps.

It will do the following:

-  automatically run Setup to configure the system if necessary
-  stop and disable Curator to avoid closing old indices
-  stop and disable all active sniffing processes (Zeek, Suricata, and Stenographer)
-  generate IDS alerts using Suricata
-  generate Zeek logs
-  store IDS alerts and Zeek logs with original timestamps
-  store pcaps where Security Onion Console (SOC) can find them

Minimum Requirements
--------------------

-  50GB storage
-  8GB RAM
-  2 CPU cores

Please note these are MINIMUM requirements.  If you can allocate more resources, please do so.

.. warning::

   Do NOT run so-import-pcap on an existing production deployment!
   
   It is designed for standalone systems designated for so-import-pcap.
   
.. tip::

   If you're running so-import-pcap in a VM with snapshot capability, you might want to take a snapshot before this program makes changes.
   
Usage
-----

Please supply the full path to at least one pcap file.

For example, to import a single pcap named ``import.pcap``:

::

    sudo so-import-pcap /full/path/to/import.pcap

To import multiple pcaps:

::

    sudo so-import-pcap /full/path/to/import1.pcap /full/path/to/import2.pcap

Warning
-------

Please note that so-import-pcap will make changes to your system! It will warn you before doing so and will prompt you to press Enter to continue or Ctrl-c to cancel.

If you want to bypass the "Press Enter to continue" prompt, you can do something like this:

::

    echo | sudo so-import-pcap /opt/samples/markofu/ie*
