.. _osquery:

osquery
=======

From https://osquery.io/:

    Osquery uses basic SQL commands to leverage a relational data-model to describe a device.
      
Fleet
-----

Security Onion includes :ref:`fleet` to manage your osquery deployment. For more information, please see the :ref:`fleet` section.

Agents - Deployment
-------------------

To deploy an osquery agent to an endpoint, go to the :ref:`soc` Downloads page and download the proper osquery agent for the operating system of that endpoint. Use :ref:`so-allow` to allow the osquery agent to connect to port ``8090`` on the manager. Then install the osquery agent and it should check into the manager and start showing up in :ref:`fleet`.

Osquery will attempt to connect to the Manager via the Manager's IP or Hostname - whichever was selected during the Manager setup. If the hostname is used, the endpoints need to be able to resolve that hostname to the Manager's IP. See this value by running the following command on the Manager:  ``sudo salt-call pillar.get global:url_base``. If this value ever changes, the osquery packages under Downloads will need to be regenerated.

All the packages (except for the macOS PKG) are customized for the specific Grid they were downloaded from, and include all the necessary configuration to connect to that Grid. The macOS package is a stock Launcher package, and will require additional configuration once it has been deployed.

For macOS deployments, install the package and then configure the following:

 - Update ``/etc/so-launcher/secret`` with the :ref:`fleet` enroll secret. This can be found by running the following on the Manager:
 
 ::

    sudo salt-call pillar.get secrets:fleet_enroll-secret
 
 - Update ``/etc/so-launcher/launcher.flags`` - change the hostname to your Manager hostname, and change the port from ``443`` to ``8090``
  
 - Update ``/etc/so-launcher/roots.pem`` with the contents from the following file (on your Manager): ``/etc/ssl/certs/intca.crt``
 
 At this point, osquery should connect up to :ref:`fleet` within a couple minutes - if not, try to manually restart the osquery agent on the macOS endpoint:
 
 ::
 
   sudo launchctl kickstart -k system/com.so-launcher.launcher


Agents - Updating
-----------------

Security Onion uses Launcher as a management wrapper around Osquery. This allows for a simpler configuration as well as auto-updates of Launcher and Osquery. Launcher will check every hour to see if an update is available and, if so, will download and install it. This is the default configuration, but can be changed within the osquery Flags file.

In an airgap environment where the endpoints do not have Internet access, updated Osquery packages can be downloaded from the Security Onion Console and used to update the endpoints. Osquery packages are periodically updated on the Manager as new versions of Osquery are released. 


Agents - Troubleshooting
------------------------

Agent logs on Windows endpoints can be found under the Application channel in the Windows Eventlog - source is Launcher.


Agents - Regenerating Install Packages
--------------------------------------

To regenerate packages, run the following on the Manager (it will take up to 5 minutes to rebuild the packages):

::

    sudo salt-call state.apply fleet.event_gen-packages

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

| We sponsored the development of :ref:`community-id` support for osquery:
| https://webcache.googleusercontent.com/search?q=cache:RGB6YUatH0gJ:https://dactiv.llc/blog/correlate-osquery-network-connections/+&cd=1&hl=en&ct=clnk&gl=us

More Information
----------------

.. seealso::

    For more information about osquery, please see https://osquery.io/.
