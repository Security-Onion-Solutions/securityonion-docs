PCAPs for Testing
=================

Security Onion 16.04 comes with several pcap samples in
``/opt/samples/``.

Links
-----

-  http://www.malware-traffic-analysis.net/

-  http://digitalcorpora.org/corpora/network-packet-dumps

-  http://www.netresec.com/?page=PcapFiles

-  http://www.netresec.com/?page=MACCDC

-  https://github.com/bro/bro/tree/master/testing/btest/Traces

-  http://www.ll.mit.edu/mission/communications/cyber/CSTcorpora/ideval/data/

-  https://wiki.wireshark.org/SampleCaptures

-  https://stratosphereips.org/category/dataset.html

-  http://old.honeynet.org/scans/

-  http://cctf.shmoo.com/

-  http://ee.lbl.gov/anonymized-traces.html

-  https://redmine.openinfosecfoundation.org/projects/suricata/wiki/Public_Data_Sets

-  http://forensicscontest.com/puzzles

-  https://www.evilfingers.com/repository/pcaps.php

-  http://www.honeynet.org/node/504

-  https://github.com/markofu/hackeire/tree/master/2011/pcap

-  http://www.defcon.org/html/links/dc-ctf.html 

-  https://archive.wrccdc.org/

-  https://github.com/chrissanders/packets

tcpreplay
---------

You can use ``tcpreplay`` to replay any of these pcaps on your Security Onion sensor. For example, please see http://blog.securityonion.net/2011/01/introduction-to-sguil-and-squert-part-3.html for a quick, easy use-case and what you should see in the Sguil console.

so-replay
---------

``so-replay`` will use ``tcpreplay`` to replay **all** pcap samples in
``/opt/samples`` to your sniffing interface.

so-import-pcap
--------------

A drawback to using tcpreplay is that it's replaying the pcap as new
traffic and thus the timestamps that you see in Kibana, Squert, and
Sguil do not reflect the original timestamps from the pcap. To avoid
this, a new tool was developed called
`so-import-pcap <so-import-pcap>`__.
