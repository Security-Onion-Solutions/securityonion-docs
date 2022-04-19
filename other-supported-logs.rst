.. _other-supported-logs:

Other Supported Logs
====================

We include :ref:`elasticsearch` ingest parsers for several log types that don't have :ref:`filebeat` modules.

Example: RITA
-------------

Starting in Security Onion 2.3.120, we include :ref:`elasticsearch` ingest parsers for :ref:`rita` logs.

To have RITA logs ingested and parsed within Security Onion, do the following:

In the relevant minion pillar add the following, then restart Filebeat on the minion(s):

::

   rita:
     enabled: True


This will tell Filebeat to start the Filebeat inputs for RITA.  The inputs look for the following files:

``/nsm/rita/beacons.csv``

``/nsm/rita/exploded-dns.csv``

``/nsm/rita/long-connections.csv``  

``/nsm/rita/open-connections.csv``  

If you are installing Filebeat on a non-Security Onion node, or your filenames differ, you will need to copy the Filebeat configuration from ``/opt/so/saltstack/default/salt/filebeat/etc/filebeat.yml`` to ``/opt/so/saltstack/local/salt/filebeat/etc/filebeat.yml`` (or modify on the non-Security Onion node in the native Filebeat configuration file) and emulate the path/filename accordingly.

Once ingested into Security Onion, you should be able to search for RITA logs in Hunt using ``event.module:rita | groupby event.dataset``.

Summary:
########
.. image:: https://user-images.githubusercontent.com/16829864/164031803-35586e1a-2c51-4c1d-bdc6-1f8034ca35c6.png
 :target: https://user-images.githubusercontent.com/16829864/164031803-35586e1a-2c51-4c1d-bdc6-1f8034ca35c6.png
 
Connections:
############ 
.. image:: https://user-images.githubusercontent.com/16829864/164031943-e7a7c296-16f5-4eaf-a4df-efb7779a98d0.png
 :target: https://user-images.githubusercontent.com/16829864/164031943-e7a7c296-16f5-4eaf-a4df-efb7779a98d0.png
 
DNS:
####

.. image:: https://user-images.githubusercontent.com/16829864/164031973-eadac445-7327-442e-805c-b30fd671b9e6.png
 :target: https://user-images.githubusercontent.com/16829864/164031973-eadac445-7327-442e-805c-b30fd671b9e6.png

Beacon:
######

.. image::  https://user-images.githubusercontent.com/16829864/164031876-e59dccf7-95cb-4e90-90c1-6eb2e0b8acfa.png
 :target:  https://user-images.githubusercontent.com/16829864/164031876-e59dccf7-95cb-4e90-90c1-6eb2e0b8acfa.png

Alert:
######

If the value for `beacon.score` in a `beacon` record equals `1`, an alert will be generated and viewable in SOC Alerts.

.. image:: https://user-images.githubusercontent.com/16829864/164031733-5633fd36-2e6e-4e93-aecc-6b13e21a2114.png
 :target: https://user-images.githubusercontent.com/16829864/164031733-5633fd36-2e6e-4e93-aecc-6b13e21a2114.png
