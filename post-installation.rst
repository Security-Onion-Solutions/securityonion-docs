.. _post-installation:

After Installation
==================

Adjust firewall rules using so-allow
------------------------------------
Depending on what kind of installation you did, the Setup wizard may have already walked you through adding firewall rules to allow your analyst IP address(es). If you need to allow other IP addresses, you can manually run :ref:`so-allow`.

Services
--------

-  Verify services are running:
   
   ::
   
      sudo so-status

Data Retention
--------------

-  Review the default :ref:`curator` configuration to see if you need to change any index retention settings.

Other
-----

-  Full-time analysts may want to connect using a dedicated :ref:`analyst-vm`.

-  Any IDS/NSM system needs to be tuned for the network it’s monitoring. Please see the :ref:`tuning` section. 

-  Configure the OS to use your preferred :ref:`ntp` server.
