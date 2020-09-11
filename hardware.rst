.. _hardware:

Hardware Requirements
=====================

The :ref:`architecture` section should have helped you determine how many machines you will need for your deployment. This section will help you determine what kind of hardware specs each of those machines will need.

CPU Architecture
----------------

Security Onion only supports x86-64 architecture (standard Intel or AMD 64-bit processors).

.. warning::

   We do not support ARM or any other non-x86-64 processors!

Minimum Specs
-------------
If you just want to import a pcap using :ref:`so-import-pcap`, then you can configure Security Onion 2.2 as an Import Node with the following minimum specs:

 - 4GB RAM
 - 2 CPU cores
 - 200GB storage

For all other configurations, the minimum specs for running Security Onion 2.2 are:

 - 12GB RAM
 - 4 CPU cores
 - 200GB storage

.. note::

   These minimum specs are for EVAL mode with minimal services running. These requirements may increase drastically as you enable more services, monitor more traffic, and consume more logs. For more information, please see the detailed sections below.

Production Deployments
----------------------
Security Onion 2.2 is a new platform with more features than previous versions of Security Onion. These additional features result in higher hardware requirements. For best results, we recommend purchasing new hardware to meet the new requirements.

.. tip::

   If you're planning to purchase new hardware, please consider official Security Onion appliances from Security Onion Solutions (https://securityonionsolutions.com). Our custom appliances have already been designed for certain roles and traffic levels and have Security Onion pre-installed. Purchasing from Security Onion Solutions will save you time and effort **and** help to support development of Security Onion as a free and open source platform!

Storage
-------

We only support local storage. Remote storage like SAN/iSCSI/FibreChannel/NFS increases complexity and points of failure, and has serious performance implications. You may be able to make remote storage work, but we do not provide any support for it. By using local storage, you keep everything self-contained and you don't have to worry about competing for resources. Local storage is usually the most cost efficient solution as well.

NIC
---

You'll need at least one wired network interface dedicated to management (preferably connected to a dedicated management network). We recommend using static IP addresses where possible.

If you plan to sniff network traffic from a tap or span port, then you will need one or more interfaces dedicated to sniffing (no IP address). The installer will automatically disable NIC offloading functions such as ``tso``, ``gso``, and ``gro`` on sniffing interfaces to ensure that Suricata and Zeek get an accurate view of the traffic.

Make sure you get good quality network cards, especially for sniffing. Most users report good experiences with Intel cards. 

Security Onion is designed to use wired interfaces.  You may be able to make wireless interfaces work, but we don't recommend or support it.

UPS
---

Like most IT systems, Security Onion has databases and those databases don't like power outages or other ungraceful shutdowns. To avoid power outages and having to manually repair databases, please consider a UPS.

Elastic Stack
-------------

Please refer to the :ref:`architecture` section for detailed deployment scenarios.

**We recommend placing all Elastic storage (/nsm/elasticsearch) on SSD or fast spinning disk in a RAID 10 configuration.**

Standalone Deployments
----------------------

In a standalone deployment, the manager components and the sensor components all run on a single box, therefore, your hardware requirements will reflect that. You'll need at minimum 16GB RAM, 4 CPU cores, and 200GB storage.

This deployment type is recommended for evaluation purposes, POCs (proof-of-concept) and small to medium size single sensor deployments. Although you can deploy Security Onion in this manner, it is recommended that you separate the backend components and sensor components.

- CPU: Used to parse incoming events, index incoming events, search metatadata, capture PCAP, analyze packets, and run the frontend components. As data and event consumption increases, a greater amount of CPU will be required.
- RAM: Used for Logstash, Elasticsearch, disk cache for Lucene, Suricata, Zeek, etc. The amount of available RAM will directly impact search speeds and reliability, as well as ability to process and capture traffic.
- Disk: Used for storage of indexed metadata. A larger amount of storage allows for a longer retention period. It is typically recommended to retain no more than 30 days of hot ES indices.

Please refer to the :ref:`architecture` section for detailed deployment scenarios.

