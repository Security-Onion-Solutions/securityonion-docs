.. _release-notes:

Release Notes
=============

2.3.61 Changes
----------------

- FIX: Airgap link to Release Notes `#4685 <https://github.com/Security-Onion-Solutions/securityonion/issues/4685>`_
- FIX: CyberChef unable to load due to recent Content Security Policy restrictions `#4885 <https://github.com/Security-Onion-Solutions/securityonion/issues/4885>`_
- UPGRADE: alpine 3.12.1 to latest for Fleet image `#4823 <https://github.com/Security-Onion-Solutions/securityonion/issues/4823>`_
- UPGRADE: Elastic 7.13.4 `#4730 <https://github.com/Security-Onion-Solutions/securityonion/issues/4730>`_
- UPGRADE: Zeek 4.0.3 `#4716 <https://github.com/Security-Onion-Solutions/securityonion/issues/4716>`_

2.3.60 Hotfix [ECSFIX, HEAVYNODE_SSL_LOGSTASH_REDIS_PIPELINES, FBPIPELINE, CURATORAUTH] Changes
----------------
- FIX: Curator's authentication to Elasticsearch was incorrectly configured for the version currently in use.
- FIX: Some logs from Filebeat were not being properly routed to the correct pipeline causing the log to fill up the disk.
- FEATURE: All hotfixes going forward will have an ISO so that airgap users can follow the standard soup process as they would for normal releases.
- FIX: Hotfix to revert Strelka and Wazuh Elastic Common Schema (ECS) changes that weren't intended for 2.3.60.
- FIX: Correct SSL certificate common name (CN) to match heavy node hostnames. Only applicable to grids with heavy nodes. May require manual restart of Redis, Elasticsearch, Filebeat, and Logstash containers (in that order), once the heavy nodes have succeeded in applying highstate. For more information see the related blog post at https://blog.securityonion.net/2021/07/security-onion-2360-heavy-node-hotfix.html

2.3.60 Changes
----------------

- FEATURE: Ability to change default SOC timezone instead of using browser's timezone `#4261 <https://github.com/Security-Onion-Solutions/securityonion/issues/4261>`_
- FEATURE: Add SOC database to the backups `#3748 <https://github.com/Security-Onion-Solutions/securityonion/issues/3748>`_
- FEATURE: Add so-elasticsearch-query tool `#4437 <https://github.com/Security-Onion-Solutions/securityonion/issues/4437>`_
- FEATURE: Create a new Quick Drilldown option in SOC `#4469 <https://github.com/Security-Onion-Solutions/securityonion/issues/4469>`_
- FEATURE: Display Security Onion version number in so-setup `#3348 <https://github.com/Security-Onion-Solutions/securityonion/issues/3348>`_
- FEATURE: Elastic Auth `#1423 <https://github.com/Security-Onion-Solutions/securityonion/issues/1423>`_
- FEATURE: Implement retention policy for InfluxDB `#3264 <https://github.com/Security-Onion-Solutions/securityonion/issues/3264>`_
- FEATURE: New Grafana dashboards for InfluxDB RPs `#4609 <https://github.com/Security-Onion-Solutions/securityonion/issues/4609>`_
- FEATURE: Pillarize Filebeat Modules `#3859 <https://github.com/Security-Onion-Solutions/securityonion/issues/3859>`_
- FEATURE: Pivot from Alerts/Hunt to CyberChef `#4081 <https://github.com/Security-Onion-Solutions/securityonion/issues/4081>`_
- FEATURE: Pivot from SOC PCAP to CyberChef `#1596 <https://github.com/Security-Onion-Solutions/securityonion/issues/1596>`_
- FEATURE: Support adjustable SOC session timeout `#4586 <https://github.com/Security-Onion-Solutions/securityonion/issues/4586>`_
- FIX: Add a prompt when soup requires the path or cdrom device to be input `#3551 <https://github.com/Security-Onion-Solutions/securityonion/issues/3551>`_
- FIX: Add event_data to Elasticsearch template(s) `#4012 <https://github.com/Security-Onion-Solutions/securityonion/issues/4012>`_
- FIX: Allow for spaces in password on kickstart script (ISO)  `#1079 <https://github.com/Security-Onion-Solutions/securityonion/issues/1079>`_
- FIX: Change Acknowledge, Escalate, and expandEvent buttons from title to tooltip `#4497 <https://github.com/Security-Onion-Solutions/securityonion/issues/4497>`_
- FIX: Disallow so-suricata-start from running on the manager node `#2977 <https://github.com/Security-Onion-Solutions/securityonion/issues/2977>`_
- FIX: Ensure fixed PCAP files are readable by Suricata during so-import-pcap execution `#4636 <https://github.com/Security-Onion-Solutions/securityonion/issues/4636>`_
- FIX: Fail curl requests if the remote server responds with a failing status code `#4266 <https://github.com/Security-Onion-Solutions/securityonion/issues/4266>`_
- FIX: Implement error handling for soup `#3220 <https://github.com/Security-Onion-Solutions/securityonion/issues/3220>`_
- FIX: Improve PCAP job lookup performance by providing a tighter time range `#4320 <https://github.com/Security-Onion-Solutions/securityonion/issues/4320>`_
- FIX: Improve administrative username password prompt to prevent backspacing into text (ISO) `#3099 <https://github.com/Security-Onion-Solutions/securityonion/issues/3099>`_
- FIX: Improve soup for older installs `#4617 <https://github.com/Security-Onion-Solutions/securityonion/issues/4617>`_
- FIX: Include secure HTTP headers in nginx responses `#4267 <https://github.com/Security-Onion-Solutions/securityonion/issues/4267>`_
- FIX: Increase default search and proxy timeouts to 5 minutes `#4321 <https://github.com/Security-Onion-Solutions/securityonion/issues/4321>`_
- FIX: OS passwords including special characters like $ and ! `#4249 <https://github.com/Security-Onion-Solutions/securityonion/issues/4249>`_
- FIX: Prevent highstate failure during soup `#3559 <https://github.com/Security-Onion-Solutions/securityonion/issues/3559>`_
- FIX: Prevent so-thehive-cortex from continuing to build if an issue is encountered installing Python packages `#4032 <https://github.com/Security-Onion-Solutions/securityonion/issues/4032>`_
- FIX: Setup should not prompt for node description when running import or eval `#4004 <https://github.com/Security-Onion-Solutions/securityonion/issues/4004>`_
- FIX: Trying to delete old pcap job results in error `#4528 <https://github.com/Security-Onion-Solutions/securityonion/issues/4528>`_
- FIX: Websocket session cleanup overly aggressive `#4598 <https://github.com/Security-Onion-Solutions/securityonion/issues/4598>`_
- FIX: so-user should support spaces in passwords for Fleet and TheHive users `#4460 <https://github.com/Security-Onion-Solutions/securityonion/issues/4460>`_
- FIX: zeek leaving post-terminate crash logs on every shutdown `#4461 <https://github.com/Security-Onion-Solutions/securityonion/issues/4461>`_
- UPGRADE: Elastic to 7.13 `#4313 <https://github.com/Security-Onion-Solutions/securityonion/issues/4313>`_
- UPGRADE: Kratos to 0.6.3-alpha.1 `#4282 <https://github.com/Security-Onion-Solutions/securityonion/issues/4282>`_
- UPGRADE: Redmine 4.2 (For Playbook) `#4159 <https://github.com/Security-Onion-Solutions/securityonion/issues/4159>`_
- UPGRADE: Suricata 6.0.3 `#4661 <https://github.com/Security-Onion-Solutions/securityonion/issues/4661>`_

