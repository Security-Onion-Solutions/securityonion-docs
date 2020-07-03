Release Notes
=============

Changes:

 - Complete overhaul of the way we handle custom and default settings and data. You will now see a default and local directory under the saltstack directory. All customizations are stored in local.
- The way firewall rules are handled has been completely revamped. This will allow the user to customize firewall rules much easier.
- Users can now change their own password in SOC.
- Hunt now allows users to enable auto-hunt. This is a toggle which, when enabled, automatically submits a new hunt when filtering, grouping, etc.
- Title bar now reflects current Hunt query. This will assist users in locating a previous query from their browser history.
- Zeek 3.0.7
- Elastic 7.7.1
- Suricata can now be used for meta data generation.
- Suricata eve.json has been moved to /nsm to align with storage of other data.
- Suricata will now properly rotate its logs.
- Grafana dashboards now work properly in standalone mode.
- Kibana Dashboard updates including osquery, community_id.
- New Elasticsearch Ingest processor to generate community_id from any log that includes the required fields.
- Community_id generated for additional logs: Zeek HTTP/SMTP/ , Sysmon shipped with Osquery or Winlogbeat.
- Major streamlining of Fleet setup & configuration - no need to run a secondary setup script anymore.
- Fleet Standalone node now includes the ability to set a FQDN to point osquery endpoints to.
- Distributed installs now support ingesting Windows Eventlogs via Winlogbeat - includes full parsing support for Sysmon.
- SOC Downloads section now includes a link to the supported version of Winlogbeat.
- Basic syslog ingestion capability now included.
- Elasticsearch index name transition fixes for various components.
- Updated URLs for pivot fields in Kibana.
- Instances of hive renamed to thehive.

Known Issues:

- The Hunt feature is currently considered "Preview" and although very useful in its current state, not everything works. We wanted to get this out as soon as possible to get the feedback from you! Let us know what you want to see! Let us know what you think we should call it!
- You cannot pivot to PCAP from Suricata alerts in Kibana or Hunt.
- Navigator is currently not working when using hostname to access SOC. IP mode works correctly.
- Due to the move to ECS, the current Playbook plays may not alert correctly at this time.
- The osquery MacOS package does not install correctly.
