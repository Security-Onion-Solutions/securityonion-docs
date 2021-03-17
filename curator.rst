.. _curator:

Curator
=======

From https://www.elastic.co/guide/en/elasticsearch/client/curator/current/about.html#about:

    Elasticsearch Curator helps you curate, or manage, your Elasticsearch indices and snapshots by:

    #. Obtaining the full list of indices (or snapshots) from the cluster, as the actionable list
    #. Iterate through a list of user-defined filters to progressively remove indices (or snapshots) from this actionable list as needed.
    #. Perform various actions on the items which remain in the actionable list.

Configuration
-------------
Curator ``actions`` are stored in ``/opt/so/conf/curator/action/``. These actions are run by cron jobs managed by :ref:`salt`.

Curator defaults to closing indices older than 30 days. To modify this, change ``cur_close_days`` in ``/opt/so/saltstack/local/pillar/minions/$SENSORNAME_$ROLE.sls``.

As your disk reaches capacity, Curator starts deleting old indices to prevent your disk from filling up. To change the limit, modify ``log_size_limit`` in ``/opt/so/saltstack/local/pillar/minions/$SENSORNAME_$ROLE.sls``.

New configurations should be stored in ``/opt/so/saltstack/local/salt/curator/files/action`` and will be copied into ``/opt/so/conf/curator/action/``.

Logs
----
When Curator completes an action, it logs its activity in a log file found in ``/opt/so/log/curator/``.

More Information
----------------

.. seealso::

    For more information about Curator, please see https://www.elastic.co/guide/en/elasticsearch/client/curator/current/about.html#about.
