AF-PACKET
=========

Starting in ``securityonion-setup - 20120912-0ubuntu0securityonion285``, running Setup will configure Suricata and Bro to use AF_PACKET. (Snort will continue to use `PF_RING <PF_RING>`__ for load balancing until Snort 3.0 is released.)

Tuning
------

If you want to change the number of AF_PACKET workers after running Setup, you can do the following.

Suricata
--------

To change the number of AF_PACKET workers for Suricata:

-  Stop sensor processes:

   ::

      sudo so-suricata-stop

-  Edit ``/etc/nsm/$HOSTNAME-$INTERFACE/sensor.conf`` and change the ``IDS_LB_PROCS`` variable to desired number of cores.

-  Start sensor processes:

   ::

      sudo so-suricata-start

-  ``so-suricata-start`` automatically copies ``$IDS_LB_PROCS`` into ``suricata.yaml`` and then Suricata creates the appropriate number of AF_PACKET workers.

Bro
---

To change the number of AF_PACKET workers for Bro:

-  Stop bro:

   ::

      sudo so-bro-stop

-  Edit ``/opt/bro/etc/node.cfg`` and change the ``lb_procs`` variable to the desired number of cores.

-  Start bro:

   ::

      sudo so-bro-start