Manager node with local log storage
-----------------------------------

In an enterprise distributed deployment, a manager node will store logs from itself and forward nodes. It can also act as a syslog destination for other log sources to be indexed into Elasticsearch. An enterprise manager node should have 8 CPU cores at a minimum, 16-128GB RAM, and enough disk space (multiple terabytes recommended) to meet your retention requirements.

- CPU: Used to parse incoming events, index incoming events, search metadata. As consumption of data and events increases, more CPU will be required.
- RAM: Used for Logstash, Elasticsearch, and disk cache for Lucene. The amount of available RAM will directly impact search speeds and reliability.
- Disk: Used for storage of indexed metadata. A larger amount of storage allows for a longer retention period. It is typically recommended to retain no more than 30 days of hot ES indices.

Please refer to the :ref:`architecture` section for detailed deployment scenarios.

Manager node with search nodes
------------------------------

This deployment type utilizes search nodes to parse and index events. As a result, the hardware requirements of the manager node are reduced. An enterprise manager node should have at least 4-8 CPU cores, 16GB RAM, and 200GB to 1TB of disk space. Many folks choose to host their manager node in their VM farm since it has lower hardware requirements than sensors but needs higher reliability and availability.

- CPU: Used to receive incoming events and place them into Redis. Used to run all the front end web comp onents and aggregate search results from the search nodes.
- RAM: Used for Logstash and Redis. The amount of available RAM directly impacts the size of the Redis queue.
- Disk: Used for general OS purposes and storing Kibana dashboards.

Please refer to the :ref:`architecture` section for detailed deployment scenarios.

Search Node
-----------

Search nodes increase search and retention capacity with regard to Elasticsearch. These nodes parse and index events, and provide the ability to scale horizontally as overall data intake increases. Search nodes should have at least 4-8 CPU cores, 16-64GB RAM, and 200GB of disk space or more depending on your logging requirements.

- CPU: Used to parse incoming events and index incoming events. As consumption of data and events increases, more CPU will be required.
- RAM: Used for Logstash, Elasticsearch, and disk cache for Lucene. The amount of available RAM will directly impact search speeds and reliability.
- Disk: Used for storage of indexed metadata. A larger amount of storage allows for a longer retention period. It is typically recommended to retain no more than 30 days of hot ES indices.

Please refer to the :ref:`architecture` section for detailed deployment scenarios.

Forward Node (Sensor)
---------------------

A forward node runs sensor components only, and forwards metadata to the manager node. All PCAP stays local to the sensor, and is accessed through use of an agent.

- CPU: Used for analyzing and storing network traffic. As monitored bandwidth increases, a greater amount of CPU will be required. See below.
- RAM: Used for write cache and processing traffic.
- Disk: Used for storage of PCAP and metadata . A larger amount of storage allows for a longer retention period.

Please refer to the :ref:`architecture` section for detailed deployment scenarios.

Heavy Node (Sensor with ES components)
--------------------------------------

A heavy node Runs all the sensor components AND Elastic components locally. This dramatically increases the hardware requirements. In this case, all indexed metadata and PCAP are retained locally. When a search is performed through Kibana, the manager node queries this node's Elasticsearch instance.

- CPU: Used to parse incoming events, index incoming events, search metadata . As monitored bandwidth (and the amount of overall data/events) increases, a greater amount of CPU will be required.
- RAM: Used for Logstash , Elasticsearch, and disk cache for Lucene. The amount of available RAM will directly impact search speeds and reliability.
- Disk: Used for storage of indexed metadata. A larger amount of storage allows for a longer retention period. It is typically recommended to retain no more than 30 days of hot ES indices.

Please refer to the :ref:`architecture` section for detailed deployment scenarios.

Sensor Hardware Considerations
------------------------------

The following hardware considerations apply to sensors. If you are using a heavy node or standalone deployment type, please note that it will dramatically increase CPU/RAM/Storage requirements.

Virtualization
~~~~~~~~~~~~~~

