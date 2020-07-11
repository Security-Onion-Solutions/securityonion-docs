.. _production-deployment:

Production Deployment
=====================

If you're going to be deploying Security Onion in production, please use the following steps.

Hardware Requirements
---------------------

First, check the :ref:`hardware` section.

Architecture
------------

Next, review the :ref:`architecture` section.

Download and Verify
-------------------

We **highly** recommend using our Security Onion ISO image as it automates many of the settings that are required for production usage!

| `Download and verify the Security Onion ISO image <https://github.com/Security-Onion-Solutions/securityonion/wiki/ISO>`__ 
| OR
| download and verify the ISO image for your preferred flavor of CentOS 7 64-bit or Ubuntu 18.04 64-bit.

Distributed Deployments
-----------------------

If deploying a distributed environment, you’ll need to perform the remaining steps on the manager node, as well as all forward and search nodes, but make sure you install and configure the manager node first. For best performance, the manager node should be dedicated to just being a server for the other nodes (the manager node should have no sniffing interfaces of its own). Please note that all nodes will need to be able to connect to the manager node on ports ``22``, ``4505``, and ``4506``.

Install
-------

Follow the appropriate installation guide but do NOT select the ``EVAL`` option. Instead, select one of the appropriate production roles.

Build the manager by following the prompts. Save the ``soremote`` password so that you can join nodes to the grid.

Build storage nodes and join them to the manager node using the ``soremote`` password.

Build forward nodes and join them to the manager node using the ``soremote`` password.

Proceed to :ref:`post-installation`.
