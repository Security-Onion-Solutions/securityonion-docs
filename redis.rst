Redis
=====

From: https://redis.io/

    Redis is an open source (BSD licensed), in-memory data structure
    store, used as a database, cache and message broker. It supports
    data structures such as strings, hashes, lists, sets, sorted sets
    with range queries, bitmaps, hyperloglogs and geospatial indexes
    with radius queries. Redis has built-in replication, Lua scripting,
    LRU eviction, transactions and different levels of on-disk
    persistence, and provides high availability via Redis Sentinel and
    automatic partitioning with Redis Cluster.

During setup, you can choose to extend your master server storage using
separate storage nodes. When you choose this option, Logstash on the
master server outputs to redis. Storage nodes then consume from redis.

.. image:: https://user-images.githubusercontent.com/16829864/37215984-91a348d4-2387-11e8-8c08-2e270b8fd986.png

Queue
-----

To see how many logs are in the redis queue:

::

    redis-cli LLEN logstash:redis

If the queue is backed up and doesn't seem to be draining, try stopping
Logstash on the master server:

::

    sudo docker stop so-logstash

Then monitor the queue to see if it drains:

::

    watch 'redis-cli llen logstash:redis'

If the Redis queue looks okay, but you are still having issues with logs
getting indexed into Elasticsearch, you will want to check the Logstash
statistics on the storage node(s).

.. |redis| image:: https://user-images.githubusercontent.com/16829864/37215984-91a348d4-2387-11e8-8c08-2e270b8fd986.png
