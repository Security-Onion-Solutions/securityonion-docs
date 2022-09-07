.. _osquery:

osquery
=======

From https://osquery.io/:

    Osquery uses basic SQL commands to leverage a relational data-model to describe a device.
      
Agents - Deployment
-------------------

To deploy an osquery agent to an endpoint, go to the :ref:`soc` :ref:`downloads` page and download the proper osquery agent for the operating system of that endpoint. Use :ref:`so-allow` to allow the osquery agent to connect to port ``8090`` on the manager. Then install the osquery agent and it should check into the manager.

Osquery will attempt to connect to the manager via the manager's IP or Hostname - whichever was selected during the manager setup. If the hostname is used, the endpoints need to be able to resolve that hostname to the manager's IP. See this value by running the following command on the manager:  ``sudo salt-call pillar.get global:url_base``. If this value ever changes, the osquery packages under the :ref:`soc` :ref:`downloads` page will need to be regenerated.

All the packages (except for the macOS PKG) are customized for the specific Security Onion grid they were downloaded from, and include all the necessary configuration to connect to that grid.

Hunt or Kibana
--------------

All osquery logs can be found by using the following query:

::

    event.module: osquery

Kibana Dashboard: Host Data --> Modules/Osquery
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This dashboard gives an overview of the osquery logs in the system. As long as the default osquery configuration is used, this dashboard should work out of the box regardless of how you schedule or name your queries and packs.

Shipping Windows Eventlogs
--------------------------

Windows Eventlogs from the local Windows system can be shipped with osquery to Security Onion. Current parsing support extends to core Windows Eventlog channels ( ``Security`` , ``Application`` , ``System`` ) as well as Sysmon under the default channel location. These logs will show up in Security Onion as ``event.dataset: windows_eventlog`` or ``event.dataset: sysmon``.

- Confirm that you can successfully live query the logs: ``SELECT * FROM windows_events limit 10;``

- Save a new query: Query -> Manage Queries -> Create New Query ``SELECT * FROM windows_events;`` -> Save

- Add the new query to a query pack that targets a Windows host - how often it should run depends on log volume on the local host; start off with 180 seconds, differential logging: Packs -> Manage Packs -> Select + Edit Pack (Modify Targets for Windows only if needed, Modify Logging options as needed)

- Save pack + Enable pack, if needed.

Please refer to the osquery documentation for further information on osquery Evented tables: https://osquery.readthedocs.io/en/stable/development/pubsub-framework/#the-pub-sub-evented-data-framework-of-osquery

Community ID
------------

We sponsored the development of :ref:`community-id` support for osquery to allow for quicker and easier log correlation from different data types.

More Information
----------------

.. seealso::

    For more information about osquery, please see https://osquery.io/.
