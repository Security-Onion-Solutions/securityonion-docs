.. _architecture:

Architecture
============

If you're going to deploy Security Onion, you should first decide on what type of deployment you want. This could be anything from a temporary Import installation in a small virtual machine on your personal laptop all the way to a large scalable enterprise deployment consisting of a manager node, multiple search nodes, and lots of forward nodes. This section will discuss what those different deployment types look like from an architecture perspective.

Import
------

The simplest architecture is an ``Import`` node. An import node is a single standalone box that runs just enough components to be able to import pcap or evtx files using the :ref:`grid` page. It does **not** support adding Elastic agents or additional Security Onion nodes.

.. image:: images/diagrams/import.png
   :align: center
   :target: _images/import.png

Evaluation
----------
The next architecture is ``Evaluation``. It's a little more complicated than ``Import`` because it has a network interface dedicated to sniffing live traffic from a TAP or span port. Processes monitor the traffic on that sniffing interface and generate logs. :ref:`elastic-agent` collects those logs and sends them directly to :ref:`elasticsearch` where they are parsed and indexed. Evaluation mode is designed for a quick installation to temporarily test out Security Onion. It is **not** designed for production usage at all and it does not support adding Elastic agents or additional Security Onion nodes.

.. image:: images/diagrams/eval.png
   :align: center
   :target: _images/eval.png

Standalone
----------
``Standalone`` is similar to ``Evaluation`` in that all components run on one box. However, instead of :ref:`elastic-agent` sending logs directly to :ref:`elasticsearch`, it sends them to :ref:`logstash`, which sends them to :ref:`redis` for queuing. A second Logstash pipeline pulls the logs out of :ref:`redis` and sends them to :ref:`elasticsearch`, where they are parsed and indexed.

This type of deployment is typically used for testing, labs, POCs, or **very** low-throughput environments. It's not as scalable as a distributed deployment.

.. image:: images/diagrams/standalone.png
   :align: center
   :target: _images/standalone.png

Distributed
-----------

A standard distributed deployment includes a **manager node**, one or more **forward nodes** running network sensor components, and one or more **search nodes** running Elastic search components. This architecture may cost more upfront, but it provides for greater scalability and performance, as you can simply add more nodes to handle more traffic or log sources.

-  Recommended deployment type
-  Consists of a manager node, one or more forward nodes, and one or more search nodes

.. note::

	If you install a dedicated manager node, you must also deploy one or more search nodes. Otherwise, all logs will queue on the manager and have no place to be stored. If you are limited on the number of nodes you can deploy, you can install a **manager search** node so that your manager node can act as a search node and store those logs. However, please keep in mind that overall performance and scalability of a **manager search** node will be lower compared to our recommended architecture of dedicated manager node and separate search nodes.
	
.. image:: images/diagrams/distributed.png
   :align: center
   :width: 450
   :target: _images/distributed.png

Node Types
----------

Management
~~~~~~~~~~

The ``manager node`` runs :ref:`soc` and :ref:`kibana`. It has its own local instance of :ref:`elasticsearch`, but that's mainly used for storing :ref:`cases` data and central configuration. An analyst connects to the manager node from a client workstation (perhaps :ref:`desktop`) to execute queries and retrieve data. Please keep in mind that a dedicated manager node requires separate search nodes.

The manager node runs the following components:

-  :ref:`soc`
-  :ref:`elasticsearch`
-  :ref:`logstash`
-  :ref:`kibana`
-  :ref:`elastalert`
-  :ref:`redis`

Search Node
~~~~~~~~~~~

Search nodes pull logs from the :ref:`redis` queue on the manager node and then parse and index those logs. When a user queries the manager node, the manager node then queries the search nodes, and they return search results.

Search Nodes run the following components:

-  :ref:`elasticsearch`
-  :ref:`logstash`

Manager Search
~~~~~~~~~~~~~~

A ``manager search`` node is both a manager node and a search node at the same time. Since it is parsing, indexing, and searching data, it has higher hardware requirements than a normal manager node. 

A manager search node runs the following components:

-  :ref:`soc`
-  :ref:`elasticsearch`
-  :ref:`logstash`
-  :ref:`kibana`
-  :ref:`elastalert`
-  :ref:`redis`

Forward Node
~~~~~~~~~~~~

A ``forward node`` forwards alerts and logs from :ref:`suricata` and :ref:`zeek` via :ref:`elastic-agent` to :ref:`logstash` on the manager node, where they are stored in :ref:`elasticsearch` on the manager node or a search node (if the manager node has been configured to use a search node). Full packet capture recorded by :ref:`stenographer` remains on the forward node itself.

Forward nodes run the following components:

-  :ref:`zeek`
-  :ref:`suricata`
-  :ref:`stenographer`

Elastic Fleet Standalone Node
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

