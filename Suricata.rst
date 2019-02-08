Suricata
========

From https://suricata-ids.org:

    Suricata is a free and open source, mature, fast and robust network
    threat detection engine. Suricata inspects the network traffic using
    a powerful and extensive rules and signature language, and has
    powerful Lua scripting support for detection of complex threats.

Performance
-----------

We compile Suricata with `PF\_RING <PF_RING>`__ to allow you to spin up
multiple workers to handle more traffic.

Configuration
-------------

| You can configure Suricata via suricata.yaml:
| ``/etc/nsm/HOSTNAME-INTERFACE/suricata.yaml``
| (where HOSTNAME is your actual hostname and INTERFACE is your actual
  sniffing interface)

If you would like to configure/manage IDS rules, please see:

`<Rules>`__

`<ManagingAlerts>`__

Logging
-------

| If you need to troubleshoot Suricata, check the log file:
| ``/var/log/nsm/HOSTNAME-INTERFACE/suricata.log``
| (where HOSTNAME is your actual hostname and INTERFACE is your actual
  sniffing interface)

More Information
----------------

| For more information about Suricata, please see:
| https://suricata-ids.org/
