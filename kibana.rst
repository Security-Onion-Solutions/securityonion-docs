.. _kibana:

Kibana
======

From https://www.elastic.co/kibana:

    Kibana is a free and open user interface that lets you visualize your Elasticsearch data and navigate the Elastic Stack. Do anything from tracking query load to understanding the way requests flow through your apps.

Screenshot
----------
.. image:: https://user-images.githubusercontent.com/1659467/87230185-168e3180-c37c-11ea-90a5-57c9d2f34f7b.png

Configuration
-------------

Kibana's configuration can be found in ``/opt/so/conf/kibana/``.

Logging
-------

Kibana logs to ``/opt/so/log/kibana/kibana.log``.

Pivoting
--------

Kibana uses multiple hyperlinked fields to accelerate investigations and decision-making:

Transcript
~~~~~~~~~~

When present, clicking the hyperlinked ``_id`` field allows an analyst to pivot to pcap transcript via :ref:`pcap`.

.. image:: https://github.com/Security-Onion-Solutions/securityonion/wiki/images/kibana_pcap.png

Indicator Dashboard
~~~~~~~~~~~~~~~~~~~

Several fields are hyperlinked to the Indicator dashboard to allow you to get all the information you can about a particular indicator:

| ``uid``
| ``source.ip``
| ``source.port``
| ``destination.ip``
| ``destination.port``

Search Results
--------------

Search results in the dashboards and through Discover are limited to the first ``100`` results for a particular query. If you don't feel like this is adequate after narrowing your search, you can adjust the value for ``discover:sampleSize`` in Kibana by navigating to ``Management`` -> ``Advanced Settings`` and changing the value. It may be best to change this value incrementally to see how it affects performance.

Timestamps
----------

By default, Kibana will display timestamps in the timezone of your local browser. If you would prefer timestamps in UTC, you can go to ``Management`` --> ``Advanced Settings`` and set ``dateFormat:tz`` to ``UTC``.

Search Request Timeout
----------------------

Sometimes searches can timeout in Kibana. To increase the timeout value to wait longer for results from Elasticsearch, we can adjust the value for ``elasticsearch.requestTimeout`` in ``/opt/so/conf/kibana/etc/kibana.yml`` and restart Kibana.

For example to increase the timeout from the default of ``90`` seconds:

::

   sudo vi /opt/so/conf/kibana/etc/kibana.yml

Modify the following line:

::

   elasticsearch.requestTimeout: 90000

Finally, restart Kibana:

::

   sudo so-kibana-restart

Plugins
-------

.. warning::

    Please note that we do not officially support installing plugins.  Do so at your own risk!

To add a plugin to Kibana, you can expose the plugins directory to the host filesystem and then copy your plugins to that directory. For example, to load the `kbn\_network <https://github.com/dlumbrer/kbn_network>`__ plugin you can do something like the following.

Create a new directory in the host filesystem called ``/nsm/kibana/plugins`` to store plugins:

::

    sudo mkdir -p /nsm/kibana/plugins

Download your desired plugin and decompress it to ``/nsm/kibana/plugins``.  For example:

::

    wget -qO- https://github.com/dlumbrer/kbn_network/releases/download/6.5.X-1/network_vis-6-5.tar.gz | sudo tar zxv -C /nsm/kibana/plugins

Kibana now requires ``jquery.flot.log`` when re-optimizing, so let's create that:

::

    sudo touch /nsm/kibana/jquery.flot.log
    
Modify ``KIBANA_OPTIONS`` in ``/etc/nsm/securityonion.conf`` to mount ``/nsm/kibana/plugins`` directory and ``jquery.flot.log`` into the container:

::

    sudo sed -i 's|^KIBANA_OPTIONS.*$|KIBANA_OPTIONS="--volume /nsm/kibana/plugins:/usr/share/kibana/plugins:ro --volume /nsm/kibana/jquery.flot.log:/usr/share/kibana/src/ui/public/flot-charts/jquery.flot.log"|g' /etc/nsm/securityonion.conf

Restart Kibana:

::

    sudo so-kibana-restart

Monitor Kibana log file for errors:

::

    tail -f /opt/so/log/kibana/kibana.log

Kibana may take a few minutes to re-optimize.  Once that's complete, you should be able to log into Kibana and test your new plugin.

More Information
----------------

For more information about Kibana, please see https://www.elastic.co/kibana.
