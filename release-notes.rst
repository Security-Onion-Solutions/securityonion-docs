.. _release-notes:

Release Notes
=============

2.4.2 Beta 3 [20230531] Changes
----------------------

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
- FIX: Review 2.4 file permissions and other local security changes `#9110 <https://github.com/Security-Onion-Solutions/securityonion/issues/9110>`_
- FIX: Prevent duplicate observables from being automatically created when attaching events to a case. `#10123 <https://github.com/Security-Onion-Solutions/securityonion/issues/10123>`_
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
