Introduction
============

| Wazuh has replaced OSSEC:
| https://blog.securityonion.net/2018/10/wazuh-361-elastic-641-and-associated.html

| You may want to see our Wazuh page:
| https://github.com/Security-Onion-Solutions/security-onion/wiki/Wazuh

Description
===========

From http://ossec.github.io/:

    OSSEC watches it all, actively monitoring all aspects of system
    activity with file integrity monitoring, log monitoring, rootcheck,
    and process monitoring.

Security Onion Usage
====================

Security Onion uses OSSEC as a Host Intrusion Detection System (HIDS).
OSSEC is monitoring and defending Security Onion itself and you can add
OSSEC agents to monitor other hosts on your network as well.

Additionally, you may want to:

-  `Configure OSSEC to send email
   notification(s) <https://github.com/Security-Onion-Solutions/security-onion/wiki/Email#how-do-i-configure-ossec-to-send-emails>`__

-  `Send OSSEC logs to an external syslog
   collector <https://github.com/Security-Onion-Solutions/security-onion/wiki/ThirdPartyIntegration#how-do-i-send-bro-and-ossec-logs-to-an-external-syslog-collector>`__

| For more information about OSSEC, please see:
| http://ossec.net

Active Response
---------------

| Sometimes, OSSEC may recognize legitimate activity as potentially
  malicious, and engage in Active Response to block a connection. This
  may result in unintended consequences and/or blacklisting of trusted
  IPs.
| You can whitelist your IP address and change other settings in
  ``/var/ossec/etc/ossec.conf`` to prevent
| this from occurring:

| ``<global>``\ 
| ``<white_list>desired_ip</white_list>``\ 
| ``</global>``

Tuning OSSEC Rules
------------------

You can add new rules and modify existing rules in
/var/ossec/rules/local\_rules.xml.

OSSEC alerts of a level of ``5`` or greater will be populated in the
Sguil database, and viewable via Sguil and/or Squert. If you would like
to change the level for which alerts are send to sguild, you can modify
the value for ``OSSEC_AGENT_LEVEL`` in ``/etc/nsm/securityonion.conf``
and restart NSM services.

Adding Agents
-------------

The OSSEC agent is cross platform and you can download agents for
Windows/Unix/Linux/FreeBSD from the OSSEC website. Once you've installed
the OSSEC agent on the host(s) to be monitored, then perform the steps
defined here:

http://ossec-docs.readthedocs.org/en/latest/manual/agent/agent-management.html#managing-agents

You may need to run
`so-allow <https://github.com/Security-Onion-Solutions/security-onion/wiki/Firewall#so-allow>`__
to allow traffic from the IP address of your OSSEC agent(s).

Maximum Number of Agents
------------------------

Security Onion is configured to support a maximum number of ``1024``
OSSEC agents reporting to a single OSSEC manager.

Automated Deployment
--------------------

Many individuals require or prefer the ability to automatically deploy
OSSEC agents on endpoint machines. Although **this is currently untested
and unsupported**, Auto-OSSEC provides a method for achieving this goal.

| For more information, please see:
| https://github.com/binarydefense/auto-ossec

Downloads
=========

| You can download OSSEC agents here:
| https://ossec.github.io/downloads.html
