.. _logstash:

Logstash
========

From https://www.elastic.co/products/logstash :

    Logstash is a free and open server-side data processing pipeline that ingests data from a multitude of sources, transforms it, and then sends it to your favorite "stash."

When Security Onion 2 is running in Standalone mode or in a full distributed deployment, Logstash transports unparsed logs to :ref:`elasticsearch` which then parses and stores those logs. It's important to note that Logstash does NOT run when Security Onion is configured for Import or Eval mode. You can read more about that in the :ref:`architecture` section.

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

If total available memory is 8GB or greater, Setup sets the Logstash heap size to 25% of available memory, but no greater than 4GB.

For more information, please see https://www.elastic.co/guide/en/elasticsearch/guide/current/heap-sizing.html#compressed_oops.

You may need to adjust the value depending on your system's performance. The changes will be applied the next time the minion checks in. You can force it to happen immediately by running ``sudo salt-call state.apply logstash`` on the actual node or by running ``sudo salt $SENSORNAME_$ROLE state.apply logstash`` on the manager node.

Parsing
-------

Since Logstash no longer parses logs in Security Onion 2, modifying existing parsers or adding new parsers should be done via :ref:`elasticsearch`.

Adding New Logs
---------------

If you want to add a new log to the list of logs that are sent to :ref:`elasticsearch` for parsing, you can update the logstash pipeline configurations by adding to ``/opt/so/saltstack/local/salt/logstash/pipelines/config/custom/``. 

If you are modifying or adding a new ``manager`` pipeline, then first copy ``/opt/so/saltstack/default/pillar/logstash/manager.sls`` to ``/opt/so/saltstack/local/pillar/logstash/``, then add the following to the ``manager.sls`` file under the ``local`` directory:

::

    logstash:
      pipelines:
        manager:
          config:
            - so/0009_input_beats.conf      
            - so/0010_input_hhbeats.conf
            - so/9999_output_redis.conf.jinja
            - custom/9999_output_custom.conf.jinja
        
If you are modifying or adding a new ``search`` pipeline for all search nodes, then first copy ``/opt/so/saltstack/default/pillar/logstash/search.sls`` to ``/opt/so/saltstack/local/pillar/logstash/``, then add the following to the ``search.sls`` file under the ``local`` directory:

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
            - custom/9701_output_custom.conf.jinja

If you only want to modify the search pipeline for a single search node, then the process is similar to the previous example. However, instead of placing ``logstash:pipelines:search:config`` in ``/opt/so/saltstack/local/pillar/logstash/search.sls``, it would be placed in ``/opt/so/saltstack/local/pillar/minions/$hostname_searchnode.sls``. 

Logstash Parsing
----------------

If you want to add a legacy Logstash parser (not recommended) then you can copy the file to ``local``. Once the file is in ``local``, then depending on which nodes you want it to apply to, you can add the proper value to either ``/opt/so/saltstack/local/pillar/logstash/manager.sls``, ``/opt/so/saltstack/local/pillar/logstash/search.sls``, or ``/opt/so/saltstack/local/pillar/minions/$hostname_searchnode.sls`` as in the previous examples.

Forwarding Events to an External Destination
--------------------------------------------

Please keep in mind that we don't provide free support for third party systems, so this section will be just a brief introduction to how you would send syslog to external syslog collectors. If you need commercial support, please see https://www.securityonionsolutions.com.

Original Event Forwarding
-------------------------
To forward events to an external destination with minimal modifications to the original event, create a new custom configuration file on the manager in ``/opt/so/saltstack/local/salt/logstash/pipelines/config/custom/`` for the applicable output. We recommend using either the ``http``, ``tcp``, ``udp``, or ``syslog`` output plugin. At this time we only support the default bundled Logstash output plugins.

For example, to forward all Zeek events from the ``dns`` dataset, we could use a configuration like the following:

::

            output {
              if [module] =~ "zeek" and [dataset] =~ "dns" {
                tcp {
                  id => "cloned_events_out"
                  host => "192.168.x.x"
                  port => 1001
                  codec => "json_lines"
                }
              }
            }

.. warning::

    When using the ``tcp`` output plugin, if the destination host/port is down, it will cause the Logstash pipeline to be blocked.  To avoid this behavior, try using the other output options, or consider having forwarded logs use a separate Logstash pipeline.
    
    Also keep in mind that when forwarding logs from the manager, Suricata's ``dataset`` value will still be set to ``common``, as the events have not yet been processed by the Ingest Node configuration.
    
Copy ``/opt/so/saltstack/default/pillar/logstash/manager.sls`` to ``/opt/so/saltstack/local/pillar/logstash/manager.sls``, and append your newly created file to the list of config files used for the ``manager`` pipeline:

``- custom/myfile.conf``

Restart Logstash on the manager with ``so-logstash-restart``.

Monitor events flowing through the output with ``curl -s localhost:9600/_node/stats | jq .pipelines.manager``.

Modified Event Forwarding
--------------------------
To forward events to an external destination AFTER they have traversed the Logstash pipelines (NOT ingest node pipelines) used by Security Onion, perform the same steps as above, but instead of adding the reference for your Logstash output to ``manager.sls``, add it to ``search.sls`` instead, and then restart services on the search nodes with something like:

::

    sudo salt "*_search*" cmd.run "so-logstash-restart"

Monitor events flowing through the output with ``curl -s localhost:9600/_node/stats | jq .pipelines.search`` on the search nodes.

Please keep in mind that events will be forwarded from all applicable search nodes, as opposed to just the manager.

Queue
-----

Memory-backed
~~~~~~~~~~~~~

From https://www.elastic.co/guide/en/logstash/current/persistent-queues.html:

    By default, Logstash uses in-memory bounded queues between pipeline stages (inputs → pipeline workers) to buffer events. The size of these in-memory queues is fixed and not configurable.

Persistent
~~~~~~~~~~

If you experience adverse effects using the default memory-backed queue, you might consider a disk-based persistent queue. From https://www.elastic.co/guide/en/logstash/current/persistent-queues.html:

    In order to protect against data loss during abnormal termination, Logstash has a persistent queue feature which will store the message queue on disk. Persistent queues provide durability of data within Logstash.

Queue Max Bytes
~~~~~~~~~~~~~~~

    The total capacity of the queue in number of bytes. Make sure the capacity of your disk drive is greater than the value you specify here. If both queue.max\_events and queue.max\_bytes are specified, Logstash uses whichever criteria is reached first.

Dead Letter Queue
~~~~~~~~~~~~~~~~~

If you want to check for dropped events, you can enable the dead letter queue. This will write all records that are not able to make it into :ref:`elasticsearch` into a sequentially-numbered file (for each start/restart of Logstash).

This can be achieved by adding the following to the Logstash configuration:

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

Diagnostic Logging
------------------

The Logstash log file is located at ``/opt/so/log/logstash/logstash.log``. Log file settings can be adjusted in ``/opt/so/conf/logstash/etc/log4j2.properties``. By default, logs are set to rollover daily and purged after 7 days. Depending on what you’re looking for, you may also need to look at the :ref:`docker` logs for the container:

::

	sudo docker logs so-logstash

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

   curl -k -XPUT -H 'Content-Type: application/json' https://localhost:9200/<your_index>/_settings -d'{ "index.blocks.read_only": false }'

More Information
----------------

.. seealso::

    For more information about Logstash, please see https://www.elastic.co/products/logstash.
