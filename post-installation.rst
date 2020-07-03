After Installation
==================

Adjust firewall rules using so-allow
------------------------------------
All firewall rules for the entire deployment are managed on the master. You will want to allow your own IP address (or range) to access Security Onion as an analyst. Run the command below and select the analyst role:

 ::
 
   sudo so-allow

This process can take up to a minute if a salt highstate on the master is already running.

Security Onion Console
----------------------
Once so-allow has completed, you should be able to open your browser and connect to Security Onion Console on your Security Onion installation. Login using the email address and corresponding password you specified in the installer. The Security Onion Console allows you to manage user accounts and also provides links to separate web interfaces like Kibana, Grafana, TheHive, and others.

Grafana
-------
| Username: admin
| Password: augusta

TheHive
-------
Log into TheHive and add a user or change the admin account https://MASTERSERVER/thehive:

| Username: hiveadmin  
| Password: hivechangeme  

Fleet / Osquery
---------------
If you selected to install Fleet during the setup, you can now login to Fleet using the email & password that you entered during the installer. You can edit the password or add a new Fleet user within Fleet itself.

Osquery packages were generated during setup - you can access these under Downloads in the Security Onion Console. They are customized specifically for your Security Onion install. Before you install a package on an endpoint, use sudo so-allow on your master to configure the SO firewall to allow inbound osquery connections.

Playbook
--------
If you enabled Playbook during setup, you can now login with the following credentials:

| Username: analyst  
| Password: changeme  

Refer to the Playbook documentation for further details.

Navigator
---------
If you enabled Navigator during setup, you can now access it - no login credentials required once you have authenticated through the Security Onion Console.

Log Shipping
------------
You can ship your endpoint logs to Security Onion using a variety of methods including Wazuh, Osquery & Winlogbeat.

Winlogbeat
----------
Run so-allow and select b to allow your Winlogbeat agents to send their logs to Security Onion.

Navigate to the Downloads page in the Security Onion Console and download the linked Winlogbeat agent - this link will take you to the correct version of Winlogbeat for your Elastic version. Install Winlogbeat and configure it to send logs to MASTER:5044. Transport encryption is not enabled by default.

If you are shipping Sysmon logs, confirm that your Winlogbeat configuration does not use the Elastic Sysmon module - Security Onion will do all the necessary parsing.

Services
--------

-  Verify services are running:
   
   ::
   
      sudo so-status

Other
-----

-  Full-time analysts may want to connect using a dedicated `Analyst VM <Analyst-VM>`__.

-  Any IDS/NSM system needs to be tuned for the network it’s monitoring. Please see the `<tuning>`__ section. 

Optional
--------

-  Exclude unnecessary traffic from your monitoring using `BPF <BPF>`__.

-  Configure the OS to use your preferred `NTP <NTP>`__ server.
