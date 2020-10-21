.. _firewall:

Firewall
========


Function
--------
The firewall state is designed to function with the idea of creating port groups and host groups, each with their own alias or name, and assiocating the two in order to create an allow rule. A node that has a port group and host group association assigned to it will allow those hosts to connect to those ports on that node.
The default allow rules for each node are defined by its role (manager, searchnode, sensor, heavynode, etc) in the grid. Host groups and port groups can be created or modified from the manager node using either :ref:`so-allow`, ``so-firewall`` or manually editing the yaml files. When setup is run on a new node, it will SSH
to the manager, using the soremote account, and add itself to the appropriate host groups. All node types are added to the minion host group to allow Salt communication. If you were to add a search node, you would see its IP appear in both the ``minion`` and the ``search_node`` host groups.

.. glossary::

  Port Groups

    Port groups are a way of grouping together ports similar to a firewall port/service alias. For example if you had a web server you could include 80 and 443 tcp into an alias or in this case a port group.

  Host Groups

    Host groups is similar to port groups but for storing lists of hosts that will be allowed to connect to the associated port groups.

There are two directories that contain the yaml files for the firewall configuration.

``/opt/so/saltstack/default/firewall``

This is where the default firewall rules are located. The files in this directory should not be modified as they could possibly be overwritten during a soup update in the event we update those files.

``/opt/so/saltstack/default/salt/firewall/portgroups.yaml``

This is where the default port groups are defined. 

.. image:: https://user-images.githubusercontent.com/17089008/96641876-5a85c080-12f3-11eb-90e3-0ac3d2dc9b8b.png
  :target: https://user-images.githubusercontent.com/17089008/96641876-5a85c080-12f3-11eb-90e3-0ac3d2dc9b8b.png


``/opt/so/saltstack/default/salt/firewall/hostgroups.yaml``

This is where the default hostgroups are defined. There isn't much in here other than anywhere, dockernet, localhost and self.

``/opt/so/saltstack/default/salt/firewall/assigned_hostgroups.map.yaml``

This is where the default allow rules come together and pair hostgroups and portgroups and assign that pairing to a node based on its role in the grid. In the image below, we can see how we define some rules for an eval node. 

.. image:: https://user-images.githubusercontent.com/17089008/96641900-62456500-12f3-11eb-94bc-2b6874f3f4f7.png
  :target: https://user-images.githubusercontent.com/17089008/96641900-62456500-12f3-11eb-94bc-2b6874f3f4f7.png


``/opt/so/saltstack/local/salt/firewall``

This is the directory where the firewall rules specific to your grid are located.

``/opt/so/saltstack/local/salt/firewall/portgroups.local.yaml``

This is where custom port groups are defined.

``/opt/so/saltstack/local/salt/firewall/hostgroups.local.yaml``

This is where many default named hostgroups get populated with IPs that are specific to your environment. When you run :ref:`so-allow` or ``so-firewall``, it modifies this file to include the IP provided in the proper hostgroup. Some node types get their IP assigned to multiple host groups

``/opt/so/saltstack/local/salt/firewall/assigned_hostgroups.local.map.yaml``

This is where host group and port group associations would be made to create custom host group and port group assignements that would apply to all nodes of a certain role type in the grid.



Managing
--------

Managing firewall rules, for all devices, should be done from the manager node using either :ref:`so-allow`, ``so-firewall`` or, for advanced cases, manually editing the yaml files.







analyst.sls
~~~~~~~~~~~
This is a list of hosts and networks that are allowed the analyst role. The analyst role allows connectivity to the sensor to use the web interface. Please note that 80 just redirects to 443 and no communication with the console is unencrypted.

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

  Please review the :ref:`salt` section to understand pillars and templates. Modifying these values outside of :ref:`so-allow` or ``so-firewall`` could lead to problems accessing your existing hosts. This is an advanced case and you most likely won't never need to modify these files.
  An example of why you might modify these templates is if you were adding some sort of agent to the hosts in your grid that are not part of Security Onion. This would allow you to open the ports needed to the hosts that required access. 

 

- Default port groups: ``/opt/so/saltstack/default/salt/firewall/portgroups.yaml``
This file contains the port groups that we have defined to be used across all the Security Onion node types. You will find that many of the aliases under firewall:aliases:ports

- Local port groups: ``/opt/so/saltstack/local/salt/firewall/portgroups.local.yaml``

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

During setup, the files from securityonion/files/firewall/ (https://github.com/Security-Onion-Solutions/securityonion/tree/master/files/firewall), are copied to the local directory located at ``/opt/so/saltstack/local/salt/firewall/``.
Once setup is complete and ``so-allow`` or ``so-firewall`` are called in the future, they modify the appropriate yaml files that are located under ``/opt/so/saltstack/local/salt/firewall/``. Since these yaml files are under ``/opt/so/saltstack/local/`` they will not be changed during a code update.
