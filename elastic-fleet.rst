.. _elastic-fleet:

Elastic Fleet
=============

:ref:`soc` includes a link on the sidebar that takes you to the Fleet page inside :ref:`kibana`.

Configuration
-------------

Elastic Fleet is pre-configured during Security Onion setup, however, centralized management of configuration is provided within its user interface inside of Kibana.

Configuration options for various components are detailed below.

Agents
------

This section displays registered Elastic agents (https://docs.securityonion.net/en/2.4/elastic-agent.html) and allows the user to add additional agents.

To view agent details, click the ``Host`` name. 

To assign the agent to a new policy, unenroll, upgrade the agent, or perform other actions, click the ``Actions`` menu on the right side of the agent listing and select the appropriate option.

By default, Elastic Agent is installed on every Security Onion grid node. As a result, all grid node agents will be enrolled in the ``SO-Grid-Nodes`` agent policy. We do not recommend removing policy settings for Security Onion grid node agents.

Adding Agents
-------------

To add a new agent to your deployment, see the following:

https://docs.securityonion.net/en/2.4/elastic-agent.html#deployment

Agent Policies
--------------

Agent policies dictate what data each agent will ingest and forward to Elasticsearch. This could be through the use of an HTTP, log file, or TCP-based input.

The individual components within each agent policy are called integrations (referred to as ``package policies`` at the API level), and refer to a specific input and settings pertinent to a data source.

For example, the ``SO-Grid-Nodes`` agent policy is comprised of the following integrations:

- elasticsearch-logs (``Elasticsearch`` integration)
- import-evtx-logs (``Custom Logs`` integration)
- import-suricata-logs (``Custom Logs`` integration)
- import-zeek-logs (``Custom Logs`` integration)
- kratos-logs (``Custom Logs`` integration)
- osquery-grid-nodes (``Osquery Manager`` integration)
- redis-logs (``Redis`` integration)
- strelka-logs (``Custom Logs`` integration)
- suricata-logs (``Custom Logs`` integration)
- syslog-tcp-514 (``Custom Logs`` integration)
- syslog-udp-514 (``Custom Logs`` integration)
- system-grid-nodes (``System`` integration)
- zeek-logs (``Custom Logs`` integration)

Agent Policies - endpoints-initial
----------------------------------

Agent installers downloaded from SOC --> Downloads, are deployed using the ``endpoints-initial`` Agent Policy. This policy includes the ``Elastic Defend``, ``Osquery Manager``, ``System``, and ``Windows`` integrations.

elastic-defend-endpoints (``Elastic Defend`` integration)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ``Elastic Defend`` integration has both free and paid features. By default, only the following free features are enabled:

- Event Collection - Windows

        - Credential Access
        - DLL and Driver Load
        - DNS
        - File
        - Network
        - Process
        - Registry
        - Security

- Event Collection - macOS

        - File
        - Process
        - Network

- Event Collection - Linux

        - File
        - Network
        - Process

osquery-endpoints (``Osquery Manager`` integration)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ``Osquery Manager`` integration runs osquery as a daemon on the endpoint, and makes the endpoint available for Live or Scheduled queries through the Osquery manager interface in Kibana.

system-endpoints (``System`` integration)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ``System`` integration collects the following logs from the endpoint, where applicable:

- System auth logs

    - ``/var/log/auth.log*``
    - ``/var/log/secure*``

- Syslog logs

    - ``/var/log/messages*``
    - ``/var/log/syslog*``
    - ``/var/log/system*``

- Windows Event Log - Application channel
- Windows Event Log - Security channel
- Windows Event Log - System channel

windows-endpoints (``Windows`` integration)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ``Windows`` integration collects the following logs from the endpoint, where applicable:

- Windows Event Log:

        - ForwardedEvents channel
        - Windows Powershell channel
        - Microsoft-Windows-Powershell/Operational channel
        - Microsoft-Windows-Sysmon/Operational channel

Integrations
------------

.. note::

    Security Onion 2.4.10 supports the following Elastic integrations:
    
    - aws
    - azure
    - cloudflare
    - elasticsearch
    - endpoint
    - fleet_server
    - fim
    - github
    - google_workspace
    - log
    - osquery_manager
    - redis
    - system
    - tcp
    - udp
    - windows
    - 1password

    Security Onion 2.4.20 supports these additional Elastic integrations:

    - apache
    - auditd
    - barracuda
    - cisco_asa
    - crowdstrike
    - darktrace
    - f5_bigip
    - fortinet
    - fortinet_fortigate
    - gcp
    - http_endpoint
    - httpjson
    - juniper
    - juniper_srx
    - kafka_log
    - lastpass
    - m365_defender
    - microsoft_defender_endpoint
    - microsoft_dhcp
    - netflow
    - o365
    - okta
    - panw
    - pfsense
    - sentinel_one
    - sonicwall_firewall
    - symantec_endpoint
    - ti_abusech
    - ti_misp
    - ti_otx
    - ti_recordedfuture
    - zscaler_zia
    - zscaler_zpa

    Security Onion 2.4.30 supports these additional Elastic integrations:

    - auth0
    - carbonblack_edr
    - checkpoint
    - cisco_duo
    - cisco_meraki
    - cisco_umbrella
    - fireeye
    - mimecast
    - pulse_connect_secure
    - snyk
    - sophos
    - sophos_central
    - tenable_sc
    - vsphere

    Security Onion 2.4.40 supports these additional Elastic integrations:

    - anomali
    - cisco_ftd
    - cisco_ios
    - cisco_ise
    - cybersixgill
    - iis
    - microsoft_sqlserver
    - mysql
    - proofpoint_tap
    - snort
    - threatquotient

You can read more about Elastic integrations at https://docs.elastic.co/integrations.

Adding an Integration
---------------------

New integrations can be added to existing policies to provide increased visibility and more comprehensive monitoring.

To add an integration to an existing policy:

From ``Fleet`` -> ``Agent policies`` -> ``$Policy name``, click ``Add Integration`` and follow the steps for adding the integration.

If the integration is designed to listen on a port to receive data, it will most likely default to listening on ``localhost`` only. Depending on how you are sending data to the integration, you may need to change that to ``0.0.0.0`` so that it can receive data from other hosts.

Adding a Custom Integration
---------------------------

A custom integration can be added by adding an integration such as the ``Custom Logs`` integration. We can specify various settings relative to the data source and define additional actions to be performed.

Enrollment Tokens
-----------------

An enrollment token allows an agent to enroll in Fleet, subscribe to a particular agent policy, and send data.

Each agent policy typically uses its own enrollment token. It is recommended that these tokens are NOT to be changed, especially those generated by default Security Onion agent policies.

Data Streams
------------

Data collected by Elastic Agent is sent to a data stream (https://www.elastic.co/guide/en/fleet/current/fleet-overview.html#data-streams-intro) by default. This allows data to be efficiently categorized and managed across a variety of datasets. This section within the Fleet UI allows for a quick review of data streams generated by data from Elastic Agent.

Settings
--------

The section provides details such as:

- Fleet server hosts in your deployment
- Configured outputs

  - specifies where data will be sent
  - this should include Elasticseach for the Fleet server and Logstash for Elastic Agent
  
- Method in which agent binaries will be downloaded

  - this will be a a local artifact repository if running an airgapped deployment)

.. warning::

    We do NOT recommend changing these settings, as they are managed by Security Onion.

Custom FQDN URL
---------------

You can add custom FQDN for Agents to connect to (for both control traffic on port TCP/8220 and data traffic on port TCP/5055) by editing the config as follows.

First, go to :ref:`administration` --> Configuration --> elasticfleet.

.. image:: images/config-item-elasticfleet.png
  :target: _images/config-item-elasticfleet.png

At the top of the page, click the ``Options`` menu and then enable the ``Show all configurable settings, including advanced settings.`` option. Then, navigate to elasticfleet --> config --> server --> custom_fqdn and set your custom FQDN. Within 15 minutes, the grid will apply these new settings and you should see the new FQDNs show up in Elastic Fleet settings. New agent installers will also be regenerated to use this new setting.

More Information
----------------

.. note::

    For more information about Fleet, please see https://www.elastic.co/guide/en/kibana/current/fleet.html.
