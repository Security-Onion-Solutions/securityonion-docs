Setup
=====

| If you have multiple CPU cores, Setup will automatically ask you how
  many PF\_RING instances you'd like for Snort/Suricata (IDS engine
  processes) and Bro and will tell you how to adjust after the fact. As
  of securityonion-setup - 20120912-0ubuntu0securityonion201, Setup
  should analyze your system and recommend a certain number of PF\_RING
  instances:
| http://blog.securityonion.net/2016/03/securityonion-setup-20120912.html

Tuning
======

If you want to change the number of PF\_RING instances after running
Setup, you can do the following.

Snort/Suricata
==============

-  Stop sensor processes:
   ``sudo nsm_sensor_ps-stop``
-  Edit ``/etc/nsm/$HOSTNAME-$INTERFACE/sensor.conf`` and change the
   ``IDS_LB_PROCS`` variable to desired number of cores.
-  Start sensor processes:
   ``sudo nsm_sensor_ps-start``

If running Snort, the script automatically spawns $IDS\_LB\_PROCS
instances of Snort (using PF\_RING), barnyard2, and snort\_agent.

If running Suricata, the script automatically copies $IDS\_LB\_PROCS
into suricata.yaml and then Suricata spins up the PF\_RING instances
itself.

Bro
===

For Bro, you would do the following:

-  Stop bro:
   ``sudo nsm_sensor_ps-stop --only-bro``
-  Edit /opt/bro/etc/node.cfg and change the lb\_procs variable to the
   desired number of cores.
-  Start bro:
   ``sudo nsm_sensor_ps-start --only-bro``

Slots
=====

If you've already run Setup and want to modify min\_num\_slots, you can
manually create/edit /etc/modprobe.d/pf\_ring.conf.

| For example, to increase min\_num\_slots to 65534, do the following:
| ``echo "options pf_ring transparent_mode=0 min_num_slots=65534" | sudo tee /etc/modprobe.d/pf_ring.conf``

| After creating/editing ``/etc/modprobe.d/pf_ring.conf``, you'll need
  to reload the PF\_RING module as follows (or just reboot):
| ``sudo nsm_sensor_ps-stop``
| ``sudo rmmod pf_ring``\ 
| ``sudo nsm_sensor_ps-start``

Updating
========

Please see the `Upgrade <Upgrade>`__ page for notes on updating the
PF\_RING kernel module.
