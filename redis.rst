Redis
=====

From: https://redis.io/

    Redis is an open source (BSD licensed), in-memory data structure
    store, used as a database, cache and message broker. It supports
    data structures such as strings, hashes, lists, sets, sorted sets
    with range queries, bitmaps, hyperloglogs and geospatial indexes
    with radius queries.

During setup, you can choose to extend your master server storage using
separate storage nodes. When you choose this option, Logstash on the
master server outputs to redis. Storage nodes then consume from redis.

.. image:: https://user-images.githubusercontent.com/16829864/37215984-91a348d4-2387-11e8-8c08-2e270b8fd986.png

Queue
-----

To see how many logs are in the redis queue:

::

    sudo so-redis-count

If the queue is backed up and doesn't seem to be draining, try stopping
Logstash on the master server:

::

    sudo so-logstash-stop

Then monitor the queue to see if it drains:

::

    watch 'sudo so-redis-count'

If the Redis queue looks okay, but you are still having issues with logs
getting indexed into Elasticsearch, you will want to check the Logstash
statistics on the storage node(s).

.. |redis| image:: https://user-images.githubusercontent.com/16829864/37215984-91a348d4-2387-11e8-8c08-2e270b8fd986.png

Tuning
------

We configure redis to use 10% of your total system memory.  If you have sufficient RAM available, you might want to increase the ``maxmemory`` setting in ``/etc/redis/redis.conf``.

Logstash on the master server is configured to send to redis via ``/etc/logstash/conf.d.redis.output/9999_output_redis.conf``.  For best performance, you'll want to ensure that ``batch`` is set to ``true`` and then tune the ``batch_events`` variable to find the sweet spot for your deployment.  For more information, please see https://www.elastic.co/guide/en/logstash/current/plugins-outputs-redis.html.

Logstash on storage nodes pulls from redis via ``/etc/logstash/conf.d/0900_input_redis.conf``.  For best performance, you'll want to tune ``batch_count`` and ``threads`` to find the sweet spot for your deployment.  For more information, please see https://www.elastic.co/guide/en/logstash/current/plugins-inputs-redis.html#plugins-inputs-redis-batch_count.