2.3.52 Changes
----------------

- FIX: packetloss.sh can cause Zeek to segfault `#4398 <https://github.com/Security-Onion-Solutions/securityonion/issues/4398>`_
- FIX: soup now generates repo tarball with correct folder structure `#4368 <https://github.com/Security-Onion-Solutions/securityonion/issues/4368>`_
- UPGRADE: Zeek 4.0.2 `#4395 <https://github.com/Security-Onion-Solutions/securityonion/issues/4395>`_

2.3.51 Changes
----------------

- FIX: Mixed case sensor hostnames lead to incomplete PCAP jobs `#4220 <https://github.com/Security-Onion-Solutions/securityonion/issues/4220>`_
- FIX: Reconcile InfluxDB/Grafana containers in certain setup modes `#4207 <https://github.com/Security-Onion-Solutions/securityonion/issues/4207>`_
- FIX: Turn down log level for Salt States and Zeek `#4231 <https://github.com/Security-Onion-Solutions/securityonion/issues/4231>`_
- FIX: Correct downloaded PCAP filename `#4234 <https://github.com/Security-Onion-Solutions/securityonion/issues/4234>`_
- FIX: Truncate /root/wait_for_web_response.log before each wait invocation `#4247 <https://github.com/Security-Onion-Solutions/securityonion/issues/4247>`_

2.3.50 Changes
----------------

