.. _syslog:

Syslog
======

If you want to send syslog from other devices, you should check to see if the device has an existing :ref:`filebeat` module at https://www.elastic.co/guide/en/beats/filebeat/current/filebeat-modules.html. If so, using the :ref:`filebeat` module should provide some parsing by default.

If your device does not have an existing :ref:`filebeat` module, you can still collect standard syslog by running :ref:`so-allow` on the manager and then choosing the ``syslog`` option to allow the port through the firewall.  If sending syslog to a sensor, please see the Examples in the :ref:`firewall` section. If you need to add custom parsing for those syslog logs, we recommend using :ref:`elasticsearch` ingest parsing.

Also note that if you're monitoring network traffic with :ref:`zeek`, then by default it will detect any syslog in that network traffic and log it even if that syslog was not destined for that particular Security Onion node.
