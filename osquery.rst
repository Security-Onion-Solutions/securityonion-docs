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

To deploy osquery agents, go to the SOC Downloads page and download the osquery agent. When installed, that agent will automatically connect to the manager.

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