- FEATURE: Add EPS Stats for Filebeat `#3872 <https://github.com/Security-Onion-Solutions/securityonion/issues/3872>`_
- FEATURE: Add copy-to-clipboard quick action menu option for copying a single field and value as 'field:value' `#3937 <https://github.com/Security-Onion-Solutions/securityonion/issues/3937>`_
- FEATURE: Add raid and so-status monitoring to SOC grid page `#3584 <https://github.com/Security-Onion-Solutions/securityonion/issues/3584>`_
- FEATURE: Add so-status to telegraf script executions and return a value `#3582 <https://github.com/Security-Onion-Solutions/securityonion/issues/3582>`_
- FEATURE: Add zeekctl wrapper script `#3441 <https://github.com/Security-Onion-Solutions/securityonion/issues/3441>`_
- FEATURE: Allow users to set an optional description for the node during setup `#2404 <https://github.com/Security-Onion-Solutions/securityonion/issues/2404>`_
- FEATURE: Initial implementation of enhanced websocket management `#3691 <https://github.com/Security-Onion-Solutions/securityonion/issues/3691>`_
- FEATURE: Combine proxy + package update questions into one menu `#3807 <https://github.com/Security-Onion-Solutions/securityonion/issues/3807>`_
- FEATURE: Configure NTP in Setup `#3053 <https://github.com/Security-Onion-Solutions/securityonion/issues/3053>`_
- FEATURE: Logstash pipeline stats wrapper `#3531 <https://github.com/Security-Onion-Solutions/securityonion/issues/3531>`_
- FEATURE: Need a way to have Hunt/Alerts perform groupbys that can optionally include event's that don't have a match for a group `#2347 <https://github.com/Security-Onion-Solutions/securityonion/issues/2347>`_
- FEATURE: Osquery WEL - Differentiate between Event & Ingest Timestamp `#3858 <https://github.com/Security-Onion-Solutions/securityonion/issues/3858>`_
- FEATURE: Provide customizable Login page banner content using markdown format `#3659 <https://github.com/Security-Onion-Solutions/securityonion/issues/3659>`_
- FEATURE: Provide customizable Overview tab content using markdown format `#3601 <https://github.com/Security-Onion-Solutions/securityonion/issues/3601>`_
- FEATURE: Redirect expired login form back to login page instead of showing error `#3690 <https://github.com/Security-Onion-Solutions/securityonion/issues/3690>`_
- FEATURE: Redirect to login when session expires `#3222 <https://github.com/Security-Onion-Solutions/securityonion/issues/3222>`_
- FEATURE: Show final selected options menu at the end of install `#3197 <https://github.com/Security-Onion-Solutions/securityonion/issues/3197>`_
- FEATURE: Show node and overall grid EPS on Grid Page `#3823 <https://github.com/Security-Onion-Solutions/securityonion/issues/3823>`_
- FEATURE: Telegraf should check for additional metrics if it is running on an appliance `#2716 <https://github.com/Security-Onion-Solutions/securityonion/issues/2716>`_
- FEATURE: VIM YAML Syntax Highlighting `#3966 <https://github.com/Security-Onion-Solutions/securityonion/issues/3966>`_
- FEATURE: allow for salt-minion start to be delayed on system start `#3543 <https://github.com/Security-Onion-Solutions/securityonion/issues/3543>`_
- FEATURE: check manager services (salt-master, so-status) during setup on a node `#1978 <https://github.com/Security-Onion-Solutions/securityonion/issues/1978>`_
- FEATURE: soup should check for OS updates `#3489 <https://github.com/Security-Onion-Solutions/securityonion/issues/3489>`_
- FIX: Alerts Total Found value should update when acknowledging or escalating `#2494 <https://github.com/Security-Onion-Solutions/securityonion/issues/2494>`_
- FIX: Alerts severity sort order `#1741 <https://github.com/Security-Onion-Solutions/securityonion/issues/1741>`_
- FIX: Change bro packet loss to be once per 2 minutes vs 30s `#3583 <https://github.com/Security-Onion-Solutions/securityonion/issues/3583>`_
- FIX: Check Zeek index close and delete settings for existing deployments `#3575 <https://github.com/Security-Onion-Solutions/securityonion/issues/3575>`_
- FIX: Firewall rules added via pillar only applies last hostgroup of the defined chain `#3709 <https://github.com/Security-Onion-Solutions/securityonion/issues/3709>`_
- FIX: Hunt not properly escaping special characters in Windows sysmon logs. `#3648 <https://github.com/Security-Onion-Solutions/securityonion/issues/3648>`_
- FIX: Hunt query for HTTP EXE downloads should work for both Zeek and Suricata `#3753 <https://github.com/Security-Onion-Solutions/securityonion/issues/3753>`_
- FIX: Incorrect retry syntax in CA and SSL states `#3948 <https://github.com/Security-Onion-Solutions/securityonion/issues/3948>`_
- FIX: Playbook Alert/Hunt showing incorrect timestamp `#2071 <https://github.com/Security-Onion-Solutions/securityonion/issues/2071>`_
- FIX: Properly handle unauthorized responses during API requests from SOC app `#2908 <https://github.com/Security-Onion-Solutions/securityonion/issues/2908>`_
- FIX: Reformat date/time on Grid and PCAP pages to enable sorting `#2686 <https://github.com/Security-Onion-Solutions/securityonion/issues/2686>`_
- FIX: Rename Fleet link in SOC to FleetDM `#3569 <https://github.com/Security-Onion-Solutions/securityonion/issues/3569>`_
- FIX: Suricata compress script should send it's output to /dev/null `#3917 <https://github.com/Security-Onion-Solutions/securityonion/issues/3917>`_
- FIX: Suricata cpu-affinity not being set if suriprocs is defined in minion pillar file. `#3926 <https://github.com/Security-Onion-Solutions/securityonion/issues/3926>`_
- FIX: TheHive Case Creation from Kibana Failure `#3870 <https://github.com/Security-Onion-Solutions/securityonion/issues/3870>`_
- FIX: WEL Shipping via Wazuh broken `#3857 <https://github.com/Security-Onion-Solutions/securityonion/issues/3857>`_
- FIX: Zeek Intel not working `#3850 <https://github.com/Security-Onion-Solutions/securityonion/issues/3850>`_
- FIX: ingest.timestamp should be date type `#3629 <https://github.com/Security-Onion-Solutions/securityonion/issues/3629>`_
- FIX: nmcli error during setup on Ubuntu + AMI `#3598 <https://github.com/Security-Onion-Solutions/securityonion/issues/3598>`_
- FIX: salt upgrade failure with versionlock `#3501 <https://github.com/Security-Onion-Solutions/securityonion/issues/3501>`_
- FIX: setup tries to connect to url used for proxy test even if the user chooses not to set one up `#3784 <https://github.com/Security-Onion-Solutions/securityonion/issues/3784>`_
- FIX: so-playbook-sync should only have one instance running `#3568 <https://github.com/Security-Onion-Solutions/securityonion/issues/3568>`_
- FIX: so-ssh-harden needs improvement `#3600 <https://github.com/Security-Onion-Solutions/securityonion/issues/3600>`_
- FIX: soup does not update /etc/soversion on distributed nodes `#3602 <https://github.com/Security-Onion-Solutions/securityonion/issues/3602>`_
- UPGRADE: Elastalert to 0.2.4-alt3 `#3947 <https://github.com/Security-Onion-Solutions/securityonion/issues/3947>`_
- UPGRADE: Salt 3003 `#3854 <https://github.com/Security-Onion-Solutions/securityonion/issues/3854>`_
- UPGRADE: Upgrade Grafana to 7.5.4 `#3916 <https://github.com/Security-Onion-Solutions/securityonion/issues/3916>`_
- UPGRADE: Upgrade external dependencies used by SOC `#3545 <https://github.com/Security-Onion-Solutions/securityonion/issues/3545>`_

2.3.50 Known Issues
-------------------

- If you had previously enabled Elastic Features and then upgrade to Security Onion 2.3.50 or higher, you may notice some features missing in Kibana. You can enable or disable features as necessary by clicking the main menu in the upper left corner, then click “Stack Management”, then click “Spaces”, then click “Default”. For more information, please see https://www.elastic.co/guide/en/kibana/master/xpack-spaces.html#spaces-control-feature-visibility.
- If you have node names in mixed case (rather than all lower case), the Grid page may show the nodes as being in the ``Fault`` state. This is a cosmetic issue and has been resolved with a hotfix: https://blog.securityonion.net/2021/05/security-onion-2350-hotfix-available.html

2.3.40 Changes
--------------

