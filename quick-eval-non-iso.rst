.. _quick-eval-non-iso:

Quick Evaluation on Ubuntu or CentOS
====================================

.. warning::

   The following guide is for quick evaluation only.  If you're building a production deployment, please see the :ref:`production-deployment` section.

If you want to quickly evaluate Security Onion on Ubuntu 18.04 or CentOS 7 (not using our Security Onion ISO image), follow these steps:

- Review the :ref:`hardware` page.
- Download the ISO image for your preferred flavor of Ubuntu 18.04 64-bit or CentOS 7 64-bit, verify the ISO image, and boot from it.
- Follow the prompts in the installer.
- Reboot into your new installation.
- Login using the username and password you specified during installation.
- If using CentOS 7 Minimal, install `git`:

  ::

    sudo yum -y install git
   
- Once you have git, then do the following:

  ::

    git clone https://github.com/Security-Onion-Solutions/securityonion
    cd securityonion
    sudo bash so-setup-network
   
- Choose the ``EVAL`` option and then follow the prompts to configure your system.

- Proceed to the :ref:`post-installation` page.
