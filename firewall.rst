.. _firewall:

Firewall
========

This section will cover both network firewalls outside of Security Onion and the host-based firewall built into Security Onion.

Network Firewalls
-----------------

This first sub-section will discuss network firewalls outside of Security Onion.

Internet Communication
~~~~~~~~~~~~~~~~~~~~~~

When configuring network firewalls for Internet-connected deployments (non-:ref:`airgap`), you'll want to ensure that the deployment can connect outbound to the following:

- repo.securityonion.net (CentOS Updates)   
- raw.githubusercontent.com (Security Onion public key)
- pkg-containers.githubusercontent.com
- sigs.securityonion.net (Signature files for Security Onion containers)  
- ghcr.io (Container downloads)  
- rules.emergingthreatspro.com (Emerging Threats IDS rules)  
- rules.emergingthreats.net (Emerging Threats IDS open rules)  
- www.snort.org (Paid Snort Talos ruleset)  
- github.com (Strelka and Sigma rules updates)  
- geoip.elastic.co (GeoIP updates for Elasticsearch)
- notary.kolide.co (osquery agent update)  
- Ubuntu PPAs (OS Updates - Ubuntu only)  
- download.docker.com (Docker packages - Ubuntu only)
- repo.saltstack.com (Salt packages - Ubuntu only)
- packages.wazuh.com (Wazuh packages - Ubuntu only) 

In the case of a distributed deployment, you can configure your nodes to pull everything from the manager so that only the manager requires Internet access.

Node Communication
~~~~~~~~~~~~~~~~~~

When configuring network firewalls for distributed deployments, you'll want to ensure that nodes can connect as shown below. 

All nodes to manager:

- 22 (only needed for initial setup)
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

Host Firewall
-------------

The remainder of this section will cover the host firewall built into Security Onion.

Port Groups
-----------

Port groups are a way of grouping together ports similar to a firewall port/service alias. For example, if you had a web server you could include 80 and 443 tcp into an alias or in this case a port group.

Host Groups
-----------

Host groups are similar to port groups but for storing lists of hosts that will be allowed to connect to the associated port groups.

Function
--------

The firewall state is designed with the idea of creating port groups and host groups, each with their own alias or name, and associating the two in order to create an allow rule. A node that has a port group and host group association assigned to it will allow those hosts to connect to those ports on that node.

The default allow rules for each node are defined by its role (manager, searchnode, sensor, heavynode, etc) in the grid. Host groups and port groups can be created or modified from the manager node using either :ref:`so-allow`, ``so-firewall`` or manually editing the yaml files. When setup is run on a new node, it will SSH to the manager using the ``soremote`` account and add itself to the appropriate host groups. All node types are added to the minion host group to allow :ref:`salt` communication. If you were to add a search node, you would see its IP appear in both the ``minion`` and the ``search_node`` host groups.

There are two directories that contain the yaml files for the firewall configuration.

``/opt/so/saltstack/default/salt/firewall/``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This directory contains the default firewall rules. The files in this directory should not be modified as they could possibly be overwritten during a :ref:`soup` update in the event we update those files.

``/opt/so/saltstack/default/salt/firewall/portgroups.yaml`` is where the default port groups are defined. 

.. image:: https://user-images.githubusercontent.com/17089008/96641876-5a85c080-12f3-11eb-90e3-0ac3d2dc9b8b.png
  :target: https://user-images.githubusercontent.com/17089008/96641876-5a85c080-12f3-11eb-90e3-0ac3d2dc9b8b.png

``/opt/so/saltstack/default/salt/firewall/hostgroups.yaml`` is where the default hostgroups are defined. There isn't much in here other than ``anywhere``, ``dockernet``, ``localhost`` and ``self``.

``/opt/so/saltstack/default/salt/firewall/assigned_hostgroups.map.yaml`` is where the default allow rules come together and pair hostgroups and portgroups and assign that pairing to a node based on its role in the grid. In the image below, we can see how we define some rules for an eval node.