- FEATURE: Add option for HTTP Method Specification/POST to Hunt/Alerts Actions `#2904 <https://github.com/Security-Onion-Solutions/securityonion/issues/2904>`_
- FEATURE: Add option to configure proxy for various tools used during setup + persist the proxy configuration `#529 <https://github.com/Security-Onion-Solutions/securityonion/issues/529>`_
- FEATURE: Alerts/Hunt - Provide method for base64-encoding pivot value `#1749 <https://github.com/Security-Onion-Solutions/securityonion/issues/1749>`_
- FEATURE: Allow users to customize links in SOC `#1248 <https://github.com/Security-Onion-Solutions/securityonion/issues/1248>`_
- FEATURE: Display user who requested PCAP in SOC `#2775 <https://github.com/Security-Onion-Solutions/securityonion/issues/2775>`_
- FEATURE: Make SOC browser app connection timeouts adjustable `#2408 <https://github.com/Security-Onion-Solutions/securityonion/issues/2408>`_
- FEATURE: Move to FleetDM `#3483 <https://github.com/Security-Onion-Solutions/securityonion/issues/3483>`_
- FEATURE: Reduce field cache expiration from 1d to 5m, and expose value as a salt pillar `#3537 <https://github.com/Security-Onion-Solutions/securityonion/issues/3537>`_
- FEATURE: Refactor docker_clean salt state to use loop w/ inspection instead of hardcoded image list `#3113 <https://github.com/Security-Onion-Solutions/securityonion/issues/3113>`_
- FEATURE: Run so-ssh-harden during setup `#1932 <https://github.com/Security-Onion-Solutions/securityonion/issues/1932>`_
- FEATURE: SOC should only display links to tools that are enabled `#1643 <https://github.com/Security-Onion-Solutions/securityonion/issues/1643>`_
- FEATURE: Update Sigmac Osquery Field Mappings `#3137 <https://github.com/Security-Onion-Solutions/securityonion/issues/3137>`_
- FEATURE: User must accept the Elastic licence during setup `#3233 <https://github.com/Security-Onion-Solutions/securityonion/issues/3233>`_
- FEATURE: soup should output more guidance for distributed deployments at the end `#3340 <https://github.com/Security-Onion-Solutions/securityonion/issues/3340>`_
- FEATURE: soup should provide some initial information and then prompt the user to continue `#3486 <https://github.com/Security-Onion-Solutions/securityonion/issues/3486>`_
- FIX: Add cronjob for so-suricata-eve-clean script `#3515 <https://github.com/Security-Onion-Solutions/securityonion/issues/3515>`_
- FIX: Change Elasticsearch heap formula `#1686 <https://github.com/Security-Onion-Solutions/securityonion/issues/1686>`_
- FIX: Create a post install version loop in soup `#3102 <https://github.com/Security-Onion-Solutions/securityonion/issues/3102>`_
- FIX: Custom Kibana settings are not being applied properly on upgrades `#3254 <https://github.com/Security-Onion-Solutions/securityonion/issues/3254>`_
- FIX: Hunt query issues with quotes `#3320 <https://github.com/Security-Onion-Solutions/securityonion/issues/3320>`_
- FIX: IP Addresses don't work with .security `#3327 <https://github.com/Security-Onion-Solutions/securityonion/issues/3327>`_
- FIX: Improve DHCP leases query in Hunt `#3395 <https://github.com/Security-Onion-Solutions/securityonion/issues/3395>`_
- FIX: Improve Setup verbiage `#3422 <https://github.com/Security-Onion-Solutions/securityonion/issues/3422>`_
- FIX: Improve Suricata DHCP logging and parsing `#3397 <https://github.com/Security-Onion-Solutions/securityonion/issues/3397>`_
- FIX: Keep RELATED,ESTABLISHED rules at the top of iptables chains `#3288 <https://github.com/Security-Onion-Solutions/securityonion/issues/3288>`_
- FIX: Populate http.status_message field `#3408 <https://github.com/Security-Onion-Solutions/securityonion/issues/3408>`_
- FIX: Remove "types removal" deprecation messages from elastic log. `#3345 <https://github.com/Security-Onion-Solutions/securityonion/issues/3345>`_
- FIX: Reword + fix formatting on ES data storage prompt `#3205 <https://github.com/Security-Onion-Solutions/securityonion/issues/3205>`_
- FIX: SMTP shoud read SNMP on Kibana SNMP view `#3413 <https://github.com/Security-Onion-Solutions/securityonion/issues/3413>`_
- FIX: Sensors can temporarily show offline while processing large PCAP jobs `#3279 <https://github.com/Security-Onion-Solutions/securityonion/issues/3279>`_
- FIX: Soup should log to the screen as well as to a file `#3467 <https://github.com/Security-Onion-Solutions/securityonion/issues/3467>`_
- FIX: Strelka port 57314 not immediately relinquished upon restart `#3457 <https://github.com/Security-Onion-Solutions/securityonion/issues/3457>`_
- FIX: Switch SOC to pull from fieldcaps API due to field caching changes in Kibana 7.11 `#3502 <https://github.com/Security-Onion-Solutions/securityonion/issues/3502>`_
- FIX: Syntax error in /etc/sysctl.d/99-reserved-ports.conf `#3308 <https://github.com/Security-Onion-Solutions/securityonion/issues/3308>`_
- FIX: Telegraf hardcoded to use https and is not aware of elasticsearch features `#2061 <https://github.com/Security-Onion-Solutions/securityonion/issues/2061>`_
- FIX: Zeek Index Close and Delete Count for curator `#3274 <https://github.com/Security-Onion-Solutions/securityonion/issues/3274>`_
- FIX: so-cortex-user-add and so-cortex-user-enable use wrong pillar value for api key `#3388 <https://github.com/Security-Onion-Solutions/securityonion/issues/3388>`_
- FIX: so-rule does not completely apply change `#3289 <https://github.com/Security-Onion-Solutions/securityonion/issues/3289>`_
- FIX: soup should recheck disk space after it tries to clean up. `#3235 <https://github.com/Security-Onion-Solutions/securityonion/issues/3235>`_
- UPGRADE: Elastic 7.11.2 `#3389 <https://github.com/Security-Onion-Solutions/securityonion/issues/3389>`_
- UPGRADE: Suricata 6.0.2 `#3217 <https://github.com/Security-Onion-Solutions/securityonion/issues/3217>`_
- UPGRADE: Zeek 4 `#3216 <https://github.com/Security-Onion-Solutions/securityonion/issues/3216>`_
- UPGRADE: Zeek container to use Python 3 `#1113 <https://github.com/Security-Onion-Solutions/securityonion/issues/1113>`_
- UPGRADE: docker-ce to latest `#3493 <https://github.com/Security-Onion-Solutions/securityonion/issues/3493>`_

2.3.40 Known Issues
-------------------

- There was a typo in the Zeek index close and delete settings. We've fixed this for new installs in https://github.com/Security-Onion-Solutions/securityonion/issues/3274. If your deployment has more than 45 days of open Zeek indices, you may want to review these settings in ``/opt/so/saltstack/local/pillar/global.sls`` and modify them as necessary. This is being tracked in https://github.com/Security-Onion-Solutions/securityonion/issues/3575.
- If you had previously enabled Elastic Features and then upgrade to Security Onion 2.3.40 or higher, you may notice some features missing in Kibana. You can enable or disable features as necessary by clicking the main menu in the upper left corner, then click “Stack Management”, then click “Spaces”, then click “Default”. For more information, please see https://www.elastic.co/guide/en/kibana/master/xpack-spaces.html#spaces-control-feature-visibility.
- If you upgrade to 2.3.40 and then :ref:`kibana` says ``Kibana server is not ready yet`` even after waiting a few minutes for it to fully initialize, then take a look at the Diagnostic Logging section of the :ref:`kibana` section.

