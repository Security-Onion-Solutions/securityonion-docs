Hardware Requirements
=====================

32-bit vs 64-bit
----------------

Security Onion only supports 64-bit hardware.

UEFI Secure Boot
----------------

If your hardware has UEFI Secure Boot enabled, please see `Secure Boot <Secure-Boot>`__.

UPS
---

Like most IT systems, Security Onion has databases and those databases don't like power outages or other ungraceful shutdowns. To avoid power outages and having to manually repair databases, please consider a UPS.

Elastic Stack
-------------

If you're going to enable the Elastic Stack, please note that the MINIMUM requirements are 4 CPU cores and 8GB RAM. These requirements increase as you monitor more traffic and consume more logs.

Please refer to our `Architecture Page <Elastic-Architecture>`__ for detailed deployment scenarios.

**We recommend placing all Elastic storage on SSD or fast spinning disk in a RAID 10 configuration.** This includes ``/nsm/elasticsearch`` and ``/nsm/logstash``.

Standalone Deployments
----------------------

In a standalone deployment, the master server components and the sensor components all run on a single box, therefore, your hardware requirements will reflect that. This deployment type is recommended for evaluation purposes, POCs (proof-of-concept) and small to medium size single sensor deployments. Although you can deploy Security Onion in this manner, it is recommended that you separate the backend components and sensor components.

- CPU: Used to parse incoming events, index incoming events, search metatadata, capture PCAP, analyze packets, and run the frontend components. As data and event consumption increases, a greater amount of CPU will be required.
- RAM: Used for Logstash, Elasticsearch, disk cache for Lucene, Snort/Suricata, Bro, Sguil, etc. The amount of available RAM will directly impact search speeds and reliability, as well as ability to process and capture traffic.
- Disk: Used for storage of indexed metadata. A larger amount of storage allows for a longer retention period. It is typically recommended to retain no more than 30 days of hot ES indices.

Please refer to our `Architecture Page <Elastic-Architecture>`__ for detailed deployment scenarios.

Master server with local log storage
------------------------------------

In an enterprise distributed deployment, a master server will store logs from itself and forward nodes. It can also act as a syslog destination for other log sources to be indexed into Elasticsearch. An enterprise master server should have 8 CPU cores at a minimum, 16-128GB RAM, and enough disk space (multiple terabytes recommended) to meet your retention requirements.

- CPU: Used to parse incoming events, index incoming events, search metadata. As consumption of data and events increases, more CPU will be required.
- RAM: Used for Logstash, Elasticsearch, and disk cache for Lucene. The amount of available RAM will directly impact search speeds and reliability.
- Disk: Used for storage of indexed metadata. A larger amount of storage allows for a longer retention period. It is typically recommended to retain no more than 30 days of hot ES indices.

Please refer to our `Architecture Page <Elastic-Architecture>`__ for detailed deployment scenarios.

Master server with storage nodes
--------------------------------

This deployment type utilizes storage nodes to parse and index of events. As a result, the hardware requirements of the master are reduced. An enterprise master server should have 4-8 CPU cores, 8-16GB RAM, and 100GB to 1TB of disk space. Many folks choose to host their master server in their VM farm since it has lower hardware requirements than sensors but needs higher reliability and availability.

- CPU: Used to receive incoming events and place them into Redis. Used to run all the front end web comp onents and aggregate search results from the storage nodes.
- RAM: Used for Logstash and Redis. The amount of available RAM directly impacts the size of the Redis queue.
- Disk: Used for general purposes, as well as storing dashboards and Sguil components.

Please refer to our `Architecture Page <Elastic-Architecture>`__ for detailed deployment scenarios.

Storage Node
------------

Storage nodes increase search and retention capacity with regard to Elasticsearch. These nodes parse and index events, and provide the ability to scale horizontally as overall data intake increases.

- CPU: Used to parse incoming events and index incoming events. As consumption of data and events increases, more CPU will be required.
- RAM: Used for Logstash, Elasticsearch, and disk cache for Lucene. The amount of available RAM will directly impact search speeds and reliability.
- Disk: Used for storage of indexed metadata. A larger amount of storage allows for a longer retention period. It is typically recommended to retain no more than 30 days of hot ES indices.

Please refer to our `Architecture Page <Elastic-Architecture>`__ for detailed deployment scenarios.

Forward Node (Sensor)
---------------------

A forward node runs sensor components only, and forwards metadata to the master server. All PCAP stays local to the sensor, and is accessed through use of an agent.

- CPU: Used for analyzing and storing network traffic. As monitored bandwidth increases, a greater amount of CPU will be required. See below.
- RAM: Used for write cache and processing traffic.
- Disk: Used for storage of PCAP and metadata . A larger amount of storage allows for a longer retention period.