.. image:: https://user-images.githubusercontent.com/17089008/96641900-62456500-12f3-11eb-94bc-2b6874f3f4f7.png
  :target: https://user-images.githubusercontent.com/17089008/96641900-62456500-12f3-11eb-94bc-2b6874f3f4f7.png

``/opt/so/saltstack/local/salt/firewall/``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This directory stores the firewall rules specific to your grid.

``/opt/so/saltstack/local/salt/firewall/portgroups.local.yaml`` defines custom port groups.

``/opt/so/saltstack/local/salt/firewall/hostgroups.local.yaml`` is where many default named hostgroups get populated with IPs that are specific to your environment. When you run :ref:`so-allow` or ``so-firewall``, it modifies this file to include the IP provided in the proper hostgroup. Some node types get their IP assigned to multiple host groups.

``/opt/so/saltstack/local/salt/firewall/assigned_hostgroups.local.map.yaml`` is where host group and port group associations would be made to create custom host group and port group assignements that would apply to all nodes of a certain role type in the grid.

Managing
--------

Managing firewall rules for all devices should be done from the manager node using either :ref:`so-allow`, ``so-firewall`` or, for advanced cases, manually editing the yaml files.

Examples
--------

Removing a host or network
~~~~~~~~~~~~~~~~~~~~~~~~~~

If you previously added a host or network to your firewall configuration and now need to remove them, you can use ``so-firewall`` with the ``excludehost`` option. For example:

::

  sudo so-firewall excludehost analyst 192.168.1.255

Allow hosts to send syslog to a sensor node
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

By default, if you use :ref:`so-allow` to add a host to the syslog hostgroup, that host will only be allowed to connect to the manager node. If we want to allow a host or group of hosts to send syslog to a sensor, then we can do the following:

1. Create a new host group that will contain the IPs of the hosts that you want to allow to connect to the sensor. This will add the host group to ``/opt/so/saltstack/local/salt/firewall/hostgroups.local.yaml``. If the host group already exists, you can skip to step 2. Run the following on the manager:

  ::

    sudo so-firewall addhostgroup <GROUP_NAME>

2. Add the desired IPs to the host group. This will add the IPs to the host group in ``/opt/so/saltstack/local/salt/firewall/hostgroups.local.yaml``.

  ::

    sudo so-firewall includehost <GROUP_NAME> <IP>

3. Since we reused the syslog port group that is already defined, we don't need to create a new port group. Now we have to build the association between the host group and the syslog port group and assign that to our sensor node. Add the following to the sensor minion pillar file located at ``/opt/so/saltstack/local/pillar/minions/<HOSTNAME>_<ROLE>.sls``:

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

    sudo salt <HOSTNAME>_<ROLE> state.apply firewall


Modify a default port group
~~~~~~~~~~~~~~~~~~~~~~~~~~~

In this example, we will be extending the default nginx port group to include port 8086 for a standalone node. By default, only the analyst hostgroup is allowed access to the nginx ports. At the end of this example IPs in the analyst host group, will be able to connect to 80, 443 and 8086 on our standalone node.

All the following will need to be run from the manager.

1. Add the custom nginx port group:

  ::

    sudo so-firewall addportgroup nginx

2. Add the required ports to the port group. In this step we are redefining the nginx port group, so be sure to include the default ports as well if you want to keep them:

  ::

    sudo so-firewall addport nginx tcp 80
    sudo so-firewall addport nginx tcp 443
    sudo so-firewall addport nginx tcp 8086

3. Associate this port group redefinition to a node. Add the following to the minion's sls file located at ``/opt/so/saltstack/local/pillar/minions/<HOSTNAME>_<ROLE>.sls``:

  ::

    firewall:
      assigned_hostgroups:
        chain:
          DOCKER-USER:
            hostgroups:
              analyst:
                portgroups:
                  - portgroups.nginx

4. Apply the firewall state to the node, or wait for the highstate to run for the changes to happen automatically:

  ::

    sudo salt-call state.apply firewall


.. warning::

  Please review the :ref:`salt` section to understand pillars and templates. Modifying these values outside of :ref:`so-allow` or ``so-firewall`` could lead to problems accessing your existing hosts. This is an advanced case and you most likely won't never need to modify these files.
