Overview
========

Ubuntu configures its NTP service to pull time updates from the NTP Pool
Project and from ntp.ubuntu.com. From ``/etc/ntp.conf``:

::

    # Use servers from the NTP Pool Project. Approved by Ubuntu Technical Board
    # on 2011-02-08 (LP: #104525). See http://www.pool.ntp.org/join.html for
    # more information.
    server 0.ubuntu.pool.ntp.org
    server 1.ubuntu.pool.ntp.org
    server 2.ubuntu.pool.ntp.org
    server 3.ubuntu.pool.ntp.org

    # Use Ubuntu's ntp server as a fallback.
    server ntp.ubuntu.com

Modifying
=========

You may want to change this default NTP config to use your preferred NTP
provider. For more information, please see
https://help.ubuntu.com/lts/serverguide/NTP.html

IDS Alerts
==========

Anybody can join the NTP Pool Project and provide NTP service.
Occasionally, somebody provides NTP service from a residential DHCP
address that at some point in time may have also been used for TOR. This
results in IDS alerts for TOR nodes where the port is 123 (NTP). This is
another good reason to modify the NTP configuration to pull time updates
from your preferred NTP provider.
