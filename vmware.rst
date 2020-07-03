VMWare
======

Overview
--------

In this section, we'll cover creating a virtual machine (VM) for Security Onion in VMWare Workstation Pro (although this should be similar for most VMWare installations).

If you don't have VMWare Workstation, you could also use VMWare Player, found here:

http://www.vmware.com/products/player/playerpro-evaluation.html

Creating VM
------------

Follow the steps below to install our Security Onion ISO image in VMware:

#. From VMWare, select File >> New Virtual Machine.
#. Select Typical installation >> Click ``Next``.
#. Installer disc image file >> SO ISO file path >> Click ``Next``.
#. Choose Linux, CentOS 7 64-Bit and click ``Next``.
#. Specify virtual machine name and click ``Next``.
#. Specify disk size (min 100GB), store as single file, click ``Next``.
#. Customize hardware and increase Memory (min 8GB for most use cases) and Processors (4 CPU cores for most use cases).
#. Network Adapter (NAT or Bridged -- if you want to be able to access
   your Security Onion machine from other devices in the network, then
   choose Bridged, otherwise choose NAT to leave it behind the host) --
   in this tutorial, this will be the management interface.
#. Add >> Network Adapter (Bridged) - this will be the sniffing (monitor) interface.
#. Click ``Close``.
#. Click ``Finish``.
#. Power on the virtual machine.

Sniffing
----------------------

-  With the sniffing interface in "bridged" mode, you will be able to
   see all traffic to/from the host machine's physical NIC. If you would
   like to see **ALL** the traffic on your network, you will need a
   method of forwarding that traffic to the interface to which the
   virtual adapter is bridged. This can be achieved by switch port
   mirroring (SPAN), or through the use of a
   `tap <Hardware#enterprise-tap-solutions>`__.
