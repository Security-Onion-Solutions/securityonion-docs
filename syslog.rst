.. _syslog:

Syslog
======

If you want to send syslog from other devices to the manager, you'll need to run :ref:`so-allow` on the manager and then choose the ``syslog`` option to allow the port through the firewall.  If sending syslog to a sensor, please see the Examples in the :ref:`firewall` section.

If you need to add custom parsing for those syslog logs, we recommend using :ref:`elasticsearch` ingest parsing.
