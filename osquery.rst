.. _osquery:

osquery
=======

From https://osquery.io/:

    Osquery uses basic SQL commands to leverage a relational data-model to describe a device.
      
Fleet
-----

Security Onion includes Kolide Fleet to manage your osquery deployment. For more information, please see the :ref:`fleet` section.

Hunt or Kibana
------

All osquery logs can be found by using the following query: ``event.module: osquery``

Kibana Dashboard: Host Data --> Modules/Osquery
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This dashboard gives an overview of the osquery logs in the system. It should work out of the box no matter how you schedule or name your queries & packs as long as the default osquery configuration is used.


Community ID
------------

We sponsored the development of :ref:`community-id` support for osquery:

https://dactiv.llc/blog/correlate-osquery-network-connections/

More Information
----------------

.. seealso::

    For more information about osquery, please see https://osquery.io/.
