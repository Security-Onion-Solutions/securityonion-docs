so-allow
========

Setup locks down the `firewall <Firewall>`_ by default.  If you need to open ports for Wazuh agents, syslog devices, or analyst VMs, you can run ``so-allow`` and it will walk you through this process. ``so-allow`` also provides an option to add firewall rules for sensors although you shouldn't need this under normal circumstances since they should automatically add their own rules.

::

    This program allows you to add a firewall rule to allow connections from a new IP address.

    Choose the role for the IP or Range you would like to add

    [a] - Analyst - ports 80/tcp and 443/tcp
    [b] - Logstash Beat - port 5044/tcp
    [o] - Osquery endpoint - port 8090/tcp
    [s] - Syslog device - 514/tcp/udp
    [w] - Wazuh agent - port 1514/tcp/udp
    [p] - Wazuh API - port 55000/tcp
    [r] - Wazuh registration service - 1515/tcp
    Please enter your selection (a - analyst, b - beats, o - osquery, w - wazuh):


Wazuh
-----
If you choose the ``analyst`` option, ``so-allow`` will also add the ``analyst`` IP address to the Wazuh safe list.  This will prevent Wazuh Active Response from blocking the ``analyst`` IP address.

so-allow-view
-------------

To view existing rules granted through the use of ``so-allow``, use the following command:

::

   so-allow-view

so-disallow
-----------
If you've added an IP address via ``so-allow`` and later need to remove it, you can use ``so-disallow``.
