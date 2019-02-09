Sguil
=====

From http://sguil.net:

    Sguil (pronounced sgweel) is built by network security analysts for
    network security analysts. Sguil's main component is an intuitive
    GUI that provides access to realtime events, session data, and raw
    packet captures. Sguil facilitates the practice of Network Security
    Monitoring and event driven analysis.

-  | Developed by Bamm Visscher:
   | http://sguil.net
   | http://nsmwiki.org/Sguil
   | http://nsmwiki.org/Sguil_Client

-  tcl/tk (not web-based)

-  Single central MySQL database

Authentication
--------------

| For login information, please see:
| `<Passwords#sguil>`__

| For information on ways to connect to Sguil/sguild, please see:
| `<ConnectingtoSguil>`__

Data Types
----------

-  NIDS alerts from Snort/Suricata (if snort_agent is enabled)
-  HIDS alerts from OSSEC (if ossec_agent is enabled)

Pivot
-----

-  pivot to transcript/Wireshark/NetworkMiner by right-clicking the Alert ID.
-  automatically pivot to ASCII transcript by middle-clicking the Alert ID.
-  pivot to Kibana by right-clicking an IP address and choosing ``Kibana IP Lookup``.

Agents
------

Because Sguil is written in tcl/tk, it can only utilize ``1024`` sockets for receiving communication from various sensor agents (ossec_agent, pcap_agent, snort_agent). Due to this restriction, you will want to keep in mind the number of sensors and sniffing interfaces you have connected to the master server/accessed by Sguil.

| See the following for more information:
| https://groups.google.com/d/msg/security-onion/DJ5NTLEu5MY/-tDQi_1eDQAJ

Management
----------

-  It is important to ensure events displayed in Sguil are regularly classified, or else it could cause problems with the Sguil database. Consider creating an `autocat rule <ManagingAlerts#autocategorize-events>`__ to assist with this.

-  `Configure Sguil alert email notification(s) <Email#how-do-i-configure-sguil-to-send-alerts-via-email>`__

-  `Configure retention for Sguil alerts <ManagingAlerts#sguil-days-to-keep>`__

Customize (Sguil client)
------------------------

-  resize columns by right-clicking on the column heading in the Sguil client.
-  change fonts by clicking File --> Change Font from within the Sguil client.
-  Sguil client settings are stored in ``/etc/sguil/sguil.conf``:
-  | You can enable "Show Rule", "Show Packet Data", and "Display
     Detail" (respectively) by setting the following (also see
     https://groups.google.com/d/topic/security-onion/MJaAlxgpMvU/discussion):
   | ``set SHOWRULE 1``\ 
   | ``set PACKETINFO 1``\ 
   | ``set DISPLAY_GENERIC 1``

-  You can separate realtime alerts into separate panes, based on
   severity level, by editing ``/etc/sguil/sguil.conf`` as follows:

::

    #Number of RealTime Event Panes
    #set RTPANES 1
    set RTPANES 3

    # Specify which priority events go into what pane   
    # According to the latest classification.config from snort,   
    # there are only 4 priorities. The sguil spp_portscan mod   
    # uses a priority of 5.    
    #set RTPANE_PRIORITY(0) "1 2 3 4 5"  
    set RTPANE_PRIORITY(0) "1"  
    set RTPANE_PRIORITY(1) "2 3"  
    set RTPANE_PRIORITY(2) "4 5"   

DNS Lookups 
-----------
Previously, when pivoting to transcript, the Sguil server would perform DNS lookups on the source and destination IP addresses.  That default has since been changed to increase performance and avoid unnecessary information leakage.  If you would like to re-enable DNS lookups, you can set the following in ``/etc/nsm/securityonion/sguild.conf``:

::

   set TRANSCRIPT_DNS_LOOKUP 1
