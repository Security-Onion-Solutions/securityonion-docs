.. _syslog:

Syslog
======

If you want to collect syslog from other devices, you'll need to run :ref:`so-allow` and then choose the ``syslog`` option to allow the port through the firewall.

If you need to add custom parsing for those syslog logs, we recommend using :ref:`elasticsearch` ingest parsing.
