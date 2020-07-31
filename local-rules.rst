.. _local-rules:

Adding Local Rules
==================

-  You can add rules in ``/opt/so/saltstack/local/salt/idstools/localrules/`` on your manager.
   
-  Let's add a simple rule that will alert on the detection of a string in a tcp session:

   ::

       alert tcp any any -> $HOME_NET 7789 (msg: "Vote for Security Onion Toolsmith Tool of 2011!"; reference: url,http://holisticinfosec.blogspot.com/2011/12/choose-2011-toolsmith-tool-of-year.html; content: "toolsmith"; flow:to_server; nocase; sid:9000547; rev:1)     

-  Run ``so-rule-update`` to merge ``/opt/so/saltstack/local/salt/idstools/localrules/`` into ``/opt/so/rules/nids/local.rules`` and restart processes as necessary:

   ::

       sudo so-rule-update

-  If you built the rule correctly, then Suricata should be back up and running.
   
Testing Local Rules
-------------------

Adding local rules in Security Onion is a rather straightforward process. However, generating custom traffic to test the alert can sometimes be a challenge. Here, we will show you how to add the local rule and then use the python library scapy to trigger the alert.

-  Generate some traffic to trigger the alert. To generate traffic we are going to use the python library ``scapy`` to craft packets with specific information to ensure we trigger the alert with the information we want:

   ::

       sudo scapy

-  Craft the layer 2 information.  The ip addresses can be random, but I would suggest sticking to RFC1918:

   ::
      
       ip = IP()
       ip.dst = "192.168.200.4"
       ip.src = "192.168.100.3"

- Craft the layer 3 information  Since we specified port 7789 in our rule:

  ::
   
       tcp = TCP()
       tcp.dport = 7789
       tcp.sport = 1234

- Set the playload:

  ::
   
       payload = "Toolsmith"

- Use the / operator to compose our packet and transfer it with the send() method:

  ::
   
       send(ip/tcp/payload)

-  Check :ref:`hunt` or :ref:`kibana` for the corresponding alert.

-  You can see that we have an alert with the IP addresses we specified and the TCP ports we specified. If you pivot from that alert to the corresponding pcap you can verify the payload we sent.

-  You can learn more about scapy at  `secdev.org <http://www.secdev.org/projects/scapy/>`__ and `itgeekchronicles.co.uk <http://itgeekchronicles.co.uk/2012/05/31/scapy-guide-the-release/>`__.

MISP
----

If you would like to pull in NIDS rules from a MISP instance, please see the :ref:`misp` section.
