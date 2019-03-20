AF-PACKET
=========

Modern versions of Setup will configure `<Suricata>`_ and `<Bro>`_ to use AF-PACKET instead of `<PF-RING>`_. (`<Snort>`_ will continue to use `<PF-RING>`__ for load balancing until Snort 3.0 is released.)

If you want to change the number of AF-PACKET workers after running Setup, you can do the following.

Suricata
--------

To change the number of AF-PACKET workers for `<Suricata>`_:

-  Stop sensor processes:

   ::

      sudo so-suricata-stop

-  Edit ``/etc/nsm/$HOSTNAME-$INTERFACE/sensor.conf`` and change the ``IDS_LB_PROCS`` variable to the desired number of workers.

-  Start sensor processes:

   ::

      sudo so-suricata-start

-  ``so-suricata-start`` automatically copies ``$IDS_LB_PROCS`` into ``suricata.yaml`` and then Suricata creates the appropriate number of AF-PACKET workers.

Bro
---

To change the number of AF-PACKET workers for `<Bro>`_:

-  Stop Bro:

   ::

      sudo so-bro-stop

-  Edit ``/opt/bro/etc/node.cfg`` and change the ``lb_procs`` variable to the desired number of cores.

-  Start Bro:

   ::

      sudo so-bro-start

tcpreplay
---------

If you try to test AF-PACKET load balancing using tcpreplay locally, please note that load balancing will not work properly and all (or most) traffic will be handled by the first worker in the AF-PACKET cluster.  If you need to test AF-PACKET load balancing properly, you can run tcpreplay on another machine connected to your AF-PACKET machine.
