After Installation
==================

-  Verify services are running:
   
   ::
   
      sudo so-status

-  If any services are not running, try starting them:

   ::
   
      sudo so-start

-  If you have problems with Snort/Suricata/Bro/PF_RING and have UEFI Secure Boot enabled, please see `Secure Boot <Secure-Boot>`__.

Tuning / Miscellaneous
----------------------

-  If you have Internet access, you can generate an IDS alert by typing the following at a terminal:

   ::
   
      curl http://testmyids.com

-  Setup defaults to only opening port 22 in the `firewall <Firewall>`__. If you need to connect `<Wazuh>`_ agents, syslog devices, or analyst VMs, you can run the `<so-allow>`_ utility which will walk you through creating firewall rules to allow these devices to connect.

-  Full-time analysts should use an `Analyst VM <Analyst-VM>`__.

-  Login to Sguil and review your IDS alerts. Squert and Kibana can be accessed by visiting https://YourSecurityOnionBox/ (please note the HTTPS) for additional in-depth analysis.

-  Run the following to see how your sensor is coping with the load. You should check this on a daily basis to make sure your sensor is not dropping packets. Consider adding it to a cronjob and having it emailed to you (see the “configure email” link below).

   ::
   
      sudo sostat | less

-  Any IDS/NSM system needs to be tuned for the network it’s monitoring. Please see `ManagingAlerts <ManagingAlerts>`__. You should only run the signatures you really care about.

-  Review and categorize events every day with the goal being to categorize all events every day. Neglecting to do so will result in database/Sguil issues as the number of uncategorized events continues to increase on a daily basis.

-  On the server running the Sguil database, set the ``DAYSTOKEEP`` variable in ``/etc/nsm/securityonion.conf`` to however many days you want to keep in your archive. The default is 30, but you may need to adjust it based on your organization’s detection/response policy and your available disk space.

-  If you’re monitoring IP address ranges other than private RFC1918 address space (192.168.0.0/16, 10.0.0.0/8, 172.16.0.0/12), you may need to update your sensor configuration with the correct IP ranges. Modern versions of Setup should automatically ask you for ``HOME_NET`` and configure these for you, but if you need to update it later, you would do the following. Sensor configuration files can be found in ``/etc/nsm/$HOSTNAME-$INTERFACE/``. Modify either ``snort.conf`` or ``suricata.yaml`` (depending on which IDS engine you chose during ``sosetup``) and update the ``HOME_NET`` variable. You may also want to consider updating the ``EXTERNAL_NET`` variable. Then update Bro’s network configuration in ``/opt/bro/etc/networks.cfg``. Finally, restart the sensor processes:

   ::
   
      sudo so-sensor-restart
      
-  `Disable any unneeded sensor processes <DisablingProcesses>`__.

-  Tune `<PF_RING>`_ or `<AF-PACKET>`_ based on your traffic load.

-  If your network traffic load is high, you may need to review `<High-Performance-Tuning>`_.

Optional
--------

-  *Optional:* exclude unnecessary traffic from your monitoring using `BPF <BPF>`__.

-  *Optional:* configure Ubuntu to use your preferred `NTP <NTP>`__ server.

-  *Optional:* add new Sguil user accounts with the following:

   ::
   
      sudo so-user-add

-  *Optional*, but highly recommended: configure `Email <Email>`__ for alerting and reporting.

-  *Optional:* place ``/etc`` under version control. If your organization doesn't already have a standard version control tool, you can use `bazaar <https://help.ubuntu.com/12.04/serverguide/bazaar.html>`__, `git <http://git-scm.com/>`__, etckeeper:

   ::
   
      sudo apt-get install etckeeper

-  *Optional:* need “remote desktop” access to your Security Onion sensor or server? We recommend SSH X-Forwarding as shown above, but if you want something more rdp-like, you can install xrdp:

   ::
   
      sudo apt-get install xrdp

Learn More
----------

-  Read more about the tools contained in Security Onion:
   `Tools <Tools>`__
