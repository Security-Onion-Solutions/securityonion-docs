.. _performance:

High Performance Tuning
=======================

CPU Affinity/Pinning
--------------------

For best performance, CPU intensive processes like Zeek and Suricata should be pinned to specific CPUs.  In most cases, you'll want to pin sniffing processes to the same CPU that your sniffing NIC is bound to.

`Suricata Performance <suricata.html#performance>`_

`Zeek Performance <zeek.html#performance>`_

Misc
----

| Consider adopting some of the suggestions from here:
| https://suricata.readthedocs.io/en/latest/performance/packet-capture.html
| https://github.com/pevma/SEPTun
| https://github.com/pevma/SEPTun-Mark-II

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
You will want to make sure that each part of the pipeline is operating at maximum efficiency.  Depending on your configuration, this may include `Logstash <logstash>`_, `Redis <redis>`__, and `Elasticsearch <elasticsearch>`__. 