2.3.30 Changes
-------------

- Zeek is now at version 3.0.13.
- CyberChef is now at version 9.27.2. 
- Elastic components are now at version 7.10.2. This is the last version that uses the Apache license.
- Suricata is now at version 6.0.1.
- Salt is now at version 3002.5.
- Suricata metadata parsing is now vastly improved.
- If you choose Suricata for metadata parsing, it will now extract files from the network and send them to Strelka. You can add additional mime types here: https://github.com/Security-Onion-Solutions/securityonion/blob/dev/salt/idstools/sorules/extraction.rules
- It is now possible to filter Suricata events from being written to the logs. This is a new Suricata 6 feature. We have included some examples here: https://github.com/Security-Onion-Solutions/securityonion/blob/dev/salt/idstools/sorules/filters.rules
- The Kratos docker container will now perform DNS lookups locally before reaching out to the network DNS provider.
- Network configuration is now more compatible with manually configured OpenVPN or Wireguard VPN interfaces. 
- so-sensor-clean will no longer spawn multiple instances.
- Suricata eve.json logs will now be cleaned up after 7 days. This can be changed via the pillar setting.
- Fixed a security issue where the backup directory had improper file permissions. 
- The automated backup script on the manager now backs up all keys along with the salt configurations. Backup retention is now set to 7 days.
- Strelka logs are now being rotated properly. 
- Elastalert can now be customized via a pillar. 
- Introduced new script ``so-monitor-add`` that allows the user to easily add interfaces to the bond for monitoring.
- Setup now validates all user input fields to give up-front feedback if an entered value is invalid.
- There have been several changes to improve install reliability. Many install steps have had their validation processes reworked to ensure that required tasks have been completed before moving on to the next step of the install.
- Users are now warned if they try to set "securityonion" as their hostname. 
- The ISO should now identify xvda and nvme devices as install targets.
- At the end of the first stage of the ISO setup, the ISO device should properly unmount and eject.
- The text selection of choosing Suricata vs Zeek for metadata is now more descriptive.
- The logic for properly setting the LOG_SIZE_LIMIT variable has been improved.
- When installing on Ubuntu, Setup will now wait for cloud init to complete before trying to start the install of packages.
- The firewall state runs considerably faster now. 
- ICMP timestamps are now disabled.
- Copyright dates on all Security Onion specific files have been updated.
- `so-tcpreplay` (and indirectly `so-test`) should now work properly.
- The Zeek packet loss script is now more accurate.
- Grafana now includes an estimated EPS graph for events ingested on the manager.
- Updated Elastalert to release `0.2.4-alt2` based on the https://github.com/jertel/elastalert alt branch.
- Pivots from Alerts/Hunts to action links will properly URI encode values.
- Hunt timeline graph will properly scale the data point interval based on the search date range.
- Grid interface will properly show "Search" as the node type instead of "so-node".
- Import node now supports airgap environments.
- The so-mysql container will now show "healthy" when viewing the `docker ps` output.
- The Soctopus configuration now uses private IPs instead of public IPs, allowing network communications to succeed within the grid.
- The Correlate action in Hunt now groups the OR filters together to ensure subsequent user-added filters are correctly ANDed to the entire OR group.
- Add support to `so-firewall` script to display existing port groups and host groups.
- Hive init during Setup will now properly check for a running ES instance and will retry connectivity checks to TheHive before proceeding.
- Changes to the .security analyzer yields more accurate query results when using Playbook.
- Several Hunt queries have been updated.
- The pfSense firewall log parser has been updated to improve compatibility.
- Kibana dashboard hyperlinks have been updated for faster navigation.
- Added a new ``so-rule`` script to make it easier to disable, enable, and modify SIDs.
- ISO now gives the option to just configure the network during setup.

2.3.30 Known Issues
-------------------

- Heavy Nodes are currently not compatible with Elastic true clustering: https://github.com/Security-Onion-Solutions/securityonion/issues/3226
- Custom Kibana settings are not being applied properly on upgrades: https://github.com/Security-Onion-Solutions/securityonion/issues/3254

2.3.21 Changes
-------------

