Snort
=====

Snort is a Network Intrusion Detection System (`<NIDS>`_). It sniffs network traffic and generates IDS alerts.

Performance
-----------

In Security Onion, we compile Snort with `<PF-RING>`__ to allow you to spin up multiple instances to handle more traffic.

Starting in ``securityonion-nsmnow-admin-scripts - 20120724-0ubuntu0securityonion226``, we now have the ability to pin Snort processes.  With this package in place, you can pin Snort processes to specific CPUs by adding a line to the ``/etc/nsm/HOSTNAME-INTERFACE/sensor.conf`` file like:

::

    IDS_LB_CPUS=1,3,5,7

and then (re)starting the Snort process(es) using ``sudo so-nids-start`` or ``sudo so-nids-restart``.

In the example above, the first four snort processes would be pinned to the first four odd-numbered CPU cores. If there are more Snort processes enabled via ``IDS_LB_PROCS`` than are listed in the pin config in ``IDS_LB_CPUS``, then any processes without a CPU listed would have the default CPU affinity.  You can verify proper pinning using ``taskset -cp PID`` where PID is the actual process ID of the Snort process you are checking.

Configuration
-------------

You can configure Snort via ``/etc/nsm/HOSTNAME-INTERFACE/snort.conf`` (where HOSTNAME is your actual hostname and INTERFACE is your actual sniffing interface).

If you would like to configure/manage IDS rules, please see the `<Rules>`__ and `<ManagingAlerts>`__ sections.

Logging
-------

If you need to troubleshoot Snort, check the Snort log file(s) ``/var/log/nsm/HOSTNAME-INTERFACE/snortu-X.log`` (where ``HOSTNAME`` is your actual hostname, ``INTERFACE`` is your actual sniffing interface, and ``X`` represents the number of PF-RING instances).

More Information
----------------

For more information about Snort, please see https://snort.org.
