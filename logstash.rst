Logstash
========

From https://www.elastic.co/products/logstash :

    Logstash is an open source, server-side data processing pipeline
    that ingests data from a multitude of sources simultaneously,
    transforms it, and then sends it to your favorite “stash".

Configuration
-------------

Here are a few of the settings which you may need to tune in ``/opt/so/saltstack/local/pillar/minions/$MINION_$ROLE.sls under logstash_settings``.

ls_pipeline_batch_size
~~~~~~~~~~~~~~~~~~~

    The maximum number of events an individual worker thread will collect from inputs before attempting to execute its filters and outputs. Larger batch sizes are generally more efficient, but come at the cost of increased memory overhead. This is set to 125 by default.
    
ls_pipeline_workers
~~~~~~~~~~~~~~~~

    The number of workers that will, in parallel, execute the filter and
    output stages of the pipeline. If you find that events are backing
    up, or that the CPU is not saturated, consider increasing this
    number to better utilize machine processing power. By default this value is set to the number of cores in the system.

For more information, please see https://www.elastic.co/guide/en/logstash/current/logstash-settings-file.html.

lsheap
~~~~~~~~~~~~~

By default, if total available memory is 8GB or greater, the Logstash heap size in ``/etc/logstash/jvm.options`` is configured (during setup) to equal 25% of available memory, but no greater than 4GB.

See
https://www.elastic.co/guide/en/elasticsearch/guide/current/heap-sizing.html#compressed_oops
for more details.

You may need to adjust the value depending on your system's performance (running ``sudo so-logstash-restart`` after).

Adding New Logs or Modifying Existing Parsing
---------------------------------------------


Parsing
~~~~~~~

Configuration files for custom parsing can be placed in ``/etc/logstash/custom``. These will automatically get copied over to ``/etc/logstash/conf.d`` during the starting of Logstash.

.. note::

    If you are using a distributed or heavy distributed `deployment type <architecture#deployment-types>`__, it is best practice to put your custom configuration files in the ``/etc/logstash/custom`` directory on the Master node.  The custom configuration files will then be replicated every 15 minutes or immediately if you use `Salt <Salt#features>`__ to force the replication to take place.

After adding your custom configuration file(s), restart Logstash and check the log(s) for errors:

::

   sudo so-logstash-restart && sudo tail -f /var/log/logstash/logstash.log

Mapping Templates
~~~~~~~~~~~~~~~~~

Logstash loads default mapping templates for Elasticsearch to use from ``/etc/logstash``.

The three templates currently being used include:

``logstash-template.json`` - applies to ``logstash-*`` indices

``logstash-ossec-template.json`` - applies to ``logstash-ossec-*`` indices

``beats-template.json`` - applies to ``logstash-beats-*`` indices

Currently, new fields that do not match the template are stored in Elasticsearch, however, they are not indexed, unless provided in a mapping template.

If sending in custom logs to Security Onion that may not match existing fields for existing indices, it is recommended to create a dedicated index for the log source, as well as define a mapping template and output file for the custom log source.

To make sure Logstash can read the custom template:

#. Place the template in ``/etc/logstash/custom``.
#. Make sure the template is added to ``LOGSTASH_OPTIONS`` in ``/etc/nsm/securityonion.conf``:
   ``LOGSTASH_OPTIONS="--volume /etc/logstash/testme-template.json:/testme-template.json:ro"``
#. Make sure the custom template is referenced in the appropriate output file (place the output file in ``/etc/logstash/custom``, then modify it.).
#. Restart Logstash.

You can check to see if templates are loaded by typing something like the following at a command prompt:

::

   sudo so-elasticsearch-template-list

You can also test the template before restarting Logstash, by using the following command:

::

   sudo so-elasticsearch-template-add

If mappings defined in the template are different than in existing indices, you will receive mapping conflicts in Kibana.

To avoid this, either remove the existing indices, wiping all data, or `re-index <re‐indexing.html>`__.

Logging
~~~~~~~

Log file settings can be adjusted in ``/etc/logstash/log4j2.properties``. Currently, logs are set to rollover daily, and configured to be deleted after 7 days.

Options
~~~~~~~

You can specify your own custom options to be appended to the Logstash startup command, by editing ``LOGSTASH_OPTIONS`` in
``/etc/nsm/securityonion.conf``.

Queue
-----

Memory-backed
~~~~~~~~~~~~~

