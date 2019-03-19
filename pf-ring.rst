PF-RING
=======

PF-RING acts as a flow-based load balancer to allow us to spin up multiple instances of Snort/Suricata/Bro to handle more traffic than a single instance.

Starting in ``securityonion-setup - 20120912-0ubuntu0securityonion285``, running Setup will configure Suricata and Bro to use `<AF-PACKET>`__ instead of PF-RING.

Tuning
------

If you want to change the number of PF-RING instances after running Setup, you can do the following.

Snort/Suricata
--------------

To change the number of PF-RING instances for Snort or Suricata:

-  Stop sensor processes:

   ::

      sudo so-sensor-stop

-  Edit ``/etc/nsm/$HOSTNAME-$INTERFACE/sensor.conf`` and change the ``IDS_LB_PROCS`` variable to desired number of cores.

-  Start sensor processes:

   ::

      sudo so-sensor-start

If running Snort, ``so-sensor-start`` automatically spawns ``$IDS_LB_PROCS`` instances of Snort (using PF-RING), barnyard2, and snort_agent.

If running Suricata, ``so-sensor-start`` automatically copies ``$IDS_LB_PROCS`` into ``suricata.yaml`` and then Suricata spins up the PF-RING instances itself.

Bro
---

To change the number of PF-RING instances for Bro:

-  Stop bro:

   ::

      sudo so-bro-stop

-  Edit ``/opt/bro/etc/node.cfg`` and change the ``lb_procs`` variable to the desired number of cores.

-  Start bro:

   ::

     sudo so-bro-start

Slots
-----

If you've already run Setup and want to modify ``min_num_slots``, you can manually create/edit ``/etc/modprobe.d/pf_ring.conf``.

For example, to increase ``min_num_slots`` to ``65534``, do the following:
::

   echo "options pf_ring transparent_mode=0 min_num_slots=65534" | sudo tee /etc/modprobe.d/pf_ring.conf

After creating/editing ``/etc/modprobe.d/pf_ring.conf``, you'll need to reload the PF-RING module as follows (or just reboot):
::

   sudo so-sensor-stop
   sudo rmmod pf_ring
   sudo so-sensor-start

Updating
--------

Please see the `Upgrade <Upgrade>`__ section for notes on updating the PF-RING kernel module.
