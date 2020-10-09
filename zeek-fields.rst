.. _zeek-fields:

Zeek Fields
===========

Zeek logs are sent to Elasticsearch where they are parsed using ingest parsing. Most Zeek logs have a few standard fields and they are parsed as follows:

| ts => @timestamp
| uid => log.id.uid
| id.orig_h => source.ip
| id.orig_p => source.port
| id.resp_h => destination.ip
| id.resp_p => destination.port

The remaining fields in each log are specific to the log type. To see how the fields are mapped for a specific Zeek log, take a look at its ingest parser.

You can find ingest parsers in your local filesystem at ``/opt/so/conf/elasticsearch/ingest/`` or you can find them online at:

https://github.com/Security-Onion-Solutions/securityonion/tree/master/salt/elasticsearch/files/ingest

For example, suppose you want to know how the Zeek conn.log is parsed. You could take a look at ``/opt/so/conf/elasticsearch/ingest/zeek.conn`` or view it online at:

https://github.com/Security-Onion-Solutions/securityonion/blob/master/salt/elasticsearch/files/ingest/zeek.conn

You'll see that ``zeek.conn`` then calls the ``zeek.common`` pipeline (``/opt/so/conf/elasticsearch/ingest/zeek.common``):

https://github.com/Security-Onion-Solutions/securityonion/blob/master/salt/elasticsearch/files/ingest/zeek.common

which in turn calls the ``common`` pipeline (``/opt/so/conf/elasticsearch/ingest/common``):

https://github.com/Security-Onion-Solutions/securityonion/blob/master/salt/elasticsearch/files/ingest/common
