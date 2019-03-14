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

For best performance, CPU intensive processes like Bro and Suricata should be pinned to specific CPUs.

| For Bro, use the ``pin_cpus`` setting in ``/opt/bro/etc/node.cfg``:
| https://docs.zeek.org/en/stable/configuration/#using-pf-ring

| For Suricata, use the affinity settings in ``suricata.yaml``:
| https://suricata.readthedocs.io/en/latest/configuration/suricata-yaml.html#threading

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

Other
-----

| Consider adopting some of the suggestions from here:
| https://suricata.readthedocs.io/en/latest/performance/packet-capture.html
| https://github.com/pevma/SEPTun
| https://github.com/pevma/SEPTun-Mark-II
