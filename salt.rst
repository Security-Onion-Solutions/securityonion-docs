.. _salt:

Salt
====

From https://docs.saltstack.com/en/latest/:

   Salt is a new approach to infrastructure management built on a dynamic communication bus. Salt can be used for data-driven orchestration, remote execution for any infrastructure, configuration management for any app stack, and much more.

.. note::

   Salt is a core component of Security Onion 2.0 as it manages all processes on all nodes. In a distributed deployment, the manager node controls all other nodes via salt. These non-manager nodes are referred to as salt minions.

Firewall Requirements
---------------------

Minions must be able to connect to the manager node on ports ``4505/tcp`` and ``4506/tcp``:

http://docs.saltstack.com/topics/tutorials/firewall.html

Checking Status
---------------

You can use salt's ``test.ping`` to verify that all your nodes are up:

::

    sudo salt '*' test.ping

Remote Execution
----------------

Similarly, you can use salt's ``cmd.run`` to execute a command on all your nodes at once. For example, to check disk space on all nodes:

::

    sudo salt '*' cmd.run 'df'

Configuration Layout
--------------------

The ``static.sls`` configuration file houses global configuration settings for your entire grid. Most of these setting can be overridden in the ``sensorname.sls`` file.

``/opt/so/saltstack/local/pillar/static.sls``

::

   static:
     hnmaster: GLOBALHOMENET - This is your home_net for your grid. Can be overridden on each sensor.
     ntpserver: YOURNTPSERVER
     homenet: YOURHOMENET
     proxy: PROXYSERVER
     broversion: BRO|COMMUNITY
     masterupdate: 0|1

``/opt/so/saltstack/local/pillar/minions/sensorname.sls``

::

   sensor:
     interface: bond0
     mainip: IPADDRESS of the Sensor
