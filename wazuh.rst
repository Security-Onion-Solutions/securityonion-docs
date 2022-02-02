.. _wazuh:

Wazuh
=====

Description
-----------

From https://wazuh.com/:

    Wazuh is a free, open source and enterprise-ready security monitoring solution for threat detection, integrity monitoring, incident response and compliance.

Usage
-----

Security Onion utilizes Wazuh as a Host Intrusion Detection System (HIDS) on each of the Security Onion nodes.

The Wazuh components include:

``manager`` - runs inside of ``so-wazuh`` Docker container and performs overall management of agents

``API`` - runs inside of ``so-wazuh`` Docker container and allows for remote management of agents, querying, etc.

``agent`` - runs directly on each host and monitors logs/activity and reports to ``manager``

The Wazuh API runs at TCP port ``55000`` locally, and currently uses the default credentials of ``user:foo`` and ``password:bar`` for authentication. Keep in mind, the API port is not exposed externally by default. Therefore, firewall rules need to be in place to reach the API from another location other than the Security Onion node on which the targeted Wazuh manager is running.

Since the manager runs inside a Docker container, many of the Wazuh binaries that you might want to run will need to be run inside the Docker container. For example, to run ``agent_upgrade``:

::

    sudo so-wazuh-agent-upgrade

Configuration
-------------

The main configuration file for Wazuh is ``/opt/so/conf/wazuh/ossec.conf``.

Email
-----

If you want to configure Wazuh to send email, please see the :ref:`email` section.

Syslog
------

If you want to send Wazuh logs to an external syslog collector, please see the :ref:`syslog-output` section.

Active Response
---------------

Sometimes, Wazuh may recognize legitimate activity as potentially malicious and engage in Active Response to block a connection. This may result in unintended consequences such as blocking of trusted IPs.  To prevent this from occurring, you can add your IP address to a safe list and change other settings in ``/opt/so/conf/wazuh/ossec.conf`` in the ``<!-- Active response -->`` section. :ref:`so-allow` does this for you automatically when you allow analyst connections.

Tuning Rules
------------

You can add new rules in ``/opt/so/rules/hids/local_rules.xml``. You can also modify existing rules by copying the rule to ``/opt/so/rules/hids/local_rules.xml``, making your changes, and adding ``overwrite="yes"`` as shown at https://documentation.wazuh.com/current/user-manual/ruleset/custom.html#changing-an-existing-rule. To suppress a Wazuh alert, you can add the rule and include ``noalert="1"`` in the ``rule`` section. 

The overall process would be as follows:

1. First, find the existing rule in ``/opt/so/rules/hids/ruleset/rules/``.
2. Copy the rule to ``/opt/so/rules/hids/local_rules.xml``.
3. Put the rule inside ``<group> </group>`` tags and give it a name.
4. Update the ``<rule>`` section to include ``noalert="1"`` along with ``overwrite="yes"``.
5. Finally, restart Wazuh with ``sudo so-wazuh-restart``.

Here is an example to suppress "Windows Logon Success" and "Windows User Logoff" alerts:

   ::
   
      <group name="customrules,">
        <rule id="60106" level="3" noalert="1" overwrite="yes">
          <if_sid>60103</if_sid>
          <field name="win.system.eventID">^528$|^540$|^673$|^4624$|^4769$</field>
          <description>Windows Logon Success</description>
          <options>no_full_log</options>
          <mitre>
            <id>T1078</id>
          </mitre>
          <group>authentication_success,pci_dss_10.2.5,gpg13_7.1,gpg13_7.2,gdpr_IV_32.2,hipaa_164.312.b,nist_800_53_AU.14,nist_800_53_AC.7,tsc_CC6.8,tsc_CC7.2,tsc_CC7.3,</group>
        </rule>

        <rule id="60137" level="3" noalert="1" overwrite="yes">
          <if_sid>60103</if_sid>
          <field name="win.system.eventID">^538$|^551$|^4634$|^4647$</field>
          <description>Windows User Logoff</description>
          <options>no_full_log</options>
          <group>pci_dss_10.2.5,gdpr_IV_32.2,hipaa_164.312.b,nist_800_53_AU.14,nist_800_53_AC.7,tsc_CC6.8,tsc_CC7.2,tsc_CC7.3,</group>
        </rule>
      </group>

.. note::

   This will not remove existing alerts that were generated before applying the new rule. Also note that this only suppresses the alert and not the underlying log.

Adding Agents
-------------

Navigate to the Downloads page in :ref:`soc` and download the appropriate Wazuh agent for your endpoint. This will ensure that you get the correct version of Wazuh. If your endpoint is not listed there, you can check the Wazuh website at https://documentation.wazuh.com/3.13/installation-guide/packages-list/index.html.

.. warning::

    It is important to ensure that you download the agent that matches the version of your Wazuh server. For example, if your Wazuh server is version 3.13.1, then you will want to deploy Wazuh agent version 3.13.1.

You can verify the version of your current Wazuh server using the following command:

::

    sudo docker exec -it so-wazuh dpkg -l |grep wazuh
    
| Once you've installed the Wazuh agent on the host(s) to be monitored, then perform the steps defined here:
| https://documentation.wazuh.com/3.13/user-manual/registering/command-line-registration.html

Please keep in mind that when you run ``manage_agents`` you will need to do so inside the ``so-wazuh`` container like this:

::

    sudo so-wazuh-agent-manage
    
You also may need to run :ref:`so-allow` to allow traffic from the IP address of your Wazuh agent(s).

Maximum Number of Agents
------------------------

Security Onion is configured to support a maximum number of ``14000`` Wazuh agents reporting to a single Wazuh manager.

Automated Deployment
--------------------

If you would like to automate the deployment of Wazuh agents, the Wazuh server includes ``ossec-authd``. You can read more about ``ossec-authd`` at https://documentation.wazuh.com/3.13/user-manual/reference/daemons/ossec-authd.html.

When using ``ossec-authd``, be sure to add a firewall exception for agents to access port ``1515/tcp`` on the Wazuh manager node by running :ref:`so-allow` and choosing the ``r`` option.

API
--------------------

The Wazuh API runs on port ``55000`` and requires a user to be created for access.

To add a new user, run ``so-wazuh-user-add``:

``so-wazuh-user-add newuser``

(you will be prompted to provide a password)

Next, restart Wazuh:

``so-wazuh-restart``

Once restarted, try accessing the API locally from the node using the newly created user and password:

``curl -k -u https://localhost:55000``

You should receive a message similar to the following indicating success:

    ::
    
    {"error":0,"data":{"msg":"Welcome to Wazuh HIDS API","api_version":"v3.13.1","hostname":"securityonion-is-the-coolest","timestamp":"Wed Feb 02 2022 13:09:03    GMT+0000 (UTC)"}}

If you receive a ``401`` (Unauthorized) error message, double-check the credentials or try running ``so-wazuh-user-passwd``, or confirm the the ``user`` file is correct within the Docker container:

``docker exec -it so-wazuh cat /var/ossec/api/configuration/auth/user``

More Information
----------------

.. seealso::

    For more information about Wazuh, please see https://documentation.wazuh.com/3.13/.
