.. _new-disk:

Adding a new disk
=================

Before doing this in production, make sure you practice this on a non-production system!

There are at least 3 different ways to do this:

Method 1: LVM (Logical Volume Management)
-----------------------------------------

| If you chose the LVM option in the installer, then this should be the easiest way of adding disk space:
| https://wiki.ubuntu.com/Lvm

Method 2: Mount a separate drive to /nsm
----------------------------------------

This can be done in the installer or after installation is complete. If doing this after running Setup, then you'll need to copy the existing data in ``/nsm`` to the new drive using something like this:

#. Comment out the cron job in ``/etc/cron.d/nsm-watchdog``
#. Restart cron:

   ::

     sudo service cron restart
   
#. Stop all services:

   ::
   
     sudo so-stop
     
#. Determine your new drive's path:

   ::
   
     sudo fdisk -l
     
#. Partition the new drive using ``fdisk`` or ``parted``
#. Format the new partition using ``mkfs``
#. Mount the new drive to a temporary location in the filesystem:

   ::
   
     sudo mount /dev/sdb2 /mnt
     
#. Copy the existing data from ``/nsm`` to the temporary location:

   ::
   
     sudo cp -av /nsm/* /mnt/
     
#. Unmount the new drive from the temporary location:

   ::
   
     sudo umount /mnt
     
#. Rename the existing ``/nsm``:

   ::
   
     sudo mv /nsm /nsm-backup
#. Update ``/etc/fstab`` to mount the new drive to ``/nsm``:

   ::
   
     sudo vi /etc/fstab
   
   (You can use blkid to find your drive's UUID to write in /etc/fstab)
   
   ::
   
     sudo blkid /dev/sdb2
     
#. Re-create nsm directory after it was renamed:

   ::
   
     mkdir /nsm
     
#. Mount the new ``/nsm``:

   ::
   
     sudo mount /nsm
     
#. Start all services:

   ::
   
     sudo so-start
     
#. Uncomment the cron job in ``/etc/cron.d/nsm-watchdog``

#. Restart cron:

   ::
   
     sudo service cron restart
     
#. Test and verify that everything works

#. Reboot:

   ::
   
     sudo reboot
     
#. Test and verify that everything works

Method 3: Make /nsm a symlink to the new logging location
---------------------------------------------------------

If you do this, you'll need to do something like the following to avoid AppArmor issues:

Stop all services:

::

  sudo so-stop

Copy existing data from ``/nsm`` to new mount point:

::

  sudo cp -av /nsm/* /mnt/nsm

Rename existing ``/nsm``:

::

  sudo mv /nsm /nsm-backup

Make ``/nsm`` a symlink to the new logging location:


::

  sudo ln -s /mnt/nsm /nsm

Go to ``/etc/apparmor.d/local/``:

::

  cd /etc/apparmor.d/local/

Edit ``usr.sbin.mysqld``, copy the ``/nsm`` line(s), and change ``/nsm`` to the new location:

::

  sudo vi usr.sbin.mysqld

Edit ``usr.sbin.tcpdump``, copy the ``/nsm`` line(s), and change ``/nsm`` to the new location:

::

  sudo vi usr.sbin.tcpdump

Restart apparmor:

::

  sudo service apparmor restart

Start all services:

::

  sudo service nsm start

