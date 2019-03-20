Suricata
========

From https://suricata-ids.org:

    Suricata is a free and open source, mature, fast and robust network
    threat detection engine. Suricata inspects the network traffic using
    a powerful and extensive rules and signature language, and has
    powerful Lua scripting support for detection of complex threats.

Performance
-----------

We compile Suricata to support both `<PF-RING>`__ and `<AF-PACKET>`_ to allow you to spin up multiple workers to handle more traffic.  Modern versions of Setup default to `<AF-PACKET>`_.

| For high traffic levels, you may want to pin Suricata to specific CPU cores using the affinity settings in ``suricata.yaml``:
| https://suricata.readthedocs.io/en/latest/configuration/suricata-yaml.html#threading

Configuration
-------------

You can configure Suricata via ``/etc/nsm/HOSTNAME-INTERFACE/suricata.yaml`` (where ``HOSTNAME`` is your actual hostname and ``INTERFACE`` is your actual sniffing interface).

If you would like to configure/manage IDS rules, please see the `<Rules>`__ and `<ManagingAlerts>`__ sections.

Logging
-------

If you need to troubleshoot Suricata, check ``/var/log/nsm/HOSTNAME-INTERFACE/suricata.log`` (where ``HOSTNAME`` is your actual hostname and ``INTERFACE`` is your actual sniffing interface).

Stats
-----

For detailed Suricata statistics, check ``/nsm/sensor_data/HOSTNAME-INTERFACE/stats.log`` (where ``HOSTNAME`` is your actual hostname and ``INTERFACE`` is your actual sniffing interface).

If you want ``stats.log`` to show per-thread stats (for example, to verify that load balancing is working properly), you can set ``threads: yes`` under the ``outputs: - stats:`` section in ``suricata.yaml`` and then restart Suricata.

More Information
----------------

For more information about Suricata, please see https://suricata-ids.org.
