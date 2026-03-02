.. _release-notes:

Release Notes
=============

.. warning::

  Security Onion 2.4.210 upgrades Salt to version 3006.19. This version of Salt has a configuration option minimum_auth_version for the Salt master. By default, this value is set to 3 and only minions on version 3006.12 or later support that version and are able to authenticate with the salt-master service. For this reason, during the soup to 2.4.210, we set the minimum_auth_version to 0. Since minions automatically update every 15 minutes, this allows older minion versions to authenticate, run a highstate, and upgrade to 3006.19.
  
  After seven days, a background process will change the minimum_auth_version from 0 to 3 and restart the salt-master service. Once this is done, any minions in the environment that have not upgraded to a version greater than 3006.12 will be unable to authenticate with the salt-master. The likely cause of this would be a minion that is offline. Additionally, if a user attempts to install a new node, using a version less than 2.4.200 (salt-minion 3006.16), the install will fail since the salt-minion will not be able to authenticate with the salt-master.
  
  If one of your nodes was unable to update by the time the minimum_auth_version was changed, then you may notice that the SOC Grid screen shows that you have a node running an older version of Security Onion that never updates. You can verify the issue by checking the following logs:

  In ``/opt/so/log/salt/minion`` on the remote node:

  ::
  
    2026-02-20 14:36:43,479 [salt.crypt       :884 ][ERROR   ][2215] Sign-in attempt failed: bad load
    2026-02-20 14:36:43,480 [salt.minion      :1155][ERROR   ][2215] Error while bringing up minion for multi-master. Is master at soman1 responding? The error message was Unable to sign_in to master: Attempt to authenticate with the salt master failed

  In ``/opt/so/log/salt/master`` on the Security Onion manager:

  ::

    2026-02-20 14:37:13,515 [salt.channel.server:147 ][WARNING ][2313166] Rejected authentication attempt using protocol version 2 (minimum required: 3)

  To force the node to update salt, you can connect to the remote node via ssh and then run the following:

  ::

    sudo dnf versionlock delete salt-* ; sudo yum clean all ; sudo sh /usr/sbin/bootstrap-salt.sh -X -r stable 3006.19
 
.. warning::

        Security Onion 2.4.200 changed the way Suricata detections are synchronized. Grids with custom Suricata rulesets will pause all Suricata detection syncing. For more information and required steps, see the :ref:`syncblock` section.

.. warning::

        Security Onion 2.4.150 included changes for the :ref:`elasticsearch` deletion process. :ref:`elasticsearch` indices are managed by both the ``so-elasticsearch-indices-delete`` utility and Index Lifecycle Management (ILM). The ``so-elasticsearch-indices-delete`` utility is primarily designed for single-node deployments like EVAL and STANDALONE configurations. Running it on a multi-node deployment with one or more search nodes has the possibility of getting into a corner case state where more data is deleted than intended. 
        
        If you have a multi-node deployment and haven't already updated to 2.4.150, then ``so-elasticsearch-indices-delete`` will be disabled when you update. You will need to ensure that ILM is configured properly to delete indices before disk usage reaches the :ref:`elasticsearch` watermark setting. Otherwise, :ref:`elasticsearch` may stop ingesting new data. For more information, please see the :ref:`elasticsearch` section.

Known Issues
~~~~~~~~~~~~

If you haven't viewed cases in a while, then escalating from Onion AI to an existing case will fail.

For all known issues, please see https://github.com/Security-Onion-Solutions/securityonion/issues.

Release History
~~~~~~~~~~~~~~~

2.4.210 [20260302] Changes
--------------------------

- FEATURE: Add graphs/charts to AI Metrics page
- FEATURE: Add support for default user roles `#15471 <https://github.com/Security-Onion-Solutions/securityonion/issues/15471>`_
- FEATURE: Allow non-airgap soup to use ISO for all large files `#15467 <https://github.com/Security-Onion-Solutions/securityonion/issues/15467>`_
- FEATURE: Gemini Adapter
- FEATURE: Model Thoughts
- FEATURE: multi-step ES upgrades smoother for airgap
- FEATURE: Onion AI model metrics
- FEATURE: OpenAI Chat Adapter
- FEATURE: OpenAI Responses Adapter
- FEATURE: Record user that acks and/or escalates events `#15373 <https://github.com/Security-Onion-Solutions/securityonion/issues/15373>`_
- FEATURE: Show context used on each request/response pair
- FEATURE: Use new suricata.capture_file to improve PCAP lookups `#15398 <https://github.com/Security-Onion-Solutions/securityonion/issues/15398>`_
- FIX: Appliance kickstart
- FIX: Change context indicator to m/k format
- FIX: Cleanup remaining idstools code `#15477 <https://github.com/Security-Onion-Solutions/securityonion/issues/15477>`_
- FIX: Collection-backed config fields don't respect forcedType
- FIX: Disable redis on heavynodes `#15422 <https://github.com/Security-Onion-Solutions/securityonion/issues/15422>`_
- FIX: Expanding alert with long unbreaking message content causes extra wide table `#15437 <https://github.com/Security-Onion-Solutions/securityonion/issues/15437>`_
- FIX: Give message field focus when user navigates to Onion AI page
- FIX: Grid node elastic agent install state
- FIX: Hide Grid/Client menu links when unavailable to non-superusers `#15446 <https://github.com/Security-Onion-Solutions/securityonion/issues/15446>`_
- FIX: If you haven't viewed cases in a while, then escalating from Onion AI to an existing case will fail
- FIX: Improve alert icon severity colors `#15450 <https://github.com/Security-Onion-Solutions/securityonion/issues/15450>`_
- FIX: Kratos field mappings include unnecessary templates `#15354 <https://github.com/Security-Onion-Solutions/securityonion/issues/15354>`_
- FIX: managed soc annotations migration
- FIX: Migrate off logs integration to filestream integration `#15364 <https://github.com/Security-Onion-Solutions/securityonion/issues/15364>`_
- FIX: MoM subgrid showing Detection status pending `#15305 <https://github.com/Security-Onion-Solutions/securityonion/issues/15305>`_
- FIX: Multiple lines of consecutive comments causes the BPF compile to error `#14908 <https://github.com/Security-Onion-Solutions/securityonion/issues/14908>`_
- FIX: Pending status should not show crosshairs `#15376 <https://github.com/Security-Onion-Solutions/securityonion/issues/15376>`_
- FIX: Rename to remaining "Forward" references to "Sensor" nodes `#15403 <https://github.com/Security-Onion-Solutions/securityonion/issues/15403>`_
- FIX: Review Kratos field parsing `#7567 <https://github.com/Security-Onion-Solutions/securityonion/issues/7567>`_
- FIX: Sensor and Heavynode Fail to install `#15441 <https://github.com/Security-Onion-Solutions/securityonion/issues/15441>`_
- FIX: SOC Config - Apply Changes to the correct node `#15395 <https://github.com/Security-Onion-Solutions/securityonion/issues/15395>`_
- FIX: SOC login form expiring without notifying user `#15346 <https://github.com/Security-Onion-Solutions/securityonion/issues/15346>`_
- FIX: so-elastic-agent-grid-upgrade upgrade heavynode agents `#15434 <https://github.com/Security-Onion-Solutions/securityonion/issues/15434>`_
- FIX: Soup fails if salt-relay.sh isn't running `#15518 <https://github.com/Security-Onion-Solutions/securityonion/issues/15518>`_
- FIX: Successful logins sometimes would show a 403 error banner `#15527 <https://github.com/Security-Onion-Solutions/securityonion/issues/15527>`_
- FIX: Telegraf logstash metrics `#15423 <https://github.com/Security-Onion-Solutions/securityonion/issues/15423>`_
- FIX: Update redis-logs integration file path `#15425 <https://github.com/Security-Onion-Solutions/securityonion/issues/15425>`_
- FIX: url_base annotation description `#15483 <https://github.com/Security-Onion-Solutions/securityonion/issues/15483>`_
- FIX: Zeek excluded_files `#15439 <https://github.com/Security-Onion-Solutions/securityonion/issues/15439>`_
- UPGRADE: Analyzer dependencies `#15512 <https://github.com/Security-Onion-Solutions/securityonion/issues/15512>`_
- UPGRADE: Docker to 29.2.1 `#15495 <https://github.com/Security-Onion-Solutions/securityonion/issues/15495>`_
- UPGRADE: Elasticsearch to 9.0.8
- UPGRADE: Go dependencies to latest versions `#15474 <https://github.com/Security-Onion-Solutions/securityonion/issues/15474>`_
- UPGRADE: ISO base image to Oracle 9.7 `#15352 <https://github.com/Security-Onion-Solutions/securityonion/issues/15352>`_
- UPGRADE: Pcapfix to 1.1.7 `#15421 <https://github.com/Security-Onion-Solutions/securityonion/issues/15421>`_
- UPGRADE: Salt to 3006.19 `#15490 <https://github.com/Security-Onion-Solutions/securityonion/issues/15490>`_
- UPGRADE: Zeek to 8.0.6 `#15445 <https://github.com/Security-Onion-Solutions/securityonion/issues/15445>`_

2.4.201 [20260114] Changes
--------------------------

- FIX: Update OnionAI video `#15380 <https://github.com/Security-Onion-Solutions/securityonion/issues/15380>`_
- FIX: Validate Suricata Overrides `#15372 <https://github.com/Security-Onion-Solutions/securityonion/issues/15372>`_
- UPGRADE: Suricata to 8.0.3 `#15377 <https://github.com/Security-Onion-Solutions/securityonion/issues/15377>`_
- UPGRADE: Zeek to 8.0.5 `#15378 <https://github.com/Security-Onion-Solutions/securityonion/issues/15378>`_

2.4.200 [20251215] Changes
--------------------------

- FEATURE: Elastic agent high performance tuning in SOC `#14965 <https://github.com/Security-Onion-Solutions/securityonion/issues/14965>`_
- FEATURE: Add QWEN 235B as a lower cost option for an OnionAI model
- FEATURE: Add info icon to the right of sync error states on detection header bar `#15256 <https://github.com/Security-Onion-Solutions/securityonion/issues/15256>`_
- FEATURE: Additional ILM config via SOC ui
- FEATURE: Make OnionAI more accurate and curious
- FEATURE: Notify user of hypervisor environment setup failures `#15245 <https://github.com/Security-Onion-Solutions/securityonion/issues/15245>`_
- FEATURE: Onion AI add tool for creating / updating / disabling / enabling detections
- FEATURE: Onion AI auto compact context support
- FEATURE: Onion AI escalate to existing case
- FEATURE: Onion AI model metrics
- FEATURE: OnionAI additional UI metrics
- FEATURE: Refactor SOC Detections NIDS for idstools removal `#15306 <https://github.com/Security-Onion-Solutions/securityonion/issues/15306>`_
- FEATURE: Remember Configuration screen Advanced toggle `#15215 <https://github.com/Security-Onion-Solutions/securityonion/issues/15215>`_
- FEATURE: Stop retrying PCAP jobs after 5 failures (configurable) `#15227 <https://github.com/Security-Onion-Solutions/securityonion/issues/15227>`_
- FEATURE: so-elasticsearch-retention-estimate `#15178 <https://github.com/Security-Onion-Solutions/securityonion/issues/15178>`_
- FIX: "Context Starts Here" line sometimes disappears depending on screen width
- FIX: Add guardrails for when users are allowed to click context compression button
- FIX: Compaction throws server error
- FIX: Creating VM with virtual disk fails with "Hypervisor NSM Disk Full" error `#15179 <https://github.com/Security-Onion-Solutions/securityonion/issues/15179>`_
- FIX: Do not prompt to continue if memory capacity is too low for certain install types `#15255 <https://github.com/Security-Onion-Solutions/securityonion/issues/15255>`_
- FIX: Docker registry may not be ready for connections when Salt pulls first container `#15058 <https://github.com/Security-Onion-Solutions/securityonion/issues/15058>`_
- FIX: Failed setup a while ago `#14945 <https://github.com/Security-Onion-Solutions/securityonion/issues/14945>`_
- FIX: Failure to download the OL9 qcow2 image can cause the setup_hypervisor runner to hang `#15246 <https://github.com/Security-Onion-Solutions/securityonion/issues/15246>`_
- FIX: Ignore control characters in minion install.txt `#15315 <https://github.com/Security-Onion-Solutions/securityonion/issues/15315>`_
- FIX: ISO swap partition on multi disk install `#15158 <https://github.com/Security-Onion-Solutions/securityonion/issues/15158>`_
- FIX: Improved chat input field
- FIX: List of users empty in SOC interface after a sort on a column `#15249 <https://github.com/Security-Onion-Solutions/securityonion/issues/15249>`_
- FIX: OIDC Link and Unlink `#15214 <https://github.com/Security-Onion-Solutions/securityonion/issues/15214>`_
- FIX: Onion AI improve error handling from API gateway
- FIX: Reduce Sensoroni pcapMaxCount default setting `#15208 <https://github.com/Security-Onion-Solutions/securityonion/issues/15208>`_
- FIX: Refactor Playbooks variable substitution
- FIX: Remove newline that appears for "&nbsp;" tool responses
- FIX: Rename Forward to Sensor `#15172 <https://github.com/Security-Onion-Solutions/securityonion/issues/15172>`_
- FIX: Reserve group IDs to prevent collisions `#15288 <https://github.com/Security-Onion-Solutions/securityonion/issues/15288>`_
- FIX: Show message when Onion AI is experiencing an outage
- FIX: Stop collecting PCAP packets if filter covers multiple stream paths `#15226 <https://github.com/Security-Onion-Solutions/securityonion/issues/15226>`_
- FIX: Tool Calls with OnionAI time out
- FIX: UI needs to be notified if context compaction fails `#15295 <https://github.com/Security-Onion-Solutions/securityonion/issues/15295>`_
- FIX: VM is created without virtual disk mounted `#15250 <https://github.com/Security-Onion-Solutions/securityonion/issues/15250>`_
- FIX: get_playbooks tool doesn't respect aggregate: true
- FIX: longer timeout for esindexsize.sh telegraf script `#15149 <https://github.com/Security-Onion-Solutions/securityonion/issues/15149>`_
- FIX: so-setup bond0 being recreated `#15233 <https://github.com/Security-Onion-Solutions/securityonion/issues/15233>`_
- UPGRADE: Salt to 3006.16 `#15173 <https://github.com/Security-Onion-Solutions/securityonion/issues/15173>`_
- UPGRADE: Strelka to 1.0.1
- UPGRADE: Suricata to 8.0.2 `#15203 <https://github.com/Security-Onion-Solutions/securityonion/issues/15203>`_
- UPGRADE: Zeek to 8.0.4 `#15060 <https://github.com/Security-Onion-Solutions/securityonion/issues/15060>`_
- UPGRADE: golang.org/x/crypto from 0.42.0 to 0.45.0 `#15258 <https://github.com/Security-Onion-Solutions/securityonion/issues/15258>`_

2.4.190 [20251024] Changes
--------------------------

