.. _alert-data-fields:

Alert Data Fields
=================

:ref:`elasticsearch` receives NIDS alerts from :ref:`suricata` via :ref:`filebeat` or :ref:`logstash` and parses them using:
| ``/opt/so/conf/elasticsearch/ingest/suricata.alert``
| ``/opt/so/conf/elasticsearch/ingest/common``

You can then find parsed NIDS alerts in :ref:`hunt` and :ref:`kibana` via their predefined queries and dashboards or by manually searching for:

| ``event.module:"suricata"``
| ``event.dataset:"alert"``

Those alerts should have the following fields:

| ``source.ip``
| ``source.port``
| ``destination.ip``
| ``destination.port``
| ``network.transport``
| ``rule.gid``
| ``rule.name``
| ``rule.rule``
| ``rule.rev``
| ``rule.severity``
| ``rule.uuid``
| ``rule.version``
