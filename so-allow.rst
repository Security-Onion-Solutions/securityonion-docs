.. _so-allow:

so-allow
========

Security Onion locks down the :ref:`firewall` by default. Depending on what kind of installation you do, Setup may walk you through allowing your analyst IP address(es). If you need to add other analyst IP addresses or open firewall ports for agents or syslog devices, you can run ``sudo so-allow`` and it will walk you through this process.

  ::
  
    This program allows you to add a firewall rule to allow connections from a new IP address.

    Choose the role for the IP or Range you would like to add

    [a] - Analyst - ports 80/tcp and 443/tcp
    [b] - Logstash Beat - port 5044/tcp
    [e] - Elasticsearch REST API - port 9200/tcp
    [f] - Strelka frontend - port 57314/tcp
    [o] - Osquery endpoint - port 8090/tcp
    [s] - Syslog device - 514/tcp/udp
    [w] - Wazuh agent - port 1514/tcp/udp
    [p] - Wazuh API - port 55000/tcp
    [r] - Wazuh registration service - 1515/tcp

    Please enter your selection:

Wazuh
-----
If you choose the ``analyst`` option, ``so-allow`` will also add the ``analyst`` IP address to the :ref:`wazuh` safe list.  This will prevent :ref:`wazuh` Active Response from blocking the ``analyst`` IP address.

Automation
----------
In addition to the interactive menu shown above, you can pass desired options as command line arguments:

::

  so-allow -h

  Usage: /usr/sbin/so-allow [-abefhoprsw] [ -i IP ]

  This program allows you to add a firewall rule to allow connections from a new IP address or CIDR range.

  If you run this program with no arguments, it will present a menu for you to choose your options.

  If you want to automate and skip the menu, you can pass the desired options as command line arguments.

  EXAMPLES

  To add 10.1.2.3 to the analyst role:
  so-allow -a -i 10.1.2.3

  To add 10.1.2.0/24 to the osquery role:
  so-allow -o -i 10.1.2.0/24
