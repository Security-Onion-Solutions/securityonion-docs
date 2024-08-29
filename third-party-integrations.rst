.. _third-party-integrations:

Third Party Integrations
========================

In addition to :ref:`network` and :ref:`host`, you may want to pull in data from other third party systems. You can do that via Elastic integrations which support many of the most common products and services. You can read more about Elastic integrations at https://docs.elastic.co/integrations.

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

For examples of this process, please see the :ref:`netflow` and :ref:`pfsense` sections.

Adding a Custom Integration
---------------------------

A custom integration can be added by adding an integration such as the ``Custom Logs`` integration. You can specify various settings relative to the data source and define additional actions to be performed.

Supported Integrations
----------------------

The current release of Security Onion supports the following Elastic integrations:

==============================  ==========================================================
Elastic Integration             Elastic Documentation
==============================  ==========================================================
1password                       https://docs.elastic.co/en/integrations/1password
apache                          https://docs.elastic.co/en/integrations/apache
auditd                          https://docs.elastic.co/en/integrations/auditd
auth0                           https://docs.elastic.co/en/integrations/auth0
aws                             https://docs.elastic.co/en/integrations/aws
azure                           https://docs.elastic.co/en/integrations/azure
barracuda                       https://docs.elastic.co/en/integrations/barracuda
carbonblack_edr                 https://docs.elastic.co/en/integrations/carbonblack_edr
cef                             https://docs.elastic.co/en/integrations/cef
checkpoint                      https://docs.elastic.co/en/integrations/checkpoint
cisco_asa                       https://docs.elastic.co/en/integrations/cisco_asa
cisco_duo                       https://docs.elastic.co/en/integrations/cisco_duo
cisco_ftd                       https://docs.elastic.co/en/integrations/cisco_ftd
cisco_ios                       https://docs.elastic.co/en/integrations/cisco_ios
cisco_ise                       https://docs.elastic.co/en/integrations/cisco_ise
cisco_meraki                    https://docs.elastic.co/en/integrations/cisco_meraki
cisco_umbrella                  https://docs.elastic.co/en/integrations/cisco_umbrella
citrix_adc                      https://docs.elastic.co/en/integrations/citrix_adc
citrix_waf                      https://docs.elastic.co/en/integrations/citrix_waf
cloudflare                      https://docs.elastic.co/en/integrations/cloudflare
crowdstrike                     https://docs.elastic.co/en/integrations/crowdstrike
darktrace                       https://docs.elastic.co/en/integrations/darktrace
elasticsearch                   https://docs.elastic.co/en/integrations/elasticsearch
endpoint                        https://docs.elastic.co/en/integrations/endpoint
f5_bigip                        https://docs.elastic.co/en/integrations/f5_bigip
fim                             https://docs.elastic.co/en/integrations/fim
fireeye                         https://docs.elastic.co/en/integrations/fireeye
fleet_server                    https://docs.elastic.co/en/integrations/fleet_server
fortinet                        https://docs.elastic.co/en/integrations/fortinet
fortinet_fortigate              https://docs.elastic.co/en/integrations/fortinet_fortigate
gcp                             https://docs.elastic.co/en/integrations/gcp
github                          https://docs.elastic.co/en/integrations/github
google_workspace                https://docs.elastic.co/en/integrations/google_workspace
http_endpoint                   https://docs.elastic.co/en/integrations/http_endpoint
httpjson                        https://docs.elastic.co/en/integrations/httpjson
iis                             https://docs.elastic.co/en/integrations/iis
journald                        https://docs.elastic.co/en/integrations/journald
juniper_srx                     https://docs.elastic.co/en/integrations/juniper_srx
kafka_log                       https://docs.elastic.co/en/integrations/kafka_log
lastpass                        https://docs.elastic.co/en/integrations/lastpass
log                             https://docs.elastic.co/en/integrations/log
m365_defender                   https://docs.elastic.co/en/integrations/m365_defender
microsoft_defender_endpoint     https://docs.elastic.co/en/integrations/microsoft_defender_endpoint
microsoft_dhcp                  https://docs.elastic.co/en/integrations/microsoft_dhcp
microsoft_sqlserver             https://docs.elastic.co/en/integrations/microsoft_sqlserver
mimecast                        https://docs.elastic.co/en/integrations/mimecast
mysql                           https://docs.elastic.co/en/integrations/mysql
:ref:`netflow`                  https://docs.elastic.co/en/integrations/netflow
nginx                           https://docs.elastic.co/en/integrations/nginx
o365                            https://docs.elastic.co/en/integrations/o365
okta                            https://docs.elastic.co/en/integrations/okta
osquery_manager                 https://docs.elastic.co/en/integrations/osquery_manager
panw                            https://docs.elastic.co/en/integrations/panw
:ref:`pfsense`                  https://docs.elastic.co/en/integrations/pfsense
proofpoint_tap                  https://docs.elastic.co/en/integrations/proofpoint_tap
pulse_connect_secure            https://docs.elastic.co/en/integrations/pulse_connect_secure
redis                           https://docs.elastic.co/en/integrations/redis
sentinel_one                    https://docs.elastic.co/en/integrations/sentinel_one
snort                           https://docs.elastic.co/en/integrations/snort
snyk                            https://docs.elastic.co/en/integrations/snyk
sonicwall_firewall              https://docs.elastic.co/en/integrations/sonicwall_firewall
sophos                          https://docs.elastic.co/en/integrations/sophos
sophos_central                  https://docs.elastic.co/en/integrations/sophos_central
symantec_endpoint               https://docs.elastic.co/en/integrations/symantec_endpoint
system                          https://docs.elastic.co/en/integrations/system
tcp                             https://docs.elastic.co/en/integrations/tcp
tenable_io                      https://docs.elastic.co/en/integrations/tenable_io
tenable_sc                      https://docs.elastic.co/en/integrations/tenable_sc
ti_abusech                      https://docs.elastic.co/en/integrations/ti_abusech
ti_anomali                      https://docs.elastic.co/en/integrations/ti_anomali
ti_cybersixgill                 https://docs.elastic.co/en/integrations/ti_cybersixgill
ti_misp                         https://docs.elastic.co/en/integrations/ti_misp
ti_otx                          https://docs.elastic.co/en/integrations/ti_otx
ti_recordedfuture               https://docs.elastic.co/en/integrations/ti_recordedfuture
ti_threatq                      https://docs.elastic.co/en/integrations/ti_threatq
udp                             https://docs.elastic.co/en/integrations/udp
vsphere                         https://docs.elastic.co/en/integrations/vsphere
windows                         https://docs.elastic.co/en/integrations/windows
winlog                          https://docs.elastic.co/en/integrations/winlog
zscaler_zia                     https://docs.elastic.co/en/integrations/zscaler_zia
zscaler_zpa                     https://docs.elastic.co/en/integrations/zscaler_zpa
==============================  ==========================================================

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

More Information
----------------

.. note::

        You can read more about Elastic integrations at https://docs.elastic.co/integrations.
