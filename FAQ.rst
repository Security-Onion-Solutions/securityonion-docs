FAQ
===

| 
| 
| `Install / Update / Upgrade <#install-update-upgrade>`__\ 
| `Users / Passwords <#users-passwords>`__\ 
| `Support / Help <#support-help>`__\ 
| `Error messages <#error-messages>`__\ 
| `IPS/IDS engines <#ips-ids-engines>`__\ 
| `Security Onion internals <#security-onion-internals>`__\ 
| `Tuning <#tuning>`__\ 
| `sostat output <#sostat-output>`__\ 
| `Miscellaneous <#miscellaneous>`__\ 
| 
| 

Install / Update / Upgrade
------------------------------

Why won't the ISO image boot on my machine?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`TroubleBooting <TroubleBooting>`__

What's the recommended procedure for installing Security Onion?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`Installation Procedure <Installation>`__

Why does the installer crash when selecting a non-English language?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| We only support the English language at this time:
| `<Installation#language>`__

Why can't I see the Continue button on the Keyboard Layout screen of the installer?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| The Keyboard Layout screen may be larger than your screen resolution
  and so the Continue button may be off the screen to the right like
  this:
| https://launchpadlibrarian.net/207213663/Screenshot_wilyi386deskmanual_2015-05-22_13%3A05%3A41.png
| You can simply slide the window over until you see the Continue
  button. For more information, please see:
| https://bugs.launchpad.net/ubuntu/+source/ubiquity/+bug/1458039

How do I install Security Onion updates?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`Upgrade Procedure <Upgrade>`__

Why do I get ``Snort/Suricata/Bro`` errors after upgrading the ``kernel`` and ``pfring`` packages?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`Updating <Upgrade>`__

What do I need to do if I'm behind a proxy?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`Proxy Configuration <Proxy>`__

Ubuntu is saying that my kernel has reached EOL (End Of Life). Should I update to the newer HWE stack?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Please see our `HWE <HWE>`__ page.

Why does my VMware image rename ``eth0`` to ``eth1``?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Usually this happens when you clone a VM. VMware asks if you moved it or copied it. If you select "copied", it will change the MAC address to avoid duplication. At the next boot, Ubuntu's udev will see a new MAC address and create a new network interface (eth1). To fix this:

::
  
   sudo rm /etc/udev/rules.d/70-persistent-net.rules
   sudo reboot

Can I run Security Onion on Raspberry Pi or some other non-x86 box?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

No, we only support x86 and x86-64 architectures. Please see the `hardware <Hardware#32-bit-vs-64-bit>`__ page.

What's the difference between a ``server`` and a ``sensor``?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| **box** 
| Definition: A physical or virtual machine running the Security Onion
  operating system.
| 
| **server** 
| Definition: A set of processes that receive data from sensors and
  allow analysts to see and investigate that data. The set of processes
  includes sguild, mysql, and optionally the Elastic stack
  (Elasticsearch, Logstash, Kibana) and Curator. The server is also
  responsible for ruleset management.
| Naming convention: The collection of server processes has a server
  name separate from the hostname of the box. Security Onion always sets
  the server name to ``securityonion``.
| Configuration files: ``/etc/nsm/securityonion/``\ 
| Controlled by: ``/usr/sbin/nsm_server`` 
| 
| **server box**\ 
| Definition: A machine running the server processes. May optionally be
  running sensor processes.
| Example 1: User runs Quick Setup on machine with hostname
  securityonion and two ethernet interfaces. Setup creates a server and
  two sensors (``securityonion-eth0`` and ``securityonion-eth1``).
| Example 2: User runs Advanced Setup and chooses Server. Setup creates
  a server only (no sensor processes).
| 
| **sensor**\ 
| Definition: A set of processes listening on a network interface. The
  set of processes currently includes Snort/Suricata, netsniff-ng, and
  bro (although this is in constant flux as we add new capabilities and
  find better tools for existing capabilities).
| Naming convention: ``$HOSTNAME-$INTERFACE``\ 
| Configuration files: ``/etc/nsm/$HOSTNAME-$INTERFACE/``\ 
| Example: ``sensor1-eth0``\ 
| Controlled by: ``/usr/sbin/nsm_sensor``\ 
| 
| **sensor box**\ 
| Definition: A machine having one or more sensors that transmit to a
  central server. Does not run server processes. Pulls ruleset from
  server box. (In some contexts, I refer to this a slave pulling rules
  from the master.)
| Example: A machine named ``sensor1`` having sensors ``sensor1-eth0``
  and ``sensor1-eth1``.
| 
| 
| `back to top <#top>`__
| 
| 

Users / Passwords
---------------------

What is the password for ``root/mysql/Sguil/Squert/Kibana``?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`Passwords <Passwords>`__

