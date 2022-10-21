.. _release-notes:

Release Notes
=============

2.3.181 [20221021] Changes
----------------

- FIX: Add find to the zeek docker container `#8922 <https://github.com/Security-Onion-Solutions/securityonion/issues/8922>`_
- FIX: Implement workaround for case events query `#8965 <https://github.com/Security-Onion-Solutions/securityonion/issues/8965>`_

2.3.180 [20221014] Changes
----------------

- FEATURE: Add Additional Zeek Plugins to the Zeek Docker Container `#8877 <https://github.com/Security-Onion-Solutions/securityonion/issues/8877>`_
- FEATURE: Add new Sysmon dashboards `#8870 <https://github.com/Security-Onion-Solutions/securityonion/issues/8870>`_
- UPGRADE: Elastic 8.4.3 `#8861 <https://github.com/Security-Onion-Solutions/securityonion/issues/8861>`_
- UPGRADE: Suricata 6.0.8 `#8820 <https://github.com/Security-Onion-Solutions/securityonion/issues/8820>`_
- UPGRADE: Zeek 5.0.2 `#8881 <https://github.com/Security-Onion-Solutions/securityonion/issues/8881>`_

2.3.170 [20220922] Changes
--------------------------

- FEATURE: Events table(s) for Windows Events matching default view `#8591 <https://github.com/Security-Onion-Solutions/securityonion/issues/8591>`_
- FEATURE: Split the winlog.event_data.Hashes field for Windows sysmon process creation events. `#8593 <https://github.com/Security-Onion-Solutions/securityonion/issues/8593>`_
- FIX: Mapping error when trying to index Strelka logs generated from ELF files. `#8592 <https://github.com/Security-Onion-Solutions/securityonion/issues/8592>`_
- UPGRADE: Elastic 8.4.1 `#8794 <https://github.com/Security-Onion-Solutions/securityonion/issues/8794>`_
- UPGRADE: Zeek 4.0.9 `#8774 <https://github.com/Security-Onion-Solutions/securityonion/issues/8774>`_

2.3.160 [20220829] Changes
--------------------------

- FEATURE: Add Advanced toggle to Alerts and Cases pages `#7559 <https://github.com/Security-Onion-Solutions/securityonion/issues/7559>`_
- FIX: Add gen_webshells.yar to Strelka ignore list `#8624 <https://github.com/Security-Onion-Solutions/securityonion/issues/8624>`_
- UPGRADE: Zeek 4.0.8 `#8610 <https://github.com/Security-Onion-Solutions/securityonion/issues/8610>`_

2.3.150 [20220820] Changes
--------------------------

- FIX: Allow Filebeat to be disabled for sensors, idh, and fleet nodes `#8404 <https://github.com/Security-Onion-Solutions/securityonion/issues/8404>`_
- FIX: Display PCAP menu action on Dashboards page `#8343 <https://github.com/Security-Onion-Solutions/securityonion/issues/8343>`_
- FIX: Elasticsearch geoip lookups fail for some users in Elastic 8 `#8373 <https://github.com/Security-Onion-Solutions/securityonion/issues/8373>`_
- FIX: Fix TLP options in Cases to align with TLP 2.0 `#8469 <https://github.com/Security-Onion-Solutions/securityonion/issues/8469>`_
- FIX: Remove Elastic Pipeline Time graph from Grafana `#8369 <https://github.com/Security-Onion-Solutions/securityonion/issues/8369>`_
- FIX: Update TALOS rules snapshot version to 29200 `#8551 <https://github.com/Security-Onion-Solutions/securityonion/issues/8551>`_
- FIX: Use systemd drop-in file for salt-minion.service override `#8441 <https://github.com/Security-Onion-Solutions/securityonion/issues/8441>`_
- FIX: soup should check for local configurations before modifying anything `#8423 <https://github.com/Security-Onion-Solutions/securityonion/issues/8423>`_
- FIX: soup should only delete elastalert indices when upgrading from Elastic versions older than 8 `#8536 <https://github.com/Security-Onion-Solutions/securityonion/issues/8536>`_
- UPGRADE: CyberChef 9.46.0 `#8299 <https://github.com/Security-Onion-Solutions/securityonion/issues/8299>`_
- UPGRADE: Elastic 8.3.3 `#8398 <https://github.com/Security-Onion-Solutions/securityonion/issues/8398>`_

2.3.140 Hotfix [20220812] Changes
---------------------------------

- FIX: so-curator-closed-delete-delete needs to reference new Elasticsearch directory `#8529 <https://github.com/Security-Onion-Solutions/securityonion/issues/8529>`_

2.3.140 Hotfix [20220719] Changes
---------------------------------

- FIX: Revise Elastalert index check/deletion logic
- FIX: Ensure Elastalert is enabled before trying to run 'so-elastalert-stop'. Also suppress error output for when so-elastalert container is missing.

2.3.140 Changes
----------------

