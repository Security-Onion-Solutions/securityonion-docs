Network Configuration
=====================

All of this configuration will happen automatically if you choose ``Yes, configure /etc/network/interfaces`` in the Setup wizard.  If for some reason you need to configure ``/etc/network/interfaces`` manually, you can do the following.

NOTE! You may lose network connectivity during this process! Have a backup plan if attempting over SSH!

Stop Network Manager:

::

   sudo /etc/init.d/network-manager stop

Prevent Network Manager from starting at next boot:

::

   sudo mv /etc/init/network-manager.conf /etc/init/network-manager.conf.DISABLED

Next, configure your network interfaces in ``/etc/network/interfaces``.

Management interface
--------------------

You'll want a management interface (preferably connected to a dedicated management network) using either DHCP OR preferably static IP. 

Sniffing interface(s)
---------------------

You'll want one or more interfaces dedicated to sniffing (no IP address). NIC offloading functions such as ``tso``, ``gso``, and ``gro`` should be disabled to ensure that Snort/Suricata get an accurate view of the traffic (see https://blog.securityonion.net/2011/10/when-is-full-packet-capture-not-full.html).

Sample /etc/network/interfaces
------------------------------

::

   auto lo
   iface lo inet loopback
   
   # Management interface using DHCP
   auto eth0
   iface eth0 inet dhcp
   
   # OR
   
   # Management interface using STATIC IP (instead of DHCP)
   auto eth0
   iface eth0 inet static
     address 192.168.1.14
     gateway 192.168.1.1
     netmask 255.255.255.0
     network 192.168.1.0
     broadcast 192.168.1.255
     dns-nameservers 192.168.1.1 192.168.1.2
   
   # AND one or more of the following
   
   # Connected to TAP or SPAN port for traffic monitoring
   auto eth1
   iface eth1 inet manual
     up ifconfig $IFACE -arp up
     up ip link set $IFACE promisc on
     down ip link set $IFACE promisc off
     down ifconfig $IFACE down
     post-up for i in rx tx sg tso ufo gso gro lro; do ethtool -K $IFACE $i off; done
     post-up echo 1 > /proc/sys/net/ipv6/conf/$IFACE/disable_ipv6

You may also want to set the RX buffer size in the post-up command like this:

::

   post-up ethtool -G $IFACE rx 4096; for i in rx tx sg tso ufo gso gro lro; do ethtool -K $IFACE $i off; done

Note that 4096 is just an example and your NIC may have a different maximum rx size. To determine the maximum rx setting for your NIC:

::

  ethtool -g ethX

| If necessary, configure DNS in ``/etc/resolv.conf``:
| http://en.wikipedia.org/wiki/Resolv.conf
| http://www.cyberciti.biz/tips/howto-ubuntu-linux-convert-dhcp-network-configuration-to-static-ip-configuration.html
| http://manpages.ubuntu.com/manpages/lucid/man5/resolver.5.html
| 
Restart networking:

::

   sudo /etc/init.d/networking restart

If you already had sensors running on these interfaces, you should restart them:

::

   sudo so-sensor-restart

For more information on network configuration in Ubuntu, please see https://help.ubuntu.com/community/NetworkConfigurationCommandLine/Automatic.
