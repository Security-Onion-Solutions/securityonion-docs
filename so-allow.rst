.. _so-allow:

so-allow
========

Setup locks down the :ref:`firewall` by default. Depending on what kind of installation you do, Setup may walk you through allowing your analyst IP address(es). If you need to add other analyst IP addresses or open firewall ports for agents or syslog devices, you can run ``sudo so-allow`` and it will walk you through this process.

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
