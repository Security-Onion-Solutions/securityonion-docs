.. _installation:

Installation
============

.. note::

  If you want to deploy in Amazon AWS using our AMI, please see :ref:`cloud-ami`.

Having downloaded your desired ISO according to the :ref:`download` section, it's now time to install! There are separate sections below to walk you through installing using our Security Onion ISO image (based on CentOS 7) **or** installing standard CentOS 7 or Ubuntu 18.04 and then installing our components on top.

.. tip::

  For most use cases, we recommend using our Security Onion ISO image as it's the quickest and easiest method.

Installation using Security Onion ISO Image
-------------------------------------------
If you want to install Security Onion using our ISO image:

#. Review the :ref:`hardware` and :ref:`release-notes` sections.
#. `Download and verify our Security Onion ISO image <https://github.com/Security-Onion-Solutions/securityonion/blob/master/VERIFY_ISO.md>`__.
#. Boot the ISO in a machine that meets the minimum hardware specs.
#. Follow the prompts to complete the installation and reboot.
#. You may need to eject the ISO image or change the boot order of the machine to boot from the newly installed OS.
#. Login using the username and password you set in the installer.
#. Security Onion Setup will automatically start. If for some reason you have to exit Setup and need to restart it, you can log out of your account and then log back in and it should automatically start. If that doesn't work, you can manually run it as follows:

    ::
    
      sudo SecurityOnion/setup/so-setup iso
      
#. Proceed to the :ref:`configuration` section.

Installation on Ubuntu or CentOS
--------------------------------
If you want to install Security Onion on CentOS 7 or Ubuntu 18.04 (**not** using our Security Onion ISO image), follow these steps:

#. Review the :ref:`hardware` and :ref:`release-notes` sections.
#. Download the ISO image for your preferred flavor of Ubuntu 18.04 64-bit or CentOS 7 64-bit, verify the ISO image, and boot from it.
#. Follow the prompts in the installer. If you're building a production deployment, you'll probably want to use LVM and dedicate most of your disk space to ``/nsm`` as discussed in the :ref:`partitioning` section.
#. Reboot into your new installation.
#. Login using the username and password you specified during installation.
#. If using CentOS 7 Minimal, install ``git``:

   ::

     sudo yum -y install git
   
#. Once you have git, then do the following:

   ::

     git clone https://github.com/Security-Onion-Solutions/securityonion
     cd securityonion
     sudo bash so-setup-network
   
#. Proceed to the :ref:`configuration` section.