- soup has been refactored. You will need to run it a few times to get all the changes properly. We are working on making this even easier for future releases.
- soup now has awareness of Elastic Features and now downloads the appropriate Docker containers.
- The Sensors interface has been renamed to Grid. This interface now includes all Security Onion nodes.
- Grid interface now includes the status of the node. The status currently shows either Online (blue) or Offline (orange). If a node does not check-in on time then it will be marked as Offline.
- Grid interface now includes the IP and Role of each node in the grid. 
- Grid interface includes a new Filter search input to filter the visible list of grid nodes to a desired subset. As an example, typing in "sensor" will hide all nodes except those that behave as a sensor.
- The Grid description field can now be customized via the local minion pillar file for each node.
- SOC will now draw attention to an unhealthy situation within the grid or with the connection between the user's browser and the manager node. For example, when the Grid has at least one Offline node the SOC interface will show an exclamation mark in front of the browser tab's title and an exclamation mark next to the Grid menu option in SOC. Additionally, the favicon will show an orange marker in the top-right corner (dynamic favicons not supported in Safari). Additionally, if the user's web browser is unable to communicate with the manager the unhealth indicators appear along with a message at the top of SOC that states there is a connection problem.
- Docker has been upgraded to the latest version.
- Docker should be more reliable now as Salt is now managing daemon.json.
- You can now install Elastic in a traditional cluster. When setting up the manager select Advanced and follow the prompts. Replicas are controlled in global.sls.
- You can now use Hot and Warm routing with Elastic in a traditional cluster. You can change the box.type in the minion's sls file. You will need to create a curator job to re-tag the indexes based on your criteria.
- Telegraf has been updated to version 1.16.3.
- Grafana has been updated to 7.3.4 to resolve some XSS vulnerabilities.
- Grafana graphs have been changed to graphs vs guages so alerting can be set up. 
- Grafana is now completely pillarized, allowing users to customize alerts and making it customizable for email, Slack, etc. See the docs here: https://securityonion.net/docs/grafana
- Yara rules now should properly install on non-airgap installs. Previously, users had to wait for an automated job to place them in the correct location.
- Strelka backend will not stop itself any more. Previously, its behavior was to shut itself down after fifteen minutes and wait for Salt to restart it to look for work before shutting down again.
- Strelka daily rule updates are now logged to `/nsm/strelka/log/yara-update.log`
- Several changes to the setup script to improve install reliability.
- Airgap now supports the import node type.
- Custom Zeek file extraction values in the pillar now work properly.
- TheHive has been updated to support Elastic 7.
- Cortex image now includes whois package to correct an issue with the CERTatPassiveDNS analyzer.
- Hunt and Alert quick action menu has been refactored into submenus.
- New clipboard quick actions now allow for copying fields or entire events to the clipboard.
- PCAP Add Job form now retains previous job details for quickly adding additional jobs. A new Clear button now exists at the bottom of this form to clear out these fields and forget the previous job details.
- PCAP Add Job form now allows users to perform arbitrary PCAP lookups of imported PCAP data (data imported via the `so-import-pcap` script).
- Downloads page now allows direct download of Wazuh agents for Linux, Mac, and Windows from the manager, and shows the version of Wazuh and Elastic installed with Security Onion.
- PCAP job interface now shows additional job filter criteria when expanding the job filter details.
- Upgraded authentication backend to Kratos 0.5.5.
- SOC tables with the "Rows per Page" dropdown no longer show truncated page counts.
- Several Hunt errors are now more descriptive, particularly those around malformed queries.
- SOC Error banner has been improved to avoid showing raw HTML syntax, making connection and server-side errors more readable.
- Hunt and Alerts interfaces will now allow pivoting to PCAP from a group of results if the grouped results contain a network.community_id field.
- New "Correlate" quick action will pivot to a new Hunt search for all events that can be correlated by at least one of various event IDs.
- Fixed bug that caused some Hunt queries to not group correctly without a .keyword suffix. This has been corrected so that the .keyword suffix is no longer necessary on those groupby terms.
- Fixed issue where PCAP interface loses formatting and color coding when opening multiple PCAP tabs.
- Alerts interface now has a Refresh button that allows users to refresh the current alerts view without refreshing the entire SOC application.
- Hunt and Alerts interfaces now have an auto-refresh dropdown that will automatically refresh the current view at the selected frequency.
- The `so-elastalert-test` script has been refactored to work with Security Onion 2.3.
- The included Logstash image now includes Kafka plugins.
- Wazuh agent registration process has been improved to support slower hardware and networks.
- An Elasticsearch ingest pipeline has been added for suricata.ftp_data.
- Elasticsearch's indices.query.bool.max_clause_count value has been increased to accommodate a slightly larger number of fields (1024 -> 1500) when querying using a wildcard.
- On nodes being added to an existing grid, setup will compare the version currently being installed to the manager (>=2.3.20), pull the correct Security Onion version from the manager if there is a mismatch, and run that version.
- Setup will gather any errors found during a failed install into /root/errors.log for easy copy/paste and debugging.
- Selecting Suricata as the metadata engine no longer results in the install failing.
- so-rule-update now accepts arguments to idstools.  For example, ``so-rule-update -f`` will force idstools to pull rules, ignoring the default 15-minute pull limit. 



2.3.10 Changes
-------------

- UEFI installs with multiple disks should work as intended now.
- Telegraf scripts will now make sure they are not already running before execution.
- You are now prompted during setup if you want to change the docker IP range. If you change this it needs to be the same on all nodes in the grid.
- Soup will now download the new containers before stopping anything. If anything fails it will now exit and leave the grid at the current version.
- All containers are now hosted on quay.io to prevent pull limitations. We are now using GPG keys to determine if the image is from Security Onion.
- Osquery installers have been updated to osquery 4.5.1
- Fix for bug where Playbook was not removing the Elastalert rules for inactive Plays
- Exifdata reported by Strelka is now constrained to a single multi-valued field to prevent mapping explosion (scan.exiftool). 
- Resolved issue with Navigator layer(s) not loading correctly.
- Wazuh authd is now started by default on port 1515/tcp.
- Wazuh API default credentials are now removed after setup.  Scripts have been added for API user management.
- Upgraded Salt to 3002.2 due to CVEs.
- If salt-minion is unable to apply states after the defined threshold, we assume salt-minion is in a bad state and the salt-minion service will be restarted.
- Fixed bug that prevented mysql from installing for Fleet if Playbook wasn't also installed.
- so-status will now show ``STARTING`` or ``WAIT_START``, instead of ``ERROR`` if so-status is run before a salt highstate has started or finished for the first time after system startup
- Stenographer can now be disabled on a sensor node by setting the pillar ``steno:enabled:false`` in its ``minion.sls`` file or globally if set in the ``global.sls`` file
- Added ``so-ssh-harden`` script that runs the commands listed in :ref:`ssh`.
- NGINX now redirects the browser to the hostname/IP address/FQDN based on ``global:url_base``
- MySQL state now waits for MySQL server to respond to a query before completing
- Added Analyst option to network installs
- Acknowledging (and Escalating) alerts did not consistently remove the alert from the visible list; this has been corrected.
- Escalating alerts that have a ``rule.case_template`` field defined will automatically assign that case template to the case generated in TheHive.
- Alerts and Hunt interface quick action bar has been converted into a vertical menu to improve quick action option clarity. Related changes also eliminated the issues that occurred when the quick action bar was appearing to the left of the visible browser area.
- Updated Go to newer version to fix a timezone, daylight savings time (DST) issue that resulted in Alerts and Hunt interfaces not consistently showing results.
- Improved Hunt and Alert table sorting.
- Alerts interface now allows absolute time searches.
- Alerts interface 'Hunt' quick action is now working as intended.
- Alerts interface 'Ack' icon tooltip has been changed from 'Dismiss' to 'Acknowledge' for consistency.
- Hunt interface bar charts will now show the quick action menu when clicked instead of assuming the click was intended to add an include filter.
- Hunt interface quick action will now cast a wider net on field searches.
- Now explicitly preventing the use of a dollar sign ($) character in web user passwords during setup.
- Cortex container will now restart properly if the SO host was not gracefully shutdown.
- Added syslog plugin to the logstash container; this is not in-use by default but available for those users that choose to use it.
- Winlogbeat download package is now available from the SOC Downloads interface.
- Upgraded Kratos authentication system.
- Added new Reset Defaults button to the SOC Profile Settings interface which allows users to reset all local browser SOC customizations back to their defaults. This includes things like default sort column, sort order, items per page, etc.

