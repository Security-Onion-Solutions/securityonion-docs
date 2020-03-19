High Performance Tuning
=======================

Ubuntu Server
-------------

For best performance, we recommend starting with Ubuntu Server (no GUI) and adding our Security Onion packages as described in our `<Production Deployment>`_ guide.

Best Practices
--------------

When you run Setup, make sure you choose `Best Practices <Best-Practices>`__.

Disable GUI
-----------

If you're unable to start with Ubuntu Server (no GUI) as recommended above, you can `disable the GUI <Desktop>`_ after the system is fully configured.

Disable Unnecessary Services
----------------------------

Disable any other unnecessary services.  For example, to disable bluetooth:

::

    sudo systemctl stop bluetooth.service
    sudo systemctl disable bluetooth.service
    
CPU Affinity/Pinning
--------------------

For best performance, CPU intensive processes like Zeek, Suricata, and Snort should be pinned to specific CPUs.

| For Zeek, use the ``pin_cpus`` setting in ``/opt/bro/etc/node.cfg``:
| https://docs.zeek.org/en/stable/configuration/#using-pf-ring

| For Suricata, use the affinity settings in ``suricata.yaml``:
| https://suricata.readthedocs.io/en/latest/configuration/suricata-yaml.html#threading

Starting in ``securityonion-nsmnow-admin-scripts - 20120724-0ubuntu0securityonion226``, we now have the ability to pin Snort processes.  With this package in place, you can pin Snort processes to specific CPUs by adding a line to the ``/etc/nsm/HOSTNAME-INTERFACE/sensor.conf`` file like:

::

    IDS_LB_CPUS=1,3,5,7

and then (re)starting the Snort process(es) using ``sudo so-nids-start`` or ``sudo so-nids-restart``.

In the example above, the first four snort processes would be pinned to the first four odd-numbered CPU cores. If there are more Snort processes enabled via ``IDS_LB_PROCS`` than are listed in the pin config in IDS_LB_CPUS, then any processes without a CPU listed would have the default CPU affinity.  You can verify proper pinning using ``taskset -cp PID`` where PID is the actual process ID of the Snort process you are checking.

RSS
---

| Check your sniffing interfaces to see if they have Receive Side Scaling (RSS) queues. If so, you may need to reduce to 1:
| https://suricata.readthedocs.io/en/latest/performance/packet-capture.html#rss

Disk/Memory
-----------

If you have plenty of RAM, disable swap altogether.

| Use ``hdparm`` to gather drive statistics and alter settings, as described here:
| http://www.linux-magazine.com/Online/Features/Tune-Your-Hard-Disk-with-hdparm

``vm.dirty_ratio`` is the maximum amount of system memory that can be filled with dirty pages before everything must get committed to disk.

``vm.dirty_background_ratio`` is the percentage of system memory that can be filled with “dirty” pages, or memory pages that still need to be written to disk -- before the pdflush/flush/kdmflush background processes kick in to write it to disk.

| More information:
| https://lonesysadmin.net/2013/12/22/better-linux-disk-caching-performance-vm-dirty_ratio/

Elastic
-------
You will want to make sure that each part of the pipeline is operating at maximum efficiency.  Depending on your configuration, this may include `syslog-ng <syslog>`__, `Logstash <logstash>`_, `Redis <redis>`__, and `Elasticsearch <elasticsearch>`__.  For really high volume logs, you may want to consider the `LOGSTASH_MINIMAL <logstash#logstash-minimal>`__ option.

Other
-----

| Consider adopting some of the suggestions from here:
| https://suricata.readthedocs.io/en/latest/performance/packet-capture.html
| https://github.com/pevma/SEPTun
| https://github.com/pevma/SEPTun-Mark-II
