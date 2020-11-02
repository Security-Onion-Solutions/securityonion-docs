.. _logstash:

Logstash
========

From https://www.elastic.co/products/logstash :

    Logstash is a free and open server-side data processing pipeline that ingests data from a multitude of sources, transforms it, and then sends it to your favorite "stash."

In Security Onion 2, Logstash transports unparsed logs to :ref:`elasticsearch` which then parses and stores those logs.

Configuration
-------------

You can configure Logstash using :ref:`salt`. Here are a few of the settings which you may need to tune in ``/opt/so/saltstack/local/pillar/minions/$MINION_$ROLE.sls`` under ``logstash_settings``.

ls_pipeline_batch_size
~~~~~~~~~~~~~~~~~~~~~~

    The maximum number of events an individual worker thread will collect from inputs before attempting to execute its filters and outputs. Larger batch sizes are generally more efficient, but come at the cost of increased memory overhead. This is set to 125 by default.
    
ls_pipeline_workers
~~~~~~~~~~~~~~~~~~~

    The number of workers that will, in parallel, execute the filter and output stages of the pipeline. If you find that events are backing up, or that the CPU is not saturated, consider increasing this number to better utilize machine processing power. By default this value is set to the number of cores in the system.

For more information, please see https://www.elastic.co/guide/en/logstash/current/logstash-settings-file.html.

lsheap
~~~~~~~~~~~~~

By default, if total available memory is 8GB or greater, the Logstash heap size in ``/etc/logstash/jvm.options`` is configured (during setup) to equal 25% of available memory, but no greater than 4GB.

For more information, please see https://www.elastic.co/guide/en/elasticsearch/guide/current/heap-sizing.html#compressed_oops.

You may need to adjust the value depending on your system's performance. The changes will be applied the next time the minion checks in. You can force it to happen immediately by running ``sudo salt-call state.apply logstash`` on the actual node or by running ``sudo salt $SENSORNAME_$ROLE state.apply logstash`` on the manager node.

Adding New Logs or Modifying Existing Parsing
---------------------------------------------

Customizing Parsing
~~~~~~~~~~~~~~~~~~~

Since Logstash no longer parses logs in Security Onion 2, modifying existing parsers or adding new parsers should be done via :ref:`elasticsearch`.

All custom logstash pipeline configurations should be places in /opt/so/saltstack/local/salt/logstash/pipelines/config/custom. 

If you are modifying/adding a new manager pipeline add the following to your global.sls files

  ::
logstash:
  pipelines:
    manager:
      config:
        - so/0009_input_beats.conf      
        - so/0010_input_hhbeats.conf
        - so/9999_output_redis.conf.jinja
        - custom/9999_output_custom.jinja
        
If you are modifying/adding a new search pipeline add the folowing to global.sls

  ::
logstash:
  pipelines:
    search:
      config:
        - so/0900_input_redis.conf.jinja
        - so/9000_output_zeek.conf.jinja
        - so/9002_output_import.conf.jinja
        - so/9034_output_syslog.conf.jinja
        - so/9100_output_osquery.conf.jinja
        - so/9400_output_suricata.conf.jinja
        - so/9500_output_beats.conf.jinja
        - so/9600_output_ossec.conf.jinja
        - so/9700_output_strelka.conf.jinja
        - custom/9701_output_custom.jinja

both:

  ::
logstash:
  pipelines:
    manager:
      config:
        - so/0009_input_beats.conf      
        - so/0010_input_hhbeats.conf
        - so/9999_output_redis.conf.jinja
        - custom/9999_output_custom.jinja
    search:
      config:
        - so/0900_input_redis.conf.jinja
        - so/9000_output_zeek.conf.jinja
        - so/9002_output_import.conf.jinja
        - so/9034_output_syslog.conf.jinja
        - so/9100_output_osquery.conf.jinja
        - so/9400_output_suricata.conf.jinja
        - so/9500_output_beats.conf.jinja
        - so/9600_output_ossec.conf.jinja
        - so/9700_output_strelka.conf.jinja
        - custom/9701_output_custom.jinja


Forwarding Events to an External Destination
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To forward events to an external destination create a new custom configuration file. Clone event and match on the output. We recommend using either the http or tcp output plugin. At this time we only support the default bundled Logstash output plugins.

Adding Legacy Logstash Parsers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you want to add a legacy Logstash parser (not recommended) then you can copy the file to local. Once the file is in local you can add the proper value to the global.sls as the example above with - custom/9701_output_custom.jinja.

Queue
-----

Memory-backed
~~~~~~~~~~~~~

From https://www.elastic.co/guide/en/logstash/current/persistent-queues.html:

    By default, Logstash uses in-memory bounded queues between pipeline stages (inputs → pipeline workers) to buffer events. The size of these in-memory queues is fixed and not configurable.

Persistent
~~~~~~~~~~

From https://www.elastic.co/guide/en/logstash/current/persistent-queues.html:

    In order to protect against data loss during abnormal termination, Logstash has a persistent queue feature which will store the message queue on disk. Persistent queues provide durability of data within Logstash.

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

    The total capacity of the queue in number of bytes. Make sure the capacity of your disk drive is greater than the value you specify here. If both queue.max\_events and queue.max\_bytes are specified, Logstash uses whichever criteria is reached first.

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

When using search nodes, Logstash on the manager node outputs to :ref:`redis` (which also runs on the manager node). Redis queues events from the Logstash output (on the manager node) and the Logstash input on the search node(s) pull(s) from Redis. If you notice new events aren't making it into Kibana, you may want to first check Logstash on the manager node and then the redis `queue <Redis#queue>`__.

Log
---

The Logstash log file is located at ``/opt/so/log/logstash/logstash.log``. Log file settings can be adjusted in ``/opt/so/conf/logstash/etc/log4j2.properties``. Currently, logs are set to rollover daily, and configured to be deleted after 7 days.

Errors
------

Read-Only
~~~~~~~~~

::

   [INFO ][logstash.outputs.elasticsearch] retrying failed action with response code: 403 ({"type"=>"cluster_block_exception", "reason"=>"blocked by: [FORBIDDEN/12/index read-only / allow delete (api)];"})

This error is usually caused by the ``cluster.routing.allocation.disk.watermark`` (``low``,\ ``high``) being exceeded.

You may want to check ``/opt/so/log/elasticsearch/<hostname>.log`` to see specifically which indices have been marked as read-only.

Additionally, you can run the following command to allow writing to the affected indices:

::

   curl -XPUT -H 'Content-Type: application/json' localhost:9200/<your_index>/_settings -d'{ "index.blocks.read_only": false }'
