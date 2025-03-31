.. _salt:

Salt
====

From https://docs.saltproject.io/en/latest/topics/about_salt_project.html#about-salt:

   Built on Python, Salt is an event-driven automation tool and framework to deploy, configure, and manage complex IT systems. Use Salt to automate common infrastructure administration tasks and ensure that all the components of your infrastructure are operating in a consistent desired state.

.. note::

   Salt is a core component of Security Onion as it manages all processes on all nodes. In a distributed deployment, the manager node controls all other nodes via salt. These non-manager nodes are referred to as salt minions.

Firewall Requirements
---------------------

Salt minions must be able to connect to the manager node on ports ``4505/tcp`` and ``4506/tcp``.

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

Node checkin
------------

If you want to force a node to do a full update of all salt states, you can run ``so-checkin``. This will execute ``salt-call state.highstate -l info`` which outputs to the terminal with the log level set to ``info`` so that you can see exactly what's happening:

::

    sudo so-checkin

Configuration
-------------

Many of the options that are configurable in Security Onion are done by going to :ref:`administration` and then Configuration.

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

.. note::

    For more information about Salt, please see https://docs.saltproject.io/en/latest/contents.html.
