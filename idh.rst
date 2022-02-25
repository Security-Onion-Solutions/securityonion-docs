.. _idh:

Intrusion Detection Honeypot
============================

Starting in Security Onion 2.3.110, we have a new Intrusion Detection Honeypot node. This allows you to build a node that mimics services. Connections to these services automatically generate alerts.

From the book, Intrusion Detection Honeypots (Sanders, C):

     An Intrusion Detection Honeypot (IDH) is a security resource placed inside your network perimeter that generates alerts when probed or attacked. These systems, services, and tokens rely on deception to lure attackers in and convince them to interact. Unbeknownst to the attacker, you’re alerted when that interaction occurs and can begin investigating the compromise.

.. warning::

        The IDH node is designed to be placed _inside_ your network perimeter - It should not be deployed Internet-facing. 
     
    

.. image:: images/idh-install-1.png
  :target: _images/idh-install-1.png

.. image:: images/idh-install-2.png
  :target: _images/idh-install-2.png

.. image:: images/idh-alert-1.png
  :target: _images/idh-alert-1.png


Configuration
============================

The IDH node utilizes the modular opensource honeypot by Thinkst, OpenCanary https://github.com/thinkst/opencanary

The following services are available for use with the IDH node:

- FTP - a File Transfer Protocol server which on login attempts
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

* Modified from https://opencanary.readthedocs.io/en/latest/starting/configuration.html#services-configuration
