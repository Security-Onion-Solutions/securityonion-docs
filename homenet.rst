.. _homenet:

Homenet
=======

The homenet variable defines the networks that are considered home networks (those networks that you are monitoring and defending). It is used for :ref:`suricata` and, starting in Security Onion 2.3.110, for :ref:`zeek` as well.

Configuration
-------------

A node can be assigned either the global homenet or its own homenet.

By default, a node will use the global homenet pillar value if it is defined in the global pillar file (``/opt/so/saltstack/local/pillar/global.sls``) under ``global:hnmanager``. 

::

  global:
    soversion: '2.3.0'
    hnmanager: '10.0.0.0/8,192.168.0.0/16,172.16.0.0/12'

In order to define a per node homenet, it can be defined in the minion pillar file (``/opt/so/saltstack/local/pillar/minions/$SENSORNAME_$ROLE.sls``) under ``sensor:hnsensor``.

::

  sensor:
    interface: 'bond0'
    mainip: '172.16.106.112'
    mainint: 'eth0'
    zeek_lbprocs: 5
    suriprocs: 2
    manager: 'somanager1'
    mtu: 1500
    uniqueid: 1602623674
    hnsensor: 10.0.0.0/8

In order to sync the configuration change with the node, we can either wait for the node to automatically highstate on the predefined interval or we can force it. Since this homenet only applies to :ref:`suricata`, we can apply the ``suricata`` state to the node.

- From the manager:

  ::

    sudo salt $SENSORNAME_$ROLE state.apply suricata

or

- From the node:

  ::

    sudo salt-call state.apply suricata


More Information
----------------

.. seealso::

    For more information about :ref:`suricata`, such as defining other address groups or ports groups, please see the :ref:`suricata` section.

