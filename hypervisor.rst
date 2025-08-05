.. _hypervisor:

Hypervisor
==========

Starting with Security Onion version 2.4.170, Security Onion Pro users can create a hypervisor node that can run virtualized instances of Security Onion. If you have machines with extra horsepower, you can use this feature to spin up additional Security Onion virtual machines (VMs) to take advantage of that extra power.

.. note::

    This is an enterprise-level feature of Security Onion. Contact Security Onion Solutions, LLC via our website at https://securityonion.com/pro for more information about purchasing a Security Onion Pro license to enable this feature.

Minimum Requirements
--------------------

Please note the following MINIMUM requirements for a Hypervisor node:

- 32 CPU cores
- 64GB RAM

Airgap
------

Users in an airgapped environment will need to follow these steps prior to accepting the hypervisor node in SOC Grid Members:
 
1. Download the Oracle 9 Qcow2 image from https://download.securityonion.net/file/securityonion/OL9U5_x86_64-kvm-b253.qcow2

2. Place OL9U5_x86_64-kvm-b253.qcow2 into /nsm/libvirt/boot/ on your manager node

Adding a Hypervisor
-------------------

Install a new node, select the ``DISTRIBUTED`` deployment option, choose ``Existing Deployment``, and then select the ``Hypervisor`` option:

.. image:: images/hypervisor/hyper-0.png
  :target: _images/hyper-0.png

The manager will need to be able to connect to the hypervisor node by name so it will either need a DNS entry or you can manually add an entry in /etc/hosts on the manager.

Once the new hypervisor node has been accepted into the grid, go to SOC Configuration, click the Options menu, enable advanced settings, and then navigate to ``hypervisor`` settings. It should look like this:

.. image:: images/hypervisor/hyper-1.png
  :target: _images/hyper-1.png

Once the base domain has been configured on the hypervisor (allowing VMs to be created), it should look like this:

.. image:: images/hypervisor/hyper-2.png
  :target: _images/hyper-2.png

Adding a Security Onion VM
--------------------------

Please note that hardware for a vm cannot be modified once a vm is created.

To create a new VM, click the plus sign:

.. image:: images/hypervisor/hyper-3.png
  :target: _images/hyper-3.png

Fill out the form and then click the green check to save and create the VM:

.. image:: images/hypervisor/hyper-4.png
  :target: _images/hyper-4.png

Once the VM is created and the first highstate is initiated, it should look like this:

.. image:: images/hypervisor/hyper-5.png
  :target: _images/hyper-5.png

Deleting a VM
-------------

To delete a VM, click the trash icon:

.. image:: images/hypervisor/hyper-6.png
  :target: _images/hyper-6.png

It will ask for confirmation:

.. image:: images/hypervisor/hyper-7.png
  :target: _images/hyper-7.png

Once you've confirmed, it will show that it is pending deletion:

.. image:: images/hypervisor/hyper-8.png
  :target: _images/hyper-8.png

