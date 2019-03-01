After Installation
==================

-  Verify services are running:
   
   ::
   
      sudo so-status

-  If any services are not running, try starting them:

   ::
   
      sudo so-start

-  If you have problems with Snort/Suricata/Bro/PF_RING and have UEFI Secure Boot enabled, please see `Secure Boot <Secure-Boot>`__.

-  Log into `<Sguil>`_, `<Squert>`_, and `<Kibana>`_ and verify that you have events in the interfaces.  If you don't have any IDS alerts, you can try to generate one by typing the following at a terminal (only works if you have Internet access):

   ::
   
      curl http://testmyids.com
      
-  Full-time analysts may want to use an `Analyst VM <Analyst-VM>`__.

-  Setup defaults to only opening port 22 in the `firewall <Firewall>`__. If you want to connect analyst VMs, `<Wazuh>`_ agents, or syslog devices, you can run the `<so-allow>`_ utility which will walk you through creating firewall rules to allow these devices to connect.

-  Run the following to see how your sensor is coping with the load. You should check this on a daily basis to make sure your sensor is not dropping packets. Consider adding it to a cronjob and having it emailed to you (see the “configure email” link below).

   ::
   
      sudo sostat | less

-  Any IDS/NSM system needs to be tuned for the network it’s monitoring. Please see the `<tuning>`__ section. 

-  Review and categorize alerts in `<Sguil>`_  or `<Squert>`_ every day.  Categorizing alerts and tuning rules should be an iterative process with the goal being to categorize *all* events every day.  You should only run the IDS rules you really care about.

     
Optional
--------

-  On the server running the Sguil database, set the ``DAYSTOKEEP`` variable in ``/etc/nsm/securityonion.conf`` to however many days you want to keep in your archive. The default is 30, but you may need to adjust it based on your organization’s detection/response policy and your available disk space.

-  If you’re monitoring IP address ranges other than private RFC1918 address space (192.168.0.0/16, 10.0.0.0/8, 172.16.0.0/12), you may need to update your sensor configuration with the correct IP ranges. Modern versions of Setup should automatically ask you for ``HOME_NET`` and configure these for you, but if you need to update it later, you would do the following. Sensor configuration files can be found in ``/etc/nsm/$HOSTNAME-$INTERFACE/``. Modify either ``snort.conf`` or ``suricata.yaml`` (depending on which IDS engine you chose during ``sosetup``) and update the ``HOME_NET`` variable. You may also want to consider updating the ``EXTERNAL_NET`` variable. Then update Bro’s network configuration in ``/opt/bro/etc/networks.cfg``. Finally, restart the sensor processes:

   ::
   
      sudo so-sensor-restart
      
-  exclude unnecessary traffic from your monitoring using `BPF <BPF>`__.

-  configure Ubuntu to use your preferred `NTP <NTP>`__ server.

-  add new Sguil user accounts with the following:

   ::
   
      sudo so-user-add

-  configure `Email <Email>`__ for alerting and reporting.

-  place ``/etc`` under version control. If your organization doesn't already have a standard version control tool, you can use `bazaar <https://help.ubuntu.com/12.04/serverguide/bazaar.html>`__, `git <http://git-scm.com/>`__, etckeeper:

   ::
   
      sudo apt install etckeeper

-  need “remote desktop” access to your Security Onion sensor or server? One option is SSH X-Forwarding, but if you want something more rdp-like, you can install xrdp:

   ::
   
      sudo apt install xrdp

Learn More
----------

-  Read more about the tools contained in Security Onion:
   `Tools <Tools>`__