An Elastic Fleet Standalone Node is ideal when there is a large number of Elastic endpoints deployed. It reduces the amount of overhead on the Manager node by transferring the workload associated with managing endpoints to a dedicated system. It is also useful for off-network Elastic Agent endpoints that do not have remote access to the Manager node as it can be deployed to the DMZ and TCP/8220 (Elastic Agent Management network traffic) and TCP/5055 (Elastic Agent log shipping) made accessible to your off-network endpoints.

Receiver Node
~~~~~~~~~~~~~

Receiver nodes were designed with 2 purposes in mind:

- reduce the load on the manager
- offer pipeline redundancy

Each receiver node runs :ref:`logstash` and :ref:`redis` and allows for events to continue to be processed by search nodes in the event the manager node is offline. When a receiver node joins the grid, :ref:`elastic-agent` on all nodes adds this new address as a load balanced :ref:`logstash` output. The search nodes add this new node as another :ref:`logstash` input. Receiver nodes are "active-active" and you can add as many as you want (within reason) and events will be balanced among them.

.. image:: images/diagrams/receiver.png
   :align: center
   :width: 450
   :target: _images/receiver.png

If you don't have any receiver nodes and the manager goes down, the search nodes do not index anything because they cannot connect to :ref:`redis`. The agents cannot connect to :ref:`logstash` so the pipeline starts backing up on the agents. In this same scenario with a receiver node the agents would not be able to talk to :ref:`logstash` on the manager and then would try to connect to the receiver node. Once connected they would send their logs to the receiver like nothing was wrong. The search nodes connect to both the manager and receiver nodes and pull events from the :ref:`redis` queue. If the manager goes down, the search nodes will keep pulling the log events from the queue on the receiver node. This allows for scaling of the pipeline. More receivers + more search nodes = more event ingestion volume.

Receiver nodes need to be close to the search nodes because when you add a new receiver node to the grid, the search nodes add the :ref:`redis` service as an input in their configs automatically. If you were to place a receiver node at a remote site, then ALL of your search nodes would be trying to access that :ref:`redis` queue remotely. You do not save any bandwidth by placing a receiver node at a remote site.

There are a couple of things to be aware of regarding receiver nodes and Elastic Agents. The first is Fleet which handles things like updating the agents and scheduling searches. The other is the Elastic Agent log output, which in this case is :ref:`logstash` running on the manager or receiver node. Due to limitations in Elastic licensing we can only have a single output policy. That means that when you add a receiver or a fleet node it gets added to a list that is distributed to the agents. The agents go down that list and stop after a successful connection. The only way to direct agents to specific receivers is to use firewall rules to block agents to certain receivers. Again keep in mind that there is no bandwidth savings here because the search nodes still need to empty the :ref:`redis` queue on the receiver nodes.

Intrusion Detection Honeypot (IDH) Node
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The :ref:`idh` node mimics common services such as HTTP, FTP, and SSH. Any interaction with these fake services will automatically result in an alert.

.. image:: images/diagrams/idh.png
   :align: center
   :width: 450
   :target: _images/idh.png

Heavy Node
~~~~~~~~~~

There is also an option to have a **manager node** and one or more **heavy nodes**.

.. warning::

	Heavy nodes are NOT recommended for most users due to performance reasons, and should only be used for testing purposes or in low-throughput environments.

-  Recommended only if a standard distributed deployment is not possible
-  Consists of a manager node and one or more heavy nodes
-  Each heavy node is an independent Elastic cluster that is queried from the manager via cross-cluster search

.. image:: images/diagrams/heavy-distributed.png
   :align: center
   :target: _images/heavy-distributed.png

.. note::

	Heavy nodes do not consume from the :ref:`redis` queue on the manager. This means that if you just have a manager and heavy nodes, then the :ref:`redis` queue on the manager will grow and never be drained. To avoid this, you have two options. If you are starting a new deployment, you can make your ``manager`` a ``manager search`` so that it will drain its own :ref:`redis` queue. Alternatively, if you have an existing deployment with a ``manager`` and want to avoid rebuilding, then you can add a separate search node (NOT heavy node) to consume from the :ref:`redis` queue on the manager.

Heavy nodes perform sensor duties and store their own logs in their own local :ref:`elasticsearch` instance. This results in higher hardware requirements and lower performance. Heavy nodes do NOT pull logs from the redis queue on the manager like search nodes do.

Heavy Nodes run the following components:

-  :ref:`elasticsearch`
-  :ref:`logstash`
-  :ref:`zeek`
-  :ref:`suricata`
-  :ref:`stenographer`

There are two instances of Elastic Agent that run on a Heavy Node:  

Instance 1 - Not connected to Fleet (runs standalone), runs in a container, picks up /nsm/ logs and other local logs (soc) and sends them to the local Heavy Node ES cluster.

Instance 2 - Connected to Grid Fleet Server, runs directly on the Heavy Node. Not currently picking up any logs, but has the osquery integration installed.