We recommend dedicated physical hardware (especially if you're monitoring lots of traffic) to avoid competing for resources. Sensors can be virtualized, but you'll have to ensure that they are allocated sufficient resources.

CPU
~~~

Suricata and Zeek are very CPU intensive. The more traffic you are monitoring, the more CPU cores you'll need. A very rough ballpark estimate would be 200Mbps per Suricata worker or Zeek worker. So if you have a fully saturated 1Gbps link and are running Suricata and Zeek, then you'll want at least 5 Suricata instances and 5 Zeek workers, which means you'll need at least 10 CPU cores for Suricata and Zeek with additional CPU cores for Stenographer and/or other services.

RAM
~~~

RAM usage is highly dependent on several variables:

-  the services that you enable
-  the **kinds** of traffic you're monitoring
-  the **actual amount of traffic** you're monitoring (example: you may be monitoring a 1Gbps link but it's only using 200Mbps most of the time)
-  the amount of packet loss that is "acceptable" to your organization

For best performance, over provision RAM so that you can fully disable swap.

The following RAM estimates are a rough guideline and assume that you're going to be running Suricata, Zeek, and Stenographer (full packet capture) and want to minimize/eliminate packet loss. Your mileage may vary!

If you just want to quickly evaluate Security Onion in a VM, the bare minimum amount of RAM needed is 12GB. More is obviously better!

If you're deploying Security Onion in production on a small network (100Mbps or less), you should plan on 16GB RAM or more. Again, more is obviously better!

If you're deploying Security Onion in production to a medium network (100Mbps - 1000Mbps), you should plan on 16GB - 128GB RAM or more.

If you're deploying Security Onion in production to a large network (1000Mbps - 10Gbps), you should plan on 128GB - 256GB RAM or more.

If you're buying a new server, go ahead and max out the RAM (it's cheap!). As always, more is obviously better!

Storage
~~~~~~~

Sensors that have full packet capture enabled need LOTS of storage. For example, suppose you are monitoring a link that averages 50Mbps, here are some quick calculations: 50Mb/s = 6.25 MB/s = 375 MB/minute = 22,500 MB/hour = 540,000 MB/day. So you're going to need about 540GB for one day's worth of pcaps (multiply this by the number of days you want to keep on disk for investigative/forensic purposes). The more disk space you have, the more PCAP retention you'll have for doing investigations after the fact. Disk is cheap, get all you can!

Packets
~~~~~~~

You need some way of getting packets into your sensor interface(s). If you're just evaluating Security Onion, you can replay :ref:`pcaps`. For a production deployment, you'll need a tap or SPAN/monitor port. Here are some inexpensive tap/span solutions:

| Sheer Simplicity and Portability (USB-powered):
| http://www.dual-comm.com/port-mirroring-LAN\_switch.htm

| Dirt Cheap and Versatile:
| https://mikrotik.com/product/RB260GS

| Netgear GS105E (requires Windows app for config):
| https://www.netgear.com/support/product/GS105E.aspx

| Netgear GS105E v2 (includes built-in web server for config):
| https://www.netgear.com/support/product/GS105Ev2

| low cost TAP that uses USB or Ethernet port:
| http://www.midbittech.com

| More exhaustive list of enterprise switches with port mirroring:
| http://www.miarec.com/knowledge/switches-port-mirroring


Enterprise Tap Solutions:

-  `Net Optics /
   Ixia <http://www.ixiacom.com/network-visibility-products>`__
-  `Arista Tap Aggregation Feature
   Set <http://www.arista.com/en/solutions/tap-aggregation>`__
-  `Gigamon <http://gigamon.com>`__
-  `cPacket <http://cpacket.com>`__
-  `Bigswitch Monitoring
   Fabric <http://www.bigswitch.com/products/big-monitoring-fabric>`__
-  `Garland Technologies
   Taps <https://www.garlandtechnology.com/products>`__
-  `APCON <https://www.apcon.com/products>`__
-  `Profitap <https://www.profitap.com>`__

Further Reading
~~~~~~~~~~~~~~~

For large networks and/or deployments, please also see https://github.com/pevma/SEPTun.