- FEATURE: Add ability to force a fleet agent installer via the --force flag `#15146 <https://github.com/Security-Onion-Solutions/securityonion/issues/15146>`_
- FEATURE: Allow customization of export CSV delimiter `#15129 <https://github.com/Security-Onion-Solutions/securityonion/issues/15129>`_
- FEATURE: Allow user to map a virtual disk to /nsm when creating a VM `#15121 <https://github.com/Security-Onion-Solutions/securityonion/issues/15121>`_
- FEATURE: BYOD hypervisor and managerhype `#15102 <https://github.com/Security-Onion-Solutions/securityonion/issues/15102>`_
- FEATURE: New grain: nsm_total `#15120 <https://github.com/Security-Onion-Solutions/securityonion/issues/15120>`_
- FEATURE: Provide notice with option to sync recently modified module `#15119 <https://github.com/Security-Onion-Solutions/securityonion/issues/15119>`_
- FEATURE: Remember Auto-Refresh Interval for Hunt, Alerts, Dashboards, etc `#15077 <https://github.com/Security-Onion-Solutions/securityonion/issues/15077>`_
- FEATURE: Security Onion AI Assistant
- FEATURE: Show query name under query input `#15128 <https://github.com/Security-Onion-Solutions/securityonion/issues/15128>`_
- FIX: Action links should replace all vars `#15084 <https://github.com/Security-Onion-Solutions/securityonion/issues/15084>`_
- FIX: Add event.module to Elasticsearch logs `#15074 <https://github.com/Security-Onion-Solutions/securityonion/issues/15074>`_
- FIX: Import node fleet output policy `#15037 <https://github.com/Security-Onion-Solutions/securityonion/issues/15037>`_
- FIX: Logstash fleet output corrupt ssl config `#15101 <https://github.com/Security-Onion-Solutions/securityonion/issues/15101>`_
- FIX: PCAP Upload validation issues `#15143 <https://github.com/Security-Onion-Solutions/securityonion/issues/15143>`_
- FIX: Setup occasionally fails if the registry container takes more than a couple seconds to start. `#15073 <https://github.com/Security-Onion-Solutions/securityonion/issues/15073>`_
- FIX: Subgrid count calculation `#15078 <https://github.com/Security-Onion-Solutions/securityonion/issues/15078>`_
- FIX: so-hypervisor bridge not created during setup `#15050 <https://github.com/Security-Onion-Solutions/securityonion/issues/15050>`_
- UPGRADE: SOC Dependencies `#15059 <https://github.com/Security-Onion-Solutions/securityonion/issues/15059>`_
- UPGRADE: Attack Navigator to 5.1.1 `#15097 <https://github.com/Security-Onion-Solutions/securityonion/issues/15097>`_
- UPGRADE: Docker base images to latest respective versions `#15093 <https://github.com/Security-Onion-Solutions/securityonion/issues/15093>`_
- UPGRADE: ElastAlert 2 to 2.26.0 `#15094 <https://github.com/Security-Onion-Solutions/securityonion/issues/15094>`_
- UPGRADE: Elastic to 8.18.8 `#15117 <https://github.com/Security-Onion-Solutions/securityonion/issues/15117>`_
- UPGRADE: Golang to 1.25.1 `#15079 <https://github.com/Security-Onion-Solutions/securityonion/issues/15079>`_
- UPGRADE: Nginx to 1.29.1 `#15096 <https://github.com/Security-Onion-Solutions/securityonion/issues/15096>`_
- UPGRADE: Redis to 7.2.11 `#15116 <https://github.com/Security-Onion-Solutions/securityonion/issues/15116>`_
- UPGRADE: Telegraf to 1.36.1 `#15095 <https://github.com/Security-Onion-Solutions/securityonion/issues/15095>`_
- UPGRADE: Zeek to 7.0.11 `#15135 <https://github.com/Security-Onion-Solutions/securityonion/issues/15135>`_

2.4.180 [20250916] Changes
--------------------------

- FEATURE: Add contextual help buttons to screen toolbars `#15027 <https://github.com/Security-Onion-Solutions/securityonion/issues/15027>`_
- FEATURE: Alert on offline agent `#14898 <https://github.com/Security-Onion-Solutions/securityonion/issues/14898>`_
- FEATURE: Allow alerts, dashboards, hunt query to be canceled by the submitter
- FEATURE: Enable static hostname mapping without reverse DNS lookups `#14900 <https://github.com/Security-Onion-Solutions/securityonion/issues/14900>`_
- FEATURE: Kafka output policy
- FEATURE: Manager with hypervisor capabilities `#14997 <https://github.com/Security-Onion-Solutions/securityonion/issues/14997>`_
- FEATURE: Preparation work for upcoming features
- FEATURE: Reporting and Exporting
- FIX: Autofocus OTP field `#14984 <https://github.com/Security-Onion-Solutions/securityonion/issues/14984>`_
- FIX: Disable Elastic Telemetry by default `#14924 <https://github.com/Security-Onion-Solutions/securityonion/issues/14924>`_
- FIX: Elastalert - verify that empty file has not been written `#14822 <https://github.com/Security-Onion-Solutions/securityonion/issues/14822>`_
- FIX: Filter out salt INFO logs for ingest `#14447 <https://github.com/Security-Onion-Solutions/securityonion/issues/14447>`_
- FIX: Hypervisor firewall rules don't get applied to Managersearch or Standalone `#14923 <https://github.com/Security-Onion-Solutions/securityonion/issues/14923>`_
- FIX: Receiver custom_fqdn `#15023 <https://github.com/Security-Onion-Solutions/securityonion/issues/15023>`_
- FIX: Refactor IDH Dockerfile `#14473 <https://github.com/Security-Onion-Solutions/securityonion/issues/14473>`_
- FIX: Review additional STIGs
- FIX: Set NIC Channels combined to 1 for monitor interfaces `#14951 <https://github.com/Security-Onion-Solutions/securityonion/issues/14951>`_
- FIX: Spacing issue on certain Configuration screens `#14989 <https://github.com/Security-Onion-Solutions/securityonion/issues/14989>`_
- FIX: Subgrid PCAP downloads `#15030 <https://github.com/Security-Onion-Solutions/securityonion/issues/15030>`_
- FIX: Suricata metadata index rollover `#15021 <https://github.com/Security-Onion-Solutions/securityonion/issues/15021>`_
- FIX: Unable to remove passkey for passwordless logins `#14926 <https://github.com/Security-Onion-Solutions/securityonion/issues/14926>`_
- FIX: Zeek DNS ingest error
- UPGRADE: Analyzer dependencies
- UPGRADE: Elasticsearch 8.18.6 `#15014 <https://github.com/Security-Onion-Solutions/securityonion/issues/15014>`_
- UPGRADE: ISO base image to Oracle 9.6 `#15007 <https://github.com/Security-Onion-Solutions/securityonion/issues/15007>`_
- UPGRADE: Kafka base image
- UPGRADE: Suricata to 7.0.12 `#15038 <https://github.com/Security-Onion-Solutions/securityonion/issues/15038>`_
- UPGRADE: Zeek to 7.0.10 `#14967 <https://github.com/Security-Onion-Solutions/securityonion/issues/14967>`_

2.4.170 [20250812] Changes
--------------------------

- FEATURE: Add JA4 Support `#14864 <https://github.com/Security-Onion-Solutions/securityonion/issues/14864>`_
- FEATURE: Add SOC dashboard for CEF logs `#14837 <https://github.com/Security-Onion-Solutions/securityonion/issues/14837>`_
- FEATURE: Add SOC dashboard for iptables logs `#14836 <https://github.com/Security-Onion-Solutions/securityonion/issues/14836>`_
- FEATURE: Add SOC dashboards for UniFi logs `#14838 <https://github.com/Security-Onion-Solutions/securityonion/issues/14838>`_
- FEATURE: Allow Custom Playbook Repo Import `#14780 <https://github.com/Security-Onion-Solutions/securityonion/issues/14780>`_
- FEATURE: Elasticsearch troubleshooting helper script `#14523 <https://github.com/Security-Onion-Solutions/securityonion/issues/14523>`_
- FEATURE: Playbooks UI - AutoExpand & Styling `#14851 <https://github.com/Security-Onion-Solutions/securityonion/issues/14851>`_
- FEATURE: Zeek JA4+ parsing `#14465 <https://github.com/Security-Onion-Solutions/securityonion/issues/14465>`_
- FIX: Add reminder to API Client dialog about permissions `#14847 <https://github.com/Security-Onion-Solutions/securityonion/issues/14847>`_
- FIX: Analyst permissions for Playbooks `#14811 <https://github.com/Security-Onion-Solutions/securityonion/issues/14811>`_
- FIX: Config Backup should exclude agent installers `#14351 <https://github.com/Security-Onion-Solutions/securityonion/issues/14351>`_
- FIX: Duplicate Detections when using local git repo `#14829 <https://github.com/Security-Onion-Solutions/securityonion/issues/14829>`_
- FIX: IDH startup message not parsed correctly `#11467 <https://github.com/Security-Onion-Solutions/securityonion/issues/11467>`_
- FIX: Incorrect file ownership for idstools/idh scripts
- FIX: JS error during Playbook usage `#14802 <https://github.com/Security-Onion-Solutions/securityonion/issues/14802>`_
- FIX: Remove atop from ISO build to address CVE-2025-31160 `#14642 <https://github.com/Security-Onion-Solutions/securityonion/issues/14642>`_
- FIX: Review ISO Size
- FIX: Sorting in the Alerts Interface Causing Duplicate Data to Appear `#14786 <https://github.com/Security-Onion-Solutions/securityonion/issues/14786>`_
- FIX: Update common pipeline to rename geoip ASN data `#14884 <https://github.com/Security-Onion-Solutions/securityonion/issues/14884>`_
- UPGRADE: Elastic to 8.18.4 `#14799 <https://github.com/Security-Onion-Solutions/securityonion/issues/14799>`_
- UPGRADE: Suricata to 7.0.11 `#14817 <https://github.com/Security-Onion-Solutions/securityonion/issues/14817>`_
- UPGRADE: Ubuntu 24.10 base images switch to LTS 24.04 `#14798 <https://github.com/Security-Onion-Solutions/securityonion/issues/14798>`_
- UPGRADE: Zeek Ethercat plugin `#14783 <https://github.com/Security-Onion-Solutions/securityonion/issues/14783>`_
- UPGRADE: Zeek to 7.0.9 `#14861 <https://github.com/Security-Onion-Solutions/securityonion/issues/14861>`_

2.4.160 [20250625] Changes
--------------------------

- FEATURE: Keyboard Accessibility and Screen Reader Support `#14715 <https://github.com/Security-Onion-Solutions/securityonion/issues/14715>`_
- FEATURE: Playbooks `#14694 <https://github.com/Security-Onion-Solutions/securityonion/issues/14694>`_
- FEATURE: Splunk App
- FEATURE: so-elasticsearch-indices-growth script `#14699 <https://github.com/Security-Onion-Solutions/securityonion/issues/14699>`_
- FIX: Disallow upper case email addresses on new user form `#14655 <https://github.com/Security-Onion-Solutions/securityonion/issues/14655>`_
- FIX: Improve annotation for Elasticsearch index deletion `#14682 <https://github.com/Security-Onion-Solutions/securityonion/issues/14682>`_
- FIX: Improve subgrid error handling
- FIX: License system improvements
- FIX: Provide HSTS header on initial page redirect `#14713 <https://github.com/Security-Onion-Solutions/securityonion/issues/14713>`_
- FIX: SOC PCAP jobs page doesn't remember the Items per page setting `#14630 <https://github.com/Security-Onion-Solutions/securityonion/issues/14630>`_
- FIX: Show OIDC users message if attempting to login with same email as a local user `#14726 <https://github.com/Security-Onion-Solutions/securityonion/issues/14726>`_
- FIX: Sigma rule repos can't have same name `#14615 <https://github.com/Security-Onion-Solutions/securityonion/issues/14615>`_
- FIX: ``global@custom`` pipeline overwriting system integration timestamps `#14693 <https://github.com/Security-Onion-Solutions/securityonion/issues/14693>`_
- FIX: so-elasticsearch-ilm-start needs shebang `#14688 <https://github.com/Security-Onion-Solutions/securityonion/issues/14688>`_
- FIX: so-suricata-testrule should disable pcap logging `#14685 <https://github.com/Security-Onion-Solutions/securityonion/issues/14685>`_
- UPGRADE: Alpine base image to 3.21.3 `#14710 <https://github.com/Security-Onion-Solutions/securityonion/issues/14710>`_
- UPGRADE: Base image for so-strelka-filestream `#14678 <https://github.com/Security-Onion-Solutions/securityonion/issues/14678>`_
- UPGRADE: Base image for so-strelka-frontend `#14679 <https://github.com/Security-Onion-Solutions/securityonion/issues/14679>`_
- UPGRADE: Base image for so-strelka-manager `#14680 <https://github.com/Security-Onion-Solutions/securityonion/issues/14680>`_
- UPGRADE: Docker registry to 3.0.0 `#14702 <https://github.com/Security-Onion-Solutions/securityonion/issues/14702>`_
- UPGRADE: ElastAlert2 to 2.24.0 `#14671 <https://github.com/Security-Onion-Solutions/securityonion/issues/14671>`_
- UPGRADE: Hydra to 2.3.0 `#14692 <https://github.com/Security-Onion-Solutions/securityonion/issues/14692>`_
- UPGRADE: IDS tool base image update to 3.13.3-slim `#14707 <https://github.com/Security-Onion-Solutions/securityonion/issues/14707>`_
- UPGRADE: ISO base image to Oracle Linux 9.5 `#14681 <https://github.com/Security-Onion-Solutions/securityonion/issues/14681>`_
- UPGRADE: InfluxDB to 2.7.12 `#14670 <https://github.com/Security-Onion-Solutions/securityonion/issues/14670>`_
- UPGRADE: Nginx base image to 1.27.5 `#14709 <https://github.com/Security-Onion-Solutions/securityonion/issues/14709>`_
- UPGRADE: PCAP Tools docker base image to 3.13.3-slim `#14708 <https://github.com/Security-Onion-Solutions/securityonion/issues/14708>`_
- UPGRADE: Redis docker to 7.2.9 `#14706 <https://github.com/Security-Onion-Solutions/securityonion/issues/14706>`_
- UPGRADE: SOC related dependencies `#14672 <https://github.com/Security-Onion-Solutions/securityonion/issues/14672>`_
- UPGRADE: Telegraf to 1.34.4 `#14705 <https://github.com/Security-Onion-Solutions/securityonion/issues/14705>`_
- UPGRADE: Zeek to 7.0.8 `#14616 <https://github.com/Security-Onion-Solutions/securityonion/issues/14616>`_

2.4.150 Hotfix [20250522] Changes
---------------------------------

- FIX: Remove python docker module from so-docker-prune `#14647 <https://github.com/Security-Onion-Solutions/securityonion/issues/14647>`_

2.4.150 [20250512] Changes
--------------------------

