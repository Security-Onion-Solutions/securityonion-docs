.. _installation:

Installation
============

.. warning::

  Please make sure that your hostname is correct during installation. Setup generates certificates based on the hostname and we do not support changing the hostname after Setup.
  
.. note::

  If you want to deploy in Amazon AWS using our AMI, you can skip to the :ref:`cloud-ami` section.
  If you want to deploy in Azure using our image, you can skip to the :ref:`cloud-azure` section.

Having downloaded your desired ISO according to the :ref:`download` section, it's now time to install! There are separate sections below to walk you through installing using our Security Onion ISO image (based on Rocky Linux 9) **or** installing standard Rocky Linux 9 or Ubuntu 22.04 and then installing our components on top.

.. warning::

  For most use cases, we recommend using our Security Onion ISO image as it's the quickest, easiest, and most consistent method. If you're not going to use our Security Onion ISO image and you're building a distributed deployment, then we recommend keeping the base OS consistent across all nodes in the deployment. Please do not mix and match Rocky Linux 9 and Ubuntu 22.04 in the same deployment.

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

Installation on Rocky Linux or Ubuntu
-------------------------------------

If you want to install Security Onion on Rocky Linux 9 Minimal or Ubuntu 22.04 (**not** using our Security Onion ISO image), follow the steps below. Please note that Ubuntu is not supported for manager nodes and will be phased out in the future.

#. Review the :ref:`hardware` and :ref:`release-notes` sections.
#. Download the ISO image for your preferred flavor of 64-bit Rocky Linux 9 Minimal or Ubuntu 22.04. Verify the ISO image and then boot from it.
#. Follow the prompts in the installer. If you're building a production deployment, you'll probably want to use LVM and dedicate most of your disk space to ``/nsm`` as discussed in the :ref:`partitioning` section.
#. Reboot into your new installation.
#. Login using the username and password you specified during installation.
#. Install prerequisites. If you're using Rocky Linux 9 Minimal:

   ::

     sudo dnf -y install git
   
   If you're using Ubuntu 22.04:
   
   ::
   
     sudo apt -y install git curl ethtool
     
#. Download our repo and start the Setup process:

   ::

     git clone -b 2.4/main https://github.com/Security-Onion-Solutions/securityonion
     cd securityonion
     sudo bash so-setup-network
     
#. Proceed to the :ref:`configuration` section.
