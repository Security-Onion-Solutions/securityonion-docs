.. _network-installation:

Network Installation
====================

.. warning::

        Network installations are not supported and should only be used as a last resort in case there is some reason you can't use our official Security Onion ISO image as shown in the :ref:`installation` section.

Our official Security Onion ISO image is the only fully supported installation method and you should use it if any of the following apply to you:

- You are deploying in an enterprise environment.
- You are deploying in an airgap environment.
- You are performing a distributed deployment.
- You want the quickest and easiest installation with the fewest issues.
- You need full support.

If NONE of the above apply to you, you MAY be able to install one of the following operating systems and then perform a network installation:

- Oracle Linux 9
- Rocky Linux 9
- Alma Linux 9
- CentOS Stream 9
- RHEL 9
- Ubuntu 22.04
- Debian 12

For the least amount of issues, choose Oracle Linux 9 since it's used for our official images. Rocky Linux 9, CentOS Stream 9, and Alma Linux 9 should also work but they are not fully tested. Another option might be RHEL 9 itself although that is a paid option.

If you really want to run Ubuntu 22.04 or Debian 12, then please note that these distros may work but they get even less testing and therefore you will be more likely to run into issues. If you choose Ubuntu 22.04, we recommend the Ubuntu 22.04 Server ISO image and selecting the ``Ubuntu Server`` installation option as there are known issues when choosing the ``Ubuntu Server (minimized)`` option.

Partitioning
------------

Our official Security Onion images take care of partitioning for you. However, if you choose to perform a network installation then it's your responsibility to make sure that partitions are configured correctly to avoid filling up a partition.

Minimum Storage
~~~~~~~~~~~~~~~

As the :ref:`hardware` section mentions, the MINIMUM requirement is 200GB storage. This is to allow 100GB for ``/nsm`` and 100GB for the rest of ``/``.

LVM
~~~

You may want to consider Logical Volume Management (LVM) as it will allow you to more easily change your partitioning in the future if you need to.

/boot
~~~~~

You probably want a dedicated ``/boot`` partition of at least 1GB at the beginning of the drive.

/nsm
~~~~

The vast majority of data will be written to ``/nsm``, so you'll want to dedicate the vast majority of your disk space to that partition. You'll want at least 100GB.

/
~

``/`` (the root partition) currently contains ``/var/lib/docker/`` (more on that below) and thus you'll want at least 100GB.

Docker
~~~~~~

Docker images are stored in ``/var/lib/docker/``. The current set of Docker images uses 30GB on disk. If you're planning a production deployment, you should plan on having enough space for another set of those Docker images for in-place updates.

Other
~~~~~

The OS installer may try to dedicate a large amount of space to ``/home``. You may need to adjust this to ensure that it is not overly large and wasting valuable disk space.

Example
~~~~~~~

Here's an example of how our current ISO image partitions a 1TB disk:

- 1GB ``/boot`` partition at the beginning of the drive
- the remainder of the drive is an ``LVM`` volume that is then partitioned as follows:

  - 630GB ``/nsm``
  - 300GB ``/``
  - 2GB ``/tmp``
  - 8GB ``swap``

Installing via the network
--------------------------

.. warning::

   Please keep in mind that network installations are NOT supported and should only be used as a last resort.

If you understand all of the warnings above and still want to perform a network installation, then you can follow the steps below.

#. Review the :ref:`hardware` and :ref:`release-notes` sections.
#. Download the ISO image for your desired x86-64 operating system. Verify the ISO image and then boot from it.
#. Follow the prompts in the installer. If you're building a production deployment, you'll probably want to use LVM and dedicate most of your disk space to ``/nsm`` as discussed in the Partitioning section above.
#. Reboot into your new installation.
#. Login using the username and password you specified during installation.
#. Install prerequisites. If you're using a RHEL flavor like Oracle Linux 9:

   ::

     sudo dnf -y install git

   If you're using a Debian flavor like Ubuntu:

   ::

     sudo apt -y install git curl ethtool

#. Download our repo and start the Setup process:

   ::

     git clone -b 2.4/main https://github.com/Security-Onion-Solutions/securityonion
     cd securityonion
     sudo bash so-setup-network

#. Proceed to the :ref:`configuration` section.
