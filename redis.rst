.. _redis:

Redis
=====

From https://redis.io/:

    Redis is an open source (BSD licensed), in-memory data structure store, used as a database, cache and message broker. It supports data structures such as strings, hashes, lists, sets, sorted sets with range queries, bitmaps, hyperloglogs and geospatial indexes with radius queries.

During setup, you can choose to extend your manager node storage using separate search nodes. When you choose this option, Logstash on the manager node outputs to Redis. Search nodes then consume from Redis.

Queue
-----

To see how many logs are in the Redis queue:

::

    sudo so-redis-count

If the queue is backed up and doesn't seem to be draining, try stopping Logstash on the manager node:

::

    sudo so-logstash-stop

Then monitor the queue to see if it drains:

::

    watch 'sudo so-redis-count'

If the Redis queue looks okay, but you are still having issues with logs getting indexed into Elasticsearch, you will want to check the Logstash statistics on the search node(s).

.. |redis| image:: https://user-images.githubusercontent.com/16829864/37215984-91a348d4-2387-11e8-8c08-2e270b8fd986.png

Tuning
------

We configure Redis to use 10% of your total system memory.  If you have sufficient RAM available, you may want to increase the ``maxmemory`` setting in ``/opt/so/conf/redis/etc/redis.conf``. However, please note that the file is managed with :ref:`salt` which means that you'll need to copy ``/opt/so/saltstack/default/salt/redis/etc/redis.conf`` to ``/opt/so/saltstack/local/salt/redis/etc/redis.conf``, make your changes there, and then have :ref:`salt` update ``/opt/so/conf/redis/etc/redis.conf``.

Logstash on the manager node is configured to send to Redis.  For best performance, you may want to ensure that ``batch`` is set to ``true`` and then tune the ``batch_events`` variable to find the sweet spot for your deployment.

.. seealso::

    For more information about logstash's output plugin for Redis, please see https://www.elastic.co/guide/en/logstash/current/plugins-outputs-redis.html.

Logstash on search nodes pulls from Redis.  For best performance, you may want to tune ``batch_count`` and ``threads`` to find the sweet spot for your deployment. 

.. seealso::

    For more information about logstash's input plugin for Redis, please see https://www.elastic.co/guide/en/logstash/current/plugins-inputs-redis.html.

Diagnostic Logging
------------------
Redis logs can be found at ``/opt/so/log/redis/``.

More Information
----------------

.. seealso::

    For more information about Redis, please see https://redis.io/.