- FEATURE: Additional grid management (MoM) `#14552 <https://github.com/Security-Onion-Solutions/securityonion/issues/14552>`_
- FEATURE: Add refresh button to more SOC screens
- FEATURE: Add setting direct hyperlink copy-to-clipboard button icon
- FEATURE: Collect ES index metrics
- FEATURE: Convert Kratos identity_id to user.name `#14598 <https://github.com/Security-Onion-Solutions/securityonion/issues/14598>`_
- FEATURE: Disable auto-upgrading non-default integrations `#14516 <https://github.com/Security-Onion-Solutions/securityonion/issues/14516>`_
- FEATURE: Enable external access to Kafka `#13754 <https://github.com/Security-Onion-Solutions/securityonion/issues/13754>`_
- FEATURE: Support wrapping UI config entries at top/bottom of list
- FIX: Add log.origin.file.line to base templates `#14417 <https://github.com/Security-Onion-Solutions/securityonion/issues/14417>`_
- FIX: Allow configuration of background actions via config UI `#14503 <https://github.com/Security-Onion-Solutions/securityonion/issues/14503>`_
- FIX: Correct joblookup route for Connect API `#14515 <https://github.com/Security-Onion-Solutions/securityonion/issues/14515>`_
- FIX: Detection Overrides should not trigger "updated" state during sync `#14361 <https://github.com/Security-Onion-Solutions/securityonion/issues/14361>`_
- FIX: Detections index refresh_interval `#14572 <https://github.com/Security-Onion-Solutions/securityonion/issues/14572>`_
- FIX: Disable import pcap button on SOC UI for heavynodes `#14430 <https://github.com/Security-Onion-Solutions/securityonion/issues/14430>`_
- FIX: Elastic Delete Cleanup Changes `#14491 <https://github.com/Security-Onion-Solutions/securityonion/issues/14491>`_
- FIX: First highstate failure after reboot `#14442 <https://github.com/Security-Onion-Solutions/securityonion/issues/14442>`_
- FIX: Influxdb not properly calculating root partition usage on STIG installations
- FIX: Issue Reboot request as async when submitted via SOC UI `#14553 <https://github.com/Security-Onion-Solutions/securityonion/issues/14553>`_
- FIX: Kafka server logs
- FIX: Logstash log rollover `#14065 <https://github.com/Security-Onion-Solutions/securityonion/issues/14065>`_
- FIX: null pointer exception in global custom pipeline `#14602 <https://github.com/Security-Onion-Solutions/securityonion/issues/14602>`_
- FIX: PCAP filter is unable to collect IPV6 ICMP `#14492 <https://github.com/Security-Onion-Solutions/securityonion/issues/14492>`_
- FIX: Remove unmaintained archiver dependency `#14597 <https://github.com/Security-Onion-Solutions/securityonion/issues/14597>`_
- FIX: SOC PCAP Rows per page setting is not remembered `#14487 <https://github.com/Security-Onion-Solutions/securityonion/issues/14487>`_
- FIX: so-import-pcap should not be installed on heavy nodes `#14431 <https://github.com/Security-Onion-Solutions/securityonion/issues/14431>`_
- FIX: Strelka backend scanner yaml config syntax error `#14406 <https://github.com/Security-Onion-Solutions/securityonion/issues/14406>`_
- FIX: Strelka containers restart when the config changes `#14498 <https://github.com/Security-Onion-Solutions/securityonion/issues/14498>`_
- FIX: Suricata Regex not working as expected `#14571 <https://github.com/Security-Onion-Solutions/securityonion/issues/14571>`_
- FIX: Configuration screen default toggle value hard to read when disabled
- FIX: Web server cert should include the url_base in alternate subject `#14573 <https://github.com/Security-Onion-Solutions/securityonion/issues/14573>`_
- FIX: x509_v2.py TypeError: list indices must be integers or slices, not str `#14452 <https://github.com/Security-Onion-Solutions/securityonion/issues/14452>`_
- UPGRADE: Analyzer dependencies `#14606 <https://github.com/Security-Onion-Solutions/securityonion/issues/14606>`_
- UPGRADE: Kafka 3.9.0 `#14485 <https://github.com/Security-Onion-Solutions/securityonion/issues/14485>`_
- UPGRADE: SOC Go external libraries

2.4.141 [20250331] Changes
--------------------------

- FIX: Clicking Absolute DateRange Drop Down Refreshes the Page `#14450 <https://github.com/Security-Onion-Solutions/securityonion/issues/14450>`_
- FIX: Config toggles fail to save if original value is raw boolean `#14449 <https://github.com/Security-Onion-Solutions/securityonion/issues/14449>`_
- FIX: Dark mode disabled toggles difficult to read `#14454 <https://github.com/Security-Onion-Solutions/securityonion/issues/14454>`_
- FIX: Improve handling of Elastic Fleet integration upgrades `#14455 <https://github.com/Security-Onion-Solutions/securityonion/issues/14455>`_

2.4.140 [20250324] Changes
--------------------------

- FEATURE: Allow moving configuration entries up or down
- FIX: Adding new user with non-analyst role will default to analyst role `#14395 <https://github.com/Security-Onion-Solutions/securityonion/issues/14395>`_
- FIX: Allow single entry for Zeek file extracts
- FIX: AQM menu option should only be visible to superusers when Pro license is applied `#14393 <https://github.com/Security-Onion-Solutions/securityonion/issues/14393>`_
- FIX: Creating a PCAP job with the new popup calendar fails to retrieve PCAP `#14387 <https://github.com/Security-Onion-Solutions/securityonion/issues/14387>`_
- FIX: Detection title under Alert Details panel overflows beyond border `#14369 <https://github.com/Security-Onion-Solutions/securityonion/issues/14369>`_
- FIX: Grid Configuration Zoom Level `#14366 <https://github.com/Security-Onion-Solutions/securityonion/issues/14366>`_
- FIX: limited-analyst and limited-auditor roles receive 403 error upon login `#14392 <https://github.com/Security-Onion-Solutions/securityonion/issues/14392>`_
- FIX: Pro license message invisible in light mode `#14382 <https://github.com/Security-Onion-Solutions/securityonion/issues/14382>`_
- FIX: Salt bootstrap `#14435 <https://github.com/Security-Onion-Solutions/securityonion/issues/14435>`_
- FIX: Unable to add more than one Suricata tuning rule without navigating away `#14374 <https://github.com/Security-Onion-Solutions/securityonion/issues/14374>`_
- FIX: Unable to extract PCAP from imported PCAPs when using Suricata for PCAP `#14426 <https://github.com/Security-Onion-Solutions/securityonion/issues/14426>`_
- FIX: Unable to import PCAP on remote sensor nodes via SOC UI `#14424 <https://github.com/Security-Onion-Solutions/securityonion/issues/14424>`_
- FIX: Unable to load YARA rules with multiline comments `#14400 <https://github.com/Security-Onion-Solutions/securityonion/issues/14400>`_
- FIX: Update global.pipeline annotation
- FIX: Zeek ldap_search missing observer.name `#14370 <https://github.com/Security-Onion-Solutions/securityonion/issues/14370>`_
- UPGRADE: SOC golang.org/x/net to 0.36.0 `#14399 <https://github.com/Security-Onion-Solutions/securityonion/issues/14399>`_
- UPGRADE: Suricata to 7.0.9 `#14401 <https://github.com/Security-Onion-Solutions/securityonion/issues/14401>`_
- UPGRADE: Zeek to 7.0.6 `#14421 <https://github.com/Security-Onion-Solutions/securityonion/issues/14421>`_

2.4.130 [20250311] Changes
--------------------------

- FEATURE: Add a pop-up calendar for the start and end time in the PCAP interface `#14115 <https://github.com/Security-Onion-Solutions/securityonion/issues/14115>`_
- FEATURE: Add notes to SOC Config about Elasticsearch ILM rollover `#14353 <https://github.com/Security-Onion-Solutions/securityonion/issues/14353>`_
- FEATURE: Add sankey chart to Elastic Agent API dashboard to show relationship between process.name and process.Ext.api.name `#14339 <https://github.com/Security-Onion-Solutions/securityonion/issues/14339>`_
- FEATURE: Additional licensing enhancements
- FEATURE: Allow query cancelation from Security Onion Console `#4161 <https://github.com/Security-Onion-Solutions/securityonion/issues/4161>`_
- FEATURE: Allow users to switch Alerts to advanced interface permanently `#14348 <https://github.com/Security-Onion-Solutions/securityonion/issues/14348>`_
- FEATURE: Enhance config UI Element capabilities
- FEATURE: Improve management of ES index templates for integrations
- FEATURE: Review ES field mapping conflicts
- FEATURE: Use new annotations to improve configuration interface `#14209 <https://github.com/Security-Onion-Solutions/securityonion/issues/14209>`_
- FEATURE: Zeek parsing
- FIX: API unauthorized vs forbidden response `#14304 <https://github.com/Security-Onion-Solutions/securityonion/issues/14304>`_
- FIX: Add TLSv1.3 to nginx config `#14252 <https://github.com/Security-Onion-Solutions/securityonion/issues/14252>`_
- FIX: Alert Overview summary overflows beyond border `#14365 <https://github.com/Security-Onion-Solutions/securityonion/issues/14365>`_
- FIX: Check for metrics indices with replicas configured causing ES to go YELLOW
- FIX: Elastic Agent Security Events dashboard should reference user.effective.name `#14325 <https://github.com/Security-Onion-Solutions/securityonion/issues/14325>`_
- FIX: No license file in repo `#14266 <https://github.com/Security-Onion-Solutions/securityonion/issues/14266>`_
- FIX: Reduce so-setup and soup console output `#14330 <https://github.com/Security-Onion-Solutions/securityonion/issues/14330>`_
- FIX: SOC Actions for process.entity_id value must be quoted `#14311 <https://github.com/Security-Onion-Solutions/securityonion/issues/14311>`_
- FIX: SOC Alerts Column Sorting `#14242 <https://github.com/Security-Onion-Solutions/securityonion/issues/14242>`_
- FIX: SOC Detections table showing incorrect numbers `#14317 <https://github.com/Security-Onion-Solutions/securityonion/issues/14317>`_
- FIX: SOC Grid Members improve REVIEW button in light mode `#14332 <https://github.com/Security-Onion-Solutions/securityonion/issues/14332>`_
- FIX: SOC Light Mode Icon Colors `#14237 <https://github.com/Security-Onion-Solutions/securityonion/issues/14237>`_
- FIX: SOC PCAP Transcript Context Menu `#14294 <https://github.com/Security-Onion-Solutions/securityonion/issues/14294>`_
- FIX: SOC PCAP column headers hidden from view `#14234 <https://github.com/Security-Onion-Solutions/securityonion/issues/14234>`_
- FIX: SOC logging 404 requests with url field that should be a string `#14293 <https://github.com/Security-Onion-Solutions/securityonion/issues/14293>`_
- FIX: Verify geoip database
- FIX: pfSense Suricata integration
- FIX: so-import-pcap not working on STIG installation
- UPGRADE: Elastic Fleet to support Elastic Defend on macOS 15.x (Sequoia) `#14010 <https://github.com/Security-Onion-Solutions/securityonion/issues/14010>`_
- UPGRADE: Elastic to 8.17.3 `#14356 <https://github.com/Security-Onion-Solutions/securityonion/issues/14356>`_
- UPGRADE: SOC Golang to 1.24 `#14230 <https://github.com/Security-Onion-Solutions/securityonion/issues/14230>`_

2.4.120 [20250212] Changes
--------------------------

- FEATURE: Additional supported integrations
- FEATURE: Add template Sigma & YARA local custom repo
- FEATURE: Allow users to prevent the kernel and other packages from being upgraded
- FEATURE: API Clients `#13928 <https://github.com/Security-Onion-Solutions/securityonion/issues/13928>`_
- FEATURE: ATT&CK Layer for Detections `#13885 <https://github.com/Security-Onion-Solutions/securityonion/issues/13885>`_
- FEATURE: Custom Local IP to Hostname Mapping
- FEATURE: Elastic Agent MSI `#13744 <https://github.com/Security-Onion-Solutions/securityonion/issues/13744>`_
- FEATURE: Expose new rule summary to Alerts page `#13770 <https://github.com/Security-Onion-Solutions/securityonion/issues/13770>`_
- FEATURE: Extract additional metadata - Created & Updated 
- FEATURE: Improve Operational Notes & Overrides
- FEATURE: Make TRACK column visible
- FEATURE: More configurable options to enable|disable Sigma rules on import
- FEATURE: Override Note `#13766 <https://github.com/Security-Onion-Solutions/securityonion/issues/13766>`_
- FEATURE: Show available Pro features on unprovisioned license screen `#14072 <https://github.com/Security-Onion-Solutions/securityonion/issues/14072>`_
- FEATURE: Suppress the Context Menu when highlighting text `#13184 <https://github.com/Security-Onion-Solutions/securityonion/issues/13184>`_
- FEATURE: Toggle Enabled|Disabled for Detection Engine syncs
- FEATURE: Trend Micro Integration
- FEATURE: When Clicking a Detection Engine Status, Run a Specific, Configurable Hunt Query `#13865 <https://github.com/Security-Onion-Solutions/securityonion/issues/13865>`_
- FEATURE: Zeek HTTP2
- FEATURE: Zeek IPSec `#14006 <https://github.com/Security-Onion-Solutions/securityonion/issues/14006>`_
- FEATURE: Zeek LDAP
- FEATURE: Zeek OpenVPN `#14005 <https://github.com/Security-Onion-Solutions/securityonion/issues/14005>`_
- FEATURE: Zeek QUIC `#6925 <https://github.com/Security-Onion-Solutions/securityonion/issues/6925>`_
- FIX: Better handling of Detections' custom git repo errors
- FIX: Cloud installs should use pre-installed docker registry data `#14044 <https://github.com/Security-Onion-Solutions/securityonion/issues/14044>`_
- FIX: Configuration YAML validator fails on valid YAML `#13965 <https://github.com/Security-Onion-Solutions/securityonion/issues/13965>`_
- FIX: Detections - Overrides list only displays 10 `#13950 <https://github.com/Security-Onion-Solutions/securityonion/issues/13950>`_
- FIX: Ensure createrepo_c is installed on airgapped manager nodes `#13857 <https://github.com/Security-Onion-Solutions/securityonion/issues/13857>`_
- FIX: Flickering Sankey chart `#14215 <https://github.com/Security-Onion-Solutions/securityonion/issues/14215>`_
- FIX: Have soup ensure that top.sls is in normal mode even if there are no soup changes `#13808 <https://github.com/Security-Onion-Solutions/securityonion/issues/13808>`_
- FIX: Invalidate a user's sessions when an administrator changes the user's password `#14076 <https://github.com/Security-Onion-Solutions/securityonion/issues/14076>`_
- FIX: Non Oracle nodes failing soup / Salt upgrade `#13926 <https://github.com/Security-Onion-Solutions/securityonion/issues/13926>`_
- FIX: null pointer exception in global@custom pipeline `#14117 <https://github.com/Security-Onion-Solutions/securityonion/issues/14117>`_
- FIX: Okta index template missing okta-mappings component template `#14106 <https://github.com/Security-Onion-Solutions/securityonion/issues/14106>`_
- FIX: Records being partially displayed in the Alerts interface when expanded `#14108 <https://github.com/Security-Onion-Solutions/securityonion/issues/14108>`_
- FIX: Review ILM settings for Detection History index
- FIX: rsync error during non-airgapped manager setup `#13860 <https://github.com/Security-Onion-Solutions/securityonion/issues/13860>`_
- FIX: Salt Repo has moved `#13898 <https://github.com/Security-Onion-Solutions/securityonion/issues/13898>`_
- FIX: Salt state warnings `#13851 <https://github.com/Security-Onion-Solutions/securityonion/issues/13851>`_
- FIX: so-repo-sync errors on non Oracle OS `#13919 <https://github.com/Security-Onion-Solutions/securityonion/issues/13919>`_
- FIX: Suricata Integrity Check fails when Suricata Metadata rules are enabled
- FIX: Update crowdstrike integration support `#13913 <https://github.com/Security-Onion-Solutions/securityonion/issues/13913>`_
- UPGRADE: ATT&CK Navigator to 5.1.0
- UPGRADE: CyberChef to 10.19.4 `#14131 <https://github.com/Security-Onion-Solutions/securityonion/issues/14131>`_
- UPGRADE: ElastAlert 2 to 2.22.0 `#14082 <https://github.com/Security-Onion-Solutions/securityonion/issues/14082>`_
- UPGRADE: Go dependencies in SOC `#14020 <https://github.com/Security-Onion-Solutions/securityonion/issues/14020>`_
- UPGRADE: InfluxDB to 2.7.10 `#14084 <https://github.com/Security-Onion-Solutions/securityonion/issues/14084>`_
- UPGRADE: Kratos to 1.3.1 `#14083 <https://github.com/Security-Onion-Solutions/securityonion/issues/14083>`_
- UPGRADE: NGINX to 1.26.2 `#14086 <https://github.com/Security-Onion-Solutions/securityonion/issues/14086>`_
- UPGRADE: Vue.js front-end UI framework to v3 `#13806 <https://github.com/Security-Onion-Solutions/securityonion/issues/13806>`_
- UPGRADE: Zeek 7

