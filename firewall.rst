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

Managing firewall rules for all devices can be done from the manager node. There are specific roles with firewall rules associated with each role. Some things have multiple roles for instance any type of node is automatically added to the ``minions.sls`` so that the salt communication can take place. So for a storage node you will see the IP show up in ``minions.sls`` as well as ``storage_nodes.sls``.

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

Advanced Firewall Customization
-------------------------------

.. warning::

  Please review the :ref:`salt` section to understand pillars and templates. Modifying these values outside of :ref:`so-allow` or ``so-firewall`` could lead to problems accessing your existing hosts. This is an advanced case and you most likely won't never need to modify these files. An example of why you might modify these templates is if you were adding some sort of agent to the hosts in your grid that are not part of Security Onion. This would allow you to open the ports needed to the hosts that required access. 

Port Groups
~~~~~~~~~~~
Port groups are a way of grouping together ports similar to a firewall port/service alias. For example if you had a web server you could include 80 and 443 tcp into an alias or in this case a port group. 

Default port groups: ``/opt/so/saltstack/local/salt/firewall/portgroup.local.yaml``

Host Groups
~~~~~~~~~~~
Host groups is similar to port groups but for storing lists of hosts.  

Default host groups: ``/opt/so/saltstack/local/salt/firewall/hostgroups.local.yaml``

Port Group Assignments
~~~~~~~~~~~~~~~~~~~~~~
Port group assignments are the way you map host groups to port groups to complete the rule.  

Default port group assignments: ``/opt/so/saltstack/local/salt/firewall/assigned_hostgroups.local.map.yaml``

More Information
~~~~~~~~~~~~~~~~
Much of information and functionality that follows is handled with :ref:`so-allow` or ``so-firewall``, but could help provide a better understanding of what those two scripts are doing under the hood.

The firewall state and pillars were designed around the idea of creating port groups and host groups and creating an allow rule by assigning a port group to a host group. A node that has a port group / host group combination assigned to it will allow the hosts in that group to connect to those ports on that node.

During setup, the files from securityonion/files/firewall/ (https://github.com/Security-Onion-Solutions/securityonion/tree/master/files/firewall), are copied to the local directory located at ``/opt/so/saltstack/local/salt/firewall/``. Once setup is complete and ``so-allow`` or ``so-firewall`` are called in the future, they modify the appropriate yaml files that are located under ``/opt/so/saltstack/local/salt/firewall/``. Since these yaml files are under ``/opt/so/saltstack/local/`` they will not be changed during a code update.
