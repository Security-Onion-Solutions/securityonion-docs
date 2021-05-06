.. _new-disk:

Adding a new disk
=================

If you ever need to add a new disk to expand your ``/nsm`` partition, there are at least 3 different ways to do this. 

.. warning::

  Before doing this in production, make sure you practice this on a non-production system!

Method 1: LVM (Logical Volume Management)
-----------------------------------------

If you installed using LVM, then you should be able to use LVM to add new disk space to your LVM partitions.

Method 2: Mount a separate drive to /nsm
----------------------------------------

If you aren't using LVM, you can mount a drive directly to ``/nsm``. If doing this after installation, you will need to stop services, move the data, and then restart services as shown below.

Stop services:

::
  
  sudo systemctl disable salt-minion
  sudo reboot

That should prevent most things from starting. If it is a manager you will need to do ``sudo service docker stop`` after the reboot.

Move the data:

::

  sudo mv /nsm /nsm.old
  sudo mkdir /nsm
  # add your new file system to mount to /nsm in /etc/fstab
  sudo mount -a
  # make sure it's mounted correctly then run:
  sudo mv /nsm.old/* /nsm/
  sudo rm -rf /nsm.old
  
Restart services:

::

  sudo systemctl enable salt-minion
  sudo reboot

Method 3: Make /nsm a symlink to the new logging location
---------------------------------------------------------

Another option is to make ``/nsm`` a symbolic link to the new logging location. If doing this after installation, you will need to stop services, move data, and then restart services. Certain services like AppArmor may need special configuration to handle the symlink.
