.. _osquery:

osquery
=======

From https://osquery.io/:

    Osquery uses basic SQL commands to leverage a relational data-model to describe a device.
      
Fleet
-----

Security Onion includes Kolide Fleet to manage your osquery deployment. For more information, please see the :ref:`fleet` section.

Agents
------

To deploy an osquery agent, go to the :ref:`soc` Downloads page and download the osquery agent. Use :ref:`so-allow` to allow port ``8090`` from the osquery agent to the manager. Then install the osquery agent and it will then check into the manager and start showing up in :ref:`fleet`.

Hunt or Kibana
--------------

All osquery logs can be found by using the following query: ``event.module: osquery``

Kibana Dashboard: Host Data --> Modules/Osquery
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This dashboard gives an overview of the osquery logs in the system. As long as the default osquery configuration is used, this dashboard should work out of the box regardless of how you schedule or name your queries and packs.

Community ID
------------

We sponsored the development of :ref:`community-id` support for osquery:

https://dactiv.llc/blog/correlate-osquery-network-connections/

More Information
----------------

.. seealso::

    For more information about osquery, please see https://osquery.io/.
