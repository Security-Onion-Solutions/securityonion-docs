Alert Data Fields
=================

Below are the fields derived from IDS alerts (Snort/Suricata), after
being processed by Logstash:

| ``type:snort``
| ``/etc/logstash/conf.d/1033_preprocess_snort.conf``

| alert
| category
| classification
| source\_ip
| source\_port
| destination\_ip
| destination\_port
| gid
| host
| priority
| protocol
| rev
| rule (*added through augmentation*)
| rule\_type
| severity
| sid
| Signature\_Info (*added through augmentation*)
