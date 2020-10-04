.. _network:

Network Visibility
==================

When you log into :ref:`soc`, you may see network-based IDS alerts from :ref:`suricata`, protocol metadata logs from :ref:`zeek`, file analysis logs from :ref:`strelka` or full packet capture from :ref:`stenographer`. How is that data generated and stored? This section covers the various processes that Security Onion uses to analyze and log network traffic.

.. image:: images/sniffing.png
   :target: _images/sniffing.png

.. toctree::
   :maxdepth: 2

   af-packet
   stenographer
   suricata
   zeek
   strelka
