.. _kibana:

Kibana
======

From https://www.elastic.co/kibana:

    Kibana is a free and open user interface that lets you visualize your Elasticsearch data and navigate the Elastic Stack. Do anything from tracking query load to understanding the way requests flow through your apps.

Screenshot
----------
.. image:: https://user-images.githubusercontent.com/1659467/95374575-81cc9e80-08ac-11eb-95ac-b2f1caf37461.png
  :target: https://user-images.githubusercontent.com/1659467/95374575-81cc9e80-08ac-11eb-95ac-b2f1caf37461.png

Dashboards
----------

We've included the old 16.04 dashboards in case you have any old 16.04 data. The new Security Onion 2 dashboards are all named with the ``Security Onion`` prefix and they should be used for any new data going forward.

If you ever need to reload dashboards, you can run the following command on your manager:

::

    so-kibana-config-load
    
Pivoting
--------

Kibana uses multiple hyperlinked fields to accelerate investigations and decision-making:

Transcript
~~~~~~~~~~

When present, clicking the hyperlinked ``_id`` field allows an analyst to pivot to full packet capture via our :ref:`pcap` interface. You can usually find the ``_id`` field as the rightmost column in the log panels at the bottom of the dashboards:

.. image:: https://user-images.githubusercontent.com/1659467/95376132-9c077c00-08ae-11eb-9675-8bddb3d20719.png
  :target: https://user-images.githubusercontent.com/1659467/95376132-9c077c00-08ae-11eb-9675-8bddb3d20719.png
  
You can also find the ``_id`` field by drilling into a row in the log panel.

.. image:: https://user-images.githubusercontent.com/1659467/95376213-c22d1c00-08ae-11eb-8ac0-73d7766d2d39.png
  :target: https://user-images.githubusercontent.com/1659467/95376213-c22d1c00-08ae-11eb-8ac0-73d7766d2d39.png

Indicator Dashboard
~~~~~~~~~~~~~~~~~~~

Several fields are hyperlinked to the Indicator dashboard to allow you to get all the information you can about a particular indicator. Here are just a few:

| ``uid``
| ``source.ip``
| ``source.port``
| ``destination.ip``
| ``destination.port``

Search Results
--------------

Search results in the dashboards and through Discover are limited to the first ``10`` results for a particular query. If you don't feel like this is adequate after narrowing your search, you can adjust the value for ``discover:sampleSize`` in Kibana by navigating to ``Stack Management`` -> ``Advanced Settings`` and changing the value. It may be best to change this value incrementally to see how it affects performance for your deployment.

Timestamps
----------

By default, Kibana will display timestamps in the timezone of your local browser. If you would prefer timestamps in UTC, you can go to ``Management`` --> ``Advanced Settings`` and set ``dateFormat:tz`` to ``UTC``.

Configuration
-------------

Kibana's configuration can be found in ``/opt/so/conf/kibana/``. However, please keep in mind that most configuration is managed with :ref:`salt`, so if you manually make any modifications in ``/opt/so/conf/kibana/``, they may be overwritten at the next salt update.

Diagnostic Logging
------------------

Kibana logs to ``/opt/so/log/kibana/kibana.log``.

If you try to access Kibana and it says ``Kibana server is not ready yet`` even after waiting a few minutes for it to fully initialize, then check ``/opt/so/log/kibana/kibana.log``. You may see something like:

::

    Another Kibana instance appears to be migrating the index. Waiting for that migration to complete. If no other Kibana instance is attempting migrations, you can get past this message by deleting index .kibana_6 and restarting Kibana
    
If that's the case, then you can do the following (replacing ``.kibana_6`` with the actual index name that was mentioned in the log):

::

    curl -k -XDELETE https://localhost:9200/.kibana_6

    sudo so-kibana-restart
    
If you then are able to login to Kibana but your dashboards don't look right, you can reload them as follows:

::

    so-kibana-config-load

More Information
----------------

.. seealso::

    For more information about Kibana, please see https://www.elastic.co/kibana.
