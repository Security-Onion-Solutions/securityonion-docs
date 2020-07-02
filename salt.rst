Salt
====

From https://docs.saltstack.com/en/latest/:

   Salt is a new approach to infrastructure management built on a dynamic communication bus. Salt can be used for data-driven orchestration, remote execution for any infrastructure, configuration management for any app stack, and much more.

Salt is a core component of Security Onion 2.0.

Firewall Requirements
---------------------

Sensors need to be able to connect to the master server on ports ``4505/tcp`` and ``4506/tcp``:

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