2.4.111 Patch [20241217] Changes
--------------------------------

- UPGRADE: Suricata 7.0.8 `#14024 <https://github.com/Security-Onion-Solutions/securityonion/issues/14024>`_

2.4.110 Hotfix [20241010] Changes
---------------------------------

- FIX: Use ID instead of name for getting integrations from agent policies `#13795 <https://github.com/Security-Onion-Solutions/securityonion/issues/13795>`_

2.4.110 [20241004] Changes
--------------------------

- FEATURE: Activate generated detection summaries `#13454 <https://github.com/Security-Onion-Solutions/securityonion/issues/13454>`_
- FEATURE: Add Elastic Integration for Barracuda CloudGen Firewall
- FEATURE: Add Elastic Integration for Imperva Cloud WAF
- FEATURE: Add new alerts for changes in SOC status `#13654 <https://github.com/Security-Onion-Solutions/securityonion/issues/13654>`_
- FEATURE: AI-Generated Rule analysis / summary
- FEATURE: Allow external access to suricata rules managed by Detections `#13655 <https://github.com/Security-Onion-Solutions/securityonion/issues/13655>`_
- FEATURE: Allow for users to add custom skins for IDH http
- FEATURE: Create ISO install options for SOS Appliances
- FEATURE: Desktop ISO install STIG support
- FEATURE: For improved upgrade experience, tag Elasticsearch image with Elastic version `#13606 <https://github.com/Security-Onion-Solutions/securityonion/issues/13606>`_
- FEATURE: Handle Custom Integration Policy Upgrades `#13560 <https://github.com/Security-Onion-Solutions/securityonion/issues/13560>`_
- FEATURE: SOS Process Filters for Elastic Agent 
- FEATURE: Standalone use Suricata for PCAP by default `#13650 <https://github.com/Security-Onion-Solutions/securityonion/issues/13650>`_
- FIX: Add additional warning text in Configuration screen when trying to disable key components
- FIX: Analysts should be able to modify and disable Suricata rules `#13668 <https://github.com/Security-Onion-Solutions/securityonion/issues/13668>`_
- FIX: Elastic integration field mappings `#13725 <https://github.com/Security-Onion-Solutions/securityonion/issues/13725>`_
- FIX: Intermittent soup errors causing soup to exit with failure message `#13247 <https://github.com/Security-Onion-Solutions/securityonion/issues/13247>`_
- FIX: Minion overrides in Config screen show global override values `#13689 <https://github.com/Security-Onion-Solutions/securityonion/issues/13689>`_
- FIX: Resolve missing CA certs in Kratos container `#13722 <https://github.com/Security-Onion-Solutions/securityonion/issues/13722>`_
- FIX: Sensor age in grid screen sometimes shows incorrect age of node `#13628 <https://github.com/Security-Onion-Solutions/securityonion/issues/13628>`_
- FIX: Since OIDC emails can have uppercase, force lowercase prior to server side dispatch `#13730 <https://github.com/Security-Onion-Solutions/securityonion/issues/13730>`_
- FIX: Stenographer packet loss differs from influxdb `#13626 <https://github.com/Security-Onion-Solutions/securityonion/issues/13626>`_
- FIX: Update Parsing of Suricata logs from pfSense and OPNsense
- FIX: When NIDS rules update, ask Suricata to reload rules rather than restart
- UPGRADE: CyberChef 10.19.2 `#13637 <https://github.com/Security-Onion-Solutions/securityonion/issues/13637>`_
- UPGRADE: Docker 27.2.0 `#13566 <https://github.com/Security-Onion-Solutions/securityonion/issues/13566>`_
- UPGRADE: ElastAlert 2 to 2.20.0 `#13700 <https://github.com/Security-Onion-Solutions/securityonion/issues/13700>`_
- UPGRADE: Kratos to 1.3.0 `#13758 <https://github.com/Security-Onion-Solutions/securityonion/issues/13758>`_
- UPGRADE: Suricata to 7.0.7 `#13760 <https://github.com/Security-Onion-Solutions/securityonion/issues/13760>`_
- UPGRADE: Zeek 6.0.8 `#13600 <https://github.com/Security-Onion-Solutions/securityonion/issues/13600>`_

2.4.100 Hotfix [20240903] Changes
---------------------------------

- FIX: Missing mappings for WEL Templates

2.4.100 [20240829] Changes
--------------------------

- FEATURE: Add breadcrumbs to Grid Configuration
- FEATURE: Add SOC Config Quick Link to allow Security Onion Desktop installations through firewall `#13412 <https://github.com/Security-Onion-Solutions/securityonion/issues/13412>`_
- FEATURE: Add warning to soup about ssh `#13466 <https://github.com/Security-Onion-Solutions/securityonion/issues/13466>`_
- FEATURE: Elastic Integration for tenable.io
- FEATURE: Optional setting to force users to setup OTP/MFA upon login `#13388 <https://github.com/Security-Onion-Solutions/securityonion/issues/13388>`_
- FEATURE: Enhanced notifications (Pro) and related configuration updates
- FIX: Admin resetting of a user's password is not removing MFA `#13468 <https://github.com/Security-Onion-Solutions/securityonion/issues/13468>`_
- FIX: Appliance kickstart updates
- FIX: Detections: YARA Detection tuning pivot should take user to detection source instead of tuning
- FIX: Duplicate variable causing Suricata failure `#13461 <https://github.com/Security-Onion-Solutions/securityonion/issues/13461>`_
- FIX: Elastic Fleet disable TLS 1.1 by default
- FIX: Exempt desktop nodes from license node count
- FIX: Firewall annotations for Kafka
- FIX: Reduce size of SOC image due to git
- FIX: Reduce SOC Config Loading Time
- FIX: Review and disable outdated ciphers for Fleet  `#11145 <https://github.com/Security-Onion-Solutions/securityonion/issues/11145>`_
- FIX: Salt packages not versionlocked `#13438 <https://github.com/Security-Onion-Solutions/securityonion/issues/13438>`_
- FIX: SOC logs ILM policy doesn't exist `#13555 <https://github.com/Security-Onion-Solutions/securityonion/issues/13555>`_
- FIX: Suricata Alerts missing kafka.id field
- FIX: Syntax Check before submitting New Rule `#13385 <https://github.com/Security-Onion-Solutions/securityonion/issues/13385>`_
- FIX: Tuning details should be included as part of the history item `#13225 <https://github.com/Security-Onion-Solutions/securityonion/issues/13225>`_
- FIX: Update Agent Builder Dependencies `#13142 <https://github.com/Security-Onion-Solutions/securityonion/issues/13142>`_
- FIX: Update pipeline version for EVTX `#13563 <https://github.com/Security-Onion-Solutions/securityonion/issues/13563>`_
- UPGRADE: Docker Registry 2.8.3 `#13510 <https://github.com/Security-Onion-Solutions/securityonion/issues/13510>`_
- UPGRADE: ElastAlert 2.19.0 `#13496 <https://github.com/Security-Onion-Solutions/securityonion/issues/13496>`_
- UPGRADE: Elastic 8.14.3 `#13263 <https://github.com/Security-Onion-Solutions/securityonion/issues/13263>`_
- UPGRADE: Kratos 1.2.0 `#13471 <https://github.com/Security-Onion-Solutions/securityonion/issues/13471>`_
- UPGRADE: Salt 3006.9 `#13423 <https://github.com/Security-Onion-Solutions/securityonion/issues/13423>`_
- UPGRADE: SOC dependencies to latest versions `#13488 <https://github.com/Security-Onion-Solutions/securityonion/issues/13488>`_
- UPGRADE: so-elastic-agent-builder base image `#13505 <https://github.com/Security-Onion-Solutions/securityonion/issues/13505>`_
- UPGRADE: so-elastic-fleet-package-registry base image
- UPGRADE: so-idh base image `#13503 <https://github.com/Security-Onion-Solutions/securityonion/issues/13503>`_
- UPGRADE: so-idstools base image `#13500 <https://github.com/Security-Onion-Solutions/securityonion/issues/13500>`_
- UPGRADE: so-influxdb base image and InfluxDB 2.7.9 `#13494 <https://github.com/Security-Onion-Solutions/securityonion/issues/13494>`_
- UPGRADE: so-kafka base image and Kafka 3.8.0 `#13497 <https://github.com/Security-Onion-Solutions/securityonion/issues/13497>`_
- UPGRADE: so-nginx base image `#13491 <https://github.com/Security-Onion-Solutions/securityonion/issues/13491>`_
- UPGRADE: so-pcaptools base image `#13495 <https://github.com/Security-Onion-Solutions/securityonion/issues/13495>`_
- UPGRADE: so-redis base image and Redis 7.2.5 `#13501 <https://github.com/Security-Onion-Solutions/securityonion/issues/13501>`_
- UPGRADE: so-steno base image `#13498 <https://github.com/Security-Onion-Solutions/securityonion/issues/13498>`_
- UPGRADE: so-strelka-backend base image
- UPGRADE: so-strelka base images `#13504 <https://github.com/Security-Onion-Solutions/securityonion/issues/13504>`_
- UPGRADE: so-suricata base image `#13492 <https://github.com/Security-Onion-Solutions/securityonion/issues/13492>`_
- UPGRADE: so-tcpreplay base image `#13499 <https://github.com/Security-Onion-Solutions/securityonion/issues/13499>`_
- UPGRADE: so-telegraf base image and Telegraf 1.31.3 `#13502 <https://github.com/Security-Onion-Solutions/securityonion/issues/13502>`_
- UPGRADE: so-zeek base image `#13493 <https://github.com/Security-Onion-Solutions/securityonion/issues/13493>`_

2.4.90 [20240729] Changes
-------------------------

- FEATURE: Add new action to SOC Actions list to allow users to more easily add their own actions `#13346 <https://github.com/Security-Onion-Solutions/securityonion/issues/13346>`_
- FEATURE: Include new Security Onion appliance images for v2 refresh
- FEATURE: Provide maximize button on configuration screen
- FEATURE: Support suricata regex enable | disable
- FEATURE: Visualize diff of history edits
- FIX: Better Timeout Error message `#12534 <https://github.com/Security-Onion-Solutions/securityonion/issues/12534>`_
- FIX: Custom defined template causes SLS rendering error in base:elasticsearch.enabled `#13328 <https://github.com/Security-Onion-Solutions/securityonion/issues/13328>`_
- FIX: Detections - Bulk Performance Revisit
- FIX: Disable logstash on heavynodes `#13073 <https://github.com/Security-Onion-Solutions/securityonion/issues/13073>`_
- FIX: Exclude policy phases if not defined in defaults `#13354 <https://github.com/Security-Onion-Solutions/securityonion/issues/13354>`_
- FIX: Heavynode architecture documentation
- FIX: Improve displayed metrics for Kafka in influxdb `#13235 <https://github.com/Security-Onion-Solutions/securityonion/issues/13235>`_
- FIX: Refactor Sync Process
- FIX: Update MOTD `#13317 <https://github.com/Security-Onion-Solutions/securityonion/issues/13317>`_
- FIX: Update SOC MOTD `#13320 <https://github.com/Security-Onion-Solutions/securityonion/issues/13320>`_
- UPGRADE: Base image for so-steno container to oracle9:latest `#13344 <https://github.com/Security-Onion-Solutions/securityonion/issues/13344>`_
- UPGRADE: Base image for so-tcpreplay container to oracle9:latest `#13345 <https://github.com/Security-Onion-Solutions/securityonion/issues/13345>`_
- UPGRADE: CyberChef 10.19.0 `#13267 <https://github.com/Security-Onion-Solutions/securityonion/issues/13267>`_
- UPGRADE: so-idh to newer base image `#13265 <https://github.com/Security-Onion-Solutions/securityonion/issues/13265>`_
- UPGRADE: so-nginx to nginx:1.26.1-alpine `#13264 <https://github.com/Security-Onion-Solutions/securityonion/issues/13264>`_
- UPGRADE: Suricata 7.0.6 `#13283 <https://github.com/Security-Onion-Solutions/securityonion/issues/13283>`_

2.4.80 [20240624] Changes
-------------------------

- FEATURE: Add `IP/VAR` column to Suricata Overrides view
- FEATURE: Add more links and descriptions to SOC MOTD `#13216 <https://github.com/Security-Onion-Solutions/securityonion/issues/13216>`_
- FEATURE: Add new Process actions `#13226 <https://github.com/Security-Onion-Solutions/securityonion/issues/13226>`_
- FEATURE: Add SOC Config Quick Links for Cold and Warm ILM Phases `#13203 <https://github.com/Security-Onion-Solutions/securityonion/issues/13203>`_
- FEATURE: Bulk Delete Custom Detections `#13151 <https://github.com/Security-Onion-Solutions/securityonion/issues/13151>`_
- FEATURE: Create Detection - Preload Rule Templates  `#13152 <https://github.com/Security-Onion-Solutions/securityonion/issues/13152>`_
- FEATURE: Guaranteed Message Delivery `#13201 <https://github.com/Security-Onion-Solutions/securityonion/issues/13201>`_
- FEATURE: Show notice in SOC if license will expire within 45 days
- FEATURE: Support Custom Suricata Rulesets via URL and local file `#13195 <https://github.com/Security-Onion-Solutions/securityonion/issues/13195>`_
- FEATURE: Support Suricata VARs for Overrides `#13194 <https://github.com/Security-Onion-Solutions/securityonion/issues/13194>`_
- FEATURE: Syntax Highlighting
- FEATURE: Toggle full query visibility in hunt screens
- FIX: Add duplicate check to Integrity Check
- FIX: Add file transfer status to ISO output
- FIX: Bulk Actions - No banner at start `#13177 <https://github.com/Security-Onion-Solutions/securityonion/issues/13177>`_
- FIX: Can not use suricata address-book names in address-group definitions `#13136 <https://github.com/Security-Onion-Solutions/securityonion/issues/13136>`_
- FIX: Custom Sigma Detection - Description field `#13159 <https://github.com/Security-Onion-Solutions/securityonion/issues/13159>`_
- FIX: Detections - Suricata Integrity Check `#13180 <https://github.com/Security-Onion-Solutions/securityonion/issues/13180>`_
- FIX: Elasticsearch index templates not loading `#13161 <https://github.com/Security-Onion-Solutions/securityonion/issues/13161>`_
- FIX: .items and .lists indices are created with a replica `#13111 <https://github.com/Security-Onion-Solutions/securityonion/issues/13111>`_
- FIX: Page limit for Fleet Agent Policies `#13131 <https://github.com/Security-Onion-Solutions/securityonion/issues/13131>`_
- FIX: Proxy support in Detections `#13153 <https://github.com/Security-Onion-Solutions/securityonion/issues/13153>`_
- FIX: Quoting when duplication Suricata Detection `#13241 <https://github.com/Security-Onion-Solutions/securityonion/issues/13241>`_
- FIX: Receiver nodes should allow connections from Elastic Agents `#13167 <https://github.com/Security-Onion-Solutions/securityonion/issues/13167>`_
- FIX: Refactor DetectionParameters
- FIX: Separate Suricata indices into alerts and metadata `#12868 <https://github.com/Security-Onion-Solutions/securityonion/issues/12868>`_
- FIX: so-test and so-tcpreplay fail when manager offline `#13104 <https://github.com/Security-Onion-Solutions/securityonion/issues/13104>`_
- FIX: Unable to add additional Suricata Overrides without page refresh `#13188 <https://github.com/Security-Onion-Solutions/securityonion/issues/13188>`_
- FIX: Visual Glitch - dupe operational notes when updating custom rule `#13199 <https://github.com/Security-Onion-Solutions/securityonion/issues/13199>`_
- UPGRADE: CyberChef 10.18.6 `#13174 <https://github.com/Security-Onion-Solutions/securityonion/issues/13174>`_
- UPGRADE: Docker `#13181 <https://github.com/Security-Onion-Solutions/securityonion/issues/13181>`_

