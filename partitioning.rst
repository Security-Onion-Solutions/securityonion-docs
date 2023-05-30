.. _partitioning:

Partitioning
============

Now that you understand :ref:`hardware`, we should next discuss disk partitioning. If you're installing Security Onion for a production deployment, you'll want to pay close attention to partitioning to make sure you don't fill up a partition at some point. 

Minimum Storage
---------------
As the :ref:`hardware` section mentions, the MINIMUM requirement is 200GB storage. This is to allow 100GB for ``/nsm`` and 100GB for the rest of ``/``.

ISO
---

If you use our Security Onion ISO image, it will automatically partition your disk for you. If you instead use Rocky Linux 9 Minimal or Ubuntu 20.04, you will most likely need to manually modify their default partition layout.

LVM
---

You may want to consider Logical Volume Management (LVM) as it will allow you to more easily change your partitioning in the future if you need to. Our Security Onion ISO image uses LVM by default.

/boot
-----

You probably want a dedicated ``/boot`` partition of at least 512MB at the beginning of the drive.

/nsm
----

The vast majority of data will be written to ``/nsm``, so you'll want to dedicate the vast majority of your disk space to that partition. You'll want at least 100GB.

/
-

``/`` (the root partition) currently contains ``/var/lib/docker/`` (more on that below) and thus you'll want at least 100GB.

Docker
------

Docker images are currently written to ``/var/lib/docker/``. The current set of Docker images uses 30GB on disk. If you're planning a production deployment, you should plan on having enough space for another set of those Docker images for in-place updates.

Other
-----

If you install using a standard Rocky Linux 9 Minimal or Ubuntu 20.04 ISO, then those installers may try to dedicate a large amount of space to ``/home``. You may need to adjust this to ensure that it is not overly large and wasting valuable disk space.

Example
-------

Here's an example of how our current Security Onion ISO image partitions a 1TB disk:

- 512MB ``/boot`` partition at the beginning of the drive
- the remainder of the drive is an ``LVM`` volume that is then partitioned as follows:

  - 630GB ``/nsm``
  - 300GB ``/``
  - 2GB ``/tmp``
  - 8GB ``swap``
