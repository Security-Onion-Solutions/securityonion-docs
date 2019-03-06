VMWare
======

Overview
--------

In this section, we'll cover setting up Security Onion 16.04 in VMWare Workstation Pro 12 (although this should be similar for most VMWare installations).

If you don't have VMWare Workstation, you could also use VMWare Player, found here:

http://www.vmware.com/products/player/playerpro-evaluation.html

Installation
------------

Follow the steps below to install our Security Onion ISO image in VMware:

#. Download and verify the latest Security Onion ISO, found here:
   https://github.com/Security-Onion-Solutions/security-onion/blob/master/Verify_ISO.md
#. From VMWare, select File >> New Virtual Machine.
#. Select Typical installation >> "Click Next".
#. Installer disc image file >> SO ISO file path >> Click "Next".
#. Choose Linux, Ubuntu 64-Bit and click "Next".
#. Specify virtual machine name and click "Next".
#. Specify disk size (min 40GB), store as single file, click Next.
#. Customize hardware:
#. Memory – 8GB or more
#. Processors – 4 CPU cores or more
#. Network Adapter (NAT or Bridged -- if you want to be able to access
   your Security Onion machine from other devices in the network, then
   choose Bridged, otherwise choose NAT to leave it behind the host) --
   in this tutorial, this will be the management interface.
#. Add >> Network Adapter (Bridged) - this will be the sniffing (monitor) interface.
#. Click "Close".
#. Click "Finish".
#. Power on the virtual machine.
#. Wait for boot or press enter while selecting “Install”.
#. From the Welcome Screen, select language and click "Continue".
#. Click “Continue”.
#. Select "Use LVM with the new SecurityOnion installation" (or "Erase
   existing disk…").
#. Click "Install Now".
#. Confirm changes and click "Install Now".
#. From the "Where are you?" prompt, select your time zone and click
   "Continue".
#. Drag the window to the left (due to a bug in the Ubuntu installer), and click "Continue".
#. Enter your name.
#. Enter your computer’s name.
#. Select a username and enter a password.
#. Click "Continue".
#. Click "Restart Now".
#. (Optional) Adjust display settings >> Terminal Icons, Settings >>
   Display > Choose and confirm resolution.

Sniffing
----------------------

-  With the sniffing interface in "bridged" mode, you will be able to
   see all traffic to/from the host machine's physical NIC. If you would
   like to see **ALL** the traffic on your network, you will need a
   method of forwarding that traffic to the interface to which the
   virtual adapter is bridged. This can be achieved by switch port
   mirroring (SPAN), or through the use of a
   `tap <Hardware#enterprise-tap-solutions>`__.
