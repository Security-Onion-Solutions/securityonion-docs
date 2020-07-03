FAQ
===

| 
| 
| `Install / Update / Upgrade <#install-update-upgrade>`__\ 
| `Users / Passwords <#users-passwords>`__\ 
| `Support / Help <#support-help>`__\ 
| `Error messages <#error-messages>`__\ 
| `IDS engines <#ids-engines>`__\ 
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

Please see the `TroubleBooting <TroubleBooting>`__ section.

What's the recommended procedure for installing Security Onion?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Please see the `Installation Procedure <Installation>`__ section.

What languages are supported?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We only support the English language at this time.

How do I install Security Onion updates?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Please see the `Upgrade Procedure <Upgrade>`__ section.

What do I need to do if I'm behind a proxy?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Please see the `Proxy Configuration <Proxy>`__ section.

Can I run Security Onion on Raspberry Pi or some other non-x86 box?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

No, we only support 64-bit Intel/AMD architectures. Please see the `hardware <Hardware>`__ section.

What's the difference between a ``server`` and a ``sensor``?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| **box** 
| Definition: A physical or virtual machine running the Security Onion
  operating system.
| 
| **server** 
| Definition: A set of processes that receive data from sensors and
  allow analysts to see and investigate that data. The set of processes
  includes the Elastic stack
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
  set of processes currently includes Suricata, Stenographer, and
  Zeek (although this is in constant flux as we add new capabilities and
  find better tools for existing capabilities).
| Naming convention: ``$HOSTNAME-$INTERFACE``\ 
| Configuration files: ``/etc/nsm/$HOSTNAME-$INTERFACE/``\ 
| Example: ``sensor1-eth0``\ 
| Controlled by: ``/usr/sbin/nsm_sensor``\ 
| 
| **sensor box**\ 
| Definition: A machine having one or more sensors that transmit to a
  central server. Does not run server processes. Pulls ruleset from
  server box. 
| Example: A machine named ``sensor1`` having sensors ``sensor1-eth0``
  and ``sensor1-eth1``.
| 
| 
| `back to top <#top>`__
| 
| 

Users / Passwords
---------------------

What is the password?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Please see the `Passwords <Passwords>`__ section.

How do I add a new user account?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| Please see the `Adding accounts <Passwords>`__ section.\ 
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

Please see the `Moderation <MailingLists#moderation>`__ section.

Is commercial support available for Security Onion?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| Yes!  Please see https://securityonionsolutions.com.
| 
| 
| `back to top <#top>`__
| 
| 

Error messages
------------------

Why does Zeek log ``Failed to open GeoIP database`` and ``Fell back to GeoIP Country database``?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The GeoIP CITY database is ``not free`` and thus we cannot include it in the distro. Zeek fails to find it and falls back to the GeoIP COUNTRY database (which is free). As long as you are seeing some country codes in your conn.log, then everything should be fine. If you really need the CITY database, see this thread for some options: https://groups.google.com/d/topic/security-onion-testing/gtc-8ZTuCi4/discussion

`back to top <#top>`__

IDS engines
-------------------

Can Security Onion run in ``IPS`` mode?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Please see the `<NIDS#NIPS>`_ section.

`back to top <#top>`__
 

Security Onion internals
----------------------------

Where can I read more about the tools contained within Security Onion?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Please see the `Tools <Tools>`__ section.

What's the directory structure of ``/nsm``?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Please see the `/nsm Directory Structure <DirectoryStructure>`__ section.

Why does Security Onion use ``UTC``?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Please see the `UTC and Time Zones <TimeZones>`__ section.

Why are the ``timestamps`` in Kibana not in UTC?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Please see the `UTC and Time Zones <TimeZones>`__ section.

Why is my disk filling up?
~~~~~~~~~~~~~~~~~~~~~~~~~~

Security Onion records full packet capture to disk. 

`back to top <#top>`__

Tuning
----------

What do I need to tune if I'm monitoring VLAN tagged traffic?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Please see the `VLAN Traffic <VLAN-Traffic>`__ section.

How do I configure email for alerting and reporting?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Please see the `Email <Email>`__ section.

How do I configure a ``BPF``?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Please see the `BPF <BPF>`__ section.

How do I filter traffic?
~~~~~~~~~~~~~~~~~~~~~~~~

Please see the `BPF <BPF>`__ section.

How do I exclude traffic?
~~~~~~~~~~~~~~~~~~~~~~~~~

Please see the `BPF <BPF>`__ section.

What are the default firewall settings and how do I change them?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Please see the `Firewall <Firewall>`__ section.

What do I need to modify in order to have the log files stored on a different mount point?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Please see the `Adding a New Disk for /nsm <NewDisk>`__ section.

How do I enable/disable processes?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Please see the `Disabling Processes <DisablingProcesses>`__ section.

 `back to top <#top>`__

Miscellaneous
-----------------

Where can I find interesting pcaps to replay?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Please see the `Pcaps <Pcaps>`__ section.

Why is Security Onion connecting to an IP address on the Internet over port 123?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Please see the `NTP <NTP>`__ section.

Should I backup my Security Onion box?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Network Security Monitoring as a whole is considered "best effort". It is not a "mission critical" resource like a file server or web server. Since we're dealing with "big data" (potentially terabytes of full packet capture), backups would be prohibitively expensive. Most organizations don't do any backups and instead just rebuild boxes when necessary.

How can I add and test local rules?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Please see the `Adding local rules and testing them with scapy <AddingLocalRules>`__ section.

Can I connect Security Onion to Active Directory?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
We understand the appeal of Active Directory integration, but we typically recommend against joining any security infrastructure (including Security Onion) to Active Directory. The reason is that when you get an adversary inside your network, one of their first goals is going to be gaining access to Active Directory. If they get access to Active Directory, then they get access to everything connected to Active Directory. For that reason, we recommend that all security infrastructure (including Security Onion) be totally separate from Active Directory.

`back to top <#top>`__
