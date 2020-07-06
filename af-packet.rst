.. _af-packet:

AF-PACKET
=========

If you want to change the number of AF-PACKET workers after running Setup, you can do the following.

Suricata
--------

To change the number of AF-PACKET workers for `<Suricata>`_:

-  Stop sensor processes:

   ::

      sudo so-suricata-stop

-  Edit ``/opt/so/saltstack/local/pillar/minions/$SENSORNAME_$ROLE.sls`` and change the ``suriprocs`` variable to the desired number of workers.

-  Start sensor processes:

   ::

      sudo so-suricata-start

-  ``so-suricata-start`` automatically copies ``$IDS_LB_PROCS`` into ``suricata.yaml`` and then Suricata creates the appropriate number of AF-PACKET workers.

Zeek
----

To change the number of AF-PACKET workers for `<Zeek>`_:

-  Stop Zeek:

   ::

      sudo so-zeek-stop

-  Edit ``/opt/so/saltstack/local/pillar/minions/$SENSORNAME_$ROLE.sls`` and change the ``bro_lbprocs`` variable to the desired number of cores.

-  Start Zeek:

   ::

      sudo so-zeek-start

tcpreplay
---------

.. warning::

   If you try to test AF-PACKET load balancing using tcpreplay locally, please note that load balancing will not work properly and all (or most) traffic will be handled by the first worker in the AF-PACKET cluster.  If you need to test AF-PACKET load balancing properly, you can run tcpreplay on another machine connected to your AF-PACKET machine.
