Cloud Client
============

**Please Note!**

This cloud client idea was developed before cloud providers offered virtual taps.  If you are able to use your cloud provider's virtual tap, please do so instead of using this cloud client workaround.  For example:

https://aws.amazon.com/blogs/aws/new-vpc-traffic-mirroring/

https://docs.microsoft.com/en-us/azure/virtual-network/virtual-network-tap-overview

**Warning! This cloud client is considered experimental! USE AT YOUR OWN RISK!**

If your cloud provider doesn't already offer a virtual tap, you can use daemonlogger or netsniff-ng as a virtual tap. This virtual tap will copy all traffic from our production cloud box to an OpenVPN bridge that transports the traffic to our
Security Onion sensor where it is then analyzed.

This guide was originally written for Security Onion 12.04 and was updated for Security Onion 14.04, but hasn't been updated or tested on 16.04.

Traffic Flow and NIC offloading functions
-----------------------------------------

The cloud client uses ``daemonlogger`` or ``netsniff-ng`` to copy all
packets from eth0 to tap0 (OpenVPN). OpenVPN transports the packets to
the cloud sensor, where tap0 is a member of bridge br0. The standard
Security Onion stack sniffs br0. NIC offloading functions must be
disabled on all of these interfaces (eth0 and tap0 on cloud client, and
tap0 and br0 on cloud sensor) to ensure that Snort, Bro, etc. all see
traffic as it appeared on the wire. This guide will walk you through
disabling NIC offloading functions on eth0 and br0 via
``/etc/network/interfaces`` and tap0 via ``/etc/openvpn/up.sh``.

Daemonlogger vs netsniff-ng
---------------------------

This guide is written using ``daemonlogger`` because it is more likely
to be available on most cloud boxes. If ``netsniff-ng`` is available, it
can provide higher performance (less packet loss), and you would just
need to change the calls from daemonlogger to netsniff-ng and translate
the options to the equivalent netsniff-ng options.

References and Thanks
---------------------

This is based on Josh Brower's great work:

http://www.slideshare.net/DefensiveDepth/so-conference-2014

The OpenVPN configuration shown below is based on the following guides:

https://help.ubuntu.com/community/OpenVPN

https://help.ubuntu.com/lts/serverguide/openvpn.html

Install Packages
----------------

If you are installing from Ubuntu 16.04, make sure you install our packages before continuing with this procedure.  For more information, please see the `Getting Started <getting-started>`__ section.

Security Onion Sensor
---------------------

We start with our Security Onion sensor.

First, ensure that the bridge-utils package is installed:

::

    sudo apt-get update
    sudo apt-get install bridge-utils

Run Security Onion Setup Phase 1 (Network Configuration), allow it to
write your ``/etc/network/interfaces`` file, but DON'T reboot at the
end:

::

    sudo sosetup

Add br0 to ``/etc/network/interfaces`` and disable offloading functions:

::

    cat << EOF | sudo tee -a /etc/network/interfaces
    # Bridge for OpenVPN tap0
    auto br0
    iface br0 inet manual
      bridge_ports none
      post-up for i in rx tx sg tso ufo gso gro lro; do ethtool -K \$IFACE \$i off; done
    EOF

Reboot:

::

    sudo reboot

Run Security Onion Setup Phase 2 and choose to monitor br0:

::

    sudo sosetup

Setup has locked down the UFW firewall, so let's go ahead and allow
OpenVPN port 1194:

::

    sudo ufw allow 1194

Install OpenVPN:

::

    sudo apt-get update
    sudo apt-get install openvpn easy-rsa

Next, copy files to the ``/etc/openvpn/easy-rsa/`` directory:

::

    sudo mkdir /etc/openvpn/easy-rsa/ 
    sudo cp -r /usr/share/easy-rsa/* /etc/openvpn/easy-rsa/

Edit ``/etc/openvpn/easy-rsa/vars``:

::

    sudo vi /etc/openvpn/easy-rsa/vars

Change these lines at the bottom so that they reflect the proper
settings for your new CA:

::

    export KEY_COUNTRY
    export KEY_PROVINCE
    export KEY_CITY
    export KEY_ORG
    export KEY_EMAIL
    export KEY_CN
    export KEY_NAME
    export KEY_OU

Setup the CA and create the first server certificate:

::

    cd /etc/openvpn/easy-rsa/ ## move to the easy-rsa directory
    sudo chown -R root:sudo .  ## make this directory writable by the system administrators
    sudo chmod g+w . ## make this directory writable by the system administrators
    source ./vars ## execute your new vars file
    ./clean-all  ## Setup the easy-rsa directory (Deletes all keys)
    ./build-ca  ## generate the master Certificate Authority (CA) certificate and key
    ./build-key-server server ## creates a server cert and private key
    ./build-dh
    cd keys
    sudo cp server.crt server.key ca.crt dh2048.pem /etc/openvpn/
    # The Certificate Authority is now setup and the needed keys are in /etc/openvpn/

Create a script that OpenVPN will call when the tunnel comes up to add
tap0 to br0 and disable offloading functions on tap0:

::

    cat << EOF | sudo tee -a /etc/openvpn/up.sh
    #!/bin/sh

    BR=\$1
    DEV=\$2
    /sbin/ip link set "\$DEV" up promisc on
    /sbin/brctl addif \$BR \$DEV

    for i in rx tx sg tso ufo gso gro lro; do ethtool -K \$DEV \$i off; done
    EOF

Create a script that OpenVPN will call when the tunnel goes down:

::

    cat << EOF | sudo tee -a /etc/openvpn/down.sh
    #!/bin/sh

    BR=\$1
    DEV=\$2

    /sbin/brctl delif \$BR \$DEV
    /sbin/ip link set "\$DEV" down
    EOF

Make both of these scripts executable:

::

    sudo chmod +x /etc/openvpn/up.sh /etc/openvpn/down.sh

Create OpenVPN ``server.conf``:

::

    sudo cp /usr/share/doc/openvpn/examples/sample-config-files/server.conf.gz /etc/openvpn/
    sudo gzip -d /etc/openvpn/server.conf.gz

Modify ``/etc/openvpn/server.conf``:

::

    sudo sed -i 's|^dev tun$|;dev tun|g' /etc/openvpn/server.conf
    sudo sed -i 's|^;dev tap|dev tap|g' /etc/openvpn/server.conf
    sudo sed -i 's|^comp-lzo|;comp-lzo|g' /etc/openvpn/server.conf
    sudo sed -i 's|^dh dh1024.pem|dh dh2048.pem|g' /etc/openvpn/server.conf


    cat << EOF | sudo tee -a /etc/openvpn/server.conf

    up "/etc/openvpn/up.sh br0"
    down "/etc/openvpn/down.sh br0"
    EOF

Restart OpenVPN server:

::

    sudo service openvpn restart

Check log for errors:

::

    sudo tail -f /var/log/syslog

Verify tap0 came up:

::

    ifconfig

Generate client certs
---------------------

Perform the steps in this section for each cloud client you want to
monitor.

Generate client cert (replacing ``client`` with the name of the cloud
client you want to add):

::

    cd /etc/openvpn/easy-rsa/ ## move to the easy-rsa directory
    source ./vars             ## execute the vars file
    ./build-key client

Copy generated files to cloud client (replacing ``client`` with the name
of the cloud client you want to add):

::

    scp /etc/openvpn/easy-rsa/keys/client* username@hostname:~/
    scp /etc/openvpn/easy-rsa/keys/ca.crt username@hostname:~/

Cloud client
------------

Perform the steps in this section on each cloud client you want to
monitor.

Install ``openvpn`` and ``daemonlogger``:

::

    sudo apt-get update
    sudo apt-get install openvpn daemonlogger

Copy crt files to ``/etc/openvpn/``:

::

    sudo cp client* /etc/openvpn/
    sudo cp ca.crt /etc/openvpn/

Create OpenVPN ``client.conf``:

::

    sudo cp /usr/share/doc/openvpn/examples/sample-config-files/client.conf /etc/openvpn/

Modify ``/etc/openvpn/client.conf``:

::

    sudo sed -i 's|^dev tun$|;dev tun|g' /etc/openvpn/client.conf
    sudo sed -i 's|^;dev tap|dev tap|g' /etc/openvpn/client.conf
    sudo sed -i 's|^comp-lzo|;comp-lzo|g' /etc/openvpn/client.conf

    cat << EOF | sudo tee -a /etc/openvpn/client.conf

    up "/etc/openvpn/up.sh"
    down "/etc/openvpn/down.sh"
    EOF

Find the "remote my-server-1 1194" line in ``/etc/openvpn/client.conf``
and replace my-server-1 with the hostname or IP address of your OpenVPN
server.

Create a script that OpenVPN will call when the tunnel comes up to
disable offloading functions on tap0 and start daemonlogger. The
daemonlogger BPF at minimum should exclude the OpenVPN traffic on port
1194 ('not port 1194'). You may need to restrict this BPF even further
if there is other traffic you do not wish to send across the OpenVPN
tunnel.

::

    cat << EOF | sudo tee -a /etc/openvpn/up.sh
    #!/bin/sh

    IN=eth0
    OUT=\$1

    daemonlogger -d -i \$IN -o \$OUT 'not port 1194'

    for i in rx tx sg tso ufo gso gro lro; do ethtool -K \$OUT \$i off; done
    EOF

Create a script that OpenVPN will call when the tunnel goes down:

::

    cat << EOF | sudo tee -a /etc/openvpn/down.sh
    #!/bin/sh

    pkill daemonlogger
    EOF

Make both of these scripts executable:

::

    sudo chmod +x /etc/openvpn/up.sh /etc/openvpn/down.sh

Restart OpenVPN client:

::

    sudo service openvpn restart

Check log for errors:

::

    tail -f /var/log/syslog

Verify that tap0 came up:

::

    ifconfig

| Disable NIC offloading functions on main ethernet interface.
| Add the following to your eth stanza in ``/etc/network/interfaces`` OR
  add to ``/etc/openvpn/up.sh``:

::

      post-up for i in rx tx sg tso ufo gso gro lro; do ethtool -K $IFACE $i off; done

Bounce the interface (you may lose access if connected remotely over
ssh) or reboot the box.

Check traffic
-------------

Your Security Onion sensor should now be seeing traffic from your Cloud
Client. Verify as follows:

::

    sudo tcpdump -nnvvAi tap0

tap0 should be a member of br0, so you should see the same traffic on
br0:

::

    sudo tcpdump -nnvvAi br0

When you ran Setup phase 2 you configured Security Onion to monitor br0,
so you should be getting IDS alerts and Bro logs.

Hardening
---------

Once you get everything working properly, you should configure OpenVPN
(server and client) and daemonlogger to run as a limited user.

Tuning
------

If your cloud box is seeing lots of traffic, daemonlogger may not be
able to keep up, resulting in packet loss. You may need to switch to
netsniff-ng for higher performance. Don't forget to run netsniff-ng as a
limited user!
