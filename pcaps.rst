.. _pcaps:

PCAPs for Testing
=================

The easiest way to download pcap files for testing is our :ref:`so-test` tool. Alternatively, you could manually download pcaps from one or more of the following locations:

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

-  https://github.com/chrissanders/packets

You can download pcap files from the links above using a standard web browser or from the command line using a tool like ``wget`` or ``curl``.

Replay
------

You can use ``tcpreplay`` to replay any standard pcap to the sniffing interface of your Security Onion sensor.

Import
------

A drawback to using tcpreplay is that it's replaying the pcap as new traffic and thus the timestamps that you see in :ref:`soc` and other interfaces do not reflect the original timestamps from the pcap. To avoid this, you can import the pcap using the :ref:`grid` page.
