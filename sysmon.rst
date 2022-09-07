.. _sysmon:

Sysmon
======

From https://technet.microsoft.com/en-us/sysinternals/sysmon:

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

Configuration
-------------

| SwiftOnSecurity has a great sysmon config file to use as a starting point:
| https://github.com/SwiftOnSecurity/sysmon-config

Downloads
---------

| Download sysmon here:
| https://download.sysinternals.com/files/Sysmon.zip

| Download SwiftOnSecurity's example sysmon config here:
| https://github.com/SwiftOnSecurity/sysmon-config/raw/master/sysmonconfig-export.xml

Transport
---------

Sysmon logs can be collected and transported using :ref:`beats`.

Winlogbeat
----------

If you are shipping Sysmon logs via Winlogbeat (see the :ref:`beats` section), confirm that your Winlogbeat configuration does NOT use the Elastic Sysmon module. Security Onion will do all the necessary parsing.

More Information
----------------

.. seealso::

    Check out our Sysmon video at https://youtu.be/Xz-7oDrZdQY!

    | For more information about sysmon, please see:
    | https://technet.microsoft.com/en-us/sysinternals/sysmon

    | TrustedSec has a great Community Guide on Sysmon:
    | https://github.com/trustedsec/SysmonCommunityGuide
