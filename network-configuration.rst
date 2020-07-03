Network Configuration
=====================

Management interface
--------------------

You'll want a management interface (preferably connected to a dedicated management network) using either DHCP OR preferably static IP. 

Sniffing interface(s)
---------------------

You'll want one or more interfaces dedicated to sniffing (no IP address). The installer will automatically disable NIC offloading functions such as ``tso``, ``gso``, and ``gro`` on sniffing interfaces to ensure that Suricata and Zeek get an accurate view of the traffic.

Wireless interfaces
-------------------

Security Onion is designed to use wired interfaces.  You may be able to make wireless interfaces work, but we don't recommend or support it.