Please refer to our `Architecture Page <Elastic-Architecture>`__ for detailed deployment scenarios.

Heavy Node (Sensor with ES components)
--------------------------------------

A heavy node Runs all the sensor components AND Elastic components locally. This dramatically increases the hardware requirements. In this case, all indexed metadata and PCAP are retained locally. When a search is performed through Kibana, the master server queries this node's Elasticsearch instance.

- CPU: Used to parse incoming events, index incoming events, search metadata . As monitored bandwidth (and the amount of overall data/events) increases, a greater amount of CPU will be required.
- RAM: Used for Logstash , Elasticsearch, and disk cache for Lucene. The amount of available RAM will directly impact search speeds and reliability.
- Disk: Used for storage of indexed metadata. A larger amount of storage allows for a longer retention period. It is typically recommended to retain no more than 30 days of hot ES indices.

Please refer to our `Architecture Page <Elastic-Architecture>`__ for detailed deployment scenarios.

Sensor Hardware Considerations
------------------------------

The following hardware considerations apply to sensors. If you are using a heavy node or standalone deployment type, please note that it will dramatically increase CPU/RAM/Storage requirements.

Virtualization
~~~~~~~~~~~~~~

We recommend dedicated physical hardware (especially if you're monitoring lots of traffic) to avoid competing for resources. Sensors can be virtualized, but you'll have to ensure that they are allocated sufficient resources.

CPU
~~~

Snort, Suricata, and Bro are very CPU intensive. The more traffic you are monitoring, the more CPU cores you'll need. A very rough ballpark estimate would be 200Mbps per Snort instance, Suricata worker, or Bro worker. So if you have a fully saturated 1Gbps link and are running Snort and Bro, then you'll want at least 5 Snort instances and 5 Bro workers, which means you'll need at least 10 CPU cores for Snort and Bro with additional CPU cores for netsniff-ng and/or other services.

RAM
~~~

RAM usage is highly dependent on several variables:

-  the services that you enable
-  the **kinds** of traffic you're monitoring
-  the **actual amount of traffic** you're monitoring (example: you may be monitoring a 1Gbps link but it's only using 200Mbps most of the time)
-  the amount of packet loss that is "acceptable" to your organization

For best performance, over provision RAM so that you can fully disable swap.

The following RAM estimates are a rough guideline and assume that you're going to be running Snort/Suricata, Bro, and netsniff-ng (full packet capture) and want to minimize/eliminate packet loss. Your mileage may vary!

If you just want to quickly evaluate Security Onion in a VM, the bare minimum amount of RAM needed is 8GB. More is obviously better!

If you're deploying Security Onion in production on a small network (50Mbps or less), you should plan on 8GB RAM or more. Again, more is obviously better!

If you're deploying Security Onion in production to a medium network (50Mbps - 500Mbps), you should plan on 16GB - 128GB RAM or more.

If you're deploying Security Onion in production to a large network (500Mbps - 1000Mbps), you should plan on 128GB - 256GB RAM or more.

If you're buying a new server, go ahead and max out the RAM (it's cheap!). As always, more is obviously better!

Storage
~~~~~~~

Sensors that have full packet capture enabled need LOTS of storage. For example, suppose you are monitoring a link that averages 50Mbps, here are some quick calculations: 50Mb/s = 6.25 MB/s = 375 MB/minute = 22,500 MB/hour = 540,000 MB/day. So you're going to need about 540GB for one day's worth of pcaps (multiply this by the number of days you want to keep on disk for investigative/forensic purposes). The more disk space you have, the more PCAP retention you'll have for doing investigations after the fact. Disk is cheap, get all you can!

We highly recommend using local storage whenever possible! SAN/iSCSI/FibreChannel/NFS can be made to work, but they increase complexity, points of failure and have serious performance implications. By using local storage, you keep everything self-contained and you don't have to worry about competing for resources. Local storage is most times the most cost efficient solution as well.

NIC
~~~

You'll need at least two wired network interfaces: one for management (preferably connected to a dedicated management network) and then one or more for sniffing (connected to tap or span). Make sure you get good quality network card, especially for sniffing. Most users report good experiences with Intel cards.

Packets
~~~~~~~

You need some way of getting packets into your sensor interface(s). If you're just evaluating Security Onion, you can replay `pcaps <Pcaps>`__. For a production deployment, you'll need a tap or SPAN/monitor port. Here are some inexpensive tap/span solutions:

| Sheer Simplicity and Portability (USB-powered):
| http://www.dual-comm.com/port-mirroring-LAN\_switch.htm

| Dirt Cheap and Versatile:
| http://www.roc-noc.com/mikrotik/routerboard/RB260GS.html

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

Further Reading
~~~~~~~~~~~~~~~

For large networks and/or deployments, please also see https://github.com/pevma/SEPTun.