- FEATURE: Provide ability to maximize view of a groupby chart or table `#8176 <https://github.com/Security-Onion-Solutions/securityonion/issues/8176>`_
- FEATURE: Remember the state of the left menu (visible or hidden) between SOC refreshes `#8186 <https://github.com/Security-Onion-Solutions/securityonion/issues/8186>`_
- FEATURE: Remove disabled accounts from Case Assignee list  `#8184 <https://github.com/Security-Onion-Solutions/securityonion/issues/8184>`_
- FEATURE: SOUP should not let you update to 2.3.140 or above unless you have updated to at least 2.3.110 `#8239 <https://github.com/Security-Onion-Solutions/securityonion/issues/8239>`_
- FEATURE: Support bulk observable data entry `#8210 <https://github.com/Security-Onion-Solutions/securityonion/issues/8210>`_
- FIX: Add ID to Filestream Inputs `#8006 <https://github.com/Security-Onion-Solutions/securityonion/issues/8006>`_
- FIX: Add event.category field to pfsense firewall logs `#8112 <https://github.com/Security-Onion-Solutions/securityonion/issues/8112>`_
- FIX: Add jinja to localfile.yaml `#8196 <https://github.com/Security-Onion-Solutions/securityonion/issues/8196>`_
- FIX: IDH ISO Disk partitions `#8144 <https://github.com/Security-Onion-Solutions/securityonion/issues/8144>`_
- FIX: Improve default dashboards `#8136 <https://github.com/Security-Onion-Solutions/securityonion/issues/8136>`_
- FIX: Strip whitespace after analyzer input strings (observable values) `#8208 <https://github.com/Security-Onion-Solutions/securityonion/issues/8208>`_
- FIX: Support group-by sorting memory on first group only `#8133 <https://github.com/Security-Onion-Solutions/securityonion/issues/8133>`_
- FIX: Using so-firewall to list default port groups `#8264 <https://github.com/Security-Onion-Solutions/securityonion/issues/8264>`_
- FIX: pam.d lastlog module breaks BPF capability `#8188 <https://github.com/Security-Onion-Solutions/securityonion/issues/8188>`_
- FIX: Ensure so-kibana indices can be cleaned up on search nodes `#8262 <https://github.com/Security-Onion-Solutions/securityonion/issues/8262>`_
- UPGRADE: Kratos to 0.10.1 `#8227 <https://github.com/Security-Onion-Solutions/securityonion/issues/8227>`_
- UPGRADE: Salt 3004.2 `#8166 <https://github.com/Security-Onion-Solutions/securityonion/issues/8166>`_
- UPGRADE: Suricata 6.0.6 `#8279 <https://github.com/Security-Onion-Solutions/securityonion/issues/8279>`_
- UPGRADE: Elastic 8.3.2 `#7563 <https://github.com/Security-Onion-Solutions/securityonion/issues/7563>`_
- UPGRADE: Redmine to 4.2.7 `#8308 <https://github.com/Security-Onion-Solutions/securityonion/issues/8308>`_

2.3.130 Changes
----------------

- FEATURE: Add "observable" button next to hash for case attachments `#7222 <https://github.com/Security-Onion-Solutions/securityonion/issues/7222>`_
- FEATURE: Add set of default analyzers `#7945 <https://github.com/Security-Onion-Solutions/securityonion/issues/7945>`_
- FEATURE: Make classification.config user-configurable `#7918 <https://github.com/Security-Onion-Solutions/securityonion/issues/7918>`_
- FEATURE: Native analyzer infrastructure `#7944 <https://github.com/Security-Onion-Solutions/securityonion/issues/7944>`_
- FEATURE: Playbook False Positive Tuning  `#8059 <https://github.com/Security-Onion-Solutions/securityonion/issues/8059>`_
- FEATURE: SOC Dashboards `#1211 <https://github.com/Security-Onion-Solutions/securityonion/issues/1211>`_
- FIX: Allow quick actions on a field value with the number 0 `#8023 <https://github.com/Security-Onion-Solutions/securityonion/issues/8023>`_
- FIX: Elastalert query in Hunt `#8049 <https://github.com/Security-Onion-Solutions/securityonion/issues/8049>`_
- FIX: Ensure failed elastic queries show an error on the SOC UI `#7846 <https://github.com/Security-Onion-Solutions/securityonion/issues/7846>`_
- FIX: Firefox OQL edits should release focus after pressing ENTER `#8063 <https://github.com/Security-Onion-Solutions/securityonion/issues/8063>`_
- UPGRADE: ElastAlert 2 from 2.2.2 to 2.5.0 `#8008 <https://github.com/Security-Onion-Solutions/securityonion/issues/8008>`_
- UPGRADE: Elastic 7.17.4 `#8002 <https://github.com/Security-Onion-Solutions/securityonion/issues/8002>`_
- UPGRADE: FleetDM 4.14.0 `#8012 <https://github.com/Security-Onion-Solutions/securityonion/issues/8012>`_
- UPGRADE: Kratos 0.8.2-alpha.1 to 0.9.0-alpha.3 `#7943 <https://github.com/Security-Onion-Solutions/securityonion/issues/7943>`_
- UPGRADE: TensorFlow from 2.5 to 2.9.1 `#8009 <https://github.com/Security-Onion-Solutions/securityonion/issues/8009>`_
- UPGRADE: attack-navigator v4.6.4 `#7977 <https://github.com/Security-Onion-Solutions/securityonion/issues/7977>`_
- UPGRADE: Zeek 4.0.6 to 4.0.7 `#8067 <https://github.com/Security-Onion-Solutions/securityonion/issues/8067>`_

2.3.120 Changes
----------------