2.4.70 [20240529] Changes
----------------------------------

- FEATURE: Add confirmation dialog for "revert to default" button in Configuration
- FEATURE: Add dashboard for NetFlow `#13009 <https://github.com/Security-Onion-Solutions/securityonion/issues/13009>`_
- FEATURE: Add dashboard for SOC Login Failures `#12738 <https://github.com/Security-Onion-Solutions/securityonion/issues/12738>`_
- FEATURE: Add dashboards specific to Elastic Agent `#12746 <https://github.com/Security-Onion-Solutions/securityonion/issues/12746>`_
- FEATURE: Add event.dataset to all Events table layouts `#12641 <https://github.com/Security-Onion-Solutions/securityonion/issues/12641>`_
- FEATURE: Add Events table columns for event.module elastic_agent `#12666 <https://github.com/Security-Onion-Solutions/securityonion/issues/12666>`_
- FEATURE: Add Events table columns for event.module kratos `#12740 <https://github.com/Security-Onion-Solutions/securityonion/issues/12740>`_
- FEATURE: Add Events table columns for event.module opencanary `#12655 <https://github.com/Security-Onion-Solutions/securityonion/issues/12655>`_
- FEATURE: Add Events table columns for event.module playbook `#12703 <https://github.com/Security-Onion-Solutions/securityonion/issues/12703>`_
- FEATURE: Add Events table columns for event.module sigma `#12743 <https://github.com/Security-Onion-Solutions/securityonion/issues/12743>`_
- FEATURE: Add Events table columns for event.module strelka `#12716 <https://github.com/Security-Onion-Solutions/securityonion/issues/12716>`_
- FEATURE: Add Events table columns for event.module system `#12628 <https://github.com/Security-Onion-Solutions/securityonion/issues/12628>`_
- FEATURE: Add Events table columns for stun logs `#12940 <https://github.com/Security-Onion-Solutions/securityonion/issues/12940>`_
- FEATURE: Add Events table columns for tunnel logs `#12937 <https://github.com/Security-Onion-Solutions/securityonion/issues/12937>`_
- FEATURE: Add Events table columns for zeek ssl and suricata ssl `#12697 <https://github.com/Security-Onion-Solutions/securityonion/issues/12697>`_
- FEATURE: Add groupby fields to Dashboards relating to sankey diagrams `#12657 <https://github.com/Security-Onion-Solutions/securityonion/issues/12657>`_
- FEATURE: Add hyperlink to airgap screen in setup `#12925 <https://github.com/Security-Onion-Solutions/securityonion/issues/12925>`_
- FEATURE: Add individual dashboards for Zeek SSL and Suricata SSL logs `#12699 <https://github.com/Security-Onion-Solutions/securityonion/issues/12699>`_
- FEATURE: Additional Supported Integrations #6
- FEATURE: Add more fields to the SOC Dashboards URL for so-import-pcap `#12972 <https://github.com/Security-Onion-Solutions/securityonion/issues/12972>`_
- FEATURE: Add process.command_line to Process Info and Process Ancestry dashboards `#12694 <https://github.com/Security-Onion-Solutions/securityonion/issues/12694>`_
- FEATURE: Add queue=True to so-checkin so that it will wait for any running states `#12815 <https://github.com/Security-Onion-Solutions/securityonion/issues/12815>`_
- FEATURE: Add SOC Quick Link for Elasticsearch ILM Deletion `#12854 <https://github.com/Security-Onion-Solutions/securityonion/issues/12854>`_
- FEATURE: Allow duplication of certain config settings
- FEATURE: Allow users to disable Elasticsearch cleanup script `#12856 <https://github.com/Security-Onion-Solutions/securityonion/issues/12856>`_
- FEATURE: Change default timeout period for Elastic Agent installation
- FEATURE: Continuation of new Detections module rollout `#12903 <https://github.com/Security-Onion-Solutions/securityonion/issues/12903>`_
- FEATURE: Delayed enrollment for Elastic Agents
- FEATURE: Enable license checks for enterprise features `#12839 <https://github.com/Security-Onion-Solutions/securityonion/issues/12839>`_
- FEATURE: Eval use Suricata for PCAP by default `#12878 <https://github.com/Security-Onion-Solutions/securityonion/issues/12878>`_
- FEATURE: Hunting for SOC logs should show relevant columns
- FEATURE: Introduce new readOnlyUi annotation
- FEATURE: Kismet integration `#12849 <https://github.com/Security-Onion-Solutions/securityonion/issues/12849>`_
- FEATURE: Lower EVAL memory requirement to 8GB RAM `#12896 <https://github.com/Security-Onion-Solutions/securityonion/issues/12896>`_
- FEATURE: pfSense Suricata logs `#12653 <https://github.com/Security-Onion-Solutions/securityonion/issues/12653>`_
- FEATURE: SOC Telemetry to provide feature usage feedback to dev team
- FEATURE: SOS Sigma ruleset
- FIX: Add annotations for BPF and Suricata PCAP `#12626 <https://github.com/Security-Onion-Solutions/securityonion/issues/12626>`_
- FIX: Add missing options to Suricata af-packet config `#12637 <https://github.com/Security-Onion-Solutions/securityonion/issues/12637>`_
- FIX: Add the write privilege to the analyst and limited-analyst roles to enable acking of alerts `#12770 <https://github.com/Security-Onion-Solutions/securityonion/issues/12770>`_
- FIX: Adjust so-import-pcap so that suricata works when it is pcapengine `#12969 <https://github.com/Security-Onion-Solutions/securityonion/issues/12969>`_
- FIX: Change Elasticsearch min_age setting for cold phase `#12890 <https://github.com/Security-Onion-Solutions/securityonion/issues/12890>`_
- FIX: Configuration screen search filter causes long delays `#12923 <https://github.com/Security-Onion-Solutions/securityonion/issues/12923>`_
- FIX: Detections alerts indices `#13005 <https://github.com/Security-Onion-Solutions/securityonion/issues/13005>`_
- FIX: Detections alerts template not being loaded because load script is trying to match names `#13048 <https://github.com/Security-Onion-Solutions/securityonion/issues/13048>`_
- FIX: Elastic retention setting not being honored when manager hostname is a subset of search node hostname `#12819 <https://github.com/Security-Onion-Solutions/securityonion/issues/12819>`_
- FIX: Elasticsearch annotation file for ILM index settings `#12726 <https://github.com/Security-Onion-Solutions/securityonion/issues/12726>`_
- FIX: Elasticsearch cleanup script should avoid Suricata alerts `#12855 <https://github.com/Security-Onion-Solutions/securityonion/issues/12855>`_
- FIX: Elasticsearch min_age regex `#12885 <https://github.com/Security-Onion-Solutions/securityonion/issues/12885>`_
- FIX: GitHub discussion/issue curator workflows fail on repo forks
- FIX: IDH node installs, but won't configure `#12991 <https://github.com/Security-Onion-Solutions/securityonion/issues/12991>`_
- FIX: idh.services is displayed in SOC Grid Configuration as an advanced setting  `#13012 <https://github.com/Security-Onion-Solutions/securityonion/issues/13012>`_
- FIX: Improve File dashboard `#12914 <https://github.com/Security-Onion-Solutions/securityonion/issues/12914>`_
- FIX: Input Validation for IPv6 addresses in Zeek and Suricata vars `#12675 <https://github.com/Security-Onion-Solutions/securityonion/issues/12675>`_
- FIX: mapping conflict with field http.response.status_code `#12543 <https://github.com/Security-Onion-Solutions/securityonion/issues/12543>`_
- FIX: Remove errant max_age setting from Elastic SOC config `#12851 <https://github.com/Security-Onion-Solutions/securityonion/issues/12851>`_
- FIX: Rendering SLS 'base:elasticsearch.enabled' failed: Jinja error: Cannot update using non-dict types in dictupdate.update() `#13030 <https://github.com/Security-Onion-Solutions/securityonion/issues/13030>`_
- FIX: Resetting a customized file to default should restore the default `#13008 <https://github.com/Security-Onion-Solutions/securityonion/issues/13008>`_
- FIX: so-elasticsearch-ilm-policy-load trying to set policy for indices not managed by ILM `#13021 <https://github.com/Security-Onion-Solutions/securityonion/issues/13021>`_
- FIX: so-index-list not working correctly `#12988 <https://github.com/Security-Onion-Solutions/securityonion/issues/12988>`_
- FIX: Sorting for older and newer indices in Elasticsearch cleanup `#12857 <https://github.com/Security-Onion-Solutions/securityonion/issues/12857>`_
- FIX: so-verify detects rare false error `#12811 <https://github.com/Security-Onion-Solutions/securityonion/issues/12811>`_
- FIX: Specify that static IP address is recommended `#12643 <https://github.com/Security-Onion-Solutions/securityonion/issues/12643>`_
- FIX: Update expected timestamp formats in ingest pipeline `#12887 <https://github.com/Security-Onion-Solutions/securityonion/issues/12887>`_
- FIX: Update so-whiptail to make installation screen more consistent `#12921 <https://github.com/Security-Onion-Solutions/securityonion/issues/12921>`_
- UPGRADE: CyberChef 10.17.0 `#12798 <https://github.com/Security-Onion-Solutions/securityonion/issues/12798>`_
- UPGRADE: Suricata 7.0.5 `#12843 <https://github.com/Security-Onion-Solutions/securityonion/issues/12843>`_
- UPGRADE: Zeek 6.0.4 `#13027 <https://github.com/Security-Onion-Solutions/securityonion/issues/13027>`_

2.4.60 [20240320] Changes
-------------------------

- FEATURE: Add Suricata classification.config for editing  `#12391 <https://github.com/Security-Onion-Solutions/securityonion/issues/12391>`_
- FEATURE: Add Suricata support for full PCAP `#12571 <https://github.com/Security-Onion-Solutions/securityonion/issues/12571>`_
- FEATURE: Add default columns for endpoint.events datasets `#12425 <https://github.com/Security-Onion-Solutions/securityonion/issues/12425>`_
- FEATURE: Add new SOC action for Process Info `#12421 <https://github.com/Security-Onion-Solutions/securityonion/issues/12421>`_
- FEATURE: Add new endpoint dashboards `#12428 <https://github.com/Security-Onion-Solutions/securityonion/issues/12428>`_
- FEATURE: Additional Supported Integrations #5
- FEATURE: Improve Grid page Reboot indicators `#12546 <https://github.com/Security-Onion-Solutions/securityonion/issues/12546>`_
- FEATURE: Initial implementation of the new Detections system (currently disabled)
- FIX: Accept Uppercase emails `#12559 <https://github.com/Security-Onion-Solutions/securityonion/issues/12559>`_
- FIX: Change the default setting for steno diskfreepercentage on standalone installations to 21 `#12541 <https://github.com/Security-Onion-Solutions/securityonion/issues/12541>`_
- FIX: Download only newest packages for network installs
- FIX: EA packages are not downloadable once STIGs have been applied
- FIX: Endpoint diagnostic template pattern `#12433 <https://github.com/Security-Onion-Solutions/securityonion/issues/12433>`_
- FIX: Exclude templates from global overrides when necessary `#12382 <https://github.com/Security-Onion-Solutions/securityonion/issues/12382>`_
- FIX: Improve the accuracy of the stenoloss script `#12477 <https://github.com/Security-Onion-Solutions/securityonion/issues/12477>`_
- FIX: Receiver node Redis queue fills up using Managersearch without a Searchnode `#12535 <https://github.com/Security-Onion-Solutions/securityonion/issues/12535>`_
- FIX: Support Oinkcode values containing leading 0's `#12506 <https://github.com/Security-Onion-Solutions/securityonion/issues/12506>`_
- FIX: Update SOC annotations for Stenographer PCAP `#12539 <https://github.com/Security-Onion-Solutions/securityonion/issues/12539>`_
- FIX: Update correlate quick action with new icon `#12387 <https://github.com/Security-Onion-Solutions/securityonion/issues/12387>`_
- FIX: Update ks.cfg for appliances
- FIX: error.message mapping for system.syslog `#12518 <https://github.com/Security-Onion-Solutions/securityonion/issues/12518>`_
- FIX: so-saltstack-update should use the proper repo in 2.4 `#12570 <https://github.com/Security-Onion-Solutions/securityonion/issues/12570>`_
- UPGRADE: CyberChef 10.8.2 `#12454 <https://github.com/Security-Onion-Solutions/securityonion/issues/12454>`_
- UPGRADE: Kratos to 1.1.0 `#12479 <https://github.com/Security-Onion-Solutions/securityonion/issues/12479>`_
- UPGRADE: Suricata 7.0.4 `#12609 <https://github.com/Security-Onion-Solutions/securityonion/issues/12609>`_

2.4.50 [20240220] Changes
-------------------------

