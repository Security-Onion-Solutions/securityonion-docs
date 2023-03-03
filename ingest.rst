.. _ingest:

Ingest
======

Here's an overview of how logs are ingested in various deployment types.

Import
------
| Core Pipeline: Elastic Agent [IMPORT Node] --> ES Ingest [IMPORT Node]
| Logs: Zeek, Suricata

Eval
----
| Core Pipeline: Elastic Agent [EVAL Node] --> ES Ingest [EVAL Node]
| Logs: Zeek, Suricata, Osquery/Fleet
| 
| Osquery Shipper Pipeline: Osquery [Endpoint] --> Fleet [EVAL Node] --> ES Ingest via Core Pipeline
| Logs: WEL, Osquery, syslog

Standalone
----------
| Core Pipeline: Elastic Agent [SA Node] --> Logstash [SA Node] --> Redis [SA Node] <--> Logstash [SA Node] --> ES Ingest [SA Node]
| Logs: Zeek, Suricata, Osquery/Fleet, syslog
| 
| WinLogbeat: Winlogbeat [Windows Endpoint]--> Logstash [SA Node] --> Redis [SA Node] <--> Logstash [SA Node] --> ES Ingest [SA Node]
| Logs: WEL, Sysmon

Fleet Standalone
----------------
| Pipeline: Elastic Agent [Fleet Node] --> Logstash [M | MS] --> ES Ingest [S | MS]
| Logs: Osquery

Manager (separate search nodes)
-------------------------------
| Core Pipeline: Elastic Agent [Fleet | Forward] --> Logstash [Manager] --> Redis [Manager]
| Logs: Zeek, Suricata, Osquery/Fleet, syslog
| 
| WinLogbeat: Winlogbeat [Windows Endpoint]--> Logstash [Manager] --> Redis [Manager]
| Logs: WEL

Manager Search
--------------
| Core Pipeline: Elastic Agent [Fleet | Forward] --> Logstash [MS] --> Redis [MS] <--> Logstash [MS] --> ES Ingest [MS]
| Logs: Zeek, Suricata, Osquery/Fleet, syslog
| 
| Pipeline: Elastic Agent [MS] --> Logstash [MS] --> ES Ingest [MS]
| Logs: Local Osquery/Fleet
| 
| WinLogbeat: Winlogbeat [Windows Endpoint]--> Logstash [MS] --> ES Ingest [MS]
| Logs: WEL

Heavy
-----
| Pipeline: Elastic Agent [Heavy Node] --> Logstash [Heavy] --> Redis [Heavy] <--> Logstash [Heavy] --> ES Ingest [Heavy] 
| Logs: Zeek, Suricata, Osquery/Fleet, syslog

Search
------
| Pipeline: Redis [Manager] --> Logstash [Search] --> ES Ingest [Search] 
| Logs: Zeek, Suricata, Osquery/Fleet, syslog

Forward
-------
| Pipeline: Elastic Agent [Forward] --> Logstash [M | MS] --> ES Ingest [S | MS]
| Logs: Zeek, Suricata, syslog
