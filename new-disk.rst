.. _new-disk:

Adding a new disk
=================

If you ever need to add a new disk to expand your ``/nsm`` partition, there are a few different ways to do this. 

.. warning::

  Before doing this in production, make sure you practice this on a non-production system!

Recommend Method: LVM (Logical Volume Management)
-------------------------------------------------

If your disk is partitioned using LVM (the default for our Security Onion ISO image), then you should be able to use LVM to add new disk space to your LVM partitions.

Unsupported Methods
-------------------

There are other methods for expanding your ``/nsm`` partition, but they are UNSUPPORTED. You should only attempt these methods if you really know what you are doing.

If you aren't using LVM, you can mount a separate physical drive directly to ``/nsm``. If doing this after installation, you will need to stop services, move the data to the new drive, and then restart services.

A variation on this method is to make ``/nsm`` a symbolic link to the new logging location. Certain services like AppArmor may need special configuration to handle the symlink.
