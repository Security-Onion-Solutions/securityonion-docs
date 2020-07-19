.. _network:

Network Visibility
==================

In the last section, you logged into :ref:`soc` and you may have seen network-based IDS alerts from Suricata, protocol metadata logs from Zeek, or full packet capture from :ref:`stenographer`. How was that data generated and stored? This section covers the various processes that Security Onion uses to analyze and log network traffic.

.. image:: images/sniffing.png
   :target: _images/sniffing.png

.. toctree::
   :maxdepth: 2

   af-packet
   stenographer
   suricata
   zeek
   strelka
