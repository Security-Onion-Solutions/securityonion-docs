Curator
=======

From:
https://www.elastic.co/guide/en/elasticsearch/client/curator/5.1/about.html#about

    Elasticsearch Curator helps you curate, or manage, your
    Elasticsearch indices and snapshots by:

    #. Obtaining the full list of indices (or snapshots) from the
       cluster, as the actionable list
    #. Iterate through a list of user-defined filters to progressively
       remove indices (or snapshots) from this actionable list
       as needed.
    #. Perform various actions on the items which remain in the
       actionable list.

Curator runs as a Docker container within Security Onion. It runs every
minute and is controlled by cron jobs defined in ``/etc/cron.d/``. When
Curator completes an action, it logs such activity in a log file found
in ``/var/log/curator/curator.log``.

Curator defaults to closing indices older than 30 days. To modify this,
change ``CURATOR_CLOSE_DAYS`` in ``/etc/nsm/securityonion.conf``.

As your disk reaches capacity, Curator starts deleting old indices to
prevent your disk from filling up. To change the limit, modify
``LOG_SIZE_LIMIT`` in ``/etc/nsm/securityonion.conf``.

Actions
-------

Curator ``actions`` are stored in ``/etc/curator/actions``. These
actions are run every minute from the cron jobs located in
``/etc/cron.d/curator-*``.

If you would like to add a new action, you can certainly do so, and add
another cron job in ``/etc/cron.d`` to automate the process.

For example, a new process for snapshotting would require a new action
file, Elasticsearch configuration, and a cron job to automate it all:

-  https://github.com/Security-Onion-Solutions/security-onion/wiki/Elasticsearch#snapshots
-  https://www.elastic.co/guide/en/elasticsearch/client/curator/current/snapshot.html