- FEATURE: Add ISO option to the installer for analyst workstation `#7502 <https://github.com/Security-Onion-Solutions/securityonion/issues/7502>`_
- FEATURE: Add new Hunt query for SOC logins `#7327 <https://github.com/Security-Onion-Solutions/securityonion/issues/7327>`_
- FEATURE: Add strelka-fileshot and strelka-oneshot binaries to analyst workstation `#7670 <https://github.com/Security-Onion-Solutions/securityonion/issues/7670>`_
- FEATURE: Expose Case user info (email address) in SOC Alert/Hunt/Cases results instead of user ID `#7548 <https://github.com/Security-Onion-Solutions/securityonion/issues/7548>`_
- FEATURE: Have Observables inherit their case's TLP by default `#7642 <https://github.com/Security-Onion-Solutions/securityonion/issues/7642>`_
- FEATURE: IDH - Separate MGT & IDH NIC `#7589 <https://github.com/Security-Onion-Solutions/securityonion/issues/7589>`_
- FEATURE: Remove thehive and cortex dockers `#7501 <https://github.com/Security-Onion-Solutions/securityonion/issues/7501>`_
- FEATURE: Stop hive related services in soup to 120 `#7599 <https://github.com/Security-Onion-Solutions/securityonion/issues/7599>`_
- FIX: Create .keyword shim for additional process fields `#7633 <https://github.com/Security-Onion-Solutions/securityonion/issues/7633>`_
- FIX: Elasticsearch & Logstash logs not compressed or cleaned `#6932 <https://github.com/Security-Onion-Solutions/securityonion/issues/6932>`_
- FIX: Failure of influxdb state if default shell is zsh `#7730 <https://github.com/Security-Onion-Solutions/securityonion/issues/7730>`_
- FIX: Hunt OR queries should work without parentheses `#7540 <https://github.com/Security-Onion-Solutions/securityonion/issues/7540>`_
- FIX: Improve Hunt query when pivoting from Cases Observables `#7405 <https://github.com/Security-Onion-Solutions/securityonion/issues/7405>`_
- FIX: Improve Zeek file extraction `#7829 <https://github.com/Security-Onion-Solutions/securityonion/issues/7829>`_
- FIX: Management IP is sometimes null at the end of setup `#7113 <https://github.com/Security-Onion-Solutions/securityonion/issues/7113>`_
- FIX: Prevent multiple instances of so-sensor-clean and so-playbook-sync `#6622 <https://github.com/Security-Onion-Solutions/securityonion/issues/6622>`_
- FIX: Prevent users from running `so-setup iso` on Ubuntu `#7601 <https://github.com/Security-Onion-Solutions/securityonion/issues/7601>`_
- FIX: Remove TheHive deps from Playbook `#7483 <https://github.com/Security-Onion-Solutions/securityonion/issues/7483>`_
- FIX: Run telegraf as non-root `#7468 <https://github.com/Security-Onion-Solutions/securityonion/issues/7468>`_
- FIX: Salt error during setup - [ERROR   ] Unable to connect pusher: Stream is closed `#7203 <https://github.com/Security-Onion-Solutions/securityonion/issues/7203>`_
- FIX: Update syslog ingest pipeline per #5251 `#6912 <https://github.com/Security-Onion-Solutions/securityonion/issues/6912>`_
- FIX: remove soremote access after analyst install joins grid `#7639 <https://github.com/Security-Onion-Solutions/securityonion/issues/7639>`_
- FIX: soup should ensure salt-master service is running prior to running `#7763 <https://github.com/Security-Onion-Solutions/securityonion/issues/7763>`_
- FIX: surilogcompress not working correctly on some systems `#7133 <https://github.com/Security-Onion-Solutions/securityonion/issues/7133>`_
- UPGRADE: CyberChef 9.37.3 `#7817 <https://github.com/Security-Onion-Solutions/securityonion/issues/7817>`_
- UPGRADE: Elastic 7.17.3 `#7807 <https://github.com/Security-Onion-Solutions/securityonion/issues/7807>`_
- UPGRADE: FleetDM 4.12.1  `#7725 <https://github.com/Security-Onion-Solutions/securityonion/issues/7725>`_
- UPGRADE: Suricata 6.0.5 `#7836 <https://github.com/Security-Onion-Solutions/securityonion/issues/7836>`_
- UPGRADE: Zeek 4.0.6 `#7839 <https://github.com/Security-Onion-Solutions/securityonion/issues/7839>`_
- UPGRADE: nginx 1.20.2 `#7808 <https://github.com/Security-Onion-Solutions/securityonion/issues/7808>`_

2.3.110 Hotfix [20220407] Changes
---------------------------------

- FIX: Previously failed Ubuntu minions will now be able to get the proper repo for install
- FIX: Fixed a regression in AIRGAP that was preventing salt from upgrading

2.3.110 Hotfix [20220407] Known Issues
--------------------------------------

- If you had a previous failed soup please ensure that the salt-master service is running before you run soup again.

2.3.110 Hotfix [20220405] Changes
---------------------------------

- FIX: Change the salt bootstrap script to pull from the proper location for Ubuntu

2.3.110 Hotfix [20220401] Changes
---------------------------------

- FIX: Updated Saltstack to 3004.1 to address CVE-2022-22934 `#7701 <https://github.com/Security-Onion-Solutions/securityonion/issues/7701>`_

2.3.110 Changes
----------------

- FEATURE: Full ECS data type compliance `#6747 <https://github.com/Security-Onion-Solutions/securityonion/issues/6747>`_
- FEATURE: Intrusion Detection Honeypot Node `#7138 <https://github.com/Security-Onion-Solutions/securityonion/issues/7138>`_
- FEATURE: Multi-Factor Authentication (MFA) for Security Onion `#7316 <https://github.com/Security-Onion-Solutions/securityonion/issues/7316>`_
- FEATURE: Populate Zeek's networks.cfg with $HOME_NET `#6854 <https://github.com/Security-Onion-Solutions/securityonion/issues/6854>`_
- FEATURE: SOC authentication logs will now be ingested into Elasticsearch `#7354 <https://github.com/Security-Onion-Solutions/securityonion/issues/7354>`_
- FEATURE: sort indices list alphabetically by index name `#6969 <https://github.com/Security-Onion-Solutions/securityonion/issues/6969>`_
- FIX: ACNG should clear the cache on restart `#7114 <https://github.com/Security-Onion-Solutions/securityonion/issues/7114>`_
- FIX: Abort so-user sync if Kratos database is locked `#7459 <https://github.com/Security-Onion-Solutions/securityonion/issues/7459>`_
- FIX: Add Endgame Index settings to the global.sls on new installs `#7293 <https://github.com/Security-Onion-Solutions/securityonion/issues/7293>`_
- FIX: Allow downgrades during docker_install `#7228 <https://github.com/Security-Onion-Solutions/securityonion/issues/7228>`_
- FIX: Avoid telegraf apparmor issues `#2560 <https://github.com/Security-Onion-Solutions/securityonion/issues/2560>`_
- FIX: Composable Templates `#4644 <https://github.com/Security-Onion-Solutions/securityonion/issues/4644>`_
- FIX: Increase minimum password length from 6 to 8 characters `#7352 <https://github.com/Security-Onion-Solutions/securityonion/issues/7352>`_
- FIX: Navigator should ship with all needed files `#1162 <https://github.com/Security-Onion-Solutions/securityonion/issues/1162>`_
- FIX: Prevent Elasticsearch deprecation notices from causing installation failures `#7353 <https://github.com/Security-Onion-Solutions/securityonion/issues/7353>`_
- FIX: Random passwords generated at setup contain character combinations that cause problems with some containers `#7233 <https://github.com/Security-Onion-Solutions/securityonion/issues/7233>`_
- FIX: curator should exclude so-case* indices `#7270 <https://github.com/Security-Onion-Solutions/securityonion/issues/7270>`_
- FIX: so-ip-update needs to update Kibana dashboards `#7237 <https://github.com/Security-Onion-Solutions/securityonion/issues/7237>`_
- FIX: so-status TTY improvements `#7355 <https://github.com/Security-Onion-Solutions/securityonion/issues/7355>`_
- UPGRADE: Elastic 7.17.1 `#7137 <https://github.com/Security-Onion-Solutions/securityonion/issues/7137>`_
- UPGRADE: FleetDM to 4.10.0 `#7245 <https://github.com/Security-Onion-Solutions/securityonion/issues/7245>`_
- UPGRADE: Grafana 8.4.1 `#7281 <https://github.com/Security-Onion-Solutions/securityonion/issues/7281>`_
- UPGRADE: Kratos 0.8.2-alpha.1 `#7351 <https://github.com/Security-Onion-Solutions/securityonion/issues/7351>`_

