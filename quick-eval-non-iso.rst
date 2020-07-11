.. _quick-eval-non-iso:

Installation on Ubuntu or CentOS
================================

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
   
