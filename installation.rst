.. _installation:

Installation
============

.. tip::

  If this is your first time using Security Onion and you just want to try it out, we recommend installing our Security Onion ISO image as it's the quickest and easiest way to get started.
  
Installation using Security Onion ISO Image
-------------------------------------------
If you want to install Security Onion using our ISO image:

#. Review the `Hardware Requirements <Hardware>`__ and `Release Notes <Release-Notes>`__ pages.
#. `Download and verify our Security Onion ISO image <https://github.com/Security-Onion-Solutions/securityonion/wiki/ISO>`__.
#. Boot the ISO in a machine that meets the minimum hardware specs.
#. Follow the prompts to complete the installation and reboot.
#. Login using the user ``onion`` and the password you set.

Installation on Ubuntu or CentOS
--------------------------------
If you want to install Security Onion on Ubuntu 18.04 or CentOS 7 (not using our Security Onion ISO image), follow these steps:

#. Review the :ref:`hardware` page.
#. Download the ISO image for your preferred flavor of Ubuntu 18.04 64-bit or CentOS 7 64-bit, verify the ISO image, and boot from it.
#. Follow the prompts in the installer.
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
   