- FEATURE: Add Suricata PCAP module to Sensoroni (currently disabled) `#12255 <https://github.com/Security-Onion-Solutions/securityonion/issues/12255>`_
- FEATURE: Add new SOC action to show process ancestry `#12345 <https://github.com/Security-Onion-Solutions/securityonion/issues/12345>`_
- FEATURE: Add new dashboards for community_id and firewall auth `#12323 <https://github.com/Security-Onion-Solutions/securityonion/issues/12323>`_
- FEATURE: Additional Supported Integrations #4
- FEATURE: Allow user to create custom elastic search pipelines without copying them over via ssh
- FEATURE: Allow user to create custom logstash pipelines without copying them over via ssh
- FEATURE: Dedicated Fleet node should have an nginx entry and cert that works for /artifacts `#11346 <https://github.com/Security-Onion-Solutions/securityonion/issues/11346>`_
- FEATURE: Determine if Elastic is on its own mount point if so adjust size for watermark `#12364 <https://github.com/Security-Onion-Solutions/securityonion/issues/12364>`_
- FEATURE: Improve Correlate and Hunt actions on SOC Actions menu `#12315 <https://github.com/Security-Onion-Solutions/securityonion/issues/12315>`_
- FEATURE: RITA Logs `#12226 <https://github.com/Security-Onion-Solutions/securityonion/issues/12226>`_
- FEATURE: Support PCAP pivots for ICMP packets in SOC
- FIX:  suricata.ike ingest pipeline does not exist `#12174 <https://github.com/Security-Onion-Solutions/securityonion/issues/12174>`_
- FIX: Add stenographer logging `#12282 <https://github.com/Security-Onion-Solutions/securityonion/issues/12282>`_
- FIX: Change field groupby button to new groupby `#12228 <https://github.com/Security-Onion-Solutions/securityonion/issues/12228>`_
- FIX: Correct SOC error messages related to malformed queries `#12269 <https://github.com/Security-Onion-Solutions/securityonion/issues/12269>`_
- FIX: Endpoint diagnostic collection index created with replicas `#12256 <https://github.com/Security-Onion-Solutions/securityonion/issues/12256>`_
- FIX: Expose node Reboot status as its own state; other grid/feature improvements
- FIX: Network Transport for suricata alerts should be lowercase `#12217 <https://github.com/Security-Onion-Solutions/securityonion/issues/12217>`_
- FIX: Strelka scan.pe.flags mapping `#12251 <https://github.com/Security-Onion-Solutions/securityonion/issues/12251>`_
- FIX: Sync the event.dataset values between the Windows Sysmon and ElasticAgent defend logs
- FIX: Syntax error running elastic fleet scripts during highstate
- FIX: User count logic providing inconsistent results `#12258 <https://github.com/Security-Onion-Solutions/securityonion/issues/12258>`_
- UPGRADE: CyberChef 10.6.0 `#12310 <https://github.com/Security-Onion-Solutions/securityonion/issues/12310>`_
- UPGRADE: Salt 3006.6 `#12304 <https://github.com/Security-Onion-Solutions/securityonion/issues/12304>`_
- UPGRADE: Strelka 0.24.01.18 `#12229 <https://github.com/Security-Onion-Solutions/securityonion/issues/12229>`_
- UPGRADE: Suricata 7.0.3 `#12327 <https://github.com/Security-Onion-Solutions/securityonion/issues/12327>`_
- UPGRADE: Zeek 6.0.3 `#12225 <https://github.com/Security-Onion-Solutions/securityonion/issues/12225>`_

2.4.40 [20240116] Changes
-------------------------

- FEATURE: Add geoip support to Suricata `#11901 <https://github.com/Security-Onion-Solutions/securityonion/issues/11901>`_
- FEATURE: Additional Supported Integrations #2 `#11958 <https://github.com/Security-Onion-Solutions/securityonion/issues/11958>`_
- FEATURE: Additional Supported Integrations #3 `#12056 <https://github.com/Security-Onion-Solutions/securityonion/issues/12056>`_
- FEATURE: Add server reboot notification to SOC  `#11852 <https://github.com/Security-Onion-Solutions/securityonion/issues/11852>`_
- FEATURE: Allow an easy way to disable incoming events to a manager `#12033 <https://github.com/Security-Onion-Solutions/securityonion/issues/12033>`_
- FEATURE: Carve out the cert_chain_fps value from SSL traffic `#11806 <https://github.com/Security-Onion-Solutions/securityonion/issues/11806>`_
- FEATURE: Echotrail, Elasticsearch, MalwareBazaar, and ThreatFox Analyzers `#12014 <https://github.com/Security-Onion-Solutions/securityonion/issues/12014>`_
- FEATURE: Grid page status/metric enhancements `#11971 <https://github.com/Security-Onion-Solutions/securityonion/issues/11971>`_
- FEATURE: Manipulate event table columns `#12145 <https://github.com/Security-Onion-Solutions/securityonion/issues/12145>`_
- FEATURE: Sublime Platform Analyzer `#11883 <https://github.com/Security-Onion-Solutions/securityonion/issues/11883>`_
- FIX: Add force option to integrations `#12017 <https://github.com/Security-Onion-Solutions/securityonion/issues/12017>`_
- FIX: Adding extra_hosts for SOC, Elasticsearch and Logstash Docker containers fails `#12015 <https://github.com/Security-Onion-Solutions/securityonion/issues/12015>`_
- FIX: Begin kickstart consolidation
- FIX: Corrupt job files should not cause SOC to exit during startup `#12082 <https://github.com/Security-Onion-Solutions/securityonion/issues/12082>`_
- FIX: Disable Elastic Agent Downloads for Import and Eval mode
- FIX: Docker service sometimes not started or enabled on remote nodes during setup `#12101 <https://github.com/Security-Onion-Solutions/securityonion/issues/12101>`_
- FIX: Documentation links under SOC - Administration - Configuration need updating `#11828 <https://github.com/Security-Onion-Solutions/securityonion/issues/11828>`_
- FIX: FIM Integration `#11847 <https://github.com/Security-Onion-Solutions/securityonion/issues/11847>`_
- FIX: Ignore Zeek analyzer log `#11892 <https://github.com/Security-Onion-Solutions/securityonion/issues/11892>`_
- FIX: Improve salt-relay reponse integrity
- FIX: ISO image should default to 1GB /boot partition `#12002 <https://github.com/Security-Onion-Solutions/securityonion/issues/12002>`_
- FIX: Logstash pipeline to point to self instead of manager `#12038 <https://github.com/Security-Onion-Solutions/securityonion/issues/12038>`_
- FIX: Make sure optional integration pillar values are merged with defaults `#12163 <https://github.com/Security-Onion-Solutions/securityonion/issues/12163>`_
- FIX: Playbook Navigator Layer `#11380 <https://github.com/Security-Onion-Solutions/securityonion/issues/11380>`_
- FIX: Remove Curator
- FIX: Remove sudo entry for so-setup after setup completes
- FIX: Rerunning setup should uninstall local Elastic Agent `#12030 <https://github.com/Security-Onion-Solutions/securityonion/issues/12030>`_
- FIX: Show more readable column names for default Case list screen `#12162 <https://github.com/Security-Onion-Solutions/securityonion/issues/12162>`_
- FIX: SOC Hunt HTTP EXE query `#11784 <https://github.com/Security-Onion-Solutions/securityonion/issues/11784>`_
- FIX: so-elastic-fleet-reset non-destructive `#12142 <https://github.com/Security-Onion-Solutions/securityonion/issues/12142>`_
- FIX: so-playbook-reset `#11790 <https://github.com/Security-Onion-Solutions/securityonion/issues/11790>`_
- FIX: Update clear scripts `#11991 <https://github.com/Security-Onion-Solutions/securityonion/issues/11991>`_
- FIX: Update dashboard and hunt query for firewall logs `#12021 <https://github.com/Security-Onion-Solutions/securityonion/issues/12021>`_
- FIX: Update NIDS rule.reference in common.nids pipeline `#11846 <https://github.com/Security-Onion-Solutions/securityonion/issues/11846>`_
- UPGRADE: Salt 3006.5 `#12143 <https://github.com/Security-Onion-Solutions/securityonion/issues/12143>`_
- UPGRADE: SOC dependencies to latest versions `#12041 <https://github.com/Security-Onion-Solutions/securityonion/issues/12041>`_
- UPGRADE: Strelka 0.23.12.01 `#11770 <https://github.com/Security-Onion-Solutions/securityonion/issues/11770>`_

2.4.30 Hotfix [20231228] Changes
--------------------------------

- FIX: Appliance kickstart files are not copying Elastic Agent tarballs `#12081 <https://github.com/Security-Onion-Solutions/securityonion/issues/12081>`_

2.4.30 Hotfix [20231219] Changes
--------------------------------

- FIX: Update appliance kickstart scripts to fix issue with package copy `#12044 <https://github.com/Security-Onion-Solutions/securityonion/issues/12044>`_

2.4.30 Hotfix [20231204] Changes
--------------------------------

- FIX: Choosing Desktop or IDH from ISO GRUB menu results in failure `#11865 <https://github.com/Security-Onion-Solutions/securityonion/issues/11865>`_
- FIX: Ensure airgap rule updates are being copied to the proper location `#11932 <https://github.com/Security-Onion-Solutions/securityonion/issues/11932>`_
- FIX: outdated import-evtx-logs pipeline versions `#11889 <https://github.com/Security-Onion-Solutions/securityonion/issues/11889>`_
- FIX: x509.pem_managed errors

2.4.30 Hotfix [20231121] Changes
--------------------------------

- FIX: Salt minion service disabled highstate in upgrade to 2.4.30 `#11851 <https://github.com/Security-Onion-Solutions/securityonion/issues/11851>`_

2.4.30 Hotfix [20231117] Changes
--------------------------------

- FIX: Elastic Defend Integration Policy Downgrade  `#11810 <https://github.com/Security-Onion-Solutions/securityonion/issues/11810>`_
- FIX: Update SSL cert to avoid Google Chrome error (2.4) `#11824 <https://github.com/Security-Onion-Solutions/securityonion/issues/11824>`_

2.4.30 [20231113] Changes
-------------------------

- FEATURE: Additional Supported Integrations `#11513 <https://github.com/Security-Onion-Solutions/securityonion/issues/11513>`_
- FEATURE: Allow for BPF comments in SOC `#11738 <https://github.com/Security-Onion-Solutions/securityonion/issues/11738>`_
- FEATURE: OpenID Connect (OIDC) support
- FEATURE: so-elastic-fleet-reset `#11697 <https://github.com/Security-Onion-Solutions/securityonion/issues/11697>`_
- FEATURE: Sublime Platform Integration `#11579 <https://github.com/Security-Onion-Solutions/securityonion/issues/11579>`_
- FIX: Add -watch to soctopus saltstate for file SOCtopus.conf. Makes container restart @ highstate if file is updated. `#11700 <https://github.com/Security-Onion-Solutions/securityonion/issues/11700>`_
- FIX: Allow ICMP to allow a node to respond to ping `#11495 <https://github.com/Security-Onion-Solutions/securityonion/issues/11495>`_
- FIX: Allow standalone install type to work with 16GB of ram `#11699 <https://github.com/Security-Onion-Solutions/securityonion/issues/11699>`_
- FIX: Allow the setting up of data_warm to the nodes list in ES
- FIX: Data not returned from mine for network.ip_addrs `#11502 <https://github.com/Security-Onion-Solutions/securityonion/issues/11502>`_
- FIX: Delete all obsolete scripts and unused code (also check so-setup, so-functions)
- FIX: Fail so-setup if Elastic Fleet Setup encounters an error `#11696 <https://github.com/Security-Onion-Solutions/securityonion/issues/11696>`_
- FIX: Global BPF prevents new sensor from applying highstate `#11610 <https://github.com/Security-Onion-Solutions/securityonion/issues/11610>`_
- FIX: Improve error handling of Elasticsearch pipeline and template load scripts `#11728 <https://github.com/Security-Onion-Solutions/securityonion/issues/11728>`_
- FIX: Logs not parsed correctly when shipped from Fleet Node `#11698 <https://github.com/Security-Onion-Solutions/securityonion/issues/11698>`_
- FIX: Only heavy nodes should be treated as remote Elastic clusters in SOC `#11553 <https://github.com/Security-Onion-Solutions/securityonion/issues/11553>`_
- FIX: Reduce ISO size `#11510 <https://github.com/Security-Onion-Solutions/securityonion/issues/11510>`_
- FIX: Set days for warm for all so-* indices
- FIX: Show container download status during soup `#11550 <https://github.com/Security-Onion-Solutions/securityonion/issues/11550>`_
- FIX: Sigma DNS mapping `#11498 <https://github.com/Security-Onion-Solutions/securityonion/issues/11498>`_
- FIX: Suricata 7 pkt_src field needs to be parsed `#11566 <https://github.com/Security-Onion-Solutions/securityonion/issues/11566>`_
- FIX: The values for specific nodes in zeek.config.local.load are being populated incorrectly `#11472 <https://github.com/Security-Onion-Solutions/securityonion/issues/11472>`_
- UPGRADE: NetworkMiner 2.8.1 `#11457 <https://github.com/Security-Onion-Solutions/securityonion/issues/11457>`_
- UPGRADE: Salt 3006.3 `#11529 <https://github.com/Security-Onion-Solutions/securityonion/issues/11529>`_
- UPGRADE: SOC dependency Axios to 1.6.1 `#11763 <https://github.com/Security-Onion-Solutions/securityonion/issues/11763>`_
- UPGRADE: Sophos Integration `#11548 <https://github.com/Security-Onion-Solutions/securityonion/issues/11548>`_
- UPGRADE: Upgrade Elastic to 8.10.4
- UPGRADE: Upgrade InfluxDB to 2.7.1 and Telegraf to 1.28.2
- UPGRADE: Upgrade Suricata to 7.0.2
- UPGRADE: Zeek 6.0.2


2.4.20 Hotfix [20231012] Changes
--------------------------------

- FIX: Elastic Defend Integration Policy Corrupted `#11527 <https://github.com/Security-Onion-Solutions/securityonion/issues/11527>`_

2.4.20 [20231006] Changes
-------------------------

