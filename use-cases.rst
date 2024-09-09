.. _use-cases:

Use Cases
=========

Let's discuss some common use cases and how they map to our different kinds of architecture.

Minimal Import
--------------

Suppose you just want to import PCAP or EVTX files. Install our ISO image on a machine and choose the ``Import`` option. You can read more in the :ref:`first-time-users` section and in the :ref:`architecture` section under Import.

Minimal Network Visibility
--------------------------

Suppose you have a small network where you just want some basic network visibility. Install our ISO image on a machine and choose the ``Evaluation`` option. This machine will then analyze network traffic from your tap or span port. You can read more in the :ref:`architecture` section under Evaluation.

Minimal Network and Host Visibility
-----------------------------------

Suppose you have a small network where you want both network visibility and host visibility. Install our ISO image on a machine and choose the ``Standalone`` option. This machine will then sniff network traffic from your tap or span port and also support deploying the :ref:`elastic-agent` to other hosts. You can read more in the :ref:`architecture` section under Standalone.

Minimal Host Visibility
-----------------------

Suppose you have a small network where you just want some basic host visibility. Install our ISO image on a machine and choose the ``ManagerSearch`` option (you can read more about this option in the :ref:`architecture` section under Distributed). You can then deploy the :ref:`elastic-agent` to your hosts.

Enterprise Deployment
---------------------

Suppose you have a large network where you want maximum visibility for both network and hosts. A distributed deployment would look like this:

- Install our ISO image on a machine and choose the ``Manager`` option.
- Install our ISO image on one or more machines and join them to the manager as search nodes.
- At this point, you can deploy the :ref:`elastic-agent` to hosts. If you will be deploying the :ref:`elastic-agent` to laptops outside of your main network, then you may want to deploy a Fleet Node to your DMZ.
- Install our ISO image on one or more machines and join them to the manager as forward nodes. They will analyze network traffic from your taps or span ports.
- If you want some pipeline redundancy, then you may want to install a receiver node and join it to your manager.
- Optionally install one or more :ref:`idh` nodes and deploy them in key locations throughout your enterprise.

You can read more about this in the :ref:`architecture` section under Distributed.
