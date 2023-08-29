.. _elasticsearch:

Elasticsearch
=============

From https://www.elastic.co/products/elasticsearch:

    Elasticsearch is a distributed, RESTful search and analytics engine capable of addressing a growing number of use cases. As the heart of the Elastic Stack, it centrally stores your data for lightning fast search, fine‑tuned relevancy, and powerful analytics that scale with ease.

Data
----

Indexing
~~~~~~~~

Starting in Security Onion 2.4, most data is associated with a data stream, which is an abstraction from traditional indices that leverages one or more backing indices to manage and represent the data within the data stream. The usage of data streams allows for greater flexibility in data management.

Data streams can be targeting during search or other operations directly, similar to how indices are targeted.

For example, a CLI-based query against Zeek connection records would look like the following:

::

	so-elasticsearch-query logs-zeek-so/_search?q=event.dataset:conn

When this query is run against the backend data, it is actually targeting one or more backing indices, such as:

::

  .ds-logs-zeek-so-2022-03-07.0001
  .ds-logs-zeek-so-2022-03-08.0001
  .ds-logs-zeek-so-2022-03-08.0002

Similarly, you can target a single backing index with the following query:

::

	so-elasticsearch-query .ds-logs-zeek-so-2022-03-08.001/_search?q=event.dataset:conn

You can learn more about data streams at https://www.elastic.co/guide/en/elasticsearch/reference/current/data-streams.html.

Schema
~~~~~~

Security Onion tries to adhere to the Elastic Common Schema wherever possible. Otherwise, additional fields or slight modifications to native Elastic field mappings may be found within the data.

Management
~~~~~~~~~~

