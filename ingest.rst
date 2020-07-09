.. _ingest:

Ingest
======

Here's an overview of how logs are ingested in various deployment types.

Eval
----
| Core Pipeline: Filebeat [EVAL Node] --> ES Ingest [EVAL Node]
| Logs: Zeek, Suricata, Wazuh, Osquery/Fleet
| 
| Osquery Shipper Pipeline: Osquery [Endpoint] --> Fleet [EVAL Node] --> ES Ingest via Core Pipeline
| Logs: WEL, Osquery, syslog

Standalone
----------
| Core Pipeline: Filebeat [SA Node] --> Logstash [SA Node] --> Redis [SA Node] <--> Logstash [SA Node] --> ES Ingest [SA Node]
| Logs: Zeek, Suricata, Wazuh, Osquery/Fleet
| 
| WinLogbeat: Winlogbeat [Windows Endpoint]--> Logstash [SA Node] --> Redis [SA Node] <--> Logstash [SA Node] --> ES Ingest [SA Node]
| Logs: WEL, Sysmon

Fleet Standalone
----------------
| Pipeline: Filebeat [Fleet Node] --> Logstash [M | M+S] --> ES Ingest [S | M+S]
| Logs: Osquery

Manager Node
------------
| Core Pipeline: Filebeat [Fleet | Forward] --> Logstash [Manager] --> ES Ingest [S]
| Logs: Zeek, Suricata, Wazuh, Osquery/Fleet
| 
| WinLogbeat: Winlogbeat [Windows Endpoint]--> Logstash [Manager] --> ES Ingest [S]
| Logs: WEL

Manager + Search
----------------
| Core Pipeline: Filebeat [Fleet | Forward] --> Logstash [M+S] --> ES Ingest [M+S]
| Logs: Zeek, Suricata, Wazuh, Osquery/Fleet
| 
| Pipeline: Filebeat [M+S] --> Logstash [M+S] --> ES Ingest [M+S]
| Logs: Local Wazuh, Osquery/Fleet
| 
| WinLogbeat: Winlogbeat [Windows Endpoint]--> Logstash [M+S] --> ES Ingest [M+S]
| Logs: WEL

Heavy
-----
| Pipeline: Filebeat [Heavy Node] --> Logstash [Heavy] --> ES Ingest [Heavy] 
| Logs: Zeek, Suricata, Wazuh, Osquery/Fleet

Search
------
| Pipeline: Redis [Search] --> Logstash [Search] --> ES Ingest [Search] 
| Logs: Zeek, Suricata, Wazuh, Osquery/Fleet

Forward
-------
| Pipeline: Filebeat [Forward] --> Logstash [M | M+S] --> ES Ingest [S | M+S]
| Logs: Zeek, Suricata, Wazuh
