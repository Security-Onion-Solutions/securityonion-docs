.. _salt:

Salt
====

From https://docs.saltstack.com/en/latest/:

   Salt is a new approach to infrastructure management built on a dynamic communication bus. Salt can be used for data-driven orchestration, remote execution for any infrastructure, configuration management for any app stack, and much more.

.. note::

   Salt is a core component of Security Onion 2 as it manages all processes on all nodes. In a distributed deployment, the manager node controls all other nodes via salt. These non-manager nodes are referred to as salt minions.

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

Many of the options that are configurable in Security Onion 2 are done via pillar assignments in either the global or minion pillar files. Pillars are a Saltstack concept, formatted typically in YAML, that can be used to parameterize states via templating. Saltstack states are used to ensure the state of objects on a minion. In many of the use cases below, we are providing the ability to modify a configuration file by editing either the global or minion pillar file.

Global pillar file: This is the pillar file that can be used to make global pillar assignments to the nodes. It is located at ``/opt/so/saltstack/local/pillar/global.sls``.

Minion pillar file: This is the minion specific pillar file that contains pillar definitions for that node. Any definitions made here will override anything defined in other pillar files, including global. This is located at ``/opt/so/saltstack/local/pillar/minions/<minionid>.sls``.

Default pillar file: This is the pillar file located under ``/opt/so/saltstack/default/pillar/``. Files here should not be modified as changes would be lost during a code update.

Local pillar file: This is the pillar file under ``/opt/so/saltstack/local/pillar/``. These are the files that will need to be changed in order to customize nodes.

.. warning::

   Salt sls files are in YAML format. When editing these files, please be very careful to respect YAML syntax, especially whitespace. For more information, please see https://docs.saltproject.io/en/latest/topics/troubleshooting/yaml_idiosyncrasies.html.
   
Here are some of the items that can be customized with pillar settings:

- :ref:`filebeat`
 
- :ref:`firewall`
 
- :ref:`managing-alerts`

- :ref:`suricata`

- :ref:`zeek`

Salt Minion Startup Options
---------------------------

Currently, the salt-minion service startup is delayed by 30 seconds. This was implemented to avoid some issues that we have seen regarding Salt states that used the ip_interfaces grain to grab the management interface IP.

If you need to increase this delay, it can be done using the ``salt:minion:service_start_delay`` pillar. This can be done in the minion pillar file if you want the delay for just that minion, or it can be done in the ``global.sls`` file if it should be applied to all minions.

::

  salt:
    minion:
      service_start_delay: 60 # in seconds.

More Information
----------------

.. seealso::

    For more information about Salt, please see https://docs.saltstack.com/en/latest/.