How do I add a new user account for logging into Sguil/Squert/Kibana?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| `Adding Sguil accounts <Passwords#sguil>`__\ 
| 
| `back to top <#top>`__
| 
| 

Support / Help
------------------

Where do I send questions/problems/suggestions?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`security-onion Google Group <MailingLists>`__

I submitted a message to the security-onion Google Group. Why isn't it showing up?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`Moderation <MailingLists#moderation>`__

Is commercial support available for Security Onion?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| Yes!  Please see:
| https://securityonionsolutions.com
| 
| 
| `back to top <#top>`__
| 
| 

Error messages
------------------

Why does rule-update fail with Error 400 when running behind a proxy?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Please see `<Proxy#pulledpork>`__

Why does rule-update fail with an error like "Error 404 when fetching s3.amazonaws.com/snort-org/www/rules/community/community-rules.tar.gz.md5"?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Snort Community ruleset has moved to a different URL. You can run the following command to update the Snort Community URL in ``pulledpork.conf``:

::

    sudo sed -i 's\rule_url=https://s3.amazonaws.com/snort-org/www/rules/community/|community-rules.tar.gz|Community\rule_url=https://snort.org/downloads/community/|community-rules.tar.gz|Community\g' /etc/nsm/pulledpork/pulledpork.conf

| For more information, please see:
| https://blog.snort.org/2015/10/are-you-getting-404-errors-attempting.html

Why does ``soup`` fail with an error message like "find: \`/usr/lib/python2.7/dist-packages/salt/': No such file or directory"?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This is a bug in the salt packages that can manifest when skipping salt versions. Resolve with the following:

::

    sudo mkdir -p /usr/lib/python2.7/dist-packages/salt/
    sudo apt-get -f install
    sudo soup

Why does barnyard2 keep failing with errors like "Returned signature\_id is not equal to updated signature\_id"?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| Please see:
| https://blog.securityonion.net/2014/06/new-securityonion-rule-update-package.html

I just updated Snort and it's now saying 'ERROR: The dynamic detection library "/usr/local/lib/snort\_dynamicrules/chat.so" version 1.0 compiled with dynamic engine library version 2.1 isn't compatible with the current dynamic engine library "/usr/lib/snort\_dynamicengine/libsf\_engine.so" version 2.4.'
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Run the following:

::

    sudo rule-update

For more information, please see:

https://blog.securityonion.net/2014/12/new-version-of-securityonion-rule.html

I get periodic MySQL crashes and/or error code 24 "out of resources" when searching in Sguil. How do I fix that?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Modern versions of Setup should set MySQL's ``open-files-limit`` to 90000 to avoid this problem.

| For more information, please see:
| http://nsmwiki.org/Sguil\_FAQ#I.27m\_seeing\_error\_code\_24\_from\_MySQL.\_How\_do\_I\_fix\_that.3F

Barnyard2 is failing with an error like "ERROR: sguil: Expected Confirm 13324 and got: Failed to insert 13324: mysqlexec/db server: Duplicate entry '9-13324' for key 'PRIMARY'". How do I fix this?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Sometimes, just restarting Barnyard will clear this up:

::

   sudo so-barnyard-restart
 

Other times, restarting Sguild and then restarting Barnyard will clear it up:

::

   sudo so-sguild-restart
   sudo so-sensor-restart --only-barnyard2

If that doesn't work, then try also restarting mysql:

::

   sudo service mysql restart
   sudo so-sguild-restart
   sudo so-sensor-restart --only-barnyard2

If that still doesn't fix it, you may have to perform MySQL surgery on the database ``securityonion_db`` as described in the Sguil FAQ:
http://nsmwiki.org/Sguil\_FAQ#Barnyard\_dies\_at\_startup.2C\_with\_.22Duplicate\_Entry.22\_error

Why does Snort segfault every day at 7:01 AM?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

7:01 AM is the time of the daily PulledPork rules update. If you're running Snort with the Snort Subscriber (Talos) ruleset, this includes updating the SO rules. There is a known issue when running Snort with the Snort Subscriber (Talos) ruleset and updating the SO rules:
https://groups.google.com/d/topic/pulledpork-users/1bQDkh3AhNs/discussion

After updating the rules, Snort is restarted, and the segfault occurs in the OLD instance of Snort (not the NEW instance). Therefore, the segfault is merely a nuisance log entry and can safely be ignored.

Why does the pcap_agent log show "Error: can't read logFile: no such variable"?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This usually means that there is an unexpected file in the dailylogs
directory. Run the following:

