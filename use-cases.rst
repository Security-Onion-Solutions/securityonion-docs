.. _use-cases:

Use Cases
=========

If you’re going to deploy Security Onion, you should first decide what your use case is. In this section, we'll discuss some common use cases and how they map to our different kinds of architecture. This could be anything from a temporary Import installation in a small virtual machine on your personal laptop all the way to a large scalable enterprise deployment consisting of a manager node, multiple search nodes, and lots of forward nodes.

Minimal Import
--------------

Suppose you just want to import PCAP or EVTX files or suppose that you have limited hardware and just want the minimal installation to get some experience with Security Onion. Install our ISO image on a machine and choose the ``Import`` option. This can be done in a minimal virtual machine with as little as 4GB RAM. You can read more about the ``Import`` option in the :ref:`first-time-users` section and in the :ref:`architecture` section.

Minimal Network Visibility
--------------------------

Suppose you have a small network where you just want some basic network visibility. This might be a homelab or other small network that doesn't require a production installation. Install our ISO image on a machine and choose the ``Evaluation`` option. This machine will then analyze network traffic from your tap or span port. You can read more about the ``Evaluation`` option in the :ref:`architecture` section.

Minimal Network and Host Visibility
-----------------------------------

Suppose you have a small network where you want both network visibility and host visibility. Install our ISO image on a machine and choose the ``Standalone`` option. This machine will then sniff network traffic from your tap or span port and also support deploying the :ref:`elastic-agent` to other hosts. You can read more about the ``Standalone`` option in the :ref:`architecture` section.

Minimal Host Visibility
-----------------------

Suppose you have a small network where you just want some basic host visibility. Install our ISO image on a machine, choose the ``ManagerSearch`` option, and then deploy the :ref:`elastic-agent` to your hosts. You can read more about the ``ManagerSearch`` option in the :ref:`architecture` section.

Enterprise Deployment
---------------------

Suppose you have a large network where you want maximum visibility for both network and hosts. A distributed deployment would look like this:

- Install our ISO image on a machine and choose the ``Manager`` option.
- Install our ISO image on one or more machines and join them to the manager as search nodes.
- At this point, you can deploy the :ref:`elastic-agent` to hosts. If you will be deploying the :ref:`elastic-agent` to laptops outside of your main network, then you may want to deploy a Fleet Node to your DMZ.
- Install our ISO image on one or more machines and join them to the manager as forward nodes. They will analyze network traffic from your taps or span ports.
- If you want some pipeline redundancy, then you may want to install a receiver node and join it to your manager.
- Optionally install one or more :ref:`idh` nodes and deploy them in key locations throughout your enterprise.

You can read more about distributed deployments in the :ref:`architecture` section.