In Security Onion 2.4, Elasticsearch data is handled partially by both :ref:`curator` and ILM (https://www.elastic.co/guide/en/elasticsearch/reference/current/index-lifecycle-management.html).

Only Curator performs the following actions:

- closing of open indices
- size-based index deletion
- size-based closed index deletion

Only ILM performs the following actions:

- size-based index rollover
- time-based index rollover
- time-based content tiers

Both Curator and ILM perform the following actions:

- time-based open index deletion
- time-based closed index deletion

Default ILM policies are preconfigured and associated with various data streams and index templates in ``/opt/so/saltstack/default/salt/elasticsearch/defaults.yaml``.

Querying
--------

You can query Elasticsearch using web interfaces like :ref:`alerts`, :ref:`dashboards`, :ref:`hunt`, and :ref:`kibana`. You can also query Elasticsearch from the command line using a tool like ``curl``. You can also use :ref:`so-elasticsearch-query`.

Authentication
--------------

We support Elastic authentication via :ref:`so-elastic-auth`.

Diagnostic Logging
------------------

-  Elasticsearch logs can be found in ``/opt/so/log/elasticsearch/``.
-  Logging configuration can be found in ``/opt/so/conf/elasticsearch/log4j2.properties``.

Depending on what you're looking for, you may also need to look at the :ref:`docker` logs for the container:

::

        sudo docker logs so-elasticsearch

Storage
-------

All of the data Elasticsearch collects is stored under ``/nsm/elasticsearch/``.

Parsing
-------

Elasticsearch receives unparsed logs from :ref:`logstash` or :ref:`elastic-agent`. Elasticsearch then parses and stores those logs. Parsers are stored in ``/opt/so/conf/elasticsearch/ingest/``.  Custom ingest parsers can be placed in ``/opt/so/saltstack/local/salt/elasticsearch/files/ingest/``.   To make these changes take effect, restart Elasticsearch using ``so-elasticsearch-restart``.

:ref:`elastic-agent` may pre-parse or act on data before the data reaches Elasticsearch, altering the data stream or index to which it is written, or other characteristics such as the event dataset or other pertinent information. This configuration is maintained in the agent policy or integration configuration in :ref:`elastic-fleet`.

.. note::

    | For more about Elasticsearch ingest parsing, please see:
    | https://www.elastic.co/guide/en/elasticsearch/reference/current/ingest.html

Templates
---------

Fields are mapped to their appropriate data type using templates. When making changes for parsing, it is necessary to ensure fields are mapped to a data type to allow for indexing, which in turn allows for effective aggregation and searching in :ref:`dashboards`, :ref:`hunt`, and :ref:`kibana`. Elasticsearch leverages both component and index templates.

Component Templates
~~~~~~~~~~~~~~~~~~~

From https://www.elastic.co/guide/en/elasticsearch/reference/current/index-templates.html:

    Component templates are reusable building blocks that configure mappings, settings, and aliases. While you can use component templates to construct index  templates, they aren’t directly applied to a set of indices.
    
Also see https://www.elastic.co/guide/en/elasticsearch/reference/current/indices-component-template.html.


Index Templates
~~~~~~~~~~~~~~~

From https://www.elastic.co/guide/en/elasticsearch/reference/current/index-templates.html:    
    
    An index template is a way to tell Elasticsearch how to configure an index when it is created. Templates are configured prior to index creation. When an index is created - either manually or through indexing a document - the template settings are used as a basis for creating the index. Index templates can contain a collection of component templates, as well as directly specify settings, mappings, and aliases.

In Security Onion, component templates are stored in ``/opt/so/saltstack/default/salt/elasticsearch/templates/component/``. 

These templates are specified to be used in the index template definitions in ``/opt/so/saltstack/default/salt/elasticsearch/defaults.yml``.

Community ID
------------

| For logs that don’t naturally include :ref:`community-id`, we use the Elasticsearch Community ID processor:
| https://www.elastic.co/guide/en/elasticsearch/reference/current/community-id-processor.html

Configuration
-------------

You can configure Elasticsearch by going to :ref:`administration`, then Configuration, and then ``elasticsearch``.

field expansion matches too many fields
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you get errors like ``failed to create query: field expansion for [*] matches too many fields, limit: 3500, got: XXXX``, then this usually means that you're sending in additional logs and so you have more fields than our default ``max_clause_count`` value. To resolve this, you can go to :ref:`administration` --> Configuration --> elasticsearch --> config --> indices --> query --> bool --> max_clause_count and adjust the value for any boxes running Elasticsearch in your deployment.
      
Shards
~~~~~~

Here are a few tips from https://www.elastic.co/blog/how-many-shards-should-i-have-in-my-elasticsearch-cluster:

    TIP: Avoid having very large shards as this can negatively affect the cluster's ability to recover from failure. There is no fixed limit on how large shards can be, but a shard size of 50GB is often quoted as a limit that has been seen to work for a variety of use-cases.

    TIP: Small shards result in small segments, which increases overhead. Aim to keep the average shard size between a few GB and a few tens of GB. For use-cases with time-based data, it is common to see shards between 20GB and 40GB in size.

    TIP: The number of shards you can hold on a node will be proportional to the amount of heap you have available, but there is no fixed limit enforced by Elasticsearch. A good rule-of-thumb is to ensure you keep the number of shards per node below 20 to 25 per GB heap it has configured. A node with a 30GB heap should therefore have a maximum of 600-750 shards, but the further below this limit you can keep it the better. This will generally help the cluster stay in good health.

To see your existing shards, run the following command and the number of shards will be shown in the fifth column:

::

    sudo so-elasticsearch-query _cat/indices
    
If you want to view the detail for each of those shards:

::

    sudo so-elasticsearch-query _cat/shards

Given the sizing tips above, if any of your indices are averaging more than 50GB per shard, then you should probably increase the shard count until you get below that recommended maximum of 50GB per shard.

The number of shards for an index can be adjusted by going to :ref:`administration` --> Configuration --> elasticsearch --> index_settings --> so-INDEX-NAME --> index_template --> template --> settings --> index --> number_of_shards.

Please keep in mind that old indices will retain previous shard settings and the above settings will only be applied to newly created indices.

Heap Size
~~~~~~~~~

If total available memory is 8GB or greater, Setup configures the heap size to be 33% of available memory, but no greater than 25GB. You may need to adjust the value for heap size depending on your system's performance. You can modify this by going to :ref:`administration` --> Configuration --> elasticsearch --> esheap.

| For more information, please see:
| https://www.elastic.co/guide/en/elasticsearch/guide/current/heap-sizing.html#compressed_oops
| https://www.elastic.co/guide/en/elasticsearch/reference/current/important-settings.html#heap-size-settings

Field limit
~~~~~~~~~~~

Security Onion currently defaults to a field limit of 5000. If you receive error messages from Logstash, or you would simply like to increase this, you can do so by going to :ref:`administration` --> Configuration --> elasticsearch --> index_settings --> so-INDEX-NAME --> index_template --> template --> settings --> index --> mapping --> total_fields --> limit.

Please note that the change to the field limit will not occur immediately, only on index creation.

Closing Indices
---------------

Elasticsearch indices are closed based on the ``close`` setting shown at :ref:`administration` --> Configuration --> elasticsearch --> index_settings --> so-INDEX-NAME --> close. This setting configures :ref:`curator` to close any index older than the value given. The more indices are open, the more heap is required. Having too many open indices can lead to performance issues. There are many factors that determine the number of days you can have in an open state, so this is a good setting to adjust specific to your environment.

Deleting Indices
----------------

Size-based Index Deletion
~~~~~~~~~~~~~~~~~~~~~~~~~

Size-based deletion of Elasticsearch indices occurs based on the value of cluster-wide ``elasticsearch.retention.retention_pct``, which is derived from the total disk space available for ``/nsm/elasticsearch`` across all nodes in the Elasticsearch cluster. The default value for this setting is ``50`` percent, and it can be modified by navigating to :ref:`administration` -> Configuration -> Show all configurable settings, including advanced settings. -> elasticsearch -> retention -> retention_pct.

The change can be applied immediately by clicking ``Synchronize Grid``. Otherwise, the change will take effect after the Salt state has been applied at the next 15-minute interval.

If your open indices are using more than ``retention_pct``, then :ref:`curator` will delete old open indices until disk space is back under ``retention_pct``. If your total Elastic disk usage (both open and closed indices) is above ``retention_pct``, then ``so-curator-closed-delete`` will delete old closed indices until disk space is back under ``retention_pct``. ``so-curator-closed-delete`` does not use :ref:`curator` because :ref:`curator` cannot calculate disk space used by closed indices. For more information, see https://www.elastic.co/guide/en/elasticsearch/client/curator/current/filtertype_space.html.

:ref:`curator` and ``so-curator-closed-delete`` run on the same schedule. This might seem like there is a potential to delete open indices before deleting closed indices. However, keep in mind that :ref:`curator`'s delete.yml is only going to see disk space used by open indices and not closed indices. So if we have both open and closed indices, we may be at ``retention_pct`` but :ref:`curator`'s delete.yml is going to see disk space at a value lower than ``retention_pct`` and so it shouldn't delete any open indices.

For example, suppose our ``retention_pct`` is 50%, total disk space is 1TB, and we have 30 days of open indices and 300 days of closed indices. We reach ``retention_pct`` and both :ref:`curator` and ``so-curator-closed-delete`` execute at the same time. Curator's delete.yml will check disk space used but it will see that disk space is at maybe 500GB so it thinks we haven't reached ``retention_pct`` and does not delete anything. ``so-curator-closed-delete`` gets a more accurate view of disk space used, sees that we have indeed reached ``retention_pct``, and so it deletes closed indices until we get lower than ``retention_pct``. In most cases, :ref:`curator` deletion should really only happen if we have open indices without any closed indices.

Time-based Index Deletion
~~~~~~~~~~~~~~~~~~~~~~~~~

Time-based deletion occurs through the use of the $data_stream.policy.phases.delete.min_age setting within the lifecycle policy tied to each index and is controlled by ILM. It is important to note that size-based deletion takes priority over time-based deletion, as disk may reach ``retention_pct`` and indices will be deleted before the ``min_age`` value is reached.

Policies can be edited within the SOC administration interface by navigating to :ref:`administration` -> Configuration -> elasticsearch -> $index -> policy -> phases -> delete -> min_age. Changes will take effect when a new index is created.

Distributed Deployments
-----------------------

Security Onion supports Elastic clustering. In this configuration, Elasticsearch instances join together to create a single cluster. When using Elastic clustering, index deletion is based on the ``delete`` settings shown in the global pillar above. The ``delete`` settings in the global pillar configure :ref:`curator` to delete indices older than the value given. For each index, please ensure that the ``close`` setting is set to a smaller value than the ``delete`` setting.

Let's discuss the process for determining appropriate ``delete`` settings. First, check your indices using :ref:`so-elasticsearch-query` to query ``_cat/indices``. For example:

::

	sudo so-elasticsearch-query _cat/indices | grep 2021.08.26

	green open  so-zeek-2021.08.26              rEtb1ERqQcyr7bfbnR95zQ 5 0  2514236      0    2.4gb    2.4gb
	green open  so-ids-2021.08.26               d3ySLbRHSJGRQ2oiS4pmMg 1 0     1385    147    3.3mb    3.3mb
	green open  so-ossec-2021.08.26             qYf1HWGUSn6fIOlOgFgJOQ 1 0   125333     61  267.1mb  267.1mb
	green open  so-elasticsearch-2021.08.26     JH8tOgr3QjaQ-EX08OGEXw 1 0    61170      0   32.7mb   32.7mb
	green open  so-firewall-2021.08.26          Qx6_ZQS3QL6VGwIXIQ8mfQ 1 0   508799      0  297.4mb  297.4mb
	green open  so-syslog-2021.08.26            3HiYP3fgSPmoV-Nbs3dlDw 1 0   181207      0     27mb     27mb
	green open  so-kibana-2021.08.26            C6v6sazHSYiwqq5HxfokQg 1 0      745      0  809.5kb  809.5kb
 
Adding all the index sizes together plus a little padding results in 3.5GB per day. We will use this as our baseline.

If we look at our total ``/nsm`` size for our search nodes (data nodes in Elastic nomenclature), we can calculate how many days open or closed that we can store. The equation shown below determines the proper delete timeframe. Note that total usable space depends on replica counts. In the example below we have 2 search nodes with 140GB for 280GB total of ``/nsm`` storage. Since we have a single replica we need to take that into account. The formula for that is: 

1 replica = 2 x Daily Index Size
2 replicas = 3 x Daily Index Size
3 replicas = 4 x Daily Index Size

Let’s use 1 replica:

Total Space / copies of data = Usable Space

280 / 2 = 140

Suppose we want a little cushion so let's make Usable Space = 130

Usable NSM space / Daily Index Size = Days

For our example above lets fill in the proper values:

130GB / 3.5GB = 37.1428571 days rounded down to 37 days

Therefore, we can set all of our ``delete`` values to 37.

Re-indexing
-----------

Re-indexing may need to occur if field data types have changed and conflicts arise.  This process can be VERY time-consuming, and we only recommend this if keeping data is absolutely critical.  

| For more information about re-indexing, please see:
| https://www.elastic.co/guide/en/elasticsearch/reference/current/docs-reindex.html

Clearing
--------

If you want to clear all Elasticsearch data including documents and indices, you can run the ``so-elastic-clear`` command.

GeoIP
-----

Elasticsearch 8 no longer includes GeoIP databases by default. We include GeoIP databases for Elasticsearch so that all users will have GeoIP functionality. If your search nodes have Internet access and can reach geoip.elastic.co and storage.googleapis.com, then you can opt-in to database updates if you want more recent information. To do this, add the following to your Elasticsearch :ref:`salt` config:

::

    config:
      ingest:
        geoip:
          downloader:
            enabled: true

More Information
----------------

.. note::

    | For more information about Elasticsearch, please see:
    | https://www.elastic.co/products/elasticsearch
