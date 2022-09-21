.. _salt:

Salt
====

From https://docs.saltstack.com/en/latest/:

   Salt is a new approach to infrastructure management built on a dynamic communication bus. Salt can be used for data-driven orchestration, remote execution for any infrastructure, configuration management for any app stack, and much more.

.. note::

   Salt is a core component of Security Onion as it manages all processes on all nodes. In a distributed deployment, the manager node controls all other nodes via salt. These non-manager nodes are referred to as salt minions.

Firewall Requirements
---------------------

| Salt minions must be able to connect to the manager node on ports ``4505/tcp`` and ``4506/tcp``:
| https://docs.saltproject.io/en/getstarted/system/communication.html

Checking Status
---------------

You can use salt's ``test.ping`` to verify that all your nodes are up:

::

    sudo salt \* test.ping

Remote Execution
----------------

Similarly, you can use salt's ``cmd.run`` to execute a command on all your nodes at once. For example, to check disk space on all nodes:

::

    sudo salt \* cmd.run 'df'

Configuration
-------------

Many of the options that are configurable in Security Onion are done by going to :ref:`administration` and then Configuration.

Salt Minion Startup Options
---------------------------

Currently, the salt-minion service startup is delayed by 30 seconds. This was implemented to avoid some issues that we have seen regarding Salt states that used the ip_interfaces grain to grab the management interface IP.

Diagnostic Logs
---------------

Diagnostic logs can be found in ``/opt/so/log/salt/``.

Known Issues
------------

You may see the following error in the salt-master log located at ``/opt/so/log/salt/master``:

::

  [ERROR   ][24983] Event iteration failed with exception: 'list' object has no attribute 'items'

The root cause of this error is a state trying to run on a minion when another state is already running. This error now occurs in the log due to a change in the exception handling within Salt's event module. Previously, in the case of an exception, the code would just pass. However, the exception is now logged. The error can be ignored as it is not an indication of any issue with the minions.

More Information
----------------

.. seealso::

    For more information about Salt, please see https://docs.saltstack.com/en/latest/.