- FEATURE: Add ingest parser for pfSense OpenVPN logs `#7656 <https://github.com/Security-Onion-Solutions/securityonion/issues/7656>`_
- FEATURE: Add new so-log-check tool to scan SO logging for anomalies
- FEATURE: Enable Analyzers to be managed through SOC `#11211 <https://github.com/Security-Onion-Solutions/securityonion/issues/11211>`_
- FEATURE: Grid screen improvements; support for desktop nodes
- FEATURE: Provide global replica value for index templates `#10998 <https://github.com/Security-Onion-Solutions/securityonion/issues/10998>`_
- FEATURE: SOC Grid Members should prompt for confirmation before actually deleting `#11223 <https://github.com/Security-Onion-Solutions/securityonion/issues/11223>`_
- FIX: Adding custom action to SOC causes the Endgame action to be replicated `#11210 <https://github.com/Security-Onion-Solutions/securityonion/issues/11210>`_
- FIX: Add Transform Role `#11309 <https://github.com/Security-Onion-Solutions/securityonion/issues/11309>`_
- FIX: CentOS stream 9 installation `#11168 <https://github.com/Security-Onion-Solutions/securityonion/issues/11168>`_
- FIX: Clean component template directory `#11331 <https://github.com/Security-Onion-Solutions/securityonion/issues/11331>`_
- FIX: Desktop via network install fails `#10975 <https://github.com/Security-Onion-Solutions/securityonion/issues/10975>`_
- FIX: Disable conn stats from being generated by default `#11410 <https://github.com/Security-Onion-Solutions/securityonion/issues/11410>`_
- FIX: Docker custom_bind_mounts not working for some containers `#11122 <https://github.com/Security-Onion-Solutions/securityonion/issues/11122>`_
- FIX: Duplicate cronjobs for filecheck `#11400 <https://github.com/Security-Onion-Solutions/securityonion/issues/11400>`_
- FIX: Elastic Agent - Installation "Not Accessible" Message `#11191 <https://github.com/Security-Onion-Solutions/securityonion/issues/11191>`_
- FIX: Elastic Fleet key and cert errors on heavynode `#11026 <https://github.com/Security-Onion-Solutions/securityonion/issues/11026>`_
- FIX: Exclude Zeek console log ingestion `#11082 <https://github.com/Security-Onion-Solutions/securityonion/issues/11082>`_
- FIX: Features pillar not showing all enabled features `#11130 <https://github.com/Security-Onion-Solutions/securityonion/issues/11130>`_
- FIX: Fleet plugin logs ERROR during kibana restart `#10955 <https://github.com/Security-Onion-Solutions/securityonion/issues/10955>`_
- FIX: Force nginx to run as user nobody `#11402 <https://github.com/Security-Onion-Solutions/securityonion/issues/11402>`_
- FIX: Heavy nodes are missing ElasticFleet integration policies `#11189 <https://github.com/Security-Onion-Solutions/securityonion/issues/11189>`_
- FIX: Heavy Nodes are not properly added to the soc.json `#11192 <https://github.com/Security-Onion-Solutions/securityonion/issues/11192>`_
- FIX: Improve consistency in cert storage across OS families `#11162 <https://github.com/Security-Onion-Solutions/securityonion/issues/11162>`_
- FIX: Improve default settings to avoid Elasticsearch hitting watermark `#11305 <https://github.com/Security-Onion-Solutions/securityonion/issues/11305>`_
- FIX: Kibana Elastic Agent Dashboard 404 `#11018 <https://github.com/Security-Onion-Solutions/securityonion/issues/11018>`_
- FIX: Maintain minion log in INFO level, add logrotate `#10921 <https://github.com/Security-Onion-Solutions/securityonion/issues/10921>`_
- FIX: Make sure a data stream is created for syslog `#11209 <https://github.com/Security-Onion-Solutions/securityonion/issues/11209>`_
- FIX: Make sure Elastic packages are loaded when changed `#11428 <https://github.com/Security-Onion-Solutions/securityonion/issues/11428>`_
- FIX: Minimum system requirements checks during setup `#11324 <https://github.com/Security-Onion-Solutions/securityonion/issues/11324>`_
- FIX: Minion log appears to show timezone bouncing `#10922 <https://github.com/Security-Onion-Solutions/securityonion/issues/10922>`_
- FIX: osquery not working on macOS
- FIX: Pre-load Integration Templates `#11146 <https://github.com/Security-Onion-Solutions/securityonion/issues/11146>`_
- FIX: Prevent repeated creation of unused Docker volumes `#9941 <https://github.com/Security-Onion-Solutions/securityonion/issues/9941>`_
- FIX: Remove default component templates to prevent conflicts `#11260 <https://github.com/Security-Onion-Solutions/securityonion/issues/11260>`_
- FIX: Remove OSSEC and add Playbook mappings for the SOC Alerts Event Table `#11015 <https://github.com/Security-Onion-Solutions/securityonion/issues/11015>`_
- FIX: Remove telegraf beats EPS script `#11412 <https://github.com/Security-Onion-Solutions/securityonion/issues/11412>`_
- FIX: Rename some SOC log fields to more unique field names `#11429 <https://github.com/Security-Onion-Solutions/securityonion/issues/11429>`_
- FIX: Reposync and yara rules shot not run in airgap `#11427 <https://github.com/Security-Onion-Solutions/securityonion/issues/11427>`_
- FIX: SOC Config pcap doc links should point to steno docs `#11302 <https://github.com/Security-Onion-Solutions/securityonion/issues/11302>`_
- FIX: SOC Config sensoroni doc links should point to correct docs `#11362 <https://github.com/Security-Onion-Solutions/securityonion/issues/11362>`_
- FIX: SOC doesn't return user to login page after session expires `#11438 <https://github.com/Security-Onion-Solutions/securityonion/issues/11438>`_
- FIX: SOC fails to parse incomplete Elastic error response `#11435 <https://github.com/Security-Onion-Solutions/securityonion/issues/11435>`_
- FIX: SOC Grid Import inconsistency with larger files `#11143 <https://github.com/Security-Onion-Solutions/securityonion/issues/11143>`_
- FIX: Some packages are installed/removed and upgraded/downgraded every 15min `#11458 <https://github.com/Security-Onion-Solutions/securityonion/issues/11458>`_
- FIX: so-import-evtx incorrect dates `#11332 <https://github.com/Security-Onion-Solutions/securityonion/issues/11332>`_
- FIX: so-salt-minion-check not rendering as jinja `#11390 <https://github.com/Security-Onion-Solutions/securityonion/issues/11390>`_
- FIX: Stop zeek from trying to email reports `#11407 <https://github.com/Security-Onion-Solutions/securityonion/issues/11407>`_
- FIX: Strelka ingest pipeline should properly index entropy 0 values and float values in the same field
- FIX: Suricata filter and extraction rules are not properly updated `#11229 <https://github.com/Security-Onion-Solutions/securityonion/issues/11229>`_
- FIX: Update firewall docs for custom port and host groups `#11053 <https://github.com/Security-Onion-Solutions/securityonion/issues/11053>`_
- FIX: Update IDH Opencanary Modules to indicate they only apply to IDH nodes `#10170 <https://github.com/Security-Onion-Solutions/securityonion/issues/10170>`_
- UPGRADE: Kratos to v1.0.0
- UPGRADE: Suricata 6.0.14 `#11319 <https://github.com/Security-Onion-Solutions/securityonion/issues/11319>`_
- UPGRADE: Zeek 5.0.10 `#11301 <https://github.com/Security-Onion-Solutions/securityonion/issues/11301>`_

2.4.10 Hotfix [20230821] Changes
--------------------------------

- FIX: Component templates not updated when packages are updated `#11065 <https://github.com/Security-Onion-Solutions/securityonion/issues/11065>`_
- FIX: Importing both PCAP and EVTX files fails `#11030 <https://github.com/Security-Onion-Solutions/securityonion/issues/11030>`_
- FIX: Logstash container missing on distributed receiver `#11099 <https://github.com/Security-Onion-Solutions/securityonion/issues/11099>`_
- FIX: pipeline with id logs-system.syslog-1.6.4 does not exist `#11038 <https://github.com/Security-Onion-Solutions/securityonion/issues/11038>`_
- FIX: Suricata permissions on Heavy Nodes are incorrect `#11031 <https://github.com/Security-Onion-Solutions/securityonion/issues/11031>`_

2.4.10 [20230815] Changes
-------------------------

- FEATURE: Auto-Upgrade Node Agents `#10949 <https://github.com/Security-Onion-Solutions/securityonion/issues/10949>`_
- FEATURE: Customize desktop environment `#10957 <https://github.com/Security-Onion-Solutions/securityonion/issues/10957>`_
- FIX: Custom actions, queries, tools can cause SOC restart to fail `#11022 <https://github.com/Security-Onion-Solutions/securityonion/issues/11022>`_
- FIX: Elastic Agents won't upgrade without Internet connection `#10981 <https://github.com/Security-Onion-Solutions/securityonion/issues/10981>`_
- FIX: Elastic Integrations not upgrading during SOUP `#10984 <https://github.com/Security-Onion-Solutions/securityonion/issues/10984>`_
- FIX: Elastic index settings annotations need synchronized with those specified in defaults `#10999 <https://github.com/Security-Onion-Solutions/securityonion/issues/10999>`_
- FIX: File extraction not working after switching from Zeek metadata to Suricata metadata `#10973 <https://github.com/Security-Onion-Solutions/securityonion/issues/10973>`_
- FIX: Fleet - url_base not working in cert CN `#11003 <https://github.com/Security-Onion-Solutions/securityonion/issues/11003>`_
- FIX: Improve wording for Firewall entries under Grid Administration Quick Links `#10990 <https://github.com/Security-Onion-Solutions/securityonion/issues/10990>`_
- FIX: Influx reporting No Results for Zeek Capture Loss `#10956 <https://github.com/Security-Onion-Solutions/securityonion/issues/10956>`_
- FIX: Suricata should not assume the interface will always be bond0 `#10954 <https://github.com/Security-Onion-Solutions/securityonion/issues/10954>`_
- FIX: Sysmon Events Table Field Rendering `#10985 <https://github.com/Security-Onion-Solutions/securityonion/issues/10985>`_
- FIX: so-desktop-install needs to change from Rocky to Oracle `#10962 <https://github.com/Security-Onion-Solutions/securityonion/issues/10962>`_
- FIX: soup may fail while trying to query Fleet server `#10974 <https://github.com/Security-Onion-Solutions/securityonion/issues/10974>`_

2.4.5 RC2 [20230807] Changes
----------------------------

- FEATURE: Add NetworkMiner to Security Onion Desktop `#10865 <https://github.com/Security-Onion-Solutions/securityonion/issues/10865>`_
- FEATURE: Add value from record in Hunt, etc as an observable to an existing or new case `#7992 <https://github.com/Security-Onion-Solutions/securityonion/issues/7992>`_
- FEATURE: Enable CommunityID for Elastic Defend Logs `#10811 <https://github.com/Security-Onion-Solutions/securityonion/issues/10811>`_
- FEATURE: Heavy Node Support `#10671 <https://github.com/Security-Onion-Solutions/securityonion/issues/10671>`_
- FEATURE: so-import-evtx - timeshift `#10743 <https://github.com/Security-Onion-Solutions/securityonion/issues/10743>`_
- FEATURE: soup should rotate its log file `#10951 <https://github.com/Security-Onion-Solutions/securityonion/issues/10951>`_
- FIX: Dashboards with multiple groupby charts always filter by the first chart's, first groupby field `#10856 <https://github.com/Security-Onion-Solutions/securityonion/issues/10856>`_
- FIX: Disable offload on monitor NICs `#10900 <https://github.com/Security-Onion-Solutions/securityonion/issues/10900>`_
- FIX: EQL Field Mappings `#10783 <https://github.com/Security-Onion-Solutions/securityonion/issues/10783>`_
- FIX: Elastic Fleet Improvements `#10846 <https://github.com/Security-Onion-Solutions/securityonion/issues/10846>`_
- FIX: Firewall state custom host group assignments for single portgroup entry `#10917 <https://github.com/Security-Onion-Solutions/securityonion/issues/10917>`_
- FIX: IDH node `#10882 <https://github.com/Security-Onion-Solutions/securityonion/issues/10882>`_
- FIX: IPTables Persistence `#10884 <https://github.com/Security-Onion-Solutions/securityonion/issues/10884>`_
- FIX: Install Error: so-yara-download failed `#10880 <https://github.com/Security-Onion-Solutions/securityonion/issues/10880>`_
- FIX: Install screen - Firewall `#10945 <https://github.com/Security-Onion-Solutions/securityonion/issues/10945>`_
- FIX: List settings updated with blank values should be stored as empty lists `#10936 <https://github.com/Security-Onion-Solutions/securityonion/issues/10936>`_
- FIX: Login page shows error banner briefly on initial page load `#10911 <https://github.com/Security-Onion-Solutions/securityonion/issues/10911>`_
- FIX: RAID status on Grid page `#10935 <https://github.com/Security-Onion-Solutions/securityonion/issues/10935>`_
- FIX: SOC Auth dashboard `#10878 <https://github.com/Security-Onion-Solutions/securityonion/issues/10878>`_
- FIX: Security Onion Desktop state should default to Gnome Classic `#10958 <https://github.com/Security-Onion-Solutions/securityonion/issues/10958>`_
- FIX: sensor MTU setting in SOC Config should be read only `#10883 <https://github.com/Security-Onion-Solutions/securityonion/issues/10883>`_
- FIX: so-status taking several seconds to complete `#10909 <https://github.com/Security-Onion-Solutions/securityonion/issues/10909>`_
- FIX: soup `#10902 <https://github.com/Security-Onion-Solutions/securityonion/issues/10902>`_
- FIX: syslog not working `#10896 <https://github.com/Security-Onion-Solutions/securityonion/issues/10896>`_
- FIX: verbiage and links in soc_sensor.yaml `#10906 <https://github.com/Security-Onion-Solutions/securityonion/issues/10906>`_
- UPGRADE: Elastic 8.8.2 `#10864 <https://github.com/Security-Onion-Solutions/securityonion/issues/10864>`_

2.4.4 RC1 [20230728] Changes
----------------------------

- FEATURE: Add DNS lookup action to SOC `#8655 <https://github.com/Security-Onion-Solutions/securityonion/issues/8655>`_
- FEATURE: Add Oracle Linux Support `#10844 <https://github.com/Security-Onion-Solutions/securityonion/issues/10844>`_
- FEATURE: Add pivots for relational operators on numbers `#8024 <https://github.com/Security-Onion-Solutions/securityonion/issues/8024>`_
- FEATURE: Add relative Timeframe and Refresh Interval as URL Parameters to Hunt `#3352 <https://github.com/Security-Onion-Solutions/securityonion/issues/3352>`_
- FEATURE: Cases - Add ability to enable dynamic observable extraction `#7972 <https://github.com/Security-Onion-Solutions/securityonion/issues/7972>`_
- FEATURE: Oracle Linux ISO `#10845 <https://github.com/Security-Onion-Solutions/securityonion/issues/10845>`_
- FEATURE: Security Onion Desktop `#10862 <https://github.com/Security-Onion-Solutions/securityonion/issues/10862>`_
- FIX: Add retry to Elastic Agent installer `#10488 <https://github.com/Security-Onion-Solutions/securityonion/issues/10488>`_
- FIX: Case status code 404 error `#10759 <https://github.com/Security-Onion-Solutions/securityonion/issues/10759>`_
- FIX: Intermittent pcap retrieval `#10750 <https://github.com/Security-Onion-Solutions/securityonion/issues/10750>`_
- FIX: Navigator Errors `#10742 <https://github.com/Security-Onion-Solutions/securityonion/issues/10742>`_
- FIX: Remove .security subfield `#10745 <https://github.com/Security-Onion-Solutions/securityonion/issues/10745>`_
- UPGRADE: CyberChef 10.5.2 `#10781 <https://github.com/Security-Onion-Solutions/securityonion/issues/10781>`_
- UPGRADE: so-registry docker image `#10727 <https://github.com/Security-Onion-Solutions/securityonion/issues/10727>`_

2.4.3 Beta 4 [20230711] Changes
-------------------------------

