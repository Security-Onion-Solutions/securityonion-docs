.. _wazuh:

Wazuh
=====

Description
-----------

From https://wazuh.com/:

    Wazuh is a free, open source and enterprise-ready security monitoring solution for threat detection, integrity monitoring, incident response and compliance.

Security Onion Usage
--------------------

Security Onion utilizes Wazuh as a Host Intrusion Detection System (HIDS) on each of the Security Onion nodes.

The Wazuh components include:

``manager`` - runs inside of ``so-wazuh`` Docker container and performs overall management of agents

``API`` - runs inside of ``so-wazuh`` Docker container and allows for remote management of agents, querying, etc.

``agent`` - runs directly on each host and monitors logs/activity and reports to ``manager``

The Wazuh API runs at TCP port 55000 locally, and currently uses the default credentials of ``user:foo`` and ``password:bar`` for authentication. Keep in mind, the API port is not exposed externally by default. Therefore, firewall rules need to be in place to reach the API from another location other than the Security Onion node on which the targeted Wazuh manager is running.

Configuration
-------------

The main configuration file for Wazuh is ``/var/ossec/etc/ossec.conf``.

Email
-----

If you want to configure Wazuh to send email, please see the :ref:`email` section.

Syslog
------

If you want to send Wazuh logs to an external syslog collector, please see the :ref:`syslog-output` section.

Active Response
---------------

Sometimes, Wazuh may recognize legitimate activity as potentially malicious, and engage in Active Response to block a connection. This may result in unintended consequences such as blocking of trusted IPs.  To prevent this from occurring,  you can add your IP address to a safe list and change other settings in ``/var/ossec/etc/ossec.conf``:

::

   <global>
   <white_list>desired_ip</white_list>
   </global>

Tuning Rules
------------

You can add new rules and modify existing rules in ``/var/ossec/rules/local_rules.xml``.

Adding Agents
-------------

| The Wazuh agent is cross platform and you can download agents for Windows/Unix/Linux/FreeBSD from the Wazuh website:
| https://documentation.wazuh.com/3.9/installation-guide/packages-list/index.html

.. note::

    It is important to ensure that you download the agent that matches the version of your Wazuh server. For example, if your Wazuh server is version 3.9.5, then you will want to deploy Wazuh agent version 3.9.5.

| Once you've installed the Wazuh agent on the host(s) to be monitored, then perform the steps defined here:
| https://documentation.wazuh.com/current/user-manual/registering/cli/using-command-line-linux.html

You may need to run :ref:`so-allow` to allow traffic from the IP address of your Wazuh agent(s).

Maximum Number of Agents
------------------------

Security Onion is configured to support a maximum number of ``14000`` Wazuh agents reporting to a single Wazuh manager.

Automated Deployment
--------------------

| If you would like to automate the deployment of Wazuh agents, the Wazuh server includes ``ossec-authd``:
| https://documentation.wazuh.com/3.9/user-manual/reference/daemons/ossec-authd.html

| When using ``ossec-authd``, be sure to add a firewall exception for agents to access port ``1515/tcp`` on the Wazuh manager node:
| ``sudo ufw allow proto tcp from agent_ip to any port 1515`` 

More Information
----------------

.. seealso::

    For more information about Wazuh, please see https://documentation.wazuh.com/3.9/.
