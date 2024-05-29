.. _ingest:

Ingest
======

Here's an overview of how logs are ingested in various deployment types.

Import
------

| Core Pipeline: Elastic Agent [IMPORT Node] --> Elasticsearch Ingest [IMPORT Node]
| Logs: Zeek, Suricata

Eval
----

| Core Pipeline: Elastic Agent [EVAL Node] --> Elasticsearch Ingest [EVAL Node]
| Logs: Zeek, Suricata

Standalone
----------

| Core Pipeline: Elastic Agent [SA Node] --> Logstash [SA Node] --> Redis [SA Node] <--> Logstash [SA Node] --> Elasticsearch Ingest [SA Node]
| Logs: Zeek, Suricata, syslog
| 
| Elastic Agent: Elastic Agent [Windows Endpoint]--> Logstash [SA Node] --> Redis [SA Node] <--> Logstash [SA Node] --> Elasticsearch Ingest [SA Node]
| Logs: WEL, Sysmon

Fleet Standalone
----------------

| Pipeline: Elastic Agent [Fleet Node] --> Logstash [M | MS] --> Elasticsearch Ingest [S | MS]
| Logs: Elastic Agent

Manager (separate search nodes)
-------------------------------

| Core Pipeline: Elastic Agent [Fleet | Forward] --> Logstash [Manager] --> Redis [Manager]
| Logs: Zeek, Suricata, syslog
| 
| Elastic Agent: Elastic Agent [Windows Endpoint]--> Logstash [Manager] --> Redis [Manager]
| Logs: WEL, Sysmon

Manager Search
--------------

| Core Pipeline: Elastic Agent [Fleet | Forward] --> Logstash [MS] --> Redis [MS] <--> Logstash [MS] --> Elasticsearch Ingest [MS]
| Logs: Zeek, Suricata, syslog
| 
| Pipeline: Elastic Agent [MS] --> Logstash [MS] --> Elasticsearch Ingest [MS]
| Logs: Local Elastic Agent
| 
| Elastic Agent: Elastic Agent [Windows Endpoint]--> Logstash [MS] --> Elasticsearch Ingest [MS]
| Logs: WEL, Sysmon

Heavy
-----

| Pipeline: Elastic Agent [Heavy Node] --> Logstash [Heavy] --> Redis [Heavy] <--> Logstash [Heavy] --> Elasticsearch Ingest [Heavy] 
| Logs: Zeek, Suricata, syslog

Search
------

| Pipeline: Redis [Manager] --> Logstash [Search] --> Elasticsearch Ingest [Search] 
| Logs: Zeek, Suricata, syslog

Forward
-------

| Pipeline: Elastic Agent [Forward] --> Logstash [M | MS] --> Elasticsearch Ingest [S | MS]
| Logs: Zeek, Suricata, syslog
