Introduction
============

Adding local rules in Security Onion is a rather straightforward
process. However, generating custom traffic to test the alert can
sometimes be a challenge. Here, we will show you how to add the local
rule and then use the python library scapy to trigger the alert.

IPS Policy
==========

Please note if you are using a ruleset that enables an IPS policy in
``/etc/nsm/pulledpork/pulledpork.conf``, your local rules will be
disabled. To enabled them, either revert the policy by remarking the
``ips_policy`` line (and run ``rule-update``), or add the policy type to
the rules in local.rules.

For example, if ``ips_policy`` was set to ``security``, you would add
the following to each rule:

``metadata:policy security-ips``

The whole rule would then look something like:

``alert tcp any any -> $HOME_NET 7789 (msg: "Vote for Security Onion Toolsmith Tool of 2011!"; reference: url,http://holisticinfosec.blogspot.com/2011/12/choose-2011-toolsmith-tool-of-year.html; content: "toolsmith"; flow:to_server; nocase; sid:9000547; metadata:policy security-ips; rev:1)``

These policy types can be found in ``/etc/nsm/rules/downloaded.rules``.

Steps
=====

-  Open ``/etc/nsm/rules/local.rules`` using your favorite text editor.
   If this is a distributed deployment, edit local.rules on your master
   server and it will replicate to your sensors.
-  Let's add a simple rule that will alert on the detection of a string
   in a tcp session.

   ::

       alert tcp any any -> $HOME_NET 7789 (msg: "Vote for Security Onion Toolsmith Tool of 2011!"; reference: url,http://holisticinfosec.blogspot.com/2011/12/choose-2011-toolsmith-tool-of-year.html; content: "toolsmith"; flow:to_server; nocase; sid:9000547; rev:1)     

-  Run rule-update (this will merge local.rules into downloaded.rules,
   update ``sid-msg.map``, and restart snort/suricata and barnyard):

   ::

       sudo rule-update

-  If you built the rule correctly, then snort should be back up and
   running.
-  Generate some traffic to trigger the alert. To generate traffic we
   are going to use the python library scapy to craft packets with
   specific information to ensure we trigger the alert with the
   information we want.

   ::

       sudo scapy

-  | Enter the following sample in a line at a time. Any line beginning
     with "#" can be ignored as it is a comment.
   | \`\`\`

   .. rubric:: Craft the layer 2 information.
      :name: craft-the-layer-2-information.

   .. rubric:: The ip addresses can be random, but I would suggest
      sticking to RFC1918
      :name: the-ip-addresses-can-be-random-but-i-would-suggest-sticking-to-rfc1918

   | ip = IP()
   | ip.dst = "192.168.200.4"
   | ip.src = "192.168.100.3"

Craft the layer 3 information.
==============================

Since we specified port 7789 in our snort rule,
===============================================

| tcp = TCP()
| tcp.dport = 7789
| tcp.sport = 1234

Set the playload
================

payload = "Toolsmith"

Use the / operator to compose our packet and transfer it with the send() method.
================================================================================

| send(ip/tcp/payload)
| \`\`\`

-  | Check sguil for the corresponding alert
   | 

-  | You can see that we have an alert with the IP addresses we
     specified and the TCP ports we specified.
   | If you right click on the **Alert ID** column you can select
     "Transcript" and verify the payload we sent.
   | 

-  You can learn more about snort and writing snort signatures from the
   `Snort Manual <http://manual.snort.org/node26.html>`__
-  You can learn more about scapy at
   `secdev.org <http://www.secdev.org/projects/scapy/>`__ and
   `itgeekchronicles.co.uk <http://itgeekchronicles.co.uk/2012/05/31/scapy-guide-the-release/>`__.

MISP
----

| If you would like to pull in NIDS rules from a MISP instance, please
  see:
| `MISP
  Rules <https://github.com/Security-Onion-Solutions/security-onion/wiki/MISP>`__
