.. _kibana:

Kibana
======

From https://www.elastic.co/kibana:

    Kibana is a free and open user interface that lets you visualize your Elasticsearch data and navigate the Elastic Stack. Do anything from tracking query load to understanding the way requests flow through your apps.

Screenshot
----------
.. image:: images/kibana.png
  :target: _images/kibana.png

Authentication
--------------

Starting in Security Onion 2.3.60, we support Elastic authentication via :ref:`so-elastic-auth`.

Dashboards
----------

We've included the old 16.04 dashboards in case you performed an in-place upgrade and have any old 16.04 data. These dashboards are named with the ``z16.04`` prefix and will only show old 16.04 data. The new Security Onion 2 dashboards are all named with the ``Security Onion`` prefix and they should be used for any new data going forward.

If you ever need to reload dashboards, you can run the following command on your manager:

::

    so-kibana-config-load
    
If you try to modify a default dashboard, your change will get overwritten. Instead of modifying, copy the desired dashboard and edit the copy.

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

Search results in the dashboards and through Discover are limited to the first ``100`` results for a particular query. If you don't feel like this is adequate after narrowing your search, you can adjust the value for ``discover:sampleSize`` in Kibana by navigating to ``Stack Management`` -> ``Advanced Settings`` and changing the value. It may be best to change this value incrementally to see how it affects performance for your deployment.

Timestamps
----------

By default, Kibana will display timestamps in the timezone of your local browser. If you would prefer timestamps in UTC, you can go to ``Management`` --> ``Advanced Settings`` and set ``dateFormat:tz`` to ``UTC``.

Configuration
-------------

Kibana's configuration can be found in ``/opt/so/conf/kibana/``. However, please keep in mind that most configuration is managed with :ref:`salt`, so if you manually make any modifications in ``/opt/so/conf/kibana/``, they may be overwritten at the next salt update.

Starting in 2.3.90, ``/opt/so/conf/kibana/etc/kibana.yml`` can be managed using the ``kibana`` pillar placed in the manager pillar file located under ``/opt/so/saltstack/local/pillar/minion``. The manager pillar file will end with either ``*_manger.sls``, ``*_mangersearch.sls``, ``*_standalone.sls``, or ``*_eval.sls`` depending on the manager type that was chosen during install. 

- An example of a Kibana pillar may look as follows:

::

  kibana:
    config:
      elasticsearch:
        requestTimeout: 120000
      data:
        autocomplete:
          valueSuggestions:
            timeout: 2000
            terminateAfter: 200000
      logging:
        root:
          level: warn

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
    
Features
--------

Starting in Security Onion 2.3.40, Elastic Features are enabled by default. If you had previously enabled Elastic Features and then upgrade to Security Onion 2.3.40 or higher, you may notice some features missing in Kibana. You can enable or disable features as necessary by clicking the main menu in the upper left corner, then click ``Stack Management``, then click ``Spaces``, then click ``Default``. For more information, please see https://www.elastic.co/guide/en/kibana/master/xpack-spaces.html#spaces-control-feature-visibility.

More Information
----------------

.. seealso::

    For more information about Kibana, please see https://www.elastic.co/kibana.