2.3.100 Hotfix [20220301] Changes
---------------------------------

- FIX: Prevent curator from pruning case indices `#7270 <https://github.com/Security-Onion-Solutions/securityonion/issues/7270>`_

2.3.100 Hotfix [20220203] Changes
---------------------------------

- FIX: SSLError for Logstash connecting to Redis if manager hostname contains uppercase `#7103 <https://github.com/Security-Onion-Solutions/securityonion/issues/7103>`_
- FIX: Add mixed case hostnames to automated testing

2.3.100 Hotfix [20220202] Changes
---------------------------------

- FIX: Add new salt URL to the ACNG config for SSL passthrough
- FIX: Managers with capitals in the hostname will now properly pull from the salt mine `#7081 <https://github.com/Security-Onion-Solutions/securityonion/issues/7081>`_

2.3.100 Changes
----------------

- FEATURE: Add verbiage to soup to denote which branch is being used `#6763 <https://github.com/Security-Onion-Solutions/securityonion/issues/6763>`_
- FEATURE: Allow for an easy way to add a local repo directory for Elastic snapshots `#7034 <https://github.com/Security-Onion-Solutions/securityonion/issues/7034>`_
- FEATURE: Install Elasticsearch plugin - repository-s3 `#6139 <https://github.com/Security-Onion-Solutions/securityonion/issues/6139>`_
- FEATURE: Introduce new Cases module for native case management `#7019 <https://github.com/Security-Onion-Solutions/securityonion/issues/7019>`_
- FEATURE: Introduce new Receiver node type `#6469 <https://github.com/Security-Onion-Solutions/securityonion/issues/6469>`_
- FEATURE: Open event from Kibana in hunt `#6748 <https://github.com/Security-Onion-Solutions/securityonion/issues/6748>`_
- FEATURE: SOC error messages should show regardless of how far down the user has scrolled `#6977 <https://github.com/Security-Onion-Solutions/securityonion/issues/6977>`_
- FEATURE: Support sort order in Elasticsearch queries `#2577 <https://github.com/Security-Onion-Solutions/securityonion/issues/2577>`_
- FIX: Reinstall on Ubuntu 18.04 fails on docker install `#6467 <https://github.com/Security-Onion-Solutions/securityonion/issues/6467>`_
- FIX: Cleanup Invalid Kolide messages in nginx logs `#3989 <https://github.com/Security-Onion-Solutions/securityonion/issues/3989>`_
- FIX: Disable Wazuh on sensors if it is disabled globally `#7016 <https://github.com/Security-Onion-Solutions/securityonion/issues/7016>`_
- FIX: During a reinstall, remove existing certs and keys generated by the ssl and ca states `#7010 <https://github.com/Security-Onion-Solutions/securityonion/issues/7010>`_
- FIX: Enable SANs for all certificates `#6381 <https://github.com/Security-Onion-Solutions/securityonion/issues/6381>`_
- FIX: Fleet broken when default Docker IP range changed `#6603 <https://github.com/Security-Onion-Solutions/securityonion/issues/6603>`_
- FIX: Generate .security subfield for `message` field `#5106 <https://github.com/Security-Onion-Solutions/securityonion/issues/5106>`_
- FIX: Improve support for grouping by fields with spaces `#6724 <https://github.com/Security-Onion-Solutions/securityonion/issues/6724>`_
- FIX: Logstash inputs beats deprication `#5194 <https://github.com/Security-Onion-Solutions/securityonion/issues/5194>`_
- FIX: Playbook Field Mappings `#3660 <https://github.com/Security-Onion-Solutions/securityonion/issues/3660>`_
- FIX: Prevent the .security keyword from being added to the rule.uuid field in Playbook   `#6276 <https://github.com/Security-Onion-Solutions/securityonion/issues/6276>`_
- FIX: Reduce excessive Elasticsearch log growth `#5190 <https://github.com/Security-Onion-Solutions/securityonion/issues/5190>`_
- FIX: Reinstall should not try to patch python3-influxdb modules if already patched. `#6765 <https://github.com/Security-Onion-Solutions/securityonion/issues/6765>`_
- FIX: Remove manager from /etc/hosts during install prompts `#6492 <https://github.com/Security-Onion-Solutions/securityonion/issues/6492>`_
- FIX: Remove xml header from ossec.conf `#6658 <https://github.com/Security-Onion-Solutions/securityonion/issues/6658>`_
- FIX: SOUP should check that en_US.UTF-8 is available before switching to it `#6599 <https://github.com/Security-Onion-Solutions/securityonion/issues/6599>`_
- FIX: Salt does not generate a fleet.crt file with CUSTOM_FLEET_HOSTNAME `#4319 <https://github.com/Security-Onion-Solutions/securityonion/issues/4319>`_
- FIX: Typo in so-image-common output `#6563 <https://github.com/Security-Onion-Solutions/securityonion/issues/6563>`_
- FIX: Wazuh WEL Parsing `#6829 <https://github.com/Security-Onion-Solutions/securityonion/issues/6829>`_
- FIX: _id fielddata deprecated message `#6703 <https://github.com/Security-Onion-Solutions/securityonion/issues/6703>`_
- FIX: elastic_curl_config depends on elastic_curl_config_distributed `#6811 <https://github.com/Security-Onion-Solutions/securityonion/issues/6811>`_
- FIX: prevent the need for adding roles in a specific order when using so-user `#6505 <https://github.com/Security-Onion-Solutions/securityonion/issues/6505>`_
- FIX: so-preflight tries to run curl before it is installed `#6899 <https://github.com/Security-Onion-Solutions/securityonion/issues/6899>`_
- FIX: so-user update should automatically sync `#6659 <https://github.com/Security-Onion-Solutions/securityonion/issues/6659>`_
- UPGRADE: CyberChef 9.32.3 `#6434 <https://github.com/Security-Onion-Solutions/securityonion/issues/6434>`_
- UPGRADE: Elastic components to 7.16.3 `#6860 <https://github.com/Security-Onion-Solutions/securityonion/issues/6860>`_
- UPGRADE: FleetDM 4.8.0 `#6828 <https://github.com/Security-Onion-Solutions/securityonion/issues/6828>`_
- UPGRADE: Grafana 8.3.2 `#6321 <https://github.com/Security-Onion-Solutions/securityonion/issues/6321>`_
- UPGRADE: Salt to 3004 `#6810 <https://github.com/Security-Onion-Solutions/securityonion/issues/6810>`_
- UPGRADE: Zeek to 4.0.5 `#6983 <https://github.com/Security-Onion-Solutions/securityonion/issues/6983>`_

