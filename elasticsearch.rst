.. _elasticsearch:

Elasticsearch
=============

From https://www.elastic.co/products/elasticsearch:

    Elasticsearch is a distributed, RESTful search and analytics engine capable of addressing a growing number of use cases. As the heart of the Elastic Stack, it centrally stores your data for lightning fast search, fine‑tuned relevancy, and powerful analytics that scale with ease.

Data
----

Indexing
~~~~~~~~

Most data is associated with a data stream, which is an abstraction from traditional indices that leverages one or more backing indices to manage and represent the data within the data stream. The usage of data streams allows for greater flexibility in data management.

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

Elasticsearch indices are managed by the ``so-elasticsearch-indices-delete`` utility and ILM (https://www.elastic.co/guide/en/elasticsearch/reference/current/index-lifecycle-management.html).

``so-elasticsearch-indices-delete`` handles size-based index deletion and ILM handles the following:

- size-based index rollover
- time-based index rollover
- time-based content tiers
- time-based index deletion

Default ILM policies are preconfigured and associated with various data streams and index templates in ``/opt/so/saltstack/default/salt/elasticsearch/defaults.yaml``.

Querying
--------

You can query Elasticsearch using web interfaces like :ref:`alerts`, :ref:`dashboards`, :ref:`hunt`, and :ref:`kibana`. You can also query Elasticsearch from the command line using a tool like ``curl``. You can also use :ref:`so-elasticsearch-query`.

Authentication
--------------

You can authenticate to Elasticsearch using the same username and password that you use for :ref:`soc`.

You can add new user accounts to both Elasticsearch and :ref:`soc` at the same time as shown in the :ref:`adding-accounts` section. Please note that if you instead create accounts directly in Elastic, then those accounts will only have access to Elastic and not :ref:`soc`.

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

You can configure Elasticsearch by going to :ref:`administration` --> Configuration --> elasticsearch.

.. image:: images/config-item-elasticsearch.png
  :target: _images/config-item-elasticsearch.png

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

    sudo so-elasticsearch-indices-list
    
If you want to view the detail for each of those shards:

::

    sudo so-elasticsearch-shards-list

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

Deleting Indices
----------------

Size-based Index Deletion
~~~~~~~~~~~~~~~~~~~~~~~~~

Size-based deletion of Elasticsearch indices occurs based on the value of cluster-wide ``elasticsearch.retention.retention_pct``, which is derived from the total disk space available for ``/nsm/elasticsearch`` across all nodes in the Elasticsearch cluster. The default value for this setting is ``50`` percent. 

To modify this value, first navigate to :ref:`administration` -> Configuration. At the top of the page, click the ``Options`` menu and then enable the ``Show all configurable settings, including advanced settings.`` option. Then navigate to elasticsearch -> retention -> retention_pct. The change will take effect at the next 15 minute interval. If you would like to make the change immediately, you can click the ``SYNCHRONIZE GRID`` button under the ``Options`` menu at the top of the page.

If your indices are using more than ``retention_pct``, then ``so-elasticsearch-indices-delete`` will delete old indices until disk space is back under ``retention_pct``.

Time-based Index Deletion
~~~~~~~~~~~~~~~~~~~~~~~~~

Time-based deletion occurs through the use of the $data_stream.policy.phases.delete.min_age setting within the lifecycle policy tied to each index and is controlled by ILM. It is important to note that size-based deletion takes priority over time-based deletion, as disk may reach ``retention_pct`` and indices will be deleted before the ``min_age`` value is reached.

Policies can be edited within the SOC administration interface by navigating to :ref:`administration` -> Configuration -> elasticsearch -> $index -> policy -> phases -> delete -> min_age. Changes will take effect when a new index is created.

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
