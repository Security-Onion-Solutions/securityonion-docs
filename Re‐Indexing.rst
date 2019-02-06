Introduction
============

When changing mappings or index settings, we may need to re-index the
existing indices to ensure there are no mapping conflicts.

One way to do this by using the following **experimental** example
script:

https://raw.githubusercontent.com/weslambert/securityonion-elastic-misc/master/so-elastic-reindex

Re-Indexing
===========

Pull down the script to your Security Onion box:

``wget https://raw.githubusercontent.com/weslambert/securityonion-elastic-misc/master/so-elastic-reindex``

Make the script executable:

``sudo chmod +x so-elastic-reindex``

Re-index all indices matching ``logstash-*``, pulling the appropriate
``refresh_interval`` from the template named ``logstash`` in
Elasticsearch:

``sudo ./so-elastic-reindex -i "logstash-*" -t "logstash"``

The script should then progress to re-index the matching indices, and
inform you when it has completed.

*Please note, abnormal execution of this script may result in data loss
-- there are **NO GUARANTEES** this process will work perfectly for
you*.