2.3.91 Changes
--------------

- UPGRADE: Elastic to 7.16.2 for log4j vulnerability mitigation

2.3.90 Hotfix [20211213]
------------------------

- FIX: Remove JndiLookup class from Elasticsearch and Logstash jar files to address additional log4j attack vectors

2.3.90 Hotfix [20211210]
------------------------

- FIX: Mitigate vulnerability in log4j

2.3.90 Hotfix [20211206]
------------------------

- FIX: soup should now properly update 2.3.90 installs that had an issue with xml headers in the ossec.conf
- FIX: soup now has more logging
- FIX: soup now checks for the existence of the endgame group before trying to apply it on a re-soup
- FIX: so-elasticsearch-pipelines now uses the proper value for applying the pipelines

2.3.90 Hotfix [AIRGAPFIX]
-------------------------

- FIX: Airgap repo was created on distributed iso nodes even in non-airgap installs `#6415 <https://github.com/Security-Onion-Solutions/securityonion/issues/6415>`_

2.3.90 Hotfix [WAZUH]
---------------------

- FIX: so-allow should not be modifying ossec.conf when Wazuh isn’t installed `#6317 <https://github.com/Security-Onion-Solutions/securityonion/issues/6317>`_
- FIX: so-allow should not be writing an XML header to the ossec.conf file `#6325 <https://github.com/Security-Onion-Solutions/securityonion/issues/6325>`_
- FIX: Correct "exisiting" typo on whiptail prompt
- FIX: Soup will no longer attempt to validate a successful salt upgrade if salt wasn’t upgraded on this soup run


2.3.90 Changes
----------------

