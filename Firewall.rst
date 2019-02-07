Firewall/Hardening
==================

Setup defaults to only allowing port 22 (ssh)
---------------------------------------------

| As of securityonion-setup - 20120912-0ubuntu0securityonion201, Setup
  now defaults to locking down the local ``ufw`` firewall to only
  allowing port 22 (ssh):
| http://blog.securityonion.net/2016/03/securityonion-setup-20120912.html

There is a note at the end of Setup that tells you this and lets you
know that, if you need to allow connections on other ports, you can run
the new ``so-allow`` utility.

Sensors automatically add their own firewall rules to the master server
-----------------------------------------------------------------------

When you run Setup on a sensor-only installation, it will ssh to the
master server and add new firewall rules to the master server to allow
the sensor to connect on the following ports:

-  22/tcp (ssh)
-  4505/tcp (salt)
-  4506/tcp (salt)
-  7736/tcp (sguil)

``so-allow``
------------

If you need to open ports for OSSEC agents, syslog devices, or analyst
VMs, you can run ``so-allow`` and it will walk you through this process.
``so-allow`` also provides an option to add firewall rules for sensors
although you shouldn't need this under normal circumstances since they
should automatically add their own rules as described above.

::

    This program allows you to add a firewall rule to allow connections from a new IP address.

    What kind of device do you want to allow?

    [a] - analyst - ports 22/tcp, 443/tcp, and 7734/tcp
    [b] - Logstash Beat - port 5044/tcp
    [c] - apt-cacher-ng client - port 3142/tcp
    [f] - Logstash Forwarder - Standard - port 6050/tcp
    [j] - Logstash Forwarder - JSON - port 6051/tcp
    [l] - syslog device - port 514
    [o] - ossec agent - port 1514/udp
    [s] - Security Onion sensor - 22/tcp, 4505/tcp, 4506/tcp, and 7736/tcp

    If you need to add any ports other than those listed above,
    you can do so using the standard 'ufw' utility.

    For more information, please see the Firewall page on our Wiki:
    https://github.com/Security-Onion-Solutions/security-onion/wiki/Firewall

    Please enter your selection (a - analyst, c - apt-cacher-ng client, l - syslog, o - ossec, or s - Security Onion sensor, etc.):

To view existing rules granted through the use of ``so-allow``, use the
following command:

``so-allow-view``

| If you have upgraded from Security Onion 12.04 and you receive
  duplicate profile warnings for UFW when adding rules, please see:
| https://github.com/Security-Onion-Solutions/security-onion/wiki/Upgrading-from-12.04-to-14.04#clean-up

More ``ufw`` documentation
--------------------------

For more information about manually adding ``ufw`` firewall rules or if
you're still running a version of Setup older than securityonion-setup -
20120912-0ubuntu0securityonion201, then you can reference the `original
firewall documentation <firewall-old>`__.
