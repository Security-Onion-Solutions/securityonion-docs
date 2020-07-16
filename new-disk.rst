.. _new-disk:

Adding a new disk
=================

Before doing this in production, make sure you practice this on a non-production system!

There are at least 3 different ways to do this:

Method 1: LVM (Logical Volume Management)
-----------------------------------------

The easiest method of adding disk space is using LVM (assuming you installed using LVM).

Method 2: Mount a separate drive to /nsm
----------------------------------------

If you aren't using LVM, you can mount a drive directly to /nsm. If doing this after installation, you will need to stop services, move data, and then restart services.

Method 3: Make /nsm a symlink to the new logging location
---------------------------------------------------------

Another option is to make /nsm a symbolic link to the new logging location. If doing this after installation, you will need to stop services, move data, and then restart services. Certain services like AppArmor may need special configuration to handle the symlink.
