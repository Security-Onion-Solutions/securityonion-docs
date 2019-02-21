so-allow
========

Setup locks down the `firewall <Firewall>`_ by default.  If you need to open ports for OSSEC agents, syslog devices, or analyst VMs, you can run ``so-allow`` and it will walk you through this process. ``so-allow`` also provides an option to add firewall rules for sensors although you shouldn't need this under normal circumstances since they should automatically add their own rules as described above.

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
    https://securityonion.net/wiki/Firewall

    Please enter your selection (a - analyst, c - apt-cacher-ng client, l - syslog, o - ossec, or s - Security Onion sensor, etc.):

so-allow-view
-------------

To view existing rules granted through the use of ``so-allow``, use the following command:

::

   so-allow-view
