.. _third-party-integrations:

Third Party Integrations
========================

In addition to :ref:`network` and :ref:`host`, you may want to pull in data from other third party systems. You can do that via Elastic integrations which support many of the most common products and services. You can read more about Elastic integrations at https://docs.elastic.co/integrations.

.. warning::

        Third party integrations are provided by Elastic and are not specifically tested by the Security Onion team. Support provided by the Security Onion team for third party integrations is considered best-effort.

Adding an Integration
---------------------

New integrations can be added to existing policies to provide increased visibility and more comprehensive monitoring.

.. tip::

        When adding a new integration, it is important that you add it to an appropriate policy. 

        If an integration pulls the data, you should add it to the Fleet Server policy. Depending on complexity and log volume, it might make sense to stand up a Fleet Node and add your integrations to it.

        If an integration receives data pushed to it (for example: receiving syslog), consider adding it to the Fleet Server policy. If that is not feasible, then you can add it to the Grid Nodes policy but make sure to set the firewall rules correctly so that you are not opening ports on all of your nodes.

To add an integration to an existing policy:

- From the main Fleet page, click the ``Agent policies`` tab.
- Select the desired agent policy.
- Click the ``Add Integration`` button.
- Follow the steps for adding the integration.

.. note::

        If the integration is designed to listen on a port to receive data, it will most likely default to listening on ``localhost`` only. Depending on how you are sending data to the integration, you may need to change that to ``0.0.0.0`` so that it can receive data from other hosts.

For examples of this process, please see the :ref:`netflow` and :ref:`pfsense` sections. The :ref:`pfsense` section includes a link to a video which illustrates the process.

Adding a Custom Integration
---------------------------

A custom integration can be added by adding an integration such as the ``Custom Logs`` integration. You can specify various settings relative to the data source and define additional actions to be performed.

Managing Integration Upgrades
-----------------------------

.. tip::

        By default, integrations are not automatically kept up to date. This avoids potential log ingest downtime if there is an issue with the latest package or if the latest package requires a manual update to your integration configuration. If you would like to automatically upgrade integrations, you can change this behavior via :ref:`administration` -> Configuration -> elasticfleet -> config -> auto_upgrade_integrations. 
        
To find integrations that have upgrades available:

- Navigate to :ref:`elastic-fleet`.
- At the top left corner, click the menu.
- Under ``Management``, select ``Integrations``.
- Click the ``Installed Integrations`` tab.
- Review any integrations listed under ``Updates available``.

Managing Third Party Integration Index Templates
------------------------------------------------

Index templates for third party integrations can be managed as described in the :ref:`elasticsearch` section, but first ``managed_integrations`` must be updated by navigating to :ref:`administration-advanced-settings` --> Configuration --> manager --> managed_integrations.

Supported Integrations
----------------------

The current release of Security Onion supports all standard Elastic integrations as shown at https://docs.elastic.co/integrations.

.. note::

    These integrations have been added over the course of several different releases.

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

    - cisco_ftd
    - cisco_ios
    - cisco_ise
    - iis
    - microsoft_sqlserver
    - mysql
    - proofpoint_tap
    - snort
    - ti_anomali
    - ti_threatq

    Security Onion 2.4.50 supports these additional Elastic integrations:

    - citrix_adc
    - citrix_waf
    - nginx
    - winlog

    Security Onion 2.4.60 supports these additional Elastic integrations:

    - journald
    - ti_cybersixgill

    Security Onion 2.4.70 supports these additional Elastic integrations:

    - CEF

    Security Onion 2.4.100 supports these additional Elastic integrations:

    - tenable_io

    Security Onion 2.4.110 supports these additional Elastic integrations:

    - barracuda_cloudgen_firewall
    - imperva_cloud_waf

    Security Onion 2.4.120 supports these additional Elastic integrations:

    - cisco_secure_email_gateway
    - cloudflare_logpush
    - ti_opencti
    - ti_rapid7_threat_command
    - trendmicro
    - trend_micro_vision_one

    Security Onion 2.4.130 supports the remaining Elastic integrations.

More Information
----------------

.. note::

        You can read more about Elastic integrations at https://docs.elastic.co/integrations.
