.. _release-notes:

Release Notes
=============

2.4.10 Hotfix [20230821] Changes
--------------------------------

FIX: Component templates not updated when packages are updated #11065 (https://github.com/Security-Onion-Solutions/securityonion/issues/11065)
FIX: Importing both PCAP and EVTX files fails #11030 (https://github.com/Security-Onion-Solutions/securityonion/issues/11030)
FIX: pipeline with id logs-system.syslog-1.6.4 does not exist #11038 (https://github.com/Security-Onion-Solutions/securityonion/issues/11038)

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
- FIX: Ensure operations on records with "*Missing" fields use correct search `#8025 <https://github.com/Security-Onion-Solutions/securityonion/issues/8025>`_
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
