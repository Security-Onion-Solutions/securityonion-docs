.. _release-notes:

Release Notes
=============

Known Issues
~~~~~~~~~~~~

If you notice an Elasticsearch status of ``Pending`` in the Grid interface, you can view affected indices by running the following command from the CLI on the manager node:

::

  sudo so-elasticsearch-query _cat/shards | grep UN

The result of the query should display affected indices. Older metrics indices for Elastic Endpoint logs may have been assigned a replica, so if you are running a single-node Elastic cluster there will be nowhere for the replica to exist.

To resolve the issue, run the following command for each affected index (replacing ``$index`` with the actual index name):

::

  sudo so-elasticsearch-query $index/_settings -d '{"number_of_replicas":0}' -XPUT

After running the command, the index should no longer use replicas and the status should change from "Pending" to "OK" once all indices have been successfully modified. 

2.4.70 [20240528] Changes
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
