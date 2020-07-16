.. _installation:

Installation
============

Once you have a machine ready for installation, you'll need to decide how you're going to install Security Onion. You can install using our Security Onion ISO image (based on CentOS 7) **or** you can manually install standard Ubuntu 18.04 or CentOS 7 and then install our components on top.

.. tip::

  We **highly** recommend using our Security Onion ISO image as it's the quickest and easiest method **and** it ensures that things like partitioning are done correctly.
  
Installation using Security Onion ISO Image
-------------------------------------------
If you want to install Security Onion using our ISO image:

#. Review the `Hardware Requirements <Hardware>`__ and `Release Notes <Release-Notes>`__ pages.
#. `Download and verify our Security Onion ISO image <https://github.com/Security-Onion-Solutions/securityonion/wiki/ISO>`__.
#. Boot the ISO in a machine that meets the minimum hardware specs.
#. Follow the prompts to complete the installation and reboot.
#. Login using the user ``onion`` and the password you set.
#. Proceed to the :ref:`configuration` page.

Installation on Ubuntu or CentOS
--------------------------------
If you want to install Security Onion on Ubuntu 18.04 or CentOS 7 (not using our Security Onion ISO image), follow these steps:

#. Review the :ref:`hardware` page.
#. Download the ISO image for your preferred flavor of Ubuntu 18.04 64-bit or CentOS 7 64-bit, verify the ISO image, and boot from it.
#. Follow the prompts in the installer. If doing a production deployment, you'll probably want to use LVM and dedicate most of your disk space to ``/nsm``.
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
   
#. Proceed to the :ref:`configuration` page.
