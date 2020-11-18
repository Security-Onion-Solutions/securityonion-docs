.. _elasticsearch:

Elasticsearch
=============

From https://www.elastic.co/products/elasticsearch:

    Elasticsearch is a distributed, RESTful search and analytics engine capable of solving a growing number of use cases. 
    As the heart of the Elastic Stack, it centrally stores your data so you can discover the expected and uncover the unexpected.

Parsing
-------

In Security Onion 2, Elasticsearch receives unparsed logs from :ref:`logstash` or :ref:`filebeat`. Elasticsearch then parses and stores those logs. Parsers are stored in ``/opt/so/conf/elasticsearch/ingest/``.  Custom ingest parsers can be placed in ``/opt/so/saltstack/local/salt/elasticsearch/files/ingest/``.   To make these changes take effect, restart Elasticsearch using ``so-elasticsearch-restart``.

.. seealso::

    For more about Elasticsearch ingest parsing, please see https://www.elastic.co/guide/en/elasticsearch/reference/master/ingest.html.
    
Community ID
------------
For logs that don’t natively support :ref:`community-id`, we sponsored the development of an Elasticsearch Ingest Processor to automatically generate Community ID values:

https://github.com/Security-Onion-Solutions/elasticsearch-ingest-community-id

Configuration
-------------

Pillar Files
~~~~~~~~~~~~

All configuration changes take place in pillar files. You should never need to modify a config file directly. There are two places that hold pillar settings for elasticsearch. The pillars are:

``/opt/so/saltstack/local/pillar/minions/$minion.sls``

::

    elasticsearch:
      mainip: 10.66.166.22
      mainint: eth0
      esheap: 4066m
      esclustername: {{ grains.host }}
      node_type: search
      es_port: 9200
      log_size_limit: 3198
      node_route_type: hot


``/opt/so/saltstack/local/pillar/global.sls``

::

    elasticsearch:
      replicas: 0
      true_cluster: False
      true_cluster_name: so
      discovery_nodes: 1
      hot_warm_enabled: False
      cluster_routing_allocation_disk.threshold_enabled: true
      cluster_routing_allocation_disk_watermark_low: 95%
      cluster_routing_allocation_disk_watermark_high: 98%
      cluster_routing_allocation_disk_watermark_flood_stage: 98%
      index_settings:
        so-beats:
          shards: 1
          warm: 7
          close: 30
          delete: 365
        so-firewall:
          shards: 1
          warm: 7
          close: 30
          delete: 365
        so-flow:
          shards: 1
          warm: 7
          close: 30
          delete: 365
        so-ids:
          shards: 1
          warm: 7
          close: 30
          delete: 365
        so-import:
          shards: 1
          warm: 7
          close: 73000
          delete: 73001
        so-osquery:
          shards: 1
          warm: 7
          close: 30
          delete: 365
        so-ossec:
          shards: 1
          warm: 7
          close: 30
          delete: 365
        so-strelka:
          shards: 1
          warm: 7
          close: 30
          delete: 365
        so-syslog:
          shards: 1
          warm: 7
          close: 30
          delete: 365
        so-zeek:
          shards: 5
          warm: 7
          close: 365
          delete: 45


Shards
~~~~~~

Here are a few tips from https://www.elastic.co/blog/how-many-shards-should-i-have-in-my-elasticsearch-cluster:

    TIP: Avoid having very large shards as this can negatively affect the cluster's ability to recover from failure. There is no fixed limit on how large shards can be, but a shard size of 50GB is often quoted as a limit that has been seen to work for a variety of use-cases.

    TIP: Small shards result in small segments, which increases overhead. Aim to keep the average shard size between a few GB and a few tens of GB. For use-cases with time-based data, it is common to see shards between 20GB and 40GB in size.

    TIP: The number of shards you can hold on a node will be proportional to the amount of heap you have available, but there is no fixed limit enforced by Elasticsearch. A good rule-of-thumb is to ensure you keep the number of shards per node below 20 to 25 per GB heap it has configured. A node with a 30GB heap should therefore have a maximum of 600-750 shards, but the further below this limit you can keep it the better. This will generally help the cluster stay in good health.

To see your existing shards:

::

    curl localhost:9200/_cat/indices
    
The number of shards will be shown in the fifth column.

If you want to view the detail for each of those shards:

::

    curl localhost:9200/_cat/shards


Given the sizing tips above, if any of your indices are averaging more than 50GB per shard, then you should probably increase the shard count until you get below that recommended maximum of 50GB per shard.

The number of shards for an index is defined in ``/opt/so/saltstack/local/pillar/global.sls``. You can adjust shard counts for each index individually to meet your needs. The next time the node checks in it will apply the settings automatically.

Please keep in mind that old indices will retain previous shard settings and the above settings will only be applied to newly created indices.

Heap Size
~~~~~~~~~

By default, if total available memory is 8GB or greater, the heap size is configured (during Setup) to equal 25% of available memory, but no greater than 25GB. You may need to adjust the value for heap size depending on your system's performance. This can be modified in ``/opt/so/saltstack/local/pillar/minions/$minion.sls``.

| For more information, please see:
| https://www.elastic.co/guide/en/elasticsearch/guide/current/heap-sizing.html#compressed_oops
| https://www.elastic.co/guide/en/elasticsearch/reference/current/heap-size.html

