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

- raw.githubusercontent.com (Security Onion public key)
- pkg-containers.githubusercontent.com
- sigs.securityonion.net (Signature files for Security Onion containers)  
- ghcr.io (Container downloads)  
- rules.emergingthreatspro.com (Emerging Threats IDS rules)  
- rules.emergingthreats.net (Emerging Threats IDS open rules)  
- github.com (Strelka and Sigma rules updates)  
- geoip.elastic.co (optional GeoIP updates for Elasticsearch)
- storage.googleapis.com (optional GeoIP updates for Elasticsearch)
- www.snort.org (if you are using the paid Snort Talos ruleset)  

If you are using our Security Onion ISO image, you will also need access to the following:

- repo.securityonion.net (Oracle Linux package updates)   

If you are not using our Security Onion ISO image and are instead performing a network installation, you will also need access to the following:

- update repo for whatever base OS you're installing on (:ref:`os` packages)
- download.docker.com (:ref:`docker` packages)
- repo.saltstack.com (:ref:`salt` packages)

Node Communication
~~~~~~~~~~~~~~~~~~

When configuring network firewalls for distributed deployments, you'll want to ensure that nodes can connect as shown below. 

All nodes to manager:

- TCP/443 - Sensoroni
- TCP/5000 - Docker registry
- TCP/8086 - influxdb
- TCP/4505 - Salt
- TCP/4506 - Salt

Elastic Agent:

- TCP/8220 (All nodes to Manager, Fleet nodes) - Elastic Agent management
- TCP/8443 (All nodes to Manager) - Elastic Agent binary updates
- TCP/5055 (All nodes to Manager, Fleet nodes, Receiver nodes) - Elastic Agent data

Search nodes from/to manager:

- TCP/9300 - Node-to-node for Elasticsearch
- TCP/9696 - Redis

Host Firewall
-------------

The remainder of this section will cover the host firewall built into Security Onion.

Configuration
-------------

You can configure the firewall by going to :ref:`administration` --> Configuration --> firewall.

Port Groups
-----------

Port groups are a way of grouping together ports similar to a firewall port/service alias. For example, if you had a web server you could include 80 and 443 tcp into an alias or in this case a port group.

Host Groups
-----------

Host groups are similar to port groups but for storing lists of hosts that will be allowed to connect to the associated port groups.

Function
--------

The firewall state is designed with the idea of creating port groups and host groups, each with their own alias or name, and associating the two in order to create an allow rule. A node that has a port group and host group association assigned to it will allow those hosts to connect to those ports on that node.

The default allow rules for each node are defined by its role (manager, searchnode, sensor, heavynode, etc) in the grid. Host groups and port groups can be created or modified from the manager node by going to :ref:`administration` --> Configuration --> firewall. When setup is run on a new node, it will ask the manager to add itself to the appropriate host groups. All node types are added to the minion host group to allow :ref:`salt` communication. If you were to add a search node, you would see its IP appear in both the ``minion`` and the ``search_node`` host groups.

Managing
--------

Managing firewall rules for all devices should be done from the manager node by going to :ref:`administration` --> Configuration --> firewall.

Examples
--------

Removing a host or network
~~~~~~~~~~~~~~~~~~~~~~~~~~

If you previously added a host or network to your firewall configuration and now need to remove them, you can use :ref:`administration` --> Configuration --> firewall.

Allow hosts to send syslog to a sensor node
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

By default, if you go to :ref:`administration` --> Configuration --> firewall and add a host to the syslog hostgroup, that host will only be allowed to connect to the manager node. 


ADVANCED Firewall Config
========================

Modify a default port group
~~~~~~~~~~~~~~~~~~~~~~~~~~~

In this example, we will be extending the default nginx port group to include port 8086 for a standalone node. By default, only the analyst hostgroup is allowed access to the nginx ports. At the end of this example, IPs in the analyst host group will be able to connect to ports 80, 443, and 8086 on our standalone node.

1. Click the Options dropdown menu and then select the "Show all configurable settings, including advanced settings." option.
2. Under ``firewall``, select ``portgroups``, and then locate the ``nginx`` portgroup. 
3. Select ``tcp``.
4. Select the manager node and then pecify the port to be added.
5. Click the checkmark to save the value.
6. Click the "SYNCHRONIZE GRID" button if you would like to apply the rules to the manager immediately.

Creating a custom host group with a custom port group
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In this example, we will be adding a new custom hostgroup to allow a custom set of hosts to connect to a custom port on the idh nodes on port 1234.

1. Select "Show all configuration settings, including advanced settings." on the options dropdown menu.
2. Under firewall select customhostgroup0 that is part of the hostgroups section.
3. Select the idh node that you want to allow access to under the dropdown.
4. Add the list of hosts that require access and select the checkmark.
5. Under firewall select customportgroup0 that is part of the portgroups section.
6. Select the idh node that you want to allow access to under the dropdown.
7. Add the apporpriate port under the appropriate protocol. In this case we will be adding 1234 tcp and selecting the checkmark.
8. Under firewall/roles select idh/chain/DOCKER-USER/hostgroups/customhostgroups/portgroups.
9. Select the idh node that we want to allow access to under the dropdown. 
10. Add the portgroup customportgroup0 to the list and select the checkmark.
11. The next time the idh node checks in it will get the appropriate firewall rules.
