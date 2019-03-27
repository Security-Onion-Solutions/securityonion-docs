Elasticsearch
=============

From https://www.elastic.co/products/elasticsearch:

    Elasticsearch is a distributed, RESTful search and analytics engine
    capable of solving a growing number of use cases. As the heart of
    the Elastic Stack, it centrally stores your data so you can discover
    the expected and uncover the unexpected.

Configuration
-------------

Shards
~~~~~~

Here are a few tips from
https://www.elastic.co/blog/how-many-shards-should-i-have-in-my-elasticsearch-cluster:

    TIP: Avoid having very large shards as this can negatively affect
    the cluster's ability to recover from failure. There is no fixed
    limit on how large shards can be, but a shard size of 50GB is often
    quoted as a limit that has been seen to work for a variety of
    use-cases.

    TIP: Small shards result in small segments, which increases
    overhead. Aim to keep the average shard size between a few GB and a
    few tens of GB. For use-cases with time-based data, it is common to
    see shards between 20GB and 40GB in size.

    TIP: The number of shards you can hold on a node will be
    proportional to the amount of heap you have available, but there is
    no fixed limit enforced by Elasticsearch. A good rule-of-thumb is to
    ensure you keep the number of shards per node below 20 to 25 per GB
    heap it has configured. A node with a 30GB heap should therefore
    have a maximum of 600-750 shards, but the further below this limit
    you can keep it the better. This will generally help the cluster
    stay in good health.

To see your existing shards:

::

    curl localhost:9200/_cat/shards

To modify your number of shards, you can change ``number_of_shards`` in ``/etc/logstash/*-template.json`` (first copy this file to ``/etc/logstash/custom``, edit the file, then restart Logstash).

Keep in mind, old indices will retain previous shard settings, and the above settings will only be applied to newly created indices.

Files
~~~~~

-  Configuration files for Elasticsearch can be found in ``/etc/elasticsearch/``.

-  Other configuration options for Elasticsearch can be found in ``/etc/nsm/securityonion.conf``.

-  By default, if total available memory is 8GB or greater, the heap size in ``/etc/elasticsearch/jvm.options`` is configured (during Setup) to equal 25% of available memory, but no greater than 25GB.

| For more information, please see:
| https://www.elastic.co/guide/en/elasticsearch/guide/current/heap-sizing.html#compressed_oops
| https://www.elastic.co/guide/en/elasticsearch/reference/current/heap-size.html

You may need to adjust the value for heap size depending on your system's performance (running ``sudo so-elastic-restart`` after).

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

Logs
----

-  Elasticsearch logs can be found in ``/var/log/elasticsearch/``.
-  Logging configuration can be found in
   ``/etc/elasticsearch/log4j2.properties``.

Distributed
-----------

Master
------

The ``master server`` runs it's own local copy of Elasticsearch, which manages cross-cluster search configuration for the deployment. This includes configuration for ``heavy nodes`` and ``storage nodes`` (where applicable), but not ``forward nodes``, as they do not run Elastic Stack components.

Forward Nodes
-------------

When using a ``forward node``, Elastic Stack components are not enabled. Syslog-NG forwards all logs to Logstash on the master server via an autossh tunnel, where they are stored in Elasticsearch on the master server or a storage node (if the master server has been configured to use storage nodes). From there, the data can be queried through the use of cross-cluster search.

Heavy Nodes
-----------

When using a ``heavy node``, Security Onion implements distributed deployments using Elasticsearch's `cross cluster search <https://www.elastic.co/guide/en/elasticsearch/reference/current/modules-cross-cluster-search.html>`__. When you run Setup and choose ``Heavy Node``, it will create a local Elasticsearch instance and then configure the master server to query that instance (similar to ELSA distributed deployments). This is done by constructing an autossh tunnel from the heavy node to the master server, configuring reverse port forwarding to allow the master server to connect to the local Elasticsearch instance, and updating \_cluster/settings on the master server so that it will query the local Elasticsearch instance.

Storage Nodes
-------------

``Storage nodes`` extend the storage and processing capabilities of the master server, and run Elasticsearch, Logstash, and Curator. Just like heavy nodes, storage nodes are added to the master's cluster search configuration, so the data that resides on the nodes can be queried from the master.

Removing a node from the master
-------------------------------

If you need to remove a node (such as a ``heavy node`` or a ``storage node``) from your cross cluster search configuration, send the following to Elasticsearch on your master server (replacing "node1" with the actual node you'd like to remove and noting that null must be in square brackets):

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

Snapshots of the current indices can be taken and stored in a designated repository for archival purposes. Currently, you'll need to add something like the following to ``/etc/elasticsearch/elasticsearch.yml``:

::

   path.repo: <your file path here>

keeping in mind that the above file path is relative to the container's view of the filesystem.

So, if you decided to add a ``path.repo`` value of ``/backups``, Elasticsearch would be looking for the file path ``/backups`` inside of the container. To achieve parity with what is present on the host's filesystem and make that directory accessible to the Elasticsearch Docker container, you'll want to add something like the following to ELASTICSEARCH_OPTIONS in ``/etc/nsm/securityonion.conf``:

::

   ELASTICSEARCH_OPTIONS="-v /backups:/backups" 

(where ``/backups`` exists on the host file system and is writable by the Elasticsearch user -- a directory named ``/backups`` will be created inside the container, and the container will be able to read/write from that location).

To automate the snapshotting process, you can use `Curator <Curator>`__, in conjunction with a cron job, much like what is done today with the close and delete jobs.
