netsniff-ng
===========

From http://netsniff-ng.org:

    netsniff-ng is a free Linux networking toolkit, a Swiss army knife
    for your daily Linux network plumbing if you will. Its gain of
    performance is reached by zero-copy mechanisms, so that on packet
    reception and transmission the kernel does not need to copy packets
    from kernel space to user space and vice versa.

Usage
-----

Security Onion uses netsniff-ng to collect full packet capture in the
form of pcap files.

Output
------

| netsniff-ng writes full packet capture in the form of pcap files to:
| ``/nsm/sensor_data/HOSTNAME-INTERFACE/dailylogs/YYYY-MM-DD/``
| where:

-  HOSTNAME is your actual hostname
-  INTERFACE is your actual sniffing interface
-  YYYY-MM-DD is the year, month, and date the pcap was recorded

Analysis
--------

Besides accessing the pcaps in the directory shown above, you can also
pivot to full packet capture from `Sguil <Sguil>`__ and
`CapMe <CapMe>`__.

Troubleshooting
---------------

| Check the netsniff-ng.log file in:
| ``/var/log/nsm/HOSTNAME-INTERFACE/netsniff-ng.log``
| (where HOSTNAME is your actual hostname and INTERFACE is your actual
  sniffing interface)

Tuning
------

If sostat report packet loss in netsniff-ng, you may want to consider
one or more of the following options in
/etc/nsm/HOSTNAME-INTERFACE/sensor.conf:

-  increase PCAP\_RING\_SIZE
-  set PCAP\_OPTIONS to "--mmap" to enable memory-mapped IO

Please note that both of these options will cause netsniff-ng to consume
more RAM.

More Information
----------------

| For more information about netsniff-ng, please see:
| http://netsniff-ng.org/

Reducing Storage
----------------

| Full packet capture obviously requires lots of disk space. Trimming
  your pcaps can allow you to store pcap for longer periods of time. For
  example, please see:
| https://www.netresec.com/?page=Blog&month=2017-12&post=Don%27t-Delete-PCAP-Files---Trim-Them
