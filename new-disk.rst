.. _new-disk:

Adding Disk Space 
=================

If you ever need to add disk space to expand your partitions, there are a few different ways to do this. 

.. warning::

  Before doing this in production, make sure you practice this on a non-production system!

Recommend Method: LVM (Logical Volume Management)
-------------------------------------------------

If your disk is partitioned using LVM (the default for our Security Onion ISO image), then you should be able to use LVM to add new disk space to your LVM partitions. 

.. note::

        For more information about LVM, please see https://docs.oracle.com/en/operating-systems/oracle-linux/9/stordev/stordev-WorkingWithLogicalVolumeManager.html#using-lvm.

LVM Example
~~~~~~~~~~~

For a simple LVM example, suppose that you have installed our Security Onion ISO image in a virtual machine (VM) using a virtualization solution like :ref:`proxmox` that allows you to increase storage on the fly. Our Security Onion ISO image automatically uses LVM and should use the XFS filesystem for ``/nsm``, so if you want to add space to ``/nsm`` here is a brief overview of the steps you would use.

First, expand the storage. If using :ref:`proxmox`, select the VM, select ``Hardware``, select the ``Hard Disk``, click ``Disk Action``, click ``Resize``, enter the amount that you would like to add to the existing disk size, and then click the ``Resize disk`` button.

Next, log into the VM, become root, and use a partition tool like ``cfdisk`` to resize the LVM partition to take advantage of the additional free space:
::

        cfdisk

Now that the LVM partition is larger, we need to enlarge the LVM physical volume (PV). Start by getting a list of all PVs:
::

        pvdisplay

Determine the PV to be enlarged and then use the ``pvresize`` command (replacing ``/dev/sda3`` with the desired PV):
::

        pvresize /dev/sda3

Verify that the desired PV has been enlarged:
::

        pvdisplay

Verify that the volume group (VG) now shows free space:
::

        vgdisplay

Now that the VG has free space, we need to enlarge the logical volume (LV). Start by getting a list of all LVs:
::

        lvdisplay

Determine the LV to be enlarged and then use the ``lvresize`` command (replacing ``/dev/system/nsm`` with the desired LV):
::

        lvresize /dev/system/nsm -l +100%FREE

Verify that the desired LV has been enlarged:
::

        lvdisplay

Now that the LV is larger, we need to enlarge the filesystem. Start by getting a list of all filesystems:
::

        df -Th

Determine the filesystem to be enlarged and then use the appropriate command (replacing ``xfs_growfs`` with the appropriate tool based on the filesystem type and replacing ``/dev/mapper/system-nsm`` with the appropriate filesystem):
::

        xfs_growfs /dev/mapper/system-nsm

Finally, verify that the filesystem has been enlarged:
::

        df -Th

Unsupported Methods
-------------------

.. warning::

        There are other methods for expanding your partitions, but they are UNSUPPORTED. You should only attempt these methods if you really know what you are doing.

If you aren't using LVM but you need to expand your ``/nsm`` partition, then you can mount a separate physical drive directly to ``/nsm``. If doing this after installation, you will need to stop services, move the data to the new drive, and then restart services.

A variation on this method is to make ``/nsm`` a symbolic link to the new logging location. Certain services like AppArmor may need special configuration to handle the symlink.
