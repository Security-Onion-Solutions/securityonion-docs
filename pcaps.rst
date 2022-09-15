.. _pcaps:

PCAPs for Testing
=================

The easiest way to download pcaps for testing is our :ref:`so-test` tool. Alternatively, you could manually download pcaps from one or more of the following locations:

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

You can download pcaps from the link above using a standard web browser or from the command line using a tool like ``wget`` or ``curl``. Here are some examples.

To download the pcap from https://www.malware-traffic-analysis.net/2020/09/16/index.html using wget:

::

  wget https://www.malware-traffic-analysis.net/2020/09/16/2020-09-16-Qakbot-infection-traffic.pcap.zip

To download a pcap from https://www.netresec.com/?page=MACCDC:

::

  wget https://download.netresec.com/pcap/maccdc-2012/maccdc2012_00000.pcap.gz

tcpreplay
---------

You can use ``tcpreplay`` to replay any standard pcap to the sniffing interface of your Security Onion sensor.

import
------

A drawback to using tcpreplay is that it's replaying the pcap as new traffic and thus the timestamps that you see in :ref:`kibana` and other interfaces do not reflect the original timestamps from the pcap. To avoid this, a new tool was developed called :ref:`so-import-pcap`.
