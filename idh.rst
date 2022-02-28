.. _idh:

Intrusion Detection Honeypot
============================

Starting in Security Onion 2.3.110, we have a new Intrusion Detection Honeypot node. This allows you to build a node that mimics services. Connections to these services automatically generate alerts.

From the book, *Intrusion Detection Honeypots* (Sanders, C):

     An Intrusion Detection Honeypot (IDH) is a security resource placed inside your network perimeter that generates alerts when probed or attacked. These systems, services, and tokens rely on deception to lure attackers in and convince them to interact. Unbeknownst to the attacker, you’re alerted when that interaction occurs and can begin investigating the compromise.

Chris Sanders and Josh Brower presented the IDH concept at Security Onion Conference 2021 and you can view the recording at https://www.youtube.com/watch?v=NzUhfARVfJk&list=PLljFlTO9rB17mESq7Z9OeFKvVh39vJW34&index=5.

.. warning::

        The IDH node is designed to be placed *inside* your network perimeter! It should not be accessible from the Internet!
     
Screenshots
-----------

Run Setup, choose to add a new node to your distributed deployment, and select the IDH option:

.. image:: images/idh-install-1.png
  :target: _images/idh-install-1.png

Then choose from one of the common honeypot options or customize:

.. image:: images/idh-install-2.png
  :target: _images/idh-install-2.png

If you choose the webserver option, anybody who connects to the webserver will see a web page like this:

.. image:: images/idh-webserver.png
  :target: _images/idh-webserver.png

Connections to honeypot services will result in ``SO IDH`` alerts that can be seen in :ref:`alerts`:

.. image:: images/idh-alert-1.png
  :target: _images/idh-alert-1.png

Technical Background
----------------------
The IDH node utilizes OpenCanary which is a modular opensource honeypot by Thinkst. You can read more about it at https://github.com/thinkst/opencanary.

OpenCanary logs can be found through SOC Hunt or Kibana using the following:

``event.module: opencanary``
``event.dataset: idh``

Sigma Plays within Playbook look for certain logs emitted by OpenCanary to generate alerts, which can be viewed in the SOC Alerts interface.

Services Configuration
----------------------

The following services are available for use with the IDH node. Pay special attention to how an alert is triggered for a service as some of them require more than a simple connection request to trigger.

- FTP - a File Transfer Protocol server which alerts on login attempts
- Git - a Git server which alerts on repo cloning
- HTTP - an HTTP web server that alerts on login attempts
- HTTP Proxy - an HTTP web proxy that alerts when there is an attempt to proxy to another page
- MSSQL - an MS SQL server that alerts on login attempts
- MySQL - a MYSQL server that alerts on login attempts
- Telnet - a Telnet server that alerts on login attempts
- SNMP - an SNMP server which alerts on oid requests
- SSH - a Secure Shell server which alerts on login attempts
- SIP - a SIP server which alerts on sip requests
- VNC - a VNC server which alerts on login attempts
- Redis - a Redis server which alerts on actions
- TFTP - a tftp server which alerts on requests
- NTP - an NTP server which alerts on ntp requests

RDP & SMB are not currently available for use within an IDH node.

* Modified from https://opencanary.readthedocs.io/en/latest/starting/configuration.html#services-configuration

In addition to changing the default ports, some of these services have further configuration options. For instance, the HTTP server has the ability to use custom HTML pages ("skins"). Consult the OpenCanary documentation for further guidance: https://opencanary.readthedocs.io/en/latest/starting/configuration.html#default-configuration

These types of configuration changes can be made by modifying the minion pillar.

SSH
---
For IDH nodes, the local sshd is configured to listen on TCP/2222 and connections are only accepted from the Manager node. This allows TCP/22 to be used for honeypot services.