From:
https://www.elastic.co/guide/en/logstash/current/persistent-queues.html

    By default, Logstash uses in-memory bounded queues between pipeline
    stages (inputs → pipeline workers) to buffer events. The size of
    these in-memory queues is fixed and not configurable.

Persistent
~~~~~~~~~~

From:
https://www.elastic.co/guide/en/logstash/current/persistent-queues.html

    In order to protect against data loss during abnormal termination,
    Logstash has a persistent queue feature which will store the
    message queue on disk. Persistent queues provide durability of data
    within Logstash.

If you experience adverse effects using the default memory-backed queue, you can configure a disk-based persistent queue by un-commenting the following lines in ``/etc/logstash/logstash.yaml`` and  modifying the values as appropriate:

::

    #queue.type: persisted
    #queue.max_bytes: 1gb

Then restart Logstash:

::

   sudo so-logstash-restart

| More information:
| https://www.elastic.co/guide/en/logstash/current/persistent-queues.html

Queue Max Bytes
~~~~~~~~~~~~~~~

    The total capacity of the queue in number of bytes. Make sure the
    capacity of your disk drive is greater than the value >you specify
    here. If both queue.max\_events and queue.max\_bytes are specified,
    Logstash uses whichever criteria is reached >first.

Dead Letter Queue
~~~~~~~~~~~~~~~~~

If you want to check for dropped events, you can enable the dead letter queue. This will write all records that are not able to make it into Elasticsearch into a sequentially-numbered file (for each start/restart of Logstash).

This can be achieved by adding the following to ``/etc/logstash/logstash.yml``:

::

dead_letter_queue.enable: true

and restarting Logstash:

::

   sudo so-logstash-restart

The dead letter queue files are located in ``/nsm/logstash/dead_letter_queue/main/``.

| More information:
| https://www.elastic.co/guide/en/logstash/current/dead-letter-queues.html

Redis
~~~~~

When using storage nodes, Logstash on the master server outputs to `Redis <Redis>`__ (on the master server). Redis queues events from the Logstash output (on the master) and the Logstash input on the storage node(s) pull(s) from Redis. If you notice new events aren't making it into Kibana, you may want to first check Logstash on the master, then the redis `queue <Redis#queue>`__.

Data Fields
-----------

Logstash process Zeek logs, syslog, IDS alerts, etc., formatting said data into many different data fields, as described in the `Data Fields <Data-Fields>`__ section.

Log
---

The Logstash log is located at ``/var/log/logstash/logstash.log``.

Errors
------

Read-Only
~~~~~~~~~

::

   [INFO ][logstash.outputs.elasticsearch] retrying failed action with response code: 403 ({"type"=>"cluster_block_exception", "reason"=>"blocked by: [FORBIDDEN/12/index read-only / allow delete (api)];"})

This error is usually caused by the ``cluster.routing.allocation.disk.watermark`` (``low``,\ ``high``) being exceeded.

You may want to check ``/var/log/elasticsearch/<hostname>.log`` to see specifically which indices have been marked as read-only.

Additionally, you can run the following command to allow writing to the affected indices:

::

   curl -XPUT -H 'Content-Type: application/json' localhost:9200/<your_index>/_settings -d'{ "index.blocks.read_only": false }'

LOGSTASH_MINIMAL
----------------

We now have a ``LOGSTASH_MINIMAL`` mode which will offload log parsing to Elasticsearch ingest node.  This allows Logstash to run in as little as 200MB RAM and start instantly.  

.. note::

    Elasticsearch ingest node parsing currently only supports standard IDS alerts and Zeek logs in JSON format.  

Starting in ``securityonion-setup - 20120912-0ubuntu0securityonion327``, ``LOGSTASH_MINIMAL`` is enabled by default for new Production Mode deployments.  Evaluation Mode continues to default to traditional Logstash parsing.  If you want to run Evaluation Mode with ``LOGSTASH_MINIMAL``, you can run minimal Setup:

::

    sudo sosetup-minimal
    
If you've already run through Setup, you can enable ``LOGSTASH_MINIMAL`` on an existing installation by adding the following to ``/etc/nsm/securityonion.conf``:

::

    LOGSTASH_MINIMAL="yes"
    
You can then optionally decrease your Logstash heap size in ``/etc/logstash/jvm.options`` and restart Logstash:

::

    sudo so-logstash-restart
    
