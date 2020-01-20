PCAPs for Testing
=================

Security Onion 16.04 comes with several pcap samples in ``/opt/samples/``.

Links
-----

-  https://www.malware-traffic-analysis.net/

-  https://digitalcorpora.org/corpora/network-packet-dumps

-  https://www.netresec.com/?page=PcapFiles

-  https://www.netresec.com/?page=MACCDC

-  https://github.com/zeek/zeek/tree/master/testing/btest/Traces

-  https://www.ll.mit.edu/r-d/datasets/2000-darpa-intrusion-detection-scenario-specific-datasets

-  https://wiki.wireshark.org/SampleCaptures

-  https://www.stratosphereips.org/datasets-overview

-  https://ee.lbl.gov/anonymized-traces.html

-  https://redmine.openinfosecfoundation.org/projects/suricata/wiki/Public_Data_Sets

-  https://forensicscontest.com/puzzles

-  https://github.com/markofu/hackeire/tree/master/2011/pcap

-  https://www.defcon.org/html/links/dc-ctf.html

-  https://archive.wrccdc.org/

-  https://github.com/chrissanders/packets

tcpreplay
---------

You can use ``tcpreplay`` to replay any of these pcaps on your Security Onion sensor. For example, please see https://blog.securityonion.net/2011/01/introduction-to-sguil-and-squert-part-3.html for a quick, easy use-case and what you should see in the Sguil console.

so-replay
---------

``so-replay`` will use ``tcpreplay`` to replay **all** pcap samples in ``/opt/samples`` to your sniffing interface.

so-import-pcap
--------------

A drawback to using tcpreplay is that it's replaying the pcap as new traffic and thus the timestamps that you see in Kibana, Squert, and Sguil do not reflect the original timestamps from the pcap. To avoid this, a new tool was developed called `so-import-pcap <so-import-pcap>`__.
