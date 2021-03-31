.. _syslog:

Syslog
======

If you want to collect syslog from other devices, if sending to the manager, you'll need to run :ref:`so-allow` and then choose the ``syslog`` option to allow the port through the firewall.  If sending to a sensor, follow the steps here to modify the firewall rules for the sensor node:

https://docs.securityonion.net/en/latest/firewall.html?highlight=firewall#allow-hosts-to-send-syslog-to-a-sensor-node

If you need to add custom parsing for those syslog logs, we recommend using :ref:`elasticsearch` ingest parsing.