- FEATURE: Add ASN annotation for GeoIP `#5068 <https://github.com/Security-Onion-Solutions/securityonion/issues/5068>`_
- FEATURE: Add Endgame Support for Security Onion `#6166 <https://github.com/Security-Onion-Solutions/securityonion/issues/6166>`_
- FEATURE: Add TI Module `#5916 <https://github.com/Security-Onion-Solutions/securityonion/issues/5916>`_
- FEATURE: Add additional flags to stenographer config `#5851 <https://github.com/Security-Onion-Solutions/securityonion/issues/5851>`_
- FEATURE: Add filebeat, auditbeat, and metricbeat downloads to SOC Download screen `#5849 <https://github.com/Security-Onion-Solutions/securityonion/issues/5849>`_
- FEATURE: Add logstash and redis input plugins to telegraf `#5960 <https://github.com/Security-Onion-Solutions/securityonion/issues/5960>`_
- FEATURE: Add so-deny script for removing access from firewall and other apps `#4621 <https://github.com/Security-Onion-Solutions/securityonion/issues/4621>`_
- FEATURE: Add support for escalation to Elastic Cases `#6048 <https://github.com/Security-Onion-Solutions/securityonion/issues/6048>`_
- FEATURE: Allow for Kibana customizations via pillar `#3933 <https://github.com/Security-Onion-Solutions/securityonion/issues/3933>`_
- FEATURE: Allow users to set their profile information `#5846 <https://github.com/Security-Onion-Solutions/securityonion/issues/5846>`_
- FEATURE: Allow vlan tagged NICs to be used as management interface `#3687 <https://github.com/Security-Onion-Solutions/securityonion/issues/3687>`_
- FEATURE: Create Pipeline Overview Dashboard for Grafana `#6177 <https://github.com/Security-Onion-Solutions/securityonion/issues/6177>`_
- FEATURE: Create script to reset elastic auth passwords `#6206 <https://github.com/Security-Onion-Solutions/securityonion/issues/6206>`_
- FEATURE: Enable Kibana Settings for encryption  `#6146 <https://github.com/Security-Onion-Solutions/securityonion/issues/6146>`_
- FEATURE: Expose new user profile field for specifying a custom note about a user `#5847 <https://github.com/Security-Onion-Solutions/securityonion/issues/5847>`_
- FEATURE: HTTP module for SOC event escalation `#5791 <https://github.com/Security-Onion-Solutions/securityonion/issues/5791>`_
- FEATURE: Increase password lengths, provide a way to change existing passwords `#6043 <https://github.com/Security-Onion-Solutions/securityonion/issues/6043>`_
- FEATURE: Indicate that setup has completed at the very end of sosetup.log `#5032 <https://github.com/Security-Onion-Solutions/securityonion/issues/5032>`_
- FEATURE: Prevent SOUP from running if there is an issue with the manager pillar `#5809 <https://github.com/Security-Onion-Solutions/securityonion/issues/5809>`_
- FEATURE: Provide quick-select date ranges from Hunt/Alerts date range picker `#5953 <https://github.com/Security-Onion-Solutions/securityonion/issues/5953>`_
- FEATURE: SOC Hunt Timeline/Charts should be collapsible `#5114 <https://github.com/Security-Onion-Solutions/securityonion/issues/5114>`_
- FEATURE: Support Ubuntu 20.04 `#601 <https://github.com/Security-Onion-Solutions/securityonion/issues/601>`_
- FEATURE: setup should run so-preflight `#3497 <https://github.com/Security-Onion-Solutions/securityonion/issues/3497>`_
- FIX: ACNG sometimes returns 503 errors when updating Ubuntu through the manager `#6151 <https://github.com/Security-Onion-Solutions/securityonion/issues/6151>`_
- FIX: Add details to Setup for Install Type menus `#6105 <https://github.com/Security-Onion-Solutions/securityonion/issues/6105>`_
- FIX: Adjust timeout in check_salt_minion_status in so-functions `#5818 <https://github.com/Security-Onion-Solutions/securityonion/issues/5818>`_
- FIX: All templates should honor replica settings `#6005 <https://github.com/Security-Onion-Solutions/securityonion/issues/6005>`_
- FIX: Clear holds on Ubuntu installs `#5588 <https://github.com/Security-Onion-Solutions/securityonion/issues/5588>`_
- FIX: Consider making the airgap option only settable on the manager `#5914 <https://github.com/Security-Onion-Solutions/securityonion/issues/5914>`_
- FIX: Docker containers should not start unless file events are completed `#5955 <https://github.com/Security-Onion-Solutions/securityonion/issues/5955>`_
- FIX: Ensure soc_users_roles file is cleaned up if incorrectly mounted by Docker `#5952 <https://github.com/Security-Onion-Solutions/securityonion/issues/5952>`_
- FIX: Favor non-aggregatable data type when a cache field has multiple conflicting data types `#5962 <https://github.com/Security-Onion-Solutions/securityonion/issues/5962>`_
- FIX: Firefox tooltips stuck on Hunt and Alerts screens `#6010 <https://github.com/Security-Onion-Solutions/securityonion/issues/6010>`_
- FIX: Grafana sensor graphs only show interface graphs when selected individually `#6007 <https://github.com/Security-Onion-Solutions/securityonion/issues/6007>`_
- FIX: Kibana saved objects `#5193 <https://github.com/Security-Onion-Solutions/securityonion/issues/5193>`_
- FIX: Modify Steno packet loss calculation to show point in time packet loss `#6060 <https://github.com/Security-Onion-Solutions/securityonion/issues/6060>`_
- FIX: Remove CURCLOSEDAYS prompt in Setup since it is no longer used `#6084 <https://github.com/Security-Onion-Solutions/securityonion/issues/6084>`_
- FIX: Remove references to xenial (Ubuntu 16.04) from setup `#4292 <https://github.com/Security-Onion-Solutions/securityonion/issues/4292>`_
- FIX: Remove unnecessary screens from Analyst Setup `#5615 <https://github.com/Security-Onion-Solutions/securityonion/issues/5615>`_
- FIX: SOC docker should not start until file managed state runs `#5954 <https://github.com/Security-Onion-Solutions/securityonion/issues/5954>`_
- FIX: SOC unable to acknowledge alerts when not grouped by rule.name `#5221 <https://github.com/Security-Onion-Solutions/securityonion/issues/5221>`_
- FIX: Setup should ask if new or existing distributed deployment `#6115 <https://github.com/Security-Onion-Solutions/securityonion/issues/6115>`_
- FIX: Setup should prevent invalid characters in Node Description field `#5937 <https://github.com/Security-Onion-Solutions/securityonion/issues/5937>`_
- FIX: Support non-WEL Beats `#6063 <https://github.com/Security-Onion-Solutions/securityonion/issues/6063>`_
- FIX: Unnecessary Port Binding for so-steno `#5981 <https://github.com/Security-Onion-Solutions/securityonion/issues/5981>`_
- FIX: Use yaml.safe_load() in so-firewall (thanks to @clairmont32) `#5750 <https://github.com/Security-Onion-Solutions/securityonion/issues/5750>`_
- FIX: Zeek state max depth not working `#5558 <https://github.com/Security-Onion-Solutions/securityonion/issues/5558>`_
- FIX: `so-ip-update` should grant mysql root user access on new IP `#4811 <https://github.com/Security-Onion-Solutions/securityonion/issues/4811>`_
- FIX: docker group can be given gid used by salt created groups `#6071 <https://github.com/Security-Onion-Solutions/securityonion/issues/6071>`_
- FIX: packetloss.sh gives an error every 10 min though ZEEK is disabled `#5759 <https://github.com/Security-Onion-Solutions/securityonion/issues/5759>`_
- FIX: so-import-evtx elastic creds & logging `#6065 <https://github.com/Security-Onion-Solutions/securityonion/issues/6065>`_
- FIX: so-user delete function causes re-migration of user roles `#5897 <https://github.com/Security-Onion-Solutions/securityonion/issues/5897>`_
- FIX: wazuh-register-agent times out after 15 minutes lower to 5 minutes `#5794 <https://github.com/Security-Onion-Solutions/securityonion/issues/5794>`_
- FIX: yum pkg.clean_metadata occasionally fails during setup `#6113 <https://github.com/Security-Onion-Solutions/securityonion/issues/6113>`_
- UPGRADE: ElastAlert to 2.2.2 `#5751 <https://github.com/Security-Onion-Solutions/securityonion/issues/5751>`_
- UPGRADE: Elastic to 7.15.2 `#5752 <https://github.com/Security-Onion-Solutions/securityonion/issues/5752>`_
- UPGRADE: FleetDM to 4.5 `#6188 <https://github.com/Security-Onion-Solutions/securityonion/issues/6188>`_
- UPGRADE: Grafana to 8.2.3 `#5852 <https://github.com/Security-Onion-Solutions/securityonion/issues/5852>`_
- UPGRADE: Kratos to 0.7.6-alpha.1 `#5848 <https://github.com/Security-Onion-Solutions/securityonion/issues/5848>`_
- UPGRADE: Redis to 6.2.6 `#6140 <https://github.com/Security-Onion-Solutions/securityonion/issues/6140>`_
- UPGRADE: Suricata to 6.0.4 `#6274 <https://github.com/Security-Onion-Solutions/securityonion/issues/6274>`_
- UPGRADE: Telegraf to 1.20.3 `#6075 <https://github.com/Security-Onion-Solutions/securityonion/issues/6075>`_


