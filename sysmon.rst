Sysmon
======

From https://technet.microsoft.com/en-us/sysinternals/sysmon:

    System Monitor (Sysmon) is a Windows system service and device
    driver that, once installed on a system, remains resident across
    system reboots to monitor and log system activity to the Windows
    event log. It provides detailed information about process creations,
    network connections, and changes to file creation time. By
    collecting the events it generates using Windows Event Collection or
    SIEM agents and subsequently analyzing them, you can identify
    malicious or anomalous activity and understand how intruders and
    malware operate on your network.

Integration
-----------

| Josh Brower wrote a great paper on integrating sysmon into Security
  Onion:
| https://digital-forensics.sans.org/community/papers/gcfa/sysmon-enrich-security-onions-host-level-capabilities_10612

Configuration
-------------

| SwiftOnSecurity has a great sysmon config file to use as a starting
  point:
| https://github.com/SwiftOnSecurity/sysmon-config

Downloads
---------

| Download sysmon here:
| https://download.sysinternals.com/files/Sysmon.zip

| Download SwiftOnSecurity's example sysmon config here:
| https://github.com/SwiftOnSecurity/sysmon-config/raw/master/sysmonconfig-export.xml

More Information
----------------

| How to Go from Responding to Hunting with Sysinternals Sysmon:
| https://onedrive.live.com/view.aspx?resid=D026B4699190F1E6!2843&ithint=file%2cpptx
