.. _firewall:

Firewall
========

Node Communication
------------------
When configuring network-based firewalls, you'll want to take into consideration the communication/ports required for nodes to talk to one another. 

All nodes to manager:

- 3142 (Apt-cacher-ng) (if manager proxy enabled)
- 5000 (Docker registry)
- 8086 (influxdb)
- 4505 (Salt)
- 4506 (Salt)
- 5644 (Filebeat)
- 443 (Sensoroni)
- 8080 (Osquery, if enabled)

Search nodes from/to manager:

- 9300 (Node-to-node for Elasticsearch)
- 9696 (Redis)

Port Groups
-----------

Port groups are a way of grouping together ports similar to a firewall port/service alias. For example if you had a web server you could include 80 and 443 tcp into an alias or in this case a port group.

Host Groups
-----------

Host groups are similar to port groups but for storing lists of hosts that will be allowed to connect to the associated port groups.

Function
--------

The firewall state is designed to function with the idea of creating port groups and host groups, each with their own alias or name, and associating the two in order to create an allow rule. A node that has a port group and host group association assigned to it will allow those hosts to connect to those ports on that node.

The default allow rules for each node are defined by its role (manager, searchnode, sensor, heavynode, etc) in the grid. Host groups and port groups can be created or modified from the manager node using either :ref:`so-allow`, ``so-firewall`` or manually editing the yaml files. When setup is run on a new node, it will SSH to the manager using the ``soremote`` account, and add itself to the appropriate host groups. All node types are added to the minion host group to allow Salt communication. If you were to add a search node, you would see its IP appear in both the ``minion`` and the ``search_node`` host groups.

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

Examples
--------

Allow hosts to send syslog to a sensor node.
############################################

By default, if you use :ref:`so-allow` to add a host to the syslog hostgroup, that host will only be allowed to connect to the manager node. If we want to allow a host or group of hosts to send syslog to a sensor, then we can do the following:

1. Create a new host group that will contain the IPs of the hosts that you want to allow to connect to the sensor. This will add the host group to ``/opt/so/saltstack/local/salt/firewall/hostgroups.local.yaml``. If the host group already exists, you can skip to step 2. From the manager run:

  ::

    sudo so-firewall addhostgroup <GROUP_NAME>

2. Add the desired IPs to the host group. This will add the IPs to the host group in ``/opt/so/saltstack/local/salt/firewall/hostgroups.local.yaml``.

  ::

    sudo so-firewall includehost <GROUP_NAME> <IP>

3. Since we reused the syslog port group that is already defined, we don't need to create a new port group. Now we have to build the association between the host group and the syslog port group and assign that to our sensor node. Add the following to the sensor minion pillar file located at ``/opt/so/saltstack/local/pillar/minions/<HOSTNAME>_<ROLE>.sls``

  ::

    firewall:
      assigned_hostgroups:
        chain:
          DOCKER-USER:
            hostgroups:
              syslogtosensor1:
                portgroups:
                  - portgroups.syslog

4. Now that the configuration is in place, you can either wait for the sensor to sync with Salt running on the manager, or you can force it to update its firewall by running the following from the manager:

  ::

    salt <HOSTNAME>_<ROLE> state.apply firewall


.. warning::

  Please review the :ref:`salt` section to understand pillars and templates. Modifying these values outside of :ref:`so-allow` or ``so-firewall`` could lead to problems accessing your existing hosts. This is an advanced case and you most likely won't never need to modify these files.
