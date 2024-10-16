.. _sysmon:

Sysmon
======

From https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon:

    System Monitor (Sysmon) is a Windows system service and device driver that, once installed on a system, remains resident across
    system reboots to monitor and log system activity to the Windows event log. It provides detailed information about process creations,
    network connections, and changes to file creation time. By collecting the events it generates using Windows Event Collection or
    SIEM agents and subsequently analyzing them, you can identify malicious or anomalous activity and understand how intruders and
    malware operate on your network.

Integration
-----------

| Josh Brower wrote a great paper on integrating sysmon into Security Onion:
| https://www.sans.org/reading-room/whitepapers/forensics/sysmon-enrich-security-onion-039-s-host-level-capabilities-35837

Please note that the paper is a few years old and was therefore written for an older version of Security Onion.

Downloads
---------

You can download sysmon from Microsoft at https://download.sysinternals.com/files/Sysmon.zip.

Once you've downloaded sysmon, you probably also want to download a sysmon config to use as a starting point. Here are a few options to choose from.

https://github.com/Neo23x0/sysmon-config

https://github.com/SwiftOnSecurity/sysmon-config

https://github.com/olafhartong/sysmon-modular

Transport
---------

Sysmon logs can be collected and transported using :ref:`elastic-agent`. Confirm that your configuration does NOT use the Elastic Sysmon module. Security Onion will do all the necessary parsing.

Visualizations
--------------

Once Security Onion is receiving and parsing Sysmon data, you can search for that data and visualize it via :ref:`dashboards`, :ref:`hunt`, or :ref:`kibana`. Each of these interfaces have at least one dashboard or query specifically designed for Sysmon data.

More Information
----------------

.. note::

    | For more information about sysmon, please see:
    | https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon

    | TrustedSec has a great Community Guide on Sysmon:
    | https://github.com/trustedsec/SysmonCommunityGuide