2.3.80 Changes
----------------

- FEATURE: Ability to disable Zeek, Suricata `#4429 <https://github.com/Security-Onion-Solutions/securityonion/issues/4429>`_
- FEATURE: Add docs link to Setup `#5459 <https://github.com/Security-Onion-Solutions/securityonion/issues/5459>`_
- FEATURE: Add evtx support in Import Node `#2206 <https://github.com/Security-Onion-Solutions/securityonion/issues/2206>`_
- FEATURE: Consolidate whiptail screens when selecting optional components `#5456 <https://github.com/Security-Onion-Solutions/securityonion/issues/5456>`_
- FEATURE: Distinguish between Zeek generated syslog and normal syslog in hunt for event fields `#5403 <https://github.com/Security-Onion-Solutions/securityonion/issues/5403>`_
- FEATURE: Enable index sorting to increase search speed `#5287 <https://github.com/Security-Onion-Solutions/securityonion/issues/5287>`_
- FEATURE: Expose options for elasticsearch.yml via Salt pillar `#1257 <https://github.com/Security-Onion-Solutions/securityonion/issues/1257>`_
- FEATURE: Role-based access control (RBAC) `#5614 <https://github.com/Security-Onion-Solutions/securityonion/issues/5614>`_
- FEATURE: soup -y for automation `#5043 <https://github.com/Security-Onion-Solutions/securityonion/issues/5043>`_
- FIX: Add new default filebeat module indices to the global pillar. `#5526 <https://github.com/Security-Onion-Solutions/securityonion/issues/5526>`_
- FIX: all.rules file can become empty on non-airgap deployments if manager does not have access to the internet. `#3619 <https://github.com/Security-Onion-Solutions/securityonion/issues/3619>`_
- FIX: Curator cron should run less often `#5189 <https://github.com/Security-Onion-Solutions/securityonion/issues/5189>`_
- FIX: Improve unit test maintainability by refactoring to use Golang assertion library  `#5604 <https://github.com/Security-Onion-Solutions/securityonion/issues/5604>`_
- FIX: Invalid password message should also mention dollar signs are not allowed `#5381 <https://github.com/Security-Onion-Solutions/securityonion/issues/5381>`_
- FIX: Max files for steno should use a pillar value for easy tuning. `#5393 <https://github.com/Security-Onion-Solutions/securityonion/issues/5393>`_
- FIX: Remove raid check for official cloud appliances `#5449 <https://github.com/Security-Onion-Solutions/securityonion/issues/5449>`_
- FIX: Remove watermark settings from global pillar. `#5520 <https://github.com/Security-Onion-Solutions/securityonion/issues/5520>`_
- FIX: SOC Username case sensitivity `#5154 <https://github.com/Security-Onion-Solutions/securityonion/issues/5154>`_
- FIX: so-user tool should validate password before adding user to SOC `#5606 <https://github.com/Security-Onion-Solutions/securityonion/issues/5606>`_
- FIX: Switch to new Curator auth params `#5273 <https://github.com/Security-Onion-Solutions/securityonion/pull/5273>`_
- UPGRADE: Curator to 5.8.4 `#5272 <https://github.com/Security-Onion-Solutions/securityonion/issues/5272>`_
- UPGRADE: CyberChef to 9.32.2 `#5158 <https://github.com/Security-Onion-Solutions/securityonion/issues/5158>`_
- UPGRADE: SOC UI 3rd Party dependencies to latest versions `#5603 <https://github.com/Security-Onion-Solutions/securityonion/issues/5603>`_
- UPGRADE: Zeek to 4.0.4 `#5630 <https://github.com/Security-Onion-Solutions/securityonion/issues/5630>`_


2.3.70 Hotfix [WAZUH]
----------------------

- FIX: wazuh-agent is updated during setup on ISO, which causes service to fail to start `#5354 <https://github.com/Security-Onion-Solutions/securityonion/issues/5354>`_

2.3.70 Hotfix [GRAFANA_DASH_ALLOW]
----------------------------------

- FIX: Grafana state trying to create undefined dashboards `#5270 <https://github.com/Security-Onion-Solutions/securityonion/pull/5270>`_

2.3.70 Hotfix [CURATOR]
-----------------------

- FIX: Rolled back curator change for true clustering deployments (will be fixed in next release) `#5226 <https://github.com/Security-Onion-Solutions/securityonion/issues/5226>`_
- FIX: Resolved benign error repeatedly logged to telegraf log file `#5195 <https://github.com/Security-Onion-Solutions/securityonion/issues/5195>`_

2.3.70 Changes
--------------

