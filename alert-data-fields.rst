Alert Data Fields
=================

Below are the fields derived from IDS alerts (Snort/Suricata), after
being processed by Logstash:

| ``type:snort``
| ``/etc/logstash/conf.d/1033_preprocess_snort.conf``

| alert
| category
| classification
| source_ip
| source_port
| destination_ip
| destination_port
| gid
| host
| priority
| protocol
| rev
| rule (*added through augmentation*)
| rule_type
| severity
| sid
| Signature_Info (*added through augmentation*)
