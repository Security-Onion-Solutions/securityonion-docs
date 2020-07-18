.. _installation:

Installation
============

Having downloaded your desired ISO according to the :ref:`download` section, it's now time to install! There are separate sections below to walk you through installing using our Security Onion ISO image (based on CentOS 7) **or** installing standard CentOS 7 or Ubuntu 18.04 and then installing our components on top.

.. tip::

  For most use cases, we recommend using our Security Onion ISO image as it's the quickest and easiest method.

.. _partitioning:

Partitioning
------------

If you're installing Security Onion for a production deployment, you'll want to pay close attention to partitioning to make sure you don't fill up a partition at some point.

ISO
~~~

If you use our Security Onion ISO image, it will automatically partition your disk for you.

LVM
~~~

For most use cases, we recommend using Logical Volume Management (LVM). This will allow you to more easily change your partitioning in the future if you need to. Please note that our current Security Onion ISO image does not use LVM, but we plan to incorporate that in the future.

/nsm
~~~~

The vast majority of data will be written to ``/nsm``, so you'll want to dedicate the vast majority of your disk space to that partition.

Wazuh
~~~~~

Wazuh is currently installed to ``/opt/so/wazuh``. If you plan to deploy lots of Wazuh agents and collect lots of Wazuh logs, you will want to ensure that this directory has plenty of space. One option may include mounting that directory as a dedicated partition.

Other
~~~~~

If you install using a standard CentOS 7 or Ubuntu 18.04 ISO, then they may try to dedicate a large amount of space to ``/home``. You may need to adjust this to ensure that it is not overly large and wasting valuable disk space.

Installation using Security Onion ISO Image
-------------------------------------------
If you want to install Security Onion using our ISO image:

#. Review the :ref:`hardware` and :ref:`release-notes` sections.
#. `Download and verify our Security Onion ISO image <https://github.com/Security-Onion-Solutions/securityonion/wiki/ISO>`__.
#. Boot the ISO in a machine that meets the minimum hardware specs.
#. Follow the prompts to complete the installation and reboot.
#. Login using the user ``onion`` and the password you set.
#. Proceed to the :ref:`configuration` section.

Installation on Ubuntu or CentOS
--------------------------------
If you want to install Security Onion on Ubuntu 18.04 or CentOS 7 (not using our Security Onion ISO image), follow these steps:

#. Review the :ref:`hardware` section.
#. Download the ISO image for your preferred flavor of Ubuntu 18.04 64-bit or CentOS 7 64-bit, verify the ISO image, and boot from it.
#. Follow the prompts in the installer. If you're building a production deployment, you'll probably want to use LVM and dedicate most of your disk space to ``/nsm`` as discussed in the Partitioning section above.
#. Reboot into your new installation.
#. Login using the username and password you specified during installation.
#. If using CentOS 7 Minimal, install `git`:

   ::

     sudo yum -y install git
   
#. Once you have git, then do the following:

   ::

     git clone https://github.com/Security-Onion-Solutions/securityonion
     cd securityonion
     sudo bash so-setup-network
   
#. Proceed to the :ref:`configuration` section.
