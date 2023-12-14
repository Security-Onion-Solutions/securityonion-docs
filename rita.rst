.. _rita:

RITA
====

From: https://github.com/activecm/rita

    RITA is an open source framework for network traffic analysis.

    The framework ingests Zeek Logs, and currently supports the following
    analysis features:

    | Beaconing: Search for signs of beaconing behavior in and out of
      your network
    | DNS Tunneling Search for signs of DNS based covert channels
    | Blacklisted: Query blacklists to search for suspicious domains and
      hosts

We can add RITA to Security Onion to enhance its current capabilities and leverage the great work from the folks at `Active Countermeasures <https://activecountermeasures.com/>`__. They've done a fantastic job of allowing RITA to be easy to integrate with Security Onion.

.. warning::

    Please keep in mind we do not officially support RITA, so installation is at your own risk.

Installation
------------

To install RITA on Security Onion:

Download the install script:

::

   wget https://raw.githubusercontent.com/activecm/rita/master/install.sh

Run the installer:

::

   sudo bash ./install.sh --disable-zeek

Configuration
-------------

You should set your own values for ``InternalSubnets`` in ``/etc/rita/config.yaml`` before importing
data into RITA. See https://github.com/activecm/rita#configuration-file for more information.

Usage
-----

You can then import logs with:

::

   rita import /nsm/zeek/logs/2019-09-04 dataset1

To see long connections, type:

::

   rita show-long-connections dataset1

To see beacons, type:

::

   rita show-beacons dataset1

Finally, you can issue an HTML report (viewable in browser) by typing:

::

   rita html-report

See other available commands with:

::

   rita --help

Logs
----

We include :ref:`elasticsearch` ingest parsers for Rita logs. To enable this support, add the following in the relevant :ref:`salt` minion pillar and then restart :ref:`elastic-agent` on the minion(s):

::

   rita:
     enabled: True

This will enable the following :ref:`elastic-agent` inputs:

``/nsm/rita/beacons.csv``

``/nsm/rita/exploded-dns.csv``

``/nsm/rita/long-connections.csv``

``/nsm/rita/open-connections.csv``

If you are installing :ref:`elastic-agent` on a non-Security Onion node or your filenames differ, you will need to copy the :ref:`elastic-agent` configuration from ``/opt/so/saltstack/default/salt/elastic-agent/etc/elastic-agent.yml`` to ``/opt/so/saltstack/local/salt/elastic-agent/etc/elastic-agent.yml`` (or modify on the non-Security Onion node in the normal Elastic Agent configuration file) and emulate the path/filename accordingly.

Once ingested into Security Onion, you should be able to search for :ref:`rita` logs in :ref:`dashboards` or :ref:`hunt` using ``event.module:rita | groupby event.dataset``. You should be able to see beacon, connection, and dns logs. If the value for ``beacon.score`` in a ``beacon`` record equals ``1``, an alert will be generated and viewable in :ref:`alerts`.

More Information
----------------

.. note::

    For more information about RITA, please see https://github.com/activecm/rita.
