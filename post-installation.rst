After Installation
==================

Resolution
----------

If you need to change the screen resolution of your Security Onion installation:

-  click the ``Applications`` menu in the upper left corner
-  click ``System Tools``
-  click ``Setttings``
-  click ``Displays``
-  select your display
-  choose your desired resolution
-  click ``Apply``

If you prefer a CLI method for changing screen resolution, you can use `xrandr`. For a list of available screen resolutions, simply execute ``xrandr``. To set the screen resolution (replace ``W`` and ``H`` with the actual Width and Height desired):

::

    xrandr -s WxH

If you have limited screen resolution options and are in a virtualized environment, you may need to install the Virtual Tools for your virtualization solution. For example, this can happen if you're running VirtualBox and you can install the VirtualBox Extensions to get more resolution options.

Services
--------

-  Verify services are running:
   
   ::
   
      sudo so-status

-  If any services are not running, try starting them:

   ::
   
      sudo so-start

-  If you have problems with Snort/Suricata/Bro/PF-RING and have UEFI Secure Boot enabled, please see the `Secure Boot <Secure-Boot>`__ section.

-  Log into `<Sguil>`_, `<Squert>`_, and `<Kibana>`_ and verify that you have events in the interfaces.  If you don't have any IDS alerts, you can try to generate one by typing the following at a terminal (only works if you have Internet access):

   ::
   
      curl http://testmyids.com
      
Other
-----

-  Full-time analysts may want to connect using a separate `Analyst VM <Analyst-VM>`__.

-  Setup defaults to only opening port 22 in the `firewall <Firewall>`__. If you want to connect analyst VMs, `<Wazuh>`_ agents, or syslog devices, you can run the `<so-allow>`_ utility which will walk you through creating firewall rules to allow these devices to connect.

-  Run the following to see how your sensor is coping with the load. You should check this on a daily basis to make sure your sensor is not dropping packets. Consider adding it to a cronjob and having it emailed to you (see the “configure email” link below).

   ::
   
      sudo sostat | less

-  Any IDS/NSM system needs to be tuned for the network it’s monitoring. Please see the `<tuning>`__ section. 

-  Review and categorize alerts in `<Sguil>`_  or `<Squert>`_ on a daily basis.  Categorizing alerts and tuning rules should be an iterative process with the goal being to categorize *all* events every day.  You should only run the IDS rules you really care about.

     
Optional
--------

-  Exclude unnecessary traffic from your monitoring using `BPF <BPF>`__.

-  Configure Ubuntu to use your preferred `NTP <NTP>`__ server.

-  Add new Sguil user accounts with the following:

   ::
   
      sudo so-user-add

-  On the server running the Sguil database, set the ``DAYSTOKEEP`` variable in ``/etc/nsm/securityonion.conf`` to however many days you want to keep in your archive. The default is 30, but you may need to adjust it based on your organization’s detection/response policy and your available disk space.

-  If you’re monitoring IP address ranges other than private RFC1918 address space (192.168.0.0/16, 10.0.0.0/8, 172.16.0.0/12), you may need to update your sensor configuration with the correct IP ranges. Modern versions of Setup should automatically ask you for ``HOME_NET`` and configure these for you, but if you need to update it later, you would do the following. Sensor configuration files can be found in ``/etc/nsm/$HOSTNAME-$INTERFACE/``. Modify either ``snort.conf`` or ``suricata.yaml`` (depending on which IDS engine you chose during ``sosetup``) and update the ``HOME_NET`` variable. You may also want to consider updating the ``EXTERNAL_NET`` variable. Then update Bro’s network configuration in ``/opt/bro/etc/networks.cfg``. Finally, restart the sensor processes:

   ::
   
      sudo so-sensor-restart
      
-  Configure `Email <Email>`__ for alerting and reporting.

-  Place ``/etc`` under version control. If your organization doesn't already have a standard version control tool, you can use `bazaar <https://help.ubuntu.com/12.04/serverguide/bazaar.html>`__, `git <http://git-scm.com/>`__, etckeeper:

   ::
   
      sudo apt install etckeeper

-  Need “remote desktop” access to your Security Onion sensor or server? One option is SSH X-Forwarding, but if you want something more rdp-like, you can install xrdp:

   ::
   
      sudo apt install xrdp

Learn More
----------

-  Read more about the tools contained in Security Onion:
   `Tools <Tools>`__
