.. _firewall:

Firewall
========

Setup defaults to only allowing port 22 (ssh)
---------------------------------------------

When you run Setup, it defaults to locking down the local firewall to only allowing port 22 (ssh).  If you need to allow connections on other ports, you can run the :ref:`so-allow` utility.

Sensors automatically add their own firewall rules to the manager node
----------------------------------------------------------------------

When you run Setup on a sensor-only installation, it will ssh to the manager node and add new firewall rules to the manager node to allow the sensor to connect on the following ports:

-  22/tcp (ssh)
-  4505/tcp (salt)
-  4506/tcp (salt)

Managing
--------

Managing firewall rules for all devices can be done from the manager node. There are specific roles with firewall rules associated with each role. Some things have multiple roles for instance any type of node is automatically added to the minions.sls so that the salt communication can take place. So for a storage node you will see the IP show up in minions.sls as well as storage_nodes.sls.

analyst.sls
~~~~~~~~~~~
This is a list of hosts and networks that are allowed the analyst role. The analyst role allows connectivity to the sensor to use the web interface. Please note that 80 just forwards to 443 and no communication with the console is unencrypted.

- 80/tcp
- 443/tcp

beats_endpoint.sls
~~~~~~~~~~~~~~~~~~
These are endpoints that are allowed to use beats to send traffic to the manager node.

- 5044

forward_nodes.sls
~~~~~~~~~~~~~~~~~
Forward nodes or sensors

- 5044
- 6379

minions.sls
~~~~~~~~~~~
- 4505
- 4506
- 8086

osquery_endpoint.sls
~~~~~~~~~~~~~~~~~~~~
- 8080

storage_nodes.sls
~~~~~~~~~~~~~~~~~