- FEATURE: Add link to Downloads page for convenient access to firewall settings `#10702 <https://github.com/Security-Onion-Solutions/securityonion/issues/10702>`_
- FEATURE: Add more SOC Config quick links `#10563 <https://github.com/Security-Onion-Solutions/securityonion/issues/10563>`_
- FEATURE: Add time zone selection to Grid page `#8629 <https://github.com/Security-Onion-Solutions/securityonion/issues/8629>`_
- FEATURE: Add webauthn support to SOC `#10608 <https://github.com/Security-Onion-Solutions/securityonion/issues/10608>`_
- FEATURE: Allow import of PCAP and EVTX via SOC UI `#10413 <https://github.com/Security-Onion-Solutions/securityonion/issues/10413>`_
- FEATURE: Elastic Fleet - Automatically Update Logstash Outputs `#10746 <https://github.com/Security-Onion-Solutions/securityonion/issues/10746>`_
- FEATURE: Elastic Fleet Server URL - Custom Domain `#10744 <https://github.com/Security-Onion-Solutions/securityonion/issues/10744>`_
- FEATURE: Supported Integrations `#10590 <https://github.com/Security-Onion-Solutions/securityonion/issues/10590>`_
- FEATURE: so-import-evtx `#10673 <https://github.com/Security-Onion-Solutions/securityonion/issues/10673>`_
- FIX: Strelka rule path `#10715 <https://github.com/Security-Onion-Solutions/securityonion/issues/10715>`_
- FIX: 2.4 ISO image won't install on Virtualbox `#10534 <https://github.com/Security-Onion-Solutions/securityonion/issues/10534>`_
- FIX: Account for Suricata XFF function in parsing and ingestion `#8643 <https://github.com/Security-Onion-Solutions/securityonion/issues/8643>`_
- FIX: Add more Zeek logs to excluded list `#10569 <https://github.com/Security-Onion-Solutions/securityonion/issues/10569>`_
- FIX: Analyzer requests and whoisit updates `#10524 <https://github.com/Security-Onion-Solutions/securityonion/issues/10524>`_
- FIX: Change Playbook index to data stream and update event.severity_label `#10523 <https://github.com/Security-Onion-Solutions/securityonion/issues/10523>`_
- FIX: Cleanup log-rotate.conf `#10545 <https://github.com/Security-Onion-Solutions/securityonion/issues/10545>`_
- FIX: Curator should ignore empty list `#10512 <https://github.com/Security-Onion-Solutions/securityonion/issues/10512>`_
- FIX: Don't override default integration ingest node pipelines `#10542 <https://github.com/Security-Onion-Solutions/securityonion/issues/10542>`_
- FIX: Ensure operations on records with "Missing" fields use correct search `#8025 <https://github.com/Security-Onion-Solutions/securityonion/issues/8025>`_
- FIX: Ensure packages aren't installed from default Rocky repos `#10630 <https://github.com/Security-Onion-Solutions/securityonion/issues/10630>`_
- FIX: Exclude System logs from Hunt/Dashboard Queries. `#10122 <https://github.com/Security-Onion-Solutions/securityonion/issues/10122>`_
- FIX: Finish SSL cert integration into SOC config UI `#10533 <https://github.com/Security-Onion-Solutions/securityonion/issues/10533>`_
- FIX: Improve SOC login error message for disabled users `#8908 <https://github.com/Security-Onion-Solutions/securityonion/issues/8908>`_
- FIX: Increase net.core.wmem_default value `#10602 <https://github.com/Security-Onion-Solutions/securityonion/issues/10602>`_
- FIX: InfluxDB NSM Disk Usage visualization `#10520 <https://github.com/Security-Onion-Solutions/securityonion/issues/10520>`_
- FIX: Integration logs not parsed correctly `#10672 <https://github.com/Security-Onion-Solutions/securityonion/issues/10672>`_
- FIX: Logstash soc.fields.query warning `#10528 <https://github.com/Security-Onion-Solutions/securityonion/issues/10528>`_
- FIX: Node description config setting should only apply at the node level `#10562 <https://github.com/Security-Onion-Solutions/securityonion/issues/10562>`_
- FIX: Remove default excluded rules from YARA repo `#10718 <https://github.com/Security-Onion-Solutions/securityonion/issues/10718>`_
- FIX: Review Kibana Dashboards `#10664 <https://github.com/Security-Onion-Solutions/securityonion/issues/10664>`_
- FIX: Rework dataset name and add tags based on suffix `#10526 <https://github.com/Security-Onion-Solutions/securityonion/issues/10526>`_
- FIX: Rework field to account for missing classifiers `#10420 <https://github.com/Security-Onion-Solutions/securityonion/issues/10420>`_
- FIX: SOC Config NTP quick link `#10519 <https://github.com/Security-Onion-Solutions/securityonion/issues/10519>`_
- FIX: Scheduled jobs trying to run during setup `#10468 <https://github.com/Security-Onion-Solutions/securityonion/issues/10468>`_
- FIX: Set Elastic Fleet certs to use url_base `#10510 <https://github.com/Security-Onion-Solutions/securityonion/issues/10510>`_
- FIX: Setup re-runs when SSH'ing into a successfully installed minion node `#10498 <https://github.com/Security-Onion-Solutions/securityonion/issues/10498>`_
- FIX: Strelka rule exclusions `#10716 <https://github.com/Security-Onion-Solutions/securityonion/issues/10716>`_
- FIX: Suricata DHCP logs not ingesting `#10565 <https://github.com/Security-Onion-Solutions/securityonion/issues/10565>`_
- FIX: Suricata dataset values for certain types of metadata `#10551 <https://github.com/Security-Onion-Solutions/securityonion/issues/10551>`_
- FIX: Update README.md `#10554 <https://github.com/Security-Onion-Solutions/securityonion/issues/10554>`_
- FIX: Update cheat sheet for 2.4 `#10532 <https://github.com/Security-Onion-Solutions/securityonion/issues/10532>`_
- UPGRADE: CyberChef 10.4.0 `#10581 <https://github.com/Security-Onion-Solutions/securityonion/issues/10581>`_
- UPGRADE: Suricata 6.0.13 `#10594 <https://github.com/Security-Onion-Solutions/securityonion/issues/10594>`_

2.4.2 Beta 3 [20230531] Changes
-------------------------------

- FEATURE: Add additional alerts for Influxdb `#10388 <https://github.com/Security-Onion-Solutions/securityonion/issues/10388>`_
- FEATURE: Add link to SOC error messages that takes user to hunt and auto-searches for recent SOC-related errors. `#10283 <https://github.com/Security-Onion-Solutions/securityonion/issues/10283>`_
- FEATURE: Add Protected checkbox on Attachment upload form `#10203 <https://github.com/Security-Onion-Solutions/securityonion/issues/10203>`_
- FEATURE: Add support for Apple Silicon Elastic Agent Installer `#10473 <https://github.com/Security-Onion-Solutions/securityonion/issues/10473>`_
- FEATURE: Add support for EQL to Playbook `#10471 <https://github.com/Security-Onion-Solutions/securityonion/issues/10471>`_
- FEATURE: Allow for any docker container to have extra hosts and custom binds `#10301 <https://github.com/Security-Onion-Solutions/securityonion/issues/10301>`_
- FEATURE: Allow users to switch between airgap and non airgap. `#10470 <https://github.com/Security-Onion-Solutions/securityonion/issues/10470>`_
- FEATURE: Dedicated Elastic Fleet Node `#10474 <https://github.com/Security-Onion-Solutions/securityonion/issues/10474>`_
- FEATURE: Enable Elastic Defend Integration on Endpoints Policy `#10475 <https://github.com/Security-Onion-Solutions/securityonion/issues/10475>`_
- FEATURE: Integrate Elastic Artifact Repo `#10053 <https://github.com/Security-Onion-Solutions/securityonion/issues/10053>`_
- FEATURE: Integrate Elastic Package Registry `#10472 <https://github.com/Security-Onion-Solutions/securityonion/issues/10472>`_
- FEATURE: ISO image `#10476 <https://github.com/Security-Onion-Solutions/securityonion/issues/10476>`_
- FEATURE: Link the Grid Interface with Docker container log files `#10149 <https://github.com/Security-Onion-Solutions/securityonion/issues/10149>`_
- FEATURE: Prompt user to verify the manager nodes IP address if a DNS record if found during setup. `#10334 <https://github.com/Security-Onion-Solutions/securityonion/issues/10334>`_
- FEATURE: Quicklinks to common configs `#10395 <https://github.com/Security-Onion-Solutions/securityonion/issues/10395>`_
- FEATURE: SOC config UI should process each line individually with regex when multiline: True is set `#10243 <https://github.com/Security-Onion-Solutions/securityonion/issues/10243>`_
- FEATURE: Support authentication rate limiting `#10308 <https://github.com/Security-Onion-Solutions/securityonion/issues/10308>`_
- FIX: AWS Instances with forced IMDSv2 enabled fail to detect running in AWS `#10205 <https://github.com/Security-Onion-Solutions/securityonion/issues/10205>`_
- FIX: Cluster delete script should use different disk space logic when /nsm is shared among services `#10418 <https://github.com/Security-Onion-Solutions/securityonion/issues/10418>`_
- FIX: Correct SOC Annotations for idstools in Grid Configuration. `#10208 <https://github.com/Security-Onion-Solutions/securityonion/issues/10208>`_
- FIX: Correct SOC Annotations of Zeek in Grid Configuration. `#10211 <https://github.com/Security-Onion-Solutions/securityonion/issues/10211>`_
- FIX: Hunt Quick Drilldown `#10377 <https://github.com/Security-Onion-Solutions/securityonion/issues/10377>`_
- FIX: If mdengine is changed to Suricata, Zeek is still shown in so-status `#10232 <https://github.com/Security-Onion-Solutions/securityonion/issues/10232>`_
- FIX: Improve SOC configuration handling of lists `#10219 <https://github.com/Security-Onion-Solutions/securityonion/issues/10219>`_
- FIX: Improve soup's local file modification logic `#8972 <https://github.com/Security-Onion-Solutions/securityonion/issues/8972>`_
- FIX: In distributed deployment, Dashboards/Kibana only show data from the first sensor added. `#10231 <https://github.com/Security-Onion-Solutions/securityonion/issues/10231>`_
- FIX: Influxdb Elasticsearch cells showing duplicate data. `#10336 <https://github.com/Security-Onion-Solutions/securityonion/issues/10336>`_
- FIX: Kibana: Ensure _id fields beginning with a hyphen work properly when pivoting to SOC from Kibana `#10305 <https://github.com/Security-Onion-Solutions/securityonion/issues/10305>`_
- FIX: Logstash WARN logstash.outputs.elasticsearch on searchnode `#10291 <https://github.com/Security-Onion-Solutions/securityonion/issues/10291>`_
- FIX: Prepare SOUP for 2.4 `#10056 <https://github.com/Security-Onion-Solutions/securityonion/issues/10056>`_
- FIX: Prevent duplicate observables from being automatically created when attaching events to a case. `#10123 <https://github.com/Security-Onion-Solutions/securityonion/issues/10123>`_
- FIX: Review 2.4 file permissions and other local security changes `#9110 <https://github.com/Security-Onion-Solutions/securityonion/issues/9110>`_
- FIX: Setting CPU affinity or number of threads for Suricata not being applied. `#10240 <https://github.com/Security-Onion-Solutions/securityonion/issues/10240>`_
- FIX: Simplify cloud detection `#10261 <https://github.com/Security-Onion-Solutions/securityonion/issues/10261>`_
- FIX: Some SOC Config settings are only visible when Advanced is enabled `#10429 <https://github.com/Security-Onion-Solutions/securityonion/issues/10429>`_
- FIX: Strelka YARA Compilation `#10271 <https://github.com/Security-Onion-Solutions/securityonion/issues/10271>`_
- FIX: Suricata ignores the threads and always is set to 1 `#10230 <https://github.com/Security-Onion-Solutions/securityonion/issues/10230>`_
- FIX: Unable to disable PCAP via web configuration `#10229 <https://github.com/Security-Onion-Solutions/securityonion/issues/10229>`_
- FIX: Use pillar values to allow Zeek log ingestion selection from the UI `#10322 <https://github.com/Security-Onion-Solutions/securityonion/issues/10322>`_
- FIX: Zeek local policies are not being updated when changed in Current Grid value. `#10209 <https://github.com/Security-Onion-Solutions/securityonion/issues/10209>`_
- FIX: Zeek not ignoring lb_procs when Zeek pins configured `#10215 <https://github.com/Security-Onion-Solutions/securityonion/issues/10215>`_
- UPGRADE: Elastic 8.7.1 `#10269 <https://github.com/Security-Onion-Solutions/securityonion/issues/10269>`_
- UPGRADE: Kratos to 0.13.0 `#10309 <https://github.com/Security-Onion-Solutions/securityonion/issues/10309>`_
- UPGRADE: SOC external dependencies `#10268 <https://github.com/Security-Onion-Solutions/securityonion/issues/10268>`_
- UPGRADE: Suricata 6.0.12 `#10311 <https://github.com/Security-Onion-Solutions/securityonion/issues/10311>`_
- UPGRADE: Zeek 5.0.9 `#10374 <https://github.com/Security-Onion-Solutions/securityonion/issues/10374>`_

2.4.1 Beta 2 [20230424] Changes
-------------------------------

- FIX: Add Dedicated Fleet Node `#10054 <https://github.com/Security-Onion-Solutions/securityonion/issues/10054>`_
- FIX: Don't create curl.config on Forward Nodes `#10057 <https://github.com/Security-Onion-Solutions/securityonion/issues/10057>`_
- FIX: Force case attachments to be downloaded `#10186 <https://github.com/Security-Onion-Solutions/securityonion/issues/10186>`_
- FIX: Improve Elasticsearch index deletion - so-elastic-clear `#10109 <https://github.com/Security-Onion-Solutions/securityonion/issues/10109>`_
- FIX: Improve Elasticsearch index deletion - so-elastic-cluster-delete-delete `#10110 <https://github.com/Security-Onion-Solutions/securityonion/issues/10110>`_
- FIX: Make sure Setup image downloads populate the screen and the log `#10052 <https://github.com/Security-Onion-Solutions/securityonion/issues/10052>`_
- FIX: Overview Customization link `#10173 <https://github.com/Security-Onion-Solutions/securityonion/issues/10173>`_
- FIX: Prevent Jinja syntax from being entered into config values via UI/API `#10187 <https://github.com/Security-Onion-Solutions/securityonion/issues/10187>`_
- FIX: Prevent Zeek from using a large amount of memory `#10190 <https://github.com/Security-Onion-Solutions/securityonion/issues/10190>`_
- FIX: Remove legacy Kibana dashboards `#8555 <https://github.com/Security-Onion-Solutions/securityonion/issues/8555>`_
- FIX: Remove template load from search nodes in distrib `#10060 <https://github.com/Security-Onion-Solutions/securityonion/issues/10060>`_
- FIX: SOC only displaying data for users assigned the superuser role `#10068 <https://github.com/Security-Onion-Solutions/securityonion/issues/10068>`_
- FIX: Sort grid members lists `#10185 <https://github.com/Security-Onion-Solutions/securityonion/issues/10185>`_
- FIX: Suricata DNS A and CNAME parsing `#10117 <https://github.com/Security-Onion-Solutions/securityonion/issues/10117>`_
- FIX: Using SOC Configuration to change mdengine from ZEEK to SURICATA fails `#10189 <https://github.com/Security-Onion-Solutions/securityonion/issues/10189>`_
- FIX: Zeek @local and @local-sigs need to strip the @ for config but replace in local.zeek `#10050 <https://github.com/Security-Onion-Solutions/securityonion/issues/10050>`_
- FIX: Zeek is not honoring lbprocs `#10062 <https://github.com/Security-Onion-Solutions/securityonion/issues/10062>`_
- UPGRADE: Elastic 8.7.0 `#10059 <https://github.com/Security-Onion-Solutions/securityonion/issues/10059>`_
- UPGRADE: Suricata 6.0.11 `#10067 <https://github.com/Security-Onion-Solutions/securityonion/issues/10067>`_
- UPGRADE: Zeek 5.0.8 `#10107 <https://github.com/Security-Onion-Solutions/securityonion/issues/10107>`_


2.4.0 Beta 1 [20230328] Changes
-------------------------------

https://blog.securityonion.net/2023/03/security-onion-24-beta-release-now.html