2.3.10 Known Issues
-------------------

- For Ubuntu, non master nodes, you may need to ssh to each node and run ``salt-call state.highstate`` in order initiate the update. To verify if this needs to be done on remote nodes, from the master, run ``salt \* pkg.version salt-minion`` after 30 minutes following the initial soup update. If the node does not return that is it running Salt 3002.2, then the node will need to manually be highstated locally from the node to complete the update.

- During soup, you may see the following during the first highstate run, it can be ignored: ``Rendering SLS '<some_sls_here>' failed: Jinja variable 'list object' has no attribute 'values'``. The second highstate will complete without that error.

- During install or soup, there is a false positive failure condition that can occur. It is caused by ``[ERROR   ] Failed to add job <job_name> to schedule.``. This error indicates that Salt was unable to add a job to a schedule. If you see this in setup or soup log, it can be confirmed if this is false positive or not by running ``salt-call schedule.list`` on the node that saw the error. If the job isn't in the schedule list, run ``salt-call state.highstate`` and check if the job was added after it completes.
    

2.3.2 Changes
-------------

- Elastic components have been upgraded to 7.9.3.
- Fixed an issue where curator was unable to delete a closed index.
- Cheat sheet is now available for airgap installs.


2.3.1 Changes
-------------

- Fixed a SOC issue in airgap mode that was preventing people from logging in.
- Downloading Elastic features images will now download the correct images.
- Winlogbeat download no longer requires Internet access.
- Adjusted Alerts quick action bar to allow searching for a specific value while remaining in Alerts view.
- /nsm will properly display disk usage on the standalone Grafana dashboard.
- The manager node now has syslog listener enabled by default (you'll still need to allow syslog traffic through the firewall of course).
- Fixed an issue when creating host groups with so-firewall.


2.3.1 Known Issues
------------------

- It is still possible to update your grid from any release candidate to 2.3. However, if you have a true production deployment, then we recommend a fresh image and install for best results.
- In 2.3.0 we made some changes to data types in the elastic index templates. This will cause some errors in Kibana around field conflicts. You can address this in 2 ways:

  - Delete all the data on the ES nodes (preserving all of your other settings such as BPFs) by running ``sudo so-elastic-clear`` on all the search nodes.
  - Re-index the data. This is not a quick process but you can find more information at https://docs.securityonion.net/en/2.3/elasticsearch.html#re-indexing
- Please be patient as we update our documentation. We have made a concerted effort to update as much as possible but some things still may be incorrect or ommited. If you have questions or feedback, please start a discussion at https://securityonion.net/discuss.
- Once you update your grid to 2.3, any new nodes that join the grid must be 2.3 so if you try to join an older node it will fail. For best results, use the latest 2.3 ISO (or 2.3 installer from github) when joining to a 2.3 grid.
- Shipping Windows Eventlogs with Osquery will fail intermittently with utf8 errors logged in the Application log. This is scheduled to be fixed in Osquery 4.5.
- When running soup to upgrade from older versions to 2.3, there is a Salt error that may occur during the final highstate. This error is related to the patch_os_schedule and can be ignored as it should not occur again in subsequent highstates.
- When Search Nodes are upgraded from older versions to 2.3, there is a chance of a race condition where certificates are missing. This will show errors in the manager log to the remote node. To fix this run the following on the search node that is having the issue:

  - Stop elasticsearch - ``sudo so-elasticsearch-stop``
  - Run the SSL state - ``sudo salt-call state.apply ssl``
  - Restart elasticsearch - ``sudo so-elasticsearch-restart``
- If you are upgrading from RC1 you might see errors around registry:2 missing. This error does not break the actual upgrade. To fix, run the following on the manager: 

  - Stop the Docker registry - ``sudo docker stop so-dockerregistry``
  - Remove the container - ``sudo docker rm so-dockerregistry``
  - Run the registry state - ``sudo salt-call state.apply registry``
  
  
2.3.0 Changes
-------------

- We have a new :ref:`alerts` interface for reviewing alerts and acknowledging or escalating them. Escalating creates a new case in :ref:`hive`. Please note that :ref:`hive` no longer receives alerts directly. 
- Kibana no longer presents the option to create alerts from events, but instead allows creation of cases from events.
- Our Security Onion ISO now works for UEFI as well as Secure Boot.
- :ref:`airgap` deployments can now be updated using the latest ISO. Please read this documentation carefully. 
- :ref:`suricata` has been updated to version 5.0.4.
- :ref:`zeek` has been updated to version 3.0.11.
- :ref:`stenographer` has been updated to the latest version.
- :ref:`soup` will now attempt to clean up old docker images to free up space.
- :ref:`hunt` actions can be customized via ``hunt.actions.json``.
- :ref:`hunt` queries can be customized via ``hunt.queries.json``.
- :ref:`hunt` event fields can be customized via ``hunt.eventfields.json``.
- :ref:`alerts` actions can be customized via ``alerts.actions.json``.
- :ref:`alerts` queries can be customized via ``alerts.queries.json``.
- :ref:`alerts` event fields can be customized via ``alerts.eventfields.json``.
- This help documentation is now viewable offline for airgap installations.
- The script `so-user-add` will now validate the password is acceptable before attempting to create the user.
- :ref:`playbook` and :ref:`grafana` no longer use static passwords for their admin accounts.
- :ref:`analyst-vm` now comes with NetworkMiner 2.6 installed.
- :ref:`strelka` YARA matches now generate alerts that can be viewed through the Alerts interface .


2.2.0 Changes
-------------

- Setup now includes an option for airgap installations
- Playbook now works properly when installed in airgap mode
- Added so-analyst script to create an analyst workstation with GNOME desktop, Chromium browser, Wireshark, and NetworkMiner
- Upgraded Zeek to version 3.0.10 to address a recent security issue
- Upgraded Docker to latest version
- Re-worked IDSTools to make it easier to modify
- Added so-* tools to the default path so you can now tab complete
- so-status can now be run from a manager node to get the status of a remote node. Run salt <target> so.status
- Salt now prevents states from running on a node that it shouldn't so you can't, for example, accidentally apply the elasticsearch state on a forward node
- Added logic to check for Salt mine corruption and recover automatically
- Collapsed Hunt filter icons and action links into a new quick action bar that will appear when a field value is clicked; actions include:

  - Filtering the hunt query
  - Pivot to PCAP
  - Create an alert in TheHive
  - Google search for the value
  - Analyze the value on VirusTotal.com
- Fixed minor bugs in Hunt user interface relating to most-recently used queries, tooltips, and more
- ``so-user-add`` now automatically adds users to Fleet and TheHive (in addition to SOC)
- Introduced ``so-user-disable`` and ``so-user-enable`` commands which allows administrators to lock out users that are no longer permitted to use Security Onion
- Added icon to SOC Users list representing their active or locked out status
- Removed User delete action from SOC interface in favor of disabling users for audit purposes
- Prune old PCAP job data from sensors once the results are streamed back to the manager node
- Hunt filtering to a specific value will search across all fields instead of only the field that was originally clicked
- Limiting PCAP jobs to extract at most 2GB from a sensor to avoid users accidentally requesting unreasonably large PCAP via the web interface
- ``so-test`` is back - run it to easily replay PCAPs and verify that all the components are working as expected
- New Elasticsearch subfield (``.security``) based on the new community-driven analyzer from @neu5ron - https://github.com/neu5ron/es_stk
- Playbook now uses the new .security subfield for case-insensitive wildcard searches


2.1.0 Changes
-------------

- Fixed an issue where the console was timing out and making it appear that the installer was hung
- Introduced Import node type ideal for running so-import-pcap to import pcap files and view the resulting logs in Hunt or Kibana
- Moved static.sls to global.sls to align the name with the functionality
- Traffic between nodes in a distributed deployment is now fully encrypted
- Playbook

  - Elastalert now runs active Plays every 3 minutes
  - Changed default rule-update config to only import Windows rules from the Sigma Community repo
  - Lots of bug fixes & stability improvements
- Ingest Node parsing updates for Osquery and Winlogbeat - implemented single pipeline for Windows eventlogs & sysmon logs
- Upgraded Osquery to 4.4 and re-enabled auto-updates
- Upgraded to Salt 3001.1
- Upgraded Wazuh to 3.13.1
- Hunt interface now shows the timezone being used for the selected date range
- Fixed Cortex initialization so that TheHive integration and initial user set is correctly configured
- Improved management of TheHive/Cortex credentials
- SOC now allows for arbitrary, time-bounded PCAP job creation, with optional filtering by host and port

2.0.3 Changes
-------------

- Resolved an issue with large drives and the ISO install  
- Modified ISO installation to use Logical Volume Management (LVM) for disk partitioning
- Updated Elastic Stack components to version 7.8.1
- Updated Zeek to version 3.0.8

2.0.2 Changes
-------------

- | Sensoroni fails on 2.0.1 ISO EVAL installation #1089
  | https://github.com/Security-Onion-Solutions/securityonion/issues/1089
  
2.0.1 Changes
-------------

- | Security Fix: variables.txt from ISO install stays on disk for 10 days
  | https://github.com/Security-Onion-Solutions/securityonion/issues/1067
  
- | Security Fix: Remove user values from static.sls
  | https://github.com/Security-Onion-Solutions/securityonion/issues/1068
  
- | Fix distributed deployment sensor interval issue allowing PCAP
  | https://github.com/Security-Onion-Solutions/securityonion/issues/1059
  
- | Support for passwords that start with special characters
  | https://github.com/Security-Onion-Solutions/securityonion/issues/1058
  
- Minor soup updates

2.0.0 Changes
-------------

- This version requires a fresh install, but there is good news - we have brought back :ref:`soup`! From now on, you should be able to run :ref:`soup` on the manager to upgrade your environment to RC2 and beyond!
- Re-branded 2.0 to give it a fresh look
- All documentation has moved to our docs site
- soup is alive! Note: This tool only updates Security Onion components. Please use the built-in OS update process to keep the OS and other components up to date
- so-import-pcap is back! See the docs here
- Fixed issue with so-features-enable
- Users can now pivot to PCAP from Suricata alerts
- ISO install now prompts users to create an admin/sudo user instead of using a default account name
- The web email & password set during setup is now used to create the initial accounts for TheHive, Cortex, and Fleet
- Fixed issue with disk cleanup
- Changed the default permissions for /opt/so to keep non-priviledged users from accessing salt and related files
- Locked down access to certain SSL keys
- Suricata logs now compress after they roll over
- Users can now easily customize shard counts per index
- Improved Elastic ingest parsers including Windows event logs and Sysmon logs shipped with WinLogbeat and Osquery (ECS)
- Elastic nodes are now "hot" by default, making it easier to add a warm node later
- so-allow now runs at the end of an install so users can enable access right away
- Alert severities across Wazuh, Suricata and Playbook (Sigma) have been standardized and copied to event.severity:

  - 1-Low / 2-Medium / 3-High / 4-Critical
  
- Initial implementation of alerting queues:

  - Low & Medium alerts are accessible through Kibana & Hunt
  - High & Critical alerts are accessible through Kibana, Hunt and sent to TheHive for immediate analysis
  
- ATT&CK Navigator is now a statically-hosted site in the nginx container
- Playbook

  - All Sigma rules in the community repo (500+) are now imported and kept up to date
  - Initial implementation of automated testing when a Play's detection logic has been edited (i.e., Unit Testing)
  - Updated UI Theme
  - Once authenticated through SOC, users can now access Playbook with analyst permissions without login
  
- Kolide Launcher has been updated to include the ability to pass arbitrary flags - new functionality sponsored by SOS
- Fixed issue with Wazuh authd registration service port not being correctly exposed
- Added option for exposure of Elasticsearch REST API (port 9200) to so-allow for easier external querying/integration with other tools
- Added option to so-allow for external Strelka file uploads (e.g., via strelka-fileshot)
- Added default YARA rules for Strelka -- default rules are maintained by Florian Roth and pulled from https://github.com/Neo23x0/signature-base
- Added the ability to use custom Zeek scripts
- Renamed "master server" to "manager node"
- Improved unification of Zeek and Strelka file data
