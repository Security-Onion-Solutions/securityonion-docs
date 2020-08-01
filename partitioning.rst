.. _partitioning:

Partitioning
============

Now that you understand :ref:`hardware`, we should next discuss disk partitioning. If you're installing Security Onion for a production deployment, you'll want to pay close attention to partitioning to make sure you don't fill up a partition at some point.

ISO
---

If you use our Security Onion ISO image, it will automatically partition your disk for you. If you instead use CentOS 7 or Ubuntu 18.04, you will most likely need to manually modify their default partition layout.

LVM
---

You may want to consider Logical Volume Management (LVM) as it will allow you to more easily change your partitioning in the future if you need to. As of Security Onion 2.0.3, our Security Onion ISO image uses LVM by default.

/nsm
----

The vast majority of data will be written to ``/nsm``, so you'll want to dedicate the vast majority of your disk space to that partition.

Wazuh
-----

Wazuh is currently installed to ``/opt/so/wazuh``. If you plan to deploy lots of Wazuh agents and collect lots of Wazuh logs, you will want to ensure that this directory has plenty of space. One option may include mounting that directory as a dedicated partition.

Docker
------

Docker images are currently written to ``/var/lib/docker/``. The current set of Docker images uses 26GB on disk. If you're planning a production deployment, you should plan on having enough space for another set of those Docker images for in-place updates.

Other
-----

If you install using a standard CentOS 7 or Ubuntu 18.04 ISO, then those installers may try to dedicate a large amount of space to ``/home``. You may need to adjust this to ensure that it is not overly large and wasting valuable disk space.
