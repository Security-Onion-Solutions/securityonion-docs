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

Minimal Enterprise Deployment
-----------------------------

Suppose you have a small or medium network where you want some visibility for both network and hosts. A minimal enterprise deployment would look like this:

- Install our ISO image on a machine and choose the ``ManagerSearch`` option.
- Deploy the :ref:`elastic-agent` to hosts.
- Install our ISO image on one or more machines and join them to the grid as forward nodes. They will analyze network traffic from your taps or span ports.

More Scalable Enterprise Deployment
-----------------------------------

Suppose you have a medium or large network where you want some visibility for both network and hosts. A more scalable enterprise deployment would look like this:

- Install our ISO image on a machine and choose the ``Manager`` option.
- Install our ISO image on one or more machines and join them to the grid as search nodes.
- Deploy the :ref:`elastic-agent` to hosts.
- Install our ISO image on one or more machines and join them to the grid as forward nodes. They will analyze network traffic from your taps or span ports.

Comprehensive Enterprise Deployment
-----------------------------------

Suppose you have a large network where you want maximum visibility for both network and hosts. A comprehensive distributed deployment would look like this:

- Install our ISO image on a machine and choose the ``Manager`` option.
- Install our ISO image on one or more machines and join them to the grid as search nodes.
- Install our ISO image on a machine in your DMZ and join it to the grid as a Fleet node.
- Deploy the :ref:`elastic-agent` to hosts.
- Install our ISO image on one or more machines and join them to the grid as forward nodes. They will analyze network traffic from your taps or span ports.
- Install our ISO image on a machine and join it to the grid as a receiver node. This provides load balancing and pipeline redundancy.
- Install our ISO image on one or more machines and join them to the grid as :ref:`idh` nodes. They will provide honeypot and deception capabilities.

You can read more about distributed deployments in the :ref:`architecture` section.