- FEATURE: Add sha.256 to suricata.fileinfo pipeline `#4224 <https://github.com/Security-Onion-Solutions/securityonion/issues/4224>`_
- FEATURE: Allow for adjustment of Kibana sampleSize setting in Discover dashboard `#4969 <https://github.com/Security-Onion-Solutions/securityonion/issues/4969>`_
- FEATURE: Allow for adjustment to automatic patch schedule `#4985 <https://github.com/Security-Onion-Solutions/securityonion/issues/4985>`_
- FEATURE: Require SOC login before allowing users to access playbook and soctopus `#4623 <https://github.com/Security-Onion-Solutions/securityonion/issues/4623>`_
- FEATURE: Scan kratos logs for anomalous login attempts `#4710 <https://github.com/Security-Onion-Solutions/securityonion/issues/4710>`_
- FEATURE: Send PCAP session transcript to CyberChef `#5010 <https://github.com/Security-Onion-Solutions/securityonion/issues/5010>`_
- FEATURE: Show model numbers of cloud-deployed nodes `#4898 <https://github.com/Security-Onion-Solutions/securityonion/issues/4898>`_
- FEATURE: Show warning when a user attempts to use a hostname or web domain entry that is not all lowercase `#4791 <https://github.com/Security-Onion-Solutions/securityonion/issues/4791>`_
- FEATURE: Simplify Grafana dashboard management and redesign dashboards `#4674 <https://github.com/Security-Onion-Solutions/securityonion/issues/4674>`_
- FEATURE: so-firewall needs an option to run apply by itself `#4765 <https://github.com/Security-Onion-Solutions/securityonion/issues/4765>`_
- FEATURE: so-pcap-export `#4210 <https://github.com/Security-Onion-Solutions/securityonion/issues/4210>`_
- FEATURE: SOUP - Prompt user when local modifications are detected  `#3860 <https://github.com/Security-Onion-Solutions/securityonion/issues/3860>`_
- FIX: Add mapping to extracted file directory `#4622 <https://github.com/Security-Onion-Solutions/securityonion/issues/4622>`_
- FIX: Clarify missing appliance images message on SOC grid `#5118 <https://github.com/Security-Onion-Solutions/securityonion/issues/5118>`_
- FIX: Curator should only run on manager when set to use true clustering. `#2806 <https://github.com/Security-Onion-Solutions/securityonion/issues/2806>`_
- FIX: Disabled user still shows as active in GUI `#5055 <https://github.com/Security-Onion-Solutions/securityonion/issues/5055>`_
- FIX: Disallow blank passwords during ISO first stage setup (kickstart) `#4947 <https://github.com/Security-Onion-Solutions/securityonion/issues/4947>`_
- FIX: Disallow ctrl-c during the first stage of ISO setup `#4948 <https://github.com/Security-Onion-Solutions/securityonion/issues/4948>`_
- FIX: Improve raid failure detection on SOS Appliances `#5064 <https://github.com/Security-Onion-Solutions/securityonion/issues/5064>`_
- FIX: Improve verbiage for initial IPv4 prompt and so-allow prompt `#5138 <https://github.com/Security-Onion-Solutions/securityonion/issues/5138>`_
- FIX: Jinja the stream.reassembly.depth value in the Suricata defaults.yaml file `#4293 <https://github.com/Security-Onion-Solutions/securityonion/issues/4293>`_
- FIX: Remove so-elastic-features. `#4542 <https://github.com/Security-Onion-Solutions/securityonion/issues/4542>`_
- FIX: SOC login page missing the hide/show password icons `#5087 <https://github.com/Security-Onion-Solutions/securityonion/issues/5087>`_
- FIX: Wazuh data ingest error: data.port `#3988 <https://github.com/Security-Onion-Solutions/securityonion/issues/3988>`_

2.3.61 Hotfix [STENO, MSEARCH]
------------------------------

- FIX: Some browsers refuse to load SOC UI due to CSP blocking wss: protocol `#4938 <https://github.com/Security-Onion-Solutions/securityonion/issues/4938>`_
- FIX: Disabling steno raises errors when applying state.highstate / running soup update `#4922 <https://github.com/Security-Onion-Solutions/securityonion/issues/4922>`_
- FIX: Manager Search does not come up properly with true clustering enabled `#4971 <https://github.com/Security-Onion-Solutions/securityonion/issues/4971>`_

2.3.61 Changes
--------------

- FIX: Airgap link to Release Notes `#4685 <https://github.com/Security-Onion-Solutions/securityonion/issues/4685>`_
- FIX: CyberChef unable to load due to recent Content Security Policy restrictions `#4885 <https://github.com/Security-Onion-Solutions/securityonion/issues/4885>`_
- FIX: Suricata dns.response.code needs to be renamed to dns.response.code_name `#4770 <https://github.com/Security-Onion-Solutions/securityonion/issues/4770>`_
- UPGRADE: alpine 3.12.1 to latest for Fleet image `#4823 <https://github.com/Security-Onion-Solutions/securityonion/issues/4823>`_
- UPGRADE: Elastic 7.13.4 `#4730 <https://github.com/Security-Onion-Solutions/securityonion/issues/4730>`_
- UPGRADE: Zeek 4.0.3 `#4716 <https://github.com/Security-Onion-Solutions/securityonion/issues/4716>`_

2.3.60 Hotfix [ECSFIX, HEAVYNODE, FBPIPELINE, CURATORAUTH] Changes
------------------------------------------------------------------
- FIX: Curator's authentication to Elasticsearch was incorrectly configured for the version currently in use.
- FIX: Some logs from Filebeat were not being properly routed to the correct pipeline causing the log to fill up the disk.
- FEATURE: All hotfixes going forward will have an ISO so that airgap users can follow the standard soup process as they would for normal releases.
- FIX: Hotfix to revert Strelka and Wazuh Elastic Common Schema (ECS) changes that weren't intended for 2.3.60.
- FIX: Correct SSL certificate common name (CN) to match heavy node hostnames. Only applicable to grids with heavy nodes. May require manual restart of Redis, Elasticsearch, Filebeat, and Logstash containers (in that order), once the heavy nodes have succeeded in applying highstate. For more information see the related blog post at https://blog.securityonion.net/2021/07/security-onion-2360-heavy-node-hotfix.html

2.3.60 Changes
--------------

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
--------------

- FIX: packetloss.sh can cause Zeek to segfault `#4398 <https://github.com/Security-Onion-Solutions/securityonion/issues/4398>`_
- FIX: soup now generates repo tarball with correct folder structure `#4368 <https://github.com/Security-Onion-Solutions/securityonion/issues/4368>`_
- UPGRADE: Zeek 4.0.2 `#4395 <https://github.com/Security-Onion-Solutions/securityonion/issues/4395>`_

2.3.51 Changes
--------------

- FIX: Mixed case sensor hostnames lead to incomplete PCAP jobs `#4220 <https://github.com/Security-Onion-Solutions/securityonion/issues/4220>`_
- FIX: Reconcile InfluxDB/Grafana containers in certain setup modes `#4207 <https://github.com/Security-Onion-Solutions/securityonion/issues/4207>`_
- FIX: Turn down log level for Salt States and Zeek `#4231 <https://github.com/Security-Onion-Solutions/securityonion/issues/4231>`_
- FIX: Correct downloaded PCAP filename `#4234 <https://github.com/Security-Onion-Solutions/securityonion/issues/4234>`_
- FIX: Truncate /root/wait_for_web_response.log before each wait invocation `#4247 <https://github.com/Security-Onion-Solutions/securityonion/issues/4247>`_

2.3.50 Changes
--------------

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
--------------

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
--------------

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
--------------

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