Field limit
~~~~~~~~~~~

Security Onion currently utilizes the default field limit for Elasticsearch indices (``1000``). If you receive error messages from Logstash, or you would simply like to increase this, you can do so with one of the following options.

Temporary
~~~~~~~~~

If you only need to increase the field limit temporarily, you can do something like:

::

   curl -XPUT -H'Content-Type: application/json' localhost:9200/logstash-syslog-*/_settings -d'{ "index.mapping.total_fields.limit": 2000 }'

The above command would increase the field limit for the ``logstash-syslog-*`` indice(s) to ``2000``. Keep in mind, this setting only applies to the current index, so when the index rolls over and a new one is created, your new settings will not apply.

Persistent
~~~~~~~~~~

If you need this change to be persistent, you can modify the ``settings`` stanza for the matched indices in ``/etc/logstash/logstash-template.json``.

::

    "settings" : {
        "number_of_replicas": 0,
        "number_of_shards": 1,
        "index.refresh_interval" : "5s",
        "index.mapping.total_fields.limit": 2000
    },

Then restart Logstash:

::

   sudo so-logstash-restart

Please note that the change to the field limit will not occur immediately -- only upon index creation. Therefore, it is recommended to run the previously mentioned temporary command and modify the template file.

Additional options
~~~~~~~~~~~~~~~~~~

If you need to make additional directories accessible to Elasticsearch, or would like to specify additional options when starting Elasticsearch, you can do so by adding these items to ``ELASTICSEARCH_OPTIONS`` in ``/etc/nsm/securityonion.conf``

Diagnostic Logging
------------------

-  Elasticsearch logs can be found in ``/opt/so/log/elasticsearch/``.
-  Logging configuration can be found in ``/opt/so/conf/elasticsearch/log4j2.properties``.

Distributed
-----------

Management
----------

The ``manager node`` runs its own local copy of Elasticsearch, which manages cross-cluster search configuration for the deployment. This includes configuration for ``heavy nodes`` and ``search nodes`` (where applicable), but not ``forward nodes``, as they do not run Elastic Stack components.

Forward Nodes
-------------

When using a ``forward node``, Elastic Stack components are not enabled. :ref:`filebeat` forwards all logs to :ref:`logstash` on the manager node, where they are stored in Elasticsearch on the manager node or a search node (if the manager node has been configured to use search nodes). From there, the data can be queried through the use of cross-cluster search.

Heavy Nodes
-----------

When using a ``heavy node``, Security Onion implements distributed deployments using Elasticsearch's `cross cluster search <https://www.elastic.co/guide/en/elasticsearch/reference/current/modules-cross-cluster-search.html>`__. When you run Setup and choose ``Heavy Node``, it will create a local Elasticsearch instance and then configure the manager node to query that instance. This is done by updating \_cluster/settings on the manager node so that it will query the local Elasticsearch instance.

Search Nodes
-------------

``Search nodes`` extend the storage and processing capabilities of the manager node, and run :ref:`elasticsearch`, :ref:`logstash`, and :ref:`curator`. Just like heavy nodes, search nodes are added to the manager node's cluster search configuration, so the data that resides on the nodes can be queried from the manager node.

Removing a node from the manager node
-------------------------------------

If you need to remove a node (such as a ``heavy node`` or a ``search node``) from your cross cluster search configuration, send the following to Elasticsearch on your manager node (replacing ``node1`` with the actual node you'd like to remove):

::

    PUT _cluster/settings
    {
    "persistent": {
    "search": {
    "remote": {
    "node1": {
    "seeds": null}}}}}

You can simply copy/paste the above code (modifying as necessary) into the Console, under "Dev Tools" in Kibana, and click the green triangle. Alternatively, you could submit it to Elasticsearch via a cURL command.

Storage
-------

All of the data Elasticsearch collects is stored under ``/nsm/elasticsearch/``.

Snapshots
---------

Snapshots of the current indices can be taken and stored in a designated repository for archival purposes. Currently, you'll need to add something like the following to ``/opt/so/conf/elasticsearch/elasticsearch.yml``:

::

   path.repo: <your file path here>

keeping in mind that the above file path is relative to the container's view of the filesystem.

So, if you decided to add a ``path.repo`` value of ``/backups``, Elasticsearch would be looking for the file path ``/backups`` inside of the container. To achieve parity with what is present on the host's filesystem and make that directory accessible to the Elasticsearch Docker container, you'll want to add something like the following to ELASTICSEARCH_OPTIONS in ``/etc/nsm/securityonion.conf``:

::

   ELASTICSEARCH_OPTIONS="-v /backups:/backups" 

(where ``/backups`` exists on the host file system and is writable by the Elasticsearch user -- a directory named ``/backups`` will be created inside the container, and the container will be able to read/write from that location).

To automate the snapshotting process, you can use :ref:`curator`, in conjunction with a cron job, much like what is done today with the close and delete jobs.

Re-indexing
-----------
Re-indexing may need to occur if field data types have changed and conflicts arise.  This process can be VERY time-consuming, and we only recommend this if keeping data is absolutely critical.  For more information on re-indexing, see:

https://www.elastic.co/guide/en/elasticsearch/reference/current/docs-reindex.html

