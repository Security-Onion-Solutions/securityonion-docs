so-import-pcap
==============

``so-import-pcap`` is a quick and dirty EXPERIMENTAL script that will import one or more pcaps into Security Onion and preserve original timestamps.

It will do the following:

-  stop and disable Curator to avoid closing old indices
-  stop and disable all active sniffing processes (Bro, Snort, Suricata, and netsniff-ng)
-  stop and disable ossec_agent
-  reconfigure and restart sguild, syslog-ng, and Logstash where necessary
-  generate IDS alerts using Snort or Suricata
-  generate Bro logs
-  store IDS alerts and Bro logs with original timestamps
-  split traffic into separate daily pcaps and store them where sguil's pcap_agent can find them

Requirements:

-  You must be running at least Security Onion Elastic Stack Release Candidate 2 (14.04.5.8 ISO).
-  You must have a sniffing interface defined (you can choose Evaluation Mode in the Setup wizard).

Warnings:

-  Do NOT run this on a production deployment. It is designed for standalone systems designated for so-import-pcap.
-  If you're running in a VM with snapshot capability, you might want to take a snapshot before this program makes changes.

Reverting System Changes:

-  If you take a VM snapshot before this program makes changes, then just revert to snapshot.
-  Otherwise, you can re-run Setup and it should overwrite all modified files to revert the system to normal operation.

Usage
-----

Please supply at least one pcap file.

For example, to import a single pcap named import.pcap:

::

    so-import-pcap import.pcap

To import multiple pcaps:

::

    so-import-pcap import1.pcap import2.pcap

Example
-------

| For a detailed walk-through with screenshots, please see:
| https://taosecurity.blogspot.com/2018/02/importing-pcap-into-security-onion.html

Warning
-------

Please note that so-import-pcap will make changes to your system! It will warn you before doing so and will prompt you to press Enter to continue or Ctrl-c to cancel.

If you want to bypass the "Press Enter to continue" prompt, you can do something like this:

::

    echo | sudo so-import-pcap /opt/samples/markofu/ie*
