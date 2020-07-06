.. _post-installation:

After Installation
==================

Adjust firewall rules using so-allow
------------------------------------
All firewall rules for the entire deployment are managed on the management server. You will want to allow your own IP address (or range) to access Security Onion as an analyst. Run the command below and select the analyst role:

 ::
 
   sudo so-allow

This process can take up to a minute if a salt highstate on the management server is already running.

Services
--------

-  Verify services are running:
   
   ::
   
      sudo so-status

Other
-----

-  Full-time analysts may want to connect using a dedicated :ref:`analyst-vm`.

-  Any IDS/NSM system needs to be tuned for the network it’s monitoring. Please see the :ref:`tuning` section. 

Optional
--------

-  Exclude unnecessary traffic from your monitoring using :ref:`bpf`.

-  Configure the OS to use your preferred :ref:`ntp` server.