::

    ls /nsm/sensor_data/*/dailylogs/

You should see a bunch of date stamped directories and you may see some
extraneous files. Remove any extraneous files and restart pcap\_agent:

::

    sudo so-pcap-agent-restart

Why does Chromium display a black screen and/or crash?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This is a known issue with certain versions of VMware. You can either:

-  go into the VM configuration and disable 3D in the video adapter
   OR
-  upgrade the VM hardware level (may require upgrading to a new version of VMware)

Why does Bro log ``Failed to open GeoIP database`` and ``Fell back to GeoIP Country database``?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The GeoIP CITY database is ``not free`` and thus we cannot include it in the distro. Bro fails to find it and falls back to the GeoIP COUNTRY database (which is free). As long as you are seeing some country codes in your conn.log, then everything should be fine. If you really need the CITY database, see this thread for some options: https://groups.google.com/d/topic/security-onion-testing/gtc-8ZTuCi4/discussion

Why does soup tell me I need a Secure Boot key?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| `Secure Boot <Secure-Boot>`__
| 
| 
| `back to top <#top>`__
| 
| 

IPS/IDS engines
-------------------

I'm currently running ``Snort``. How do I switch to ``Suricata``?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Please note that, if you're running the Snort Talos ruleset, Snort Shared Object rules will not load in Suricata. Most folks who choose the Suricata engine choose to run the Emerging Threats ruleset.

::

   sudo so-sensor-stop
   sudo sed -i 's\|ENGINE=snort\|ENGINE=suricata\|g' /etc/nsm/securityonion.conf
   sudo rule-update 
   sudo so-sensor-start

I'm currently running ``Suricata``. How do I switch to ``Snort``?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

   sudo so-sensor-stop
   sudo sed -i 's|ENGINE=suricata|ENGINE=snort|g' /etc/nsm/securityonion.conf
   sudo rule-update
   sudo so-sensor-start

Can Security Onion run in ``IPS`` mode?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|Running Security Onion as an IPS requires manual configuration and is ``not supported``.
| 
| 
| `back to top <#top>`__
| 
| 

Security Onion internals
----------------------------

Where can I read more about the tools contained within Security Onion?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`Tools <Tools>`__

What's the directory structure of ``/nsm``?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`/nsm Directory Structure <DirectoryStructure>`__

Why does Security Onion use ``UTC``?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`UTC and Time Zones <TimeZones>`__

Why are the ``timestamps`` in Kibana not in UTC?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`UTC and Time Zones <TimeZones>`__

Why is my disk filling up?
~~~~~~~~~~~~~~~~~~~~~~~~~~

Sguil uses netsniff-ng to record full packet captures to disk. These pcaps are stored in ``nsm/sensor_data/$HOSTNAME-$INTERFACE/dailylogs/``. ``/etc/cron.d/sensor-clean`` is a cronjob that runs every minute that should delete old pcaps when the disk reaches your defined disk usage threshold (90% by default). It's important to properly size your disk storage so that you avoid filling the disk to 100% between purges.

I just rebooted and it looks like the services aren't starting automatically.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Older versions of Security Onion waited 60 seconds after boot to ensure network interfaces are fully initialized before starting services.  Starting in 16.04, services should start automatically as soon as network interfaces are initialized.

Why do apt-get and the Update Manager show ``tcl8.5 as held back``?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| `tcl <tcl>`__
| 
| 
| `back to top <#top>`__
| 
| 

Tuning
----------

What do I need to tune if I'm monitoring VLAN tagged traffic?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`VLAN Traffic <VLAN-Traffic>`__

How do I configure email for alerting and reporting?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`Email <Email>`__

How do I configure a ``BPF`` for ``Snort/Suricata/Bro/netsniff-ng/prads``?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`BPF <BPF>`__

How do I filter traffic?
~~~~~~~~~~~~~~~~~~~~~~~~

`BPF <BPF>`__

How do I exclude traffic?
~~~~~~~~~~~~~~~~~~~~~~~~~

`BPF <BPF>`__

What are the default firewall settings and how do I change them?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`Firewall <Firewall>`__

What do I need to modify in order to have the log files stored on a different mount point?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`Adding a New Disk for /nsm <NewDisk>`__

How do I disable the graphical ``Network Manager`` and configuring networking from the command line?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`Network Configuration <NetworkConfiguration>`__

How do I enable/disable processes?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`Disabling Processes <DisablingProcesses>`__

I disabled some Sguil agents but they still appear in Sguil's ``Agent Status`` tab.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`Disabling Processes <DisablingProcesses#Sguil_Agent>`__

What can I do to decrease the size of my ``securityonion_db`` (sguild) MySQL database?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| You can lower the ``DAYSTOKEEP`` setting in ``/etc/nsm/securityonion.conf``.
| Also see ``UNCAT_MAX``:
| https://blog.securityonion.net/2015/01/new-version-of-sguil-db-purge-helps.html

How do I change the fonts in the Sguil client?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In the Sguil client, click the ``File`` menu and then go to ``Change Font``. You can change both the Standard and Fixed fonts.

Can I be alerted when an interface stops receiving traffic?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`Interface stops receiving traffic <SensorStopsSeeingTraffic>`__

How do I boot Security Onion to text mode (CLI instead of GUI)?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In ``/etc/default/grub``, change this line:

::

    GRUB_CMDLINE_LINUX_DEFAULT="splash quiet"

to:

::

    GRUB_CMDLINE_LINUX_DEFAULT="text"

Then run:

::

    sudo update-grub

| For more information, please see:
| http://ubuntuforums.org/showthread.php?t=1690118

If you're doing a new installation, you can avoid this altogether by installing our packages on top of Ubuntu Server (minimal installation, no GUI) instead of using the Security Onion ISO image.

I'm running Security Onion in a VM and the screensaver is using lots of CPU. How do I change/disable the screensaver?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

   <ol><li>Click Applications.<br>
   </li><li>Click Settings.<br>
   </li><li>Click Screensaver.<br>
   </li><li>Screensaver Preferences window appears.  Click the Mode dropdown and select "Disable Screen Saver" or "Blank Screen Only".<br>
   </li><li>Close the Screensaver Preferences window.<br></li></ol>

| `back to top <#top>`__
| 
| 

``sostat`` output
---------------------

What does it mean if ``sostat`` show a high number of ``Sguil Uncategorized Events``?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``Sguild`` has to load uncategorized events into memory when it starts and it won't accept connections until that's complete. You can either:

-  wait for sguild to start up (may take a LONG time), then log into  Sguil, and ``F8`` LOTS of events
   OR
-  stop sguild

   ::

       sudo so-sguild-stop

   | and manually categorize events using ``mysql``\ 
   | (see http://taosecurity.blogspot.com/2013/02/recovering-from-suricata-gone-wild.html)
   | OR
   | lower your ``DAYSTOKEEP`` setting in ``/etc/nsm/securityonion.conf`` and run

   ::

       sudo sguil-db-purge

   To keep ``Uncategorized Events`` from getting too high, you should log into Sguil/Squert on a daily/weekly basis and categorize events.

| 
| `back to top <#top>`__
| 
| 

Miscellaneous
-----------------

Where can I find the version information for Security Onion?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If the machine was built with the Security Onion 16.04 ISO image, version information can be found in ``/etc/PinguyBuilder.conf``.

Where can I find interesting pcaps to replay?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`Pcaps <Pcaps>`__

Why is Security Onion connecting to an IP address on the Internet over port 123?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`NTP <NTP>`__

Should I backup my Security Onion box?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Network Security Monitoring as a whole is considered "best effort". It is not a "mission critical" resource like a file server or web server. Since we're dealing with "big data" (potentially terabytes of full packet capture), backups would be prohibitively expensive. Most organizations don't do any backups and instead just rebuild boxes when necessary.

How can I add and test local rules?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`Adding local rules and testing them with scapy <AddingLocalRules>`__

Where can I get the source code?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can download the full source code for any of our packages like this:

::

   apt-get source PACKAGE-NAME

where ``PACKAGE-NAME`` is usually something like ``securityonion-snort``. Here's a list of all of our packages:
| https://launchpad.net/~securityonion/+archive/stable

How can I remote control my Security Onion box?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| A few options:
| "ssh -X" - any program started in the SSH session will be displayed on your local desktop (requires a local X server)
| xrdp - sudo apt-get install xrdp - requires an rdp client

Why isn't Squert showing GeoIP data properly?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If the Squert map is not showing the country for IPs, try running the following:

::

   sudo /usr/bin/php -e /var/www/so/squert/.inc/ip2c.php 0'/

Why do I get segfaults when booting on VMware ESX?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| This is a known issue with Ubuntu 10.04 and ESXi 4.1 and is unrelated to Security Onion. Please see:
| http://ubuntuforums.org/showthread.php?t=1674759
| https://bugs.launchpad.net/ubuntu/+source/linux/+bug/659422

How do I run ``ntopng`` on Security Onion?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`Deploying NtopNG <DeployingNtopng>`__

How do I open rar files?
~~~~~~~~~~~~~~~~~~~~~~~~

We're not allowed to redistribute the unrar plugin, so you'll need to install it manually:

::

    sudo apt-get update
    sudo apt-get install unrar

How do I perform "X" in Ubuntu?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Security Onion is based on Ubuntu, but we don't provide community support for the Ubuntu OS itself. If you have questions about Ubuntu, you should check the Ubuntu website, forums, and Google.

`back to top <#top>`__
