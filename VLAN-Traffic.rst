Latest updates
==============

If you're running Security Onion 14.04 with all updates applied as of
2016/08/31, then you should be able to monitor VLAN tagged traffic with
no special configuration. The current version of Suricata will
automatically increase its snaplen setting to account for VLAN tags and
our current NSM scripts will automatically update Snort's snaplen in the
same way.

Older software
==============

If for some reason you are unable to install the latest updates and have
to run older software, you may need to modify your configuration to
avoid inconsistent alerting. Here are some things to consider.

Snort
-----

Snort's default Snap Length is 1514. To allow for VLAN tags, you can
increase this to 1518 by setting the following option in your Snort
configuration file ``/etc/nsm/HOSTNAME-INTERFACE/snort.conf``:

::

    config snaplen: 1518

(However, please keep in mind that our latest NSM scripts will set
Snort's snaplen setting on the command line, overriding what you set in
snort.conf.)

Restart Snort:

::

    sudo nsm_sensor_ps-restart --only-snort-alert

Test to ensure that you're now receiving consistent alerting.

Suricata
--------

When Suricata (older versions) receives packets from PF\_RING, it sets
the Snap Length (Bucket Len) to 1516 by default (the default MTU of the
sniffing interface 1500 plus 16). To increase Suricata's Snap Length to
1518, increase the MTU of your sniffing interface to 1502 by adding the
following line to the sniffing interface section of your network
interface config file ``/etc/network/interfaces``:

::

        mtu 1502

(Please note that setting a non-standard MTU like this may result in the
interface not coming up correctly on boot.)

Then bounce the interface as follows (replacing eth1 with your actual
sniffing interface):

::

    sudo ifdown eth1
    sudo ifup eth1

If you have inconsistent VLAN tags (for example, VLAN tags in one
direction but not the other), then you may also need to set the
following option in your Suricata configuration file
``/etc/nsm/HOSTNAME-INTERFACE/suricata.yaml``:

::

    vlan:
      use-for-tracking: false

Restart Suricata:

::

    sudo nsm_sensor_ps-restart --only-snort-alert

Test to ensure that you're now receiving consistent alerting.
