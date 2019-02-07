Kibana
======

From https://www.elastic.co/products/kibana :

    Kibana lets you visualize your Elasticsearch data and navigate the
    Elastic Stack, so you can do anything from learning why you're
    getting paged at 2:00 a.m. to understanding the impact rain might
    have on your quarterly numbers.

Configuration
-------------

-  Configuration files for Kibana can be found in ``/etc/kibana/``.

-  Other configuration options for Kibana can be found in
   ``/etc/nsm/securityonion.conf``.

-  Kibana logs can be found in ``/var/log/kibana/``.

Pivoting
--------

Kibana uses multiple hyperlinked fields to accelerate investigations and
decision-making:

Transcript
~~~~~~~~~~

When present, clicking the ``_id`` field allows an analyst to pivot to
transcript via CapMe.

Indicator Dashboard
~~~~~~~~~~~~~~~~~~~

When present, clicking these fields allows an analyst to pivot to the
Indicator dashboard, where a variety of information is presented
relative to the term:value.

| ``uid``
| ``source_ip``
| ``source_port``
| ``destination_ip``
| ``destination_port``

Plugins
-------

To add a plugin to Kibana, you can expose the plugins directory to the
host filesystem and then copy your plugins to that directory. For
example, to load the
`kbn\_network <https://github.com/dlumbrer/kbn_network>`__ plugin you
can do something like this:

Create a directory in the host filesystem to store plugins:

::

    sudo mkdir -p /nsm/kibana/plugins

Download plugin to that directory:

::

    wget -qO- https://github.com/dlumbrer/kbn_network/releases/download/6.0.X-2/network_vis.tar.gz | sudo tar xvJ -C /nsm/kibana/plugins

Modify Kibana options to mount that directory into the container:

::

    sudo sed -i 's|KIBANA_OPTIONS=""|KIBANA_OPTIONS="--volume /nsm/kibana/plugins:/usr/share/kibana/plugins:ro"|g' /etc/nsm/securityonion.conf

Restart Kibana:

::

    sudo so-kibana-restart

Search Results
--------------

Search results in the dashboards and through Discover are limited to the
first ``10`` results for a particular query. If you don't feel like this
is adequate after narrowing your search, you can adjust the value for
``discover:sampleSize`` in Kibana by navigating to
``Management > Advanced Settings`` and changing the value. It may be
best to change this value incrementally to see how it affects
performance.

Search Request Timeout
----------------------

Sometimes searches can timeout in Kibana. To increase the timeout value
to wait longer for results from Elasticsearch, we can adjust the value
for ``elasticsearch.requestTimeout`` in ``/etc/kibana/kibana.yml`` and
restart Kibana.

For example to increase the timeout from the default of ``30`` seconds
to ``90`` seconds:

``sudo vi /etc/kibana/kibana.yml``

Add the following line:

``elasticsearch.requestTimeout: 90000``

Restart Kibana:

``sudo so-kibana-restart``
