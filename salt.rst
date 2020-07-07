.. _salt:

Salt
====

From https://docs.saltstack.com/en/latest/:

   Salt is a new approach to infrastructure management built on a dynamic communication bus. Salt can be used for data-driven orchestration, remote execution for any infrastructure, configuration management for any app stack, and much more.

Salt is a core component of Security Onion 2.0.

Firewall Requirements
---------------------

Sensors need to be able to connect to the management server on ports ``4505/tcp`` and ``4506/tcp``:

http://docs.saltstack.com/topics/tutorials/firewall.html

Checking Status
---------------

Want to verify all your sensors are up?

::

    sudo salt '*' test.ping

Remote Execution
----------------

Want to execute a command on all your sensors at once?

::

    sudo salt '*' cmd.run 'InsertYourCommandHere'

Configuration Layout
--------------------

The ``static.sls`` configuration file houses global configuration settings for your entire grid. Most of these setting can be overridden in the ``sensorname.sls`` file.

``/opt/so/saltstack/local/pillar/static.sls``

::

   static:
     hnmaster: GLOBALHOMENET - This is your home_net for you grid. Can be overridden on each sensor.
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
